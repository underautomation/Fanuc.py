import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class IOType(int):
	DI = io_type.DI
	DO = io_type.DO
	RI = io_type.RI
	RO = io_type.RO
	SI = io_type.SI
	SO = io_type.SO
	WI = io_type.WI
	WO = io_type.WO
	UI = io_type.UI
	UO = io_type.UO
	WSI = io_type.WSI
	WSO = io_type.WSO
	F = io_type.F
	M = io_type.M
