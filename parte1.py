from is_wire.core import Channel, Message, Subscription, Logger
from RequisicaoRobo_pb2 import RequisicaoRobo
from google.protobuf.empty_pb2 import Empty
from random import randint
import socket
import time

log_set = Logger(name='SET_POSITION')
log_get = Logger(name='GET_POSITION')
log = Logger(name='OPERATOR')
log.info("Creating channel...")
channel = Channel("amqp://guest:guest@localhost:5672")
message = Message()
subscription = Subscription(channel)


log.info("Creating TURN ON  message...")
message.body = "Ligar sistema".encode('latin1')


subscription.subscribe(topic="Resposta.sistema")


while True:
	
	log.info("Sending TURN ON  message...")
	channel.publish(message, topic="Controle.console")
	
	log.info("Waiting reply...")
	message2 = channel.consume()
	
	if message2.body.decode('latin1') == "Sistema Ligado":
		log.info("SYSTEM ONLINE...")
		break
		
	log.warn("System offline. Trying again...")
	time.sleep(1)




while True:

	requisicao = RequisicaoRobo()
	subscription = Subscription(channel)
	
	#1° REQUEST
	log.info("Getting a ramdomized ID")
	requisicao.id = int(input("Enter your robot id "))
	log.info(f"Robot ID: {requisicao.id}")
	requisicao.function = "GET POSITION"

	log.info("Creating GET POSITION request...")
	message2 = Message(content = requisicao, reply_to = subscription)

	channel.publish(message2, topic="Requisicao.Robo")
	log.info("Sending GET POSITION request...")

	log.info("Waiting GET POSITION reply...")
	
	try:
	    reply = channel.consume(timeout=1.0)
	    log.info("GET POSITION reply:") 
	    log.info(f'{reply.status.why}')
	    time.sleep(1)
    
	except socket.timeout:
	    print('No reply :(')
	    

	#2° REQUEST
	requisicao.function = "SET POSITION"
	requisicao.positions.x = randint(-2,5)
	requisicao.positions.y = randint(-2,5)
	log.info(f"Creating SET POSITION request with x:{requisicao.positions.x} y:{requisicao.positions.y}")

	subscription = Subscription(channel)

	message2 = Message(content = requisicao, reply_to = subscription)

	channel.publish(message2, topic="Requisicao.Robo")
	log.info("Sending SET POSITION request...")

	log.info("Waiting SET POSITION reply...")
	try:
	    reply = channel.consume(timeout=1.0) 
	    log.info(f'SET POSITION reply: {reply.status.code}')
	    time.sleep(1)

	    
	except socket.timeout:
	    print('No reply :(')
	    
	    
	#3° REQUEST
	log.info("Getting a ramdomized ID")
	log.info(f"Robot ID: {requisicao.id}")
	requisicao.function = "GET POSITION"

	log.info("Creating GET POSITION request...")
	message2 = Message(content = requisicao, reply_to = subscription)

	channel.publish(message2, topic="Requisicao.Robo")
	log.info("Sending GET POSITION request...")

	log.info("Waiting GET POSITION reply...")
	
	try:
	    reply = channel.consume(timeout=1.0)
	    log.info("GET POSITION reply:") 
	    log.info(f'{reply.status.why}')
	    time.sleep(1)
    
	except socket.timeout:
	    print('No reply :(')


