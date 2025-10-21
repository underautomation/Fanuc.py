import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import CommunicationVerb as communication_verb

class CommunicationVerb(int):
	FRC_Connect = communication_verb.FRC_Connect
	FRC_Disconnect = communication_verb.FRC_Disconnect
	FRC_Terminate = communication_verb.FRC_Terminate
	FRC_SystemFault = communication_verb.FRC_SystemFault
