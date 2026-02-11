import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import PortType as port_type

class PortType(int):
	DOUT = int(port_type.DOUT)
	ROUT = int(port_type.ROUT)

	def __repr__(self):
		for name, value in vars(PortType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
