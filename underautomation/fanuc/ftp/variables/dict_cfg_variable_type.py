import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DictCfgVariableType as dict_cfg_variable_type

class DictCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dict_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def cache_enb(self) -> bool:
		return self._instance.CacheEnb
	@property
	def cache_size(self) -> int:
		return self._instance.CacheSize
	@property
	def curr_only(self) -> bool:
		return self._instance.CurrOnly
	@property
	def lang_suffix(self) -> str:
		return self._instance.LangSuffix
	@property
	def locale(self) -> int:
		return self._instance.Locale
	@property
	def dummy5(self) -> int:
		return self._instance.Dummy5
	@property
	def dummy6(self) -> int:
		return self._instance.Dummy6
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
