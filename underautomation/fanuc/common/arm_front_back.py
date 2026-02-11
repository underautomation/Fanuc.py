import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmFrontBack as arm_front_back

class ArmFrontBack(int):
	Unknown = int(arm_front_back.Unknown)
	Front = int(arm_front_back.Front)
	Back = int(arm_front_back.Back)

	def __repr__(self):
		for name, value in vars(ArmFrontBack).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
