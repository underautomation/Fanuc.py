import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmLeftRight as arm_left_right

class ArmLeftRight(int):
	Unknown = int(arm_left_right.Unknown)
	Left = int(arm_left_right.Left)
	Right = int(arm_left_right.Right)

	def __repr__(self):
		for name, value in vars(ArmLeftRight).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
