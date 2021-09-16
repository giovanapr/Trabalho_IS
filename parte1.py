from is_wire.core import Channel, Message, Subscription, Logger
from RequisicaoRobo_pb2 import RequisicaoRobo
from google.protobuf.empty_pb2 import Empty
import socket
import time

log_set = Logger(name='SET_POSITION')
log_get = Logger(name='GET_POSITION')
log = Logger(name='OPERATOR')
a = 0


#CONNECT TO THE BROKER
log.info("Creating channel...")
channel = Channel("amqp://guest:guest@localhost:5672")


#PUBLISH
log.info("Creating TURN ON  message...")
message = Message()
message.body = "Ligar sistema".encode('latin1')


#SUBSCRIBE
subscription = Subscription(channel)
subscription.subscribe(topic="Resposta.sistema")


while a == 0:
	
	#PUBLISH
	log.info("Sending TURN ON  message...")
	channel.publish(message, topic="Controle.console")
	
	log.info("Waiting reply...")
	message2 = channel.consume()
	
	if message2.body.decode('latin1') == "Sistema Ligado":
		a = 1
		log.info("SYSTEM ONLINE...")
		
	log.info("System offline. Trying again...")


#PRIMEIRA REQUISICAO
time.sleep(1)

requisicao = RequisicaoRobo()
log.info("Getting a ramdomized ID")
requisicao.id = 1
log.info(f"Robot ID: {requisicao.id}")
requisicao.function = "GET POSITION"

subscription = Subscription(channel)

log.info("Creating GET POSITION request...")
message2 = Message(content = requisicao, reply_to = subscription)

channel.publish(message2, topic="Requisicao.Robo")
log.info("Sending GET POSITION request...")

log.info("Waiting GET POSITION reply...")
try:
    reply = channel.consume(timeout=1.0)
    log.info("GET POSITION reply:") 
    log.info(f'{reply.status.why}')
    
except socket.timeout:
    print('No reply :(')

#SEGUNDA REQUISICAO
requisicao = RequisicaoRobo()
requisicao.id = 1
requisicao.function = "SET POSITION"
requisicao.positions.x = 5
requisicao.positions.y = 1
log.info(f"Creating SET POSITION request with x:{requisicao.positions.x} y:{requisicao.positions.y}")

subscription = Subscription(channel)

message2 = Message(content = requisicao, reply_to = subscription)

channel.publish(message2, topic="Requisicao.Robo")
log.info("Sending SET POSITION request...")

log.info("Waiting SET POSITION reply...")
try:
    reply = channel.consume(timeout=1.0) 
    log.info(f'SET POSITION reply: {reply.status.code}')
    
except socket.timeout:
    print('No reply :(')


#TERCEIRA REQUISICAO
requisicao = RequisicaoRobo()
log.info("Getting a ramdomized ID")
requisicao.id = 1
log.info(f"Robot ID: {requisicao.id}")
requisicao.function = "GET POSITION"

subscription = Subscription(channel)

log.info("Creating GET POSITION request...")
message2 = Message(content = requisicao, reply_to = subscription)

channel.publish(message2, topic="Requisicao.Robo")
log.info("Sending GET POSITION request...")

log.info("Waiting GET POSITION reply...")
try:
    reply = channel.consume(timeout=1.0)
    log.info("GET POSITION reply:") 
    log.info(f'{reply.status.why}')
    
except socket.timeout:
    print('No reply :(')
