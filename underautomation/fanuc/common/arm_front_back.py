import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmFrontBack as arm_front_back

class ArmFrontBack(int):
	Unknown = arm_front_back.Unknown
	Front = arm_front_back.Front
	Back = arm_front_back.Back
