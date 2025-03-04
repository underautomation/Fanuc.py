import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.License import LicenseState as license_state

class LicenseState(int):
	Invalid = license_state.Invalid
	Trial = license_state.Trial
	ExtraTrial = license_state.ExtraTrial
	Expired = license_state.Expired
	MaintenanceNeeded = license_state.MaintenanceNeeded
	Licensed = license_state.Licensed
