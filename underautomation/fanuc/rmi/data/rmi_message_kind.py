import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import RmiMessageKind as rmi_message_kind

class RmiMessageKind(int):
	Communication = int(rmi_message_kind.Communication)
	Command = int(rmi_message_kind.Command)
	Instruction = int(rmi_message_kind.Instruction)

	def __repr__(self):
		for name, value in vars(RmiMessageKind).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
