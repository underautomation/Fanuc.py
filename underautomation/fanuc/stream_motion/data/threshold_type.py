import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class ThresholdType(int):
	Velocity = threshold_type.Velocity
	Acceleration = threshold_type.Acceleration
	Jerk = threshold_type.Jerk
