import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import DigitalPorts as digital_ports

class DigitalPorts(int):
	DIN = digital_ports.DIN
	DOUT = digital_ports.DOUT
	UI = digital_ports.UI
	UO = digital_ports.UO
	SI = digital_ports.SI
	SO = digital_ports.SO
	RI = digital_ports.RI
	RO = digital_ports.RO
	FLG = digital_ports.FLG
