import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AmpCoefVariableType as amp_coef_variable_type

class AmpCoefVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = amp_coef_variable_type()
		else:
			self._instance = _internal
	@property
	def coef_a(self) -> typing.List[float]:
		return self._instance.CoefA
	@property
	def coef_c(self) -> float:
		return self._instance.CoefC
	@property
	def mask(self) -> int:
		return self._instance.Mask
	@property
	def dual_mask(self) -> int:
		return self._instance.DualMask
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
