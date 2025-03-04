import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcssCnstcyVariableType as dcss_cnstcy_variable_type

class DcssCnstcyVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_cnstcy_variable_type()
		else:
			self._instance = _internal
	@property
	def sig1_type(self) -> int:
		return self._instance.Sig1Type
	@property
	def sig1_idx(self) -> int:
		return self._instance.Sig1Idx
	@property
	def sig2_type(self) -> int:
		return self._instance.Sig2Type
	@property
	def sig2_idx(self) -> int:
		return self._instance.Sig2Idx
	@property
	def not_ope(self) -> int:
		return self._instance.NotOpe
	@property
	def time(self) -> int:
		return self._instance.Time
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
