import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import KCLPorts as kcl_ports

class KCLPorts(int):
	DIN = int(kcl_ports.DIN)
	DOUT = int(kcl_ports.DOUT)
	RDO = int(kcl_ports.RDO)
	OPOUT = int(kcl_ports.OPOUT)
	TPOUT = int(kcl_ports.TPOUT)
	WDI = int(kcl_ports.WDI)
	WDO = int(kcl_ports.WDO)
	AIN = int(kcl_ports.AIN)
	AOUT = int(kcl_ports.AOUT)
	GIN = int(kcl_ports.GIN)
	GOUT = int(kcl_ports.GOUT)

	def __repr__(self):
		for name, value in vars(KCLPorts).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
