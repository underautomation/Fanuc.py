import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MaxPldCalVariableType as max_pld_cal_variable_type

class MaxPldCalVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = max_pld_cal_variable_type()
		else:
			self._instance = _internal
	@property
	def aa(self) -> float:
		return self._instance.Aa
	@property
	def bb(self) -> float:
		return self._instance.Bb
	@property
	def cc(self) -> float:
		return self._instance.Cc
	@property
	def dd(self) -> float:
		return self._instance.Dd
	@property
	def ee(self) -> float:
		return self._instance.Ee
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
