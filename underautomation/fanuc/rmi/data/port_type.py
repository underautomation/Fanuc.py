import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import PortType as port_type

class PortType(int):
	DOUT = port_type.DOUT
	ROUT = port_type.ROUT
