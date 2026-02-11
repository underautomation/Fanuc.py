import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import OnOff as on_off

class OnOff(int):
	OFF = int(on_off.OFF)
	ON = int(on_off.ON)

	def __repr__(self):
		for name, value in vars(OnOff).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
