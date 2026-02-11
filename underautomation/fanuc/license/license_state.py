import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.License import LicenseState as license_state

class LicenseState(int):
	Invalid = int(license_state.Invalid)
	Trial = int(license_state.Trial)
	ExtraTrial = int(license_state.ExtraTrial)
	Expired = int(license_state.Expired)
	MaintenanceNeeded = int(license_state.MaintenanceNeeded)
	Licensed = int(license_state.Licensed)

	def __repr__(self):
		for name, value in vars(LicenseState).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
