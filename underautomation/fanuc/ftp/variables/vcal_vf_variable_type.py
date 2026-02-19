import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcalVfVariableType as vcal_vf_variable_type

class VcalVfVariableType(GenericVariableType):
	'''Describes the Fanuc type VCAL_VF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcal_vf_variable_type()
		else:
			self._instance = _internal

	@property
	def trgt_val_vt(self) -> float:
		'''Value of variable TRGT_VAL_VT'''
		return self._instance.TrgtValVt

	@property
	def trgt_val_hz(self) -> float:
		'''Value of variable TRGT_VAL_HZ'''
		return self._instance.TrgtValHz

	@property
	def trgt_val_s(self) -> float:
		'''Value of variable TRGT_VAL_S'''
		return self._instance.TrgtValS

	@property
	def vfb_mat(self) -> typing.List[float]:
		'''Value of variable VFB_MAT'''
		return self._instance.VfbMat

	@property
	def mat_size(self) -> float:
		'''Value of variable MAT_SIZE'''
		return self._instance.MatSize

	@property
	def vfb_tol(self) -> float:
		'''Value of variable VFB_TOL'''
		return self._instance.VfbTol

	@property
	def vfb_limit(self) -> float:
		'''Value of variable VFB_LIMIT'''
		return self._instance.VfbLimit

	@property
	def max_loop(self) -> int:
		'''Value of variable MAX_LOOP'''
		return self._instance.MaxLoop

	@property
	def hand_eye(self) -> bool:
		'''Value of variable HAND_EYE'''
		return self._instance.HandEye

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcalVfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
