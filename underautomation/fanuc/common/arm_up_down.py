import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ArmUpDown as arm_up_down

class ArmUpDown(int):
	Unknown = int(arm_up_down.Unknown)
	Up = int(arm_up_down.Up)
	Down = int(arm_up_down.Down)

	def __repr__(self):
		for name, value in vars(ArmUpDown).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
