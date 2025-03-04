import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmLeftRight as arm_left_right

class ArmLeftRight(int):
	Unknown = arm_left_right.Unknown
	Left = arm_left_right.Left
	Right = arm_left_right.Right
