import typing
from datetime import datetime, timedelta
from UnderAutomation.Fanuc.Ftp.Diagnosis import HeaderSection as header_section

class HeaderSection:
	'''Header information of a diagnostic file'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = header_section()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def f_number(self) -> str:
		'''Failsafe number'''
		return self._instance.FNumber

	@property
	def version(self) -> str:
		'''Controller version'''
		return self._instance.Version

	@property
	def version_firmware(self) -> str:
		'''Firmware version'''
		return self._instance.VersionFirmware

	@property
	def version_date(self) -> datetime:
		'''Firmware release date'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.VersionDate.Ticks // 10)

	@property
	def date(self) -> datetime:
		'''Current controller time'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Date.Ticks // 10)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HeaderSection):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
