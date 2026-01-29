import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeFromRobot as packet_type_from_robot

class PacketTypeFromRobot(int):
	State = packet_type_from_robot.State
	Ack = packet_type_from_robot.Ack
