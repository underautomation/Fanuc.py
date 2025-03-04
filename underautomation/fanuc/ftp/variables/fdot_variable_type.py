import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FdotVariableType as fdot_variable_type

class FdotVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fdot_variable_type()
		else:
			self._instance = _internal
	@property
	def num_iteratio(self) -> int:
		return self._instance.NumIteratio
	@property
	def equal_thres(self) -> float:
		return self._instance.EqualThres
	@property
	def area_thres(self) -> float:
		return self._instance.AreaThres
	@property
	def angle_thres(self) -> float:
		return self._instance.AngleThres
	@property
	def diff_pitch(self) -> float:
		return self._instance.DiffPitch
	@property
	def conv_thres(self) -> float:
		return self._instance.ConvThres
	@property
	def wp_rate(self) -> float:
		return self._instance.WPRate
	@property
	def residual_err(self) -> float:
		return self._instance.ResidualErr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
