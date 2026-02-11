import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeFromRobot as packet_type_from_robot

class PacketTypeFromRobot(int):
	State = int(packet_type_from_robot.State)
	Ack = int(packet_type_from_robot.Ack)

	def __repr__(self):
		for name, value in vars(PacketTypeFromRobot).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
