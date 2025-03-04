import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpsnapFile as tpsnap_file

class TpsnapFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpsnap_file()
		else:
			self._instance = _internal
	@property
	def day(self) -> int:
		return self._instance.Day
	@property
	def day_str(self) -> str:
		return self._instance.DayStr
	@property
	def dev_path_str(self) -> str:
		return self._instance.DevPathStr
	@property
	def dev_str(self) -> str:
		return self._instance.DevStr
	@property
	def entry(self) -> int:
		return self._instance.Entry
	@property
	def hour(self) -> int:
		return self._instance.Hour
	@property
	def hour_str(self) -> str:
		return self._instance.HourStr
	@property
	def lang_str(self) -> str:
		return self._instance.LangStr
	@property
	def min(self) -> int:
		return self._instance.Min
	@property
	def min_str(self) -> str:
		return self._instance.MinStr
	@property
	def month(self) -> int:
		return self._instance.Month
	@property
	def month_str(self) -> str:
		return self._instance.MonthStr
	@property
	def png_str(self) -> str:
		return self._instance.PngStr
	@property
	def sec(self) -> int:
		return self._instance.Sec
	@property
	def sec_str(self) -> str:
		return self._instance.SecStr
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def time_int(self) -> int:
		return self._instance.TimeInt
	@property
	def time_str(self) -> str:
		return self._instance.TimeStr
	@property
	def time_str2(self) -> str:
		return self._instance.TimeStr2
	@property
	def t_int(self) -> int:
		return self._instance.TInt
	@property
	def t_str(self) -> str:
		return self._instance.TStr
	@property
	def year(self) -> int:
		return self._instance.Year
	@property
	def year_str(self) -> str:
		return self._instance.YearStr
