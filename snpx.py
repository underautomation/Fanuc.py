
from underautomation.fanuc.fanuc_robot import FanucRobot
from underautomation.fanuc.connection_parameters import ConnectionParameters

robot = FanucRobot()

parameters = ConnectionParameters("192.168.8.129") # connect to real robot
#  parameters = ConnectionParameters("C:\\\\Users\\fg\\Documents\\My Workcells\\TestRobotIF\\Robot_1") # connect to Roboguide on this machine
#parameters = ConnectionParameters("\\\\192.168.8.129\\Users\\fg\\Documents\\My Workcells\\TestRobotIF\\Robot_1") # Connect to Roboguide on another machine
parameters.telnet.enable=False
parameters.ftp.enable=False
parameters.snpx.enable=True
parameters.snpx.port=60008

robot.connect(parameters)

# read world position of first robot arm driven by the controller
world_position = robot.snpx.current_position.read_world_position(1)

print(f"X: {world_position.cartesian_position.x}, Y: {world_position.cartesian_position.y}, Z: {world_position.cartesian_position.z}")
