import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import PacketType as packet_type

class PacketType(int):
	INIT = packet_type.INIT
	REQUEST = packet_type.REQUEST
	ACK = packet_type.ACK
	UNKNOWN_8 = packet_type.UNKNOWN_8
