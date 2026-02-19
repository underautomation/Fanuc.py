import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DictCfgVariableType as dict_cfg_variable_type

class DictCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DICT_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dict_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def cache_enb(self) -> bool:
		'''Value of variable $CACHE_ENB'''
		return self._instance.CacheEnb

	@property
	def cache_size(self) -> int:
		'''Value of variable $CACHE_SIZE'''
		return self._instance.CacheSize

	@property
	def curr_only(self) -> bool:
		'''Value of variable $CURR_ONLY'''
		return self._instance.CurrOnly

	@property
	def lang_suffix(self) -> str:
		'''Value of variable $LANG_SUFFIX'''
		return self._instance.LangSuffix

	@property
	def locale(self) -> int:
		'''Value of variable $LOCALE'''
		return self._instance.Locale

	@property
	def dummy5(self) -> int:
		'''Value of variable $DUMMY5'''
		return self._instance.Dummy5

	@property
	def dummy6(self) -> int:
		'''Value of variable $DUMMY6'''
		return self._instance.Dummy6

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DictCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
