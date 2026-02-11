import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class ThresholdType(int):
	Velocity = int(threshold_type.Velocity)
	Acceleration = int(threshold_type.Acceleration)
	Jerk = int(threshold_type.Jerk)

	def __repr__(self):
		for name, value in vars(ThresholdType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
