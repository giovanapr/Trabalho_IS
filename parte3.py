from is_wire.rpc import ServiceProvider, LogInterceptor
from is_wire.core import Channel, StatusCode, Status, Logger
from google.protobuf.empty_pb2 import Empty
from is_msgs.robot_pb2 import PathRequest
import time

log = Logger(name = 'ROBOT CONTROLLER')

class Robot():
    def __init__(self, id, x, y):
        self.id = id
        self.pos_x = x
        self.pos_y = y

    def get_id(self):
        return self.id

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_position(self):
        return self.pos_x, self.pos_y

log.info("Initializing robots...")
robot1 = Robot(id=1, x=1, y=1)
log.info(f'ROBOT:{robot1.id} - x: {robot1.pos_x} - y: {robot1.pos_y}')

robot2 = Robot(id=2, x=1, y=1)
log.info(f'ROBOT:{robot2.id} - x: {robot2.pos_x} - y: {robot2.pos_y}')

robot3 = Robot(id=3, x=1, y=1)
log.info(f'ROBOT:{robot3.id} - x: {robot3.pos_x} - y: {robot3.pos_y}')

robot4 = Robot(id=4, x=1, y=1)
log.info(f'ROBOT:{robot4.id} - x: {robot4.pos_x} - y: {robot4.pos_y}')

robot5 = Robot(id=5, x=1, y=1)
log.info(f'ROBOT:{robot5.id} - x: {robot5.pos_x} - y: {robot5.pos_y}')

log.info("Creating channel...")
channel = Channel("amqp://guest:guest@localhost:5672")

log.info("Creating the RPC Server and waiting requests...")
def get_position(pathrequest, ctx):
	
	if pathrequest.id == robot1.id:
		positionget = PathRequest()
		positionget.destination_pose.position.x, positionget.destination_pose.position.y = robot1.get_position()
		positionget.id = robot1.id
		return positionget
		
	if pathrequest.id == robot2.id:
		positionget = PathRequest()
		positionget.destination_pose.position.x, positionget.destination_pose.position.y = robot2.get_position()
		return positionget
		
	if pathrequest.id == robot3.id:
		positionget = PathRequest()
		positionget.destination_pose.position.x, positionget.destination_pose.position.y = robot3.get_position()
		return positionget
		
	if pathrequest.id == robot4.id:
		positionget = PathRequest()
		positionget.destination_pose.position.x, positionget.destination_pose.position.y = robot4.get_position()
		positionget.id = robot4.id
		return positionget
		
	if pathrequest.id == robot5.id:
		positionget = PathRequest()
		positionget.destination_pose.position.x, positionget.destination_pose.position.y = robot5.get_position()
		return positionget

def set_position(pathrequest, ctx):
	
	if pathrequest.id == robot1.id:
		if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
			return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

		robot1.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
		return Empty()
	
	
	elif pathrequest.id == robot2.id:
		if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
			return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

		robot2.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
		return Empty()
	
	
	elif pathrequest.id == robot3.id:
		if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
			return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

		robot3.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
		return Empty()
		
	elif pathrequest.id == robot4.id:
		if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
			return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

		robot4.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
		return Empty()
		
		
	elif pathrequest.id == robot5.id:
		if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
			return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")

		robot5.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
		return Empty()
		
provider = ServiceProvider(channel)
logging = LogInterceptor() # Log requests to console
provider.add_interceptor(logging)

# Os tipos das mensagens devem ser passados, tanto no request como no reply
provider.delegate(
    topic="Get.Position",
   
    function=get_position,
    request_type=PathRequest,
    reply_type=PathRequest) 

provider.delegate(
    topic="Set.Position",
    function=set_position,
    request_type=PathRequest,
    reply_type=Empty)

provider.run()
