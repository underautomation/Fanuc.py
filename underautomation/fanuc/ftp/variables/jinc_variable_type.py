import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import JincVariableType as jinc_variable_type

class JincVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jinc_variable_type()
		else:
			self._instance = _internal
	@property
	def jinc_enb(self) -> bool:
		return self._instance.JincEnb
	@property
	def jog_incre(self) -> int:
		return self._instance.JogIncre
	@property
	def incre_trans(self) -> typing.List[float]:
		return self._instance.IncreTrans
	@property
	def incre_jnt(self) -> typing.List[float]:
		return self._instance.IncreJnt
	@property
	def flex_i(self) -> typing.List[int]:
		return self._instance.FlexI
	@property
	def flex_r(self) -> typing.List[float]:
		return self._instance.FlexR
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
