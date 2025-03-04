import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcmrTrgtVariableType as vcmr_trgt_variable_type

class VcmrTrgtVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcmr_trgt_variable_type()
		else:
			self._instance = _internal
	@property
	def target_pnt(self) -> typing.List[float]:
		return self._instance.TargetPnt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
