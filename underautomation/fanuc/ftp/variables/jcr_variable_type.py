import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import JcrVariableType as jcr_variable_type

class JcrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jcr_variable_type()
		else:
			self._instance = _internal
	@property
	def jog_gp(self) -> int:
		return self._instance.JogGp
	@property
	def jog_subgp(self) -> bool:
		return self._instance.JogSubgp
	@property
	def jog_dct_nam(self) -> typing.List[int]:
		return self._instance.JogDctNam
	@property
	def jog_dct_ele(self) -> typing.List[int]:
		return self._instance.JogDctEle
	@property
	def mp_jog(self) -> int:
		return self._instance.MpJog
	@property
	def spjog_msk(self) -> int:
		return self._instance.SpjogMsk
	@property
	def ijog_key(self) -> int:
		return self._instance.IjogKey
	@property
	def ijog_stat(self) -> int:
		return self._instance.IjogStat
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
