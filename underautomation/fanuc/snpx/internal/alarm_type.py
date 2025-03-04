import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import AlarmType as alarm_type

class AlarmType(int):
	Active = alarm_type.Active
	History = alarm_type.History
