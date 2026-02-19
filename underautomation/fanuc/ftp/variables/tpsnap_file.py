import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import TpsnapFile as tpsnap_file

class TpsnapFile(GenericVariableFile):
	'''Describes the Fanuc variable file tpsnap.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpsnap_file()
		else:
			self._instance = _internal

	@property
	def day(self) -> int:
		'''Value of variable DAY'''
		return self._instance.Day

	@property
	def day_str(self) -> str:
		'''Value of variable DAY_STR'''
		return self._instance.DayStr

	@property
	def dev_path_str(self) -> str:
		'''Value of variable DEV_PATH_STR'''
		return self._instance.DevPathStr

	@property
	def dev_str(self) -> str:
		'''Value of variable DEV_STR'''
		return self._instance.DevStr

	@property
	def entry(self) -> int:
		'''Value of variable ENTRY'''
		return self._instance.Entry

	@property
	def hour(self) -> int:
		'''Value of variable HOUR'''
		return self._instance.Hour

	@property
	def hour_str(self) -> str:
		'''Value of variable HOUR_STR'''
		return self._instance.HourStr

	@property
	def lang_str(self) -> str:
		'''Value of variable LANG_STR'''
		return self._instance.LangStr

	@property
	def min(self) -> int:
		'''Value of variable MIN'''
		return self._instance.Min

	@property
	def min_str(self) -> str:
		'''Value of variable MIN_STR'''
		return self._instance.MinStr

	@property
	def month(self) -> int:
		'''Value of variable MONTH'''
		return self._instance.Month

	@property
	def month_str(self) -> str:
		'''Value of variable MONTH_STR'''
		return self._instance.MonthStr

	@property
	def png_str(self) -> str:
		'''Value of variable PNG_STR'''
		return self._instance.PngStr

	@property
	def sec(self) -> int:
		'''Value of variable SEC'''
		return self._instance.Sec

	@property
	def sec_str(self) -> str:
		'''Value of variable SEC_STR'''
		return self._instance.SecStr

	@property
	def status(self) -> int:
		'''Value of variable STATUS'''
		return self._instance.Status

	@property
	def time_int(self) -> int:
		'''Value of variable TIME_INT'''
		return self._instance.TimeInt

	@property
	def time_str(self) -> str:
		'''Value of variable TIME_STR'''
		return self._instance.TimeStr

	@property
	def time_str2(self) -> str:
		'''Value of variable TIME_STR2'''
		return self._instance.TimeStr2

	@property
	def t_int(self) -> int:
		'''Value of variable T_INT'''
		return self._instance.TInt

	@property
	def t_str(self) -> str:
		'''Value of variable T_STR'''
		return self._instance.TStr

	@property
	def year(self) -> int:
		'''Value of variable YEAR'''
		return self._instance.Year

	@property
	def year_str(self) -> str:
		'''Value of variable YEAR_STR'''
		return self._instance.YearStr

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpsnapFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
