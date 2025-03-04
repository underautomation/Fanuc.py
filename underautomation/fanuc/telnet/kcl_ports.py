import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import KCLPorts as kcl_ports

class KCLPorts(int):
	DIN = kcl_ports.DIN
	DOUT = kcl_ports.DOUT
	RDO = kcl_ports.RDO
	OPOUT = kcl_ports.OPOUT
	TPOUT = kcl_ports.TPOUT
	WDI = kcl_ports.WDI
	WDO = kcl_ports.WDO
	AIN = kcl_ports.AIN
	AOUT = kcl_ports.AOUT
	GIN = kcl_ports.GIN
	GOUT = kcl_ports.GOUT
