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

robot = [Robot(id=1, x=1, y=1), Robot(id=2, x=1, y=1), Robot(id=3, x=1, y=1), Robot(id=4, x=1, y=1), Robot(id=5, x=1, y=1)]
log.info(f'ROBOT:{robot[0].id} - x: {robot[0].pos_x} - y: {robot[0].pos_y}')
log.info(f'ROBOT:{robot[1].id} - x: {robot[1].pos_x} - y: {robot[1].pos_y}')
log.info(f'ROBOT:{robot[2].id} - x: {robot[2].pos_x} - y: {robot[2].pos_y}')
log.info(f'ROBOT:{robot[3].id} - x: {robot[3].pos_x} - y: {robot[3].pos_y}')
log.info(f'ROBOT:{robot[4].id} - x: {robot[4].pos_x} - y: {robot[4].pos_y}')

log.info("Creating channel...")
channel = Channel("amqp://guest:guest@localhost:5672")

log.info("Creating the RPC Server and waiting requests...")
def get_position(pathrequest, ctx):
	for robotfor in robot:
		if robotfor.id == pathrequest.id:
			positionget = PathRequest()
			positionget.destination_pose.position.x, positionget.destination_pose.position.y = robotfor.get_position()
			positionget.id = robotfor.id
			return positionget
		

def set_position(pathrequest, ctx):
	for robotfor in robot:
		if robotfor.id == pathrequest.id:
			if pathrequest.destination_pose.position.x < 0 or pathrequest.destination_pose.position.y < 0:
				return Status(StatusCode.OUT_OF_RANGE, "The number must be positive")
		
			robotfor.set_position(x=pathrequest.destination_pose.position.x, y=pathrequest.destination_pose.position.y)
			return Empty()
		
		
provider = ServiceProvider(channel)
logging = LogInterceptor() # Log requests to console
provider.add_interceptor(logging)

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
