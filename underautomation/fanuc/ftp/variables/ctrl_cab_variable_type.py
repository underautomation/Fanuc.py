import typing
from underautomation.fanuc.ftp.variables.amp_coef_variable_type import AmpCoefVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CtrlCabVariableType as ctrl_cab_variable_type

class CtrlCabVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ctrl_cab_variable_type()
		else:
			self._instance = _internal
	@property
	def trans_a(self) -> float:
		return self._instance.TransA
	@property
	def idle_pwr(self) -> float:
		return self._instance.IdlePwr
	@property
	def amp_coefb(self) -> float:
		return self._instance.AmpCoefb
	@property
	def sv_num(self) -> int:
		return self._instance.SvNum
	@property
	def sv_amp(self) -> typing.List[AmpCoefVariableType]:
		return [AmpCoefVariableType(x) for x in self._instance.SvAmp]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
