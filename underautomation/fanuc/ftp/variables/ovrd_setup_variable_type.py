import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import OvrdSetupVariableType as ovrd_setup_variable_type

class OvrdSetupVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ovrd_setup_variable_type()
		else:
			self._instance = _internal
	@property
	def ovrd_num(self) -> int:
		return self._instance.OvrdNum
	@property
	def override(self) -> typing.List[int]:
		return self._instance.Override
	@property
	def ovrd_num_s(self) -> int:
		return self._instance.OvrdNumS
	@property
	def override_s(self) -> typing.List[int]:
		return self._instance.OverrideS
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
