from is_wire.rpc import ServiceProvider, LogInterceptor
from is_wire.core import Channel, Message, Subscription, StatusCode, Status, Logger
from google.protobuf.empty_pb2 import Empty
from is_msgs.common_pb2 import Position
from is_msgs.robot_pb2 import PathRequest
import time
from random import randint
from RequisicaoRobo_pb2 import RequisicaoRobo
import socket

log = Logger(name = "CONSOLE")
log_set = Logger(name = 'SET_POSITION')
log_get = Logger(name = 'OPERATOR')

#CONNECT TO THE BROKER
log.info("Creating channel...")
channel = Channel("amqp://guest:guest@localhost:5672")


#SUBSCRIBE
subscription = Subscription(channel)
subscription.subscribe(topic="Controle.console")
	
log.info("Waiting TURN ON message...")

while True:
	rand = randint(0,1)
	
	#Receive message
	message = channel.consume()
	
	#Simulate connection
	log.info("Message received. Checking content and trying to bring the system online...")
	
	#PUBLISH
	if rand == 1:
		log.info("SYSTEM ONLINE...")
		message = Message()
		message.body = "Sistema Ligado".encode('latin1')
		log.info("Seding notification to OPERATOR...")
		channel.publish(message, topic="Resposta.sistema")
		break
	else:
		log.warn("Failed to bring the system online.")
		message = Message()
		message.body = "Sistema nao foi Ligado".encode('latin1')
		log.info("Seding notification to OPERATOR...")
		channel.publish(message, topic="Resposta.sistema")
	time.sleep(2)

log.info("Creating the RPC Server and waiting requests...")


#RPC GATEWAY
def send_message(requisicaorobo, ctx):
	
	if requisicaorobo.function == "SET POSITION":
		
		log.info("SET POSITION request received from OPERATOR...")
		
		subscription = Subscription(channel)
		
		requisicao = PathRequest()
		requisicao.id = requisicaorobo.id
		requisicao.destination_pose.position.x = requisicaorobo.positions.x
		requisicao.destination_pose.position.y = requisicaorobo.positions.y
		
		log.info("Sending SET POSITION request to ROBOT CONTROLLER...")
		log.info(f'ROBOT:{requisicao.id} - x: {requisicao.destination_pose.position.x} - y: {requisicao.destination_pose.position.y}')
		
		message2 = Message(content = requisicao, reply_to = subscription)

		channel.publish(message2, topic="Set.Position")
		
		log.info("Waiting SET POSITION reply from ROBOT CONTROLLER...")
		try:
			reply = channel.consume(timeout=1.0)
			log.info(f"SET POSITION reply {reply.status.code}")
			log_set.info(f'{reply.status.code}')
			return reply.status
    
		except socket.timeout:
			print('No reply :(')
    	
	elif requisicaorobo.function == "GET POSITION":
    		
    		log.info("GET POSITION request received from OPERATOR...")
    		
    		subscription = Subscription(channel)
    		
    		requisicao2 = PathRequest()
    		requisicao2.id = requisicaorobo.id
    		
    		message3 = Message(content = requisicao2, reply_to = subscription)
    		log.info("Sending GET POSITION request to ROBOT CONTROLLER...")
    		channel.publish(message3, topic="Get.Position")
    		
    		log.info("Waiting GET POSITION reply from ROBOT CONTROLLER...")
    		try:
    			reply = channel.consume(timeout=1.0)
    			log.info("GET POSITION from ROBOT CONTROLLER received:")
    			position = reply.unpack(PathRequest)
    			log.info(f'ROBOT ID:{position.id} - x: {position.destination_pose.position.x} - y: {position.destination_pose.position.y}')
    			log.info('Sending GET POSITION reply to OPERATOR...')
    			return Status(StatusCode.OK, f'Robot ID: {position.id} FUNCTION: get_position x: {position.destination_pose.position.x} - y: {position.destination_pose.position.y}')
    		
    		except socket.timeout:
    			print('No reply :(')
    			
    		
	#return Status(StatusCode.OUT_OF_RANGE, "Invalid Request")
	
channel = Channel("amqp://guest:guest@localhost:5672")
provider = ServiceProvider(channel)
#logging = LogInterceptor() # Log requests to console
#provider.add_interceptor(logging)

provider.delegate(
    topic="Requisicao.Robo",
    function=send_message,
    request_type=RequisicaoRobo,
    reply_type=Empty)

provider.run()

	
