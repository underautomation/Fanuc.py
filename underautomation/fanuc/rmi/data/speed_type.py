import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import SpeedType as speed_type

class SpeedType(int):
	MmSec = int(speed_type.MmSec)
	InchMin = int(speed_type.InchMin)
	Time = int(speed_type.Time)
	Percent = int(speed_type.Percent)

	def __repr__(self):
		for name, value in vars(SpeedType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
