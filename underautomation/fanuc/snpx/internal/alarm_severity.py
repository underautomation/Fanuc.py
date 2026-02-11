import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import AlarmSeverity as alarm_severity

class AlarmSeverity(int):
	NONE = int(alarm_severity.NONE)
	WARN = int(alarm_severity.WARN)
	PAUSE_L = int(alarm_severity.PAUSE_L)
	PAUSE_G = int(alarm_severity.PAUSE_G)
	STOP_L = int(alarm_severity.STOP_L)
	STOP_G = int(alarm_severity.STOP_G)
	SERVO = int(alarm_severity.SERVO)
	ABORT_L = int(alarm_severity.ABORT_L)
	ABORT_G = int(alarm_severity.ABORT_G)
	SERVO2 = int(alarm_severity.SERVO2)
	SYSTEM = int(alarm_severity.SYSTEM)

	def __repr__(self):
		for name, value in vars(AlarmSeverity).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
