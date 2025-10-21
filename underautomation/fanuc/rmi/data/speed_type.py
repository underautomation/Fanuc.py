import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import SpeedType as speed_type

class SpeedType(int):
	MmSec = speed_type.MmSec
	InchMin = speed_type.InchMin
	Time = speed_type.Time
	Percent = speed_type.Percent
