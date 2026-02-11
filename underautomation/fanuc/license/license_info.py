import typing
from datetime import datetime, timedelta
from underautomation.fanuc.license.license_state import LicenseState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.License import LicenseInfo as license_info
from UnderAutomation.Fanuc.License import LicenseState as license_state

class LicenseInfo:
	def __init__(self, licenseIdentifier: str, licenseKey: str, _internal = 0):
		if(_internal == 0):
			self._instance = license_info(licenseIdentifier, licenseKey)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def license_key(self) -> str:
		return self._instance.LicenseKey
	@property
	def product(self) -> str:
		return self._instance.Product
	@property
	def evaluation_days_left(self) -> int | None:
		return self._instance.EvaluationDaysLeft
	@property
	def evaluation_start_date(self) -> datetime:
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.EvaluationStartDate.Ticks // 10)
	@property
	def licensee(self) -> str:
		return self._instance.Licensee
	@property
	def trial_period_expiration_date(self) -> datetime | None:
		return None if self._instance.TrialPeriodExpirationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.TrialPeriodExpirationDate.Ticks // 10)
	@property
	def state(self) -> LicenseState:
		return LicenseState(self._instance.State)
	@property
	def product_release_date(self) -> datetime:
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.ProductReleaseDate.Ticks // 10)
	@property
	def maintenance_years(self) -> int:
		return self._instance.MaintenanceYears
	@property
	def license_issued_date(self) -> datetime | None:
		return None if self._instance.LicenseIssuedDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.LicenseIssuedDate.Ticks // 10)
	@property
	def maintenance_expiration_date(self) -> datetime | None:
		return None if self._instance.MaintenanceExpirationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.MaintenanceExpirationDate.Ticks // 10)
