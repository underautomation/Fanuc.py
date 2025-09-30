import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import OnOff as on_off

class OnOff(int):
	OFF = on_off.OFF
	ON = on_off.ON
