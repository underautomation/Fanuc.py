import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class IOType(int):
	DI = int(io_type.DI)
	DO = int(io_type.DO)
	RI = int(io_type.RI)
	RO = int(io_type.RO)
	SI = int(io_type.SI)
	SO = int(io_type.SO)
	WI = int(io_type.WI)
	WO = int(io_type.WO)
	UI = int(io_type.UI)
	UO = int(io_type.UO)
	WSI = int(io_type.WSI)
	WSO = int(io_type.WSO)
	F = int(io_type.F)
	M = int(io_type.M)

	def __repr__(self):
		for name, value in vars(IOType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
