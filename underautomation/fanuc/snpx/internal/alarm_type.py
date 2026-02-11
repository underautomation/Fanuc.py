import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import AlarmType as alarm_type

class AlarmType(int):
	Active = int(alarm_type.Active)
	History = int(alarm_type.History)

	def __repr__(self):
		for name, value in vars(AlarmType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
