import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeToRobot as packet_type_to_robot

class PacketTypeToRobot(int):
	Start = packet_type_to_robot.Start
	Command = packet_type_to_robot.Command
	Stop = packet_type_to_robot.Stop
	Request = packet_type_to_robot.Request
