import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import MessageType as message_type

class MessageType(int):
	SHORT = message_type.SHORT
	SHORT_ACK = message_type.SHORT_ACK
	LONG = message_type.LONG
	LONG_ACK = message_type.LONG_ACK
	SHORT_FAILED = message_type.SHORT_FAILED
