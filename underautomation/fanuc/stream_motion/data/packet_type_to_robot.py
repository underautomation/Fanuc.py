import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeToRobot as packet_type_to_robot

class PacketTypeToRobot(int):
	Start = int(packet_type_to_robot.Start)
	Command = int(packet_type_to_robot.Command)
	Stop = int(packet_type_to_robot.Stop)
	Request = int(packet_type_to_robot.Request)

	def __repr__(self):
		for name, value in vars(PacketTypeToRobot).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
