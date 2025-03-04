import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcalVfVariableType as vcal_vf_variable_type

class VcalVfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_vf_variable_type()
		else:
			self._instance = _internal
	@property
	def trgt_val_vt(self) -> float:
		return self._instance.TrgtValVt
	@property
	def trgt_val_hz(self) -> float:
		return self._instance.TrgtValHz
	@property
	def trgt_val_s(self) -> float:
		return self._instance.TrgtValS
	@property
	def vfb_mat(self) -> typing.List[float]:
		return self._instance.VfbMat
	@property
	def mat_size(self) -> float:
		return self._instance.MatSize
	@property
	def vfb_tol(self) -> float:
		return self._instance.VfbTol
	@property
	def vfb_limit(self) -> float:
		return self._instance.VfbLimit
	@property
	def max_loop(self) -> int:
		return self._instance.MaxLoop
	@property
	def hand_eye(self) -> bool:
		return self._instance.HandEye
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
