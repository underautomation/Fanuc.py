import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import CommunicationVerb as communication_verb

class CommunicationVerb(int):
	FRC_Connect = int(communication_verb.FRC_Connect)
	FRC_Disconnect = int(communication_verb.FRC_Disconnect)
	FRC_Terminate = int(communication_verb.FRC_Terminate)
	FRC_SystemFault = int(communication_verb.FRC_SystemFault)

	def __repr__(self):
		for name, value in vars(CommunicationVerb).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
