import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import DigitalPorts as digital_ports

class DigitalPorts(int):
	DIN = int(digital_ports.DIN)
	DOUT = int(digital_ports.DOUT)
	UI = int(digital_ports.UI)
	UO = int(digital_ports.UO)
	SI = int(digital_ports.SI)
	SO = int(digital_ports.SO)
	RI = int(digital_ports.RI)
	RO = int(digital_ports.RO)
	FLG = int(digital_ports.FLG)

	def __repr__(self):
		for name, value in vars(DigitalPorts).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
