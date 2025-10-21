import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import RmiMessageKind as rmi_message_kind

class RmiMessageKind(int):
	Communication = rmi_message_kind.Communication
	Command = rmi_message_kind.Command
	Instruction = rmi_message_kind.Instruction
