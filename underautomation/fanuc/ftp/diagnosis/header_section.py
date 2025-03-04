import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import HeaderSection as header_section

class HeaderSection:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = header_section()
		else:
			self._instance = _internal
	@property
	def f_number(self) -> str:
		return self._instance.FNumber
	@property
	def version(self) -> str:
		return self._instance.Version
	@property
	def version_firmware(self) -> str:
		return self._instance.VersionFirmware
	@property
	def version_date(self) -> typing.Any:
		return self._instance.VersionDate
	@property
	def date(self) -> typing.Any:
		return self._instance.Date
