import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmUpDown as arm_up_down

class ArmUpDown(int):
	Unknown = arm_up_down.Unknown
	Up = arm_up_down.Up
	Down = arm_up_down.Down
