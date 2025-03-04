import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import AlarmSeverity as alarm_severity

class AlarmSeverity(int):
	NONE = alarm_severity.NONE
	WARN = alarm_severity.WARN
	PAUSE_L = alarm_severity.PAUSE_L
	PAUSE_G = alarm_severity.PAUSE_G
	STOP_L = alarm_severity.STOP_L
	STOP_G = alarm_severity.STOP_G
	SERVO = alarm_severity.SERVO
	ABORT_L = alarm_severity.ABORT_L
	ABORT_G = alarm_severity.ABORT_G
	SERVO2 = alarm_severity.SERVO2
	SYSTEM = alarm_severity.SYSTEM
