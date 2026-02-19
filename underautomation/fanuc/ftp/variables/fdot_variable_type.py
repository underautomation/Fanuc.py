import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FdotVariableType as fdot_variable_type

class FdotVariableType(GenericVariableType):
	'''Describes the Fanuc type FDOT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fdot_variable_type()
		else:
			self._instance = _internal

	@property
	def num_iteratio(self) -> int:
		'''Value of variable NUM_ITERATIO'''
		return self._instance.NumIteratio

	@property
	def equal_thres(self) -> float:
		'''Value of variable EQUAL_THRES'''
		return self._instance.EqualThres

	@property
	def area_thres(self) -> float:
		'''Value of variable AREA_THRES'''
		return self._instance.AreaThres

	@property
	def angle_thres(self) -> float:
		'''Value of variable ANGLE_THRES'''
		return self._instance.AngleThres

	@property
	def diff_pitch(self) -> float:
		'''Value of variable DIFF_PITCH'''
		return self._instance.DiffPitch

	@property
	def conv_thres(self) -> float:
		'''Value of variable CONV_THRES'''
		return self._instance.ConvThres

	@property
	def wp_rate(self) -> float:
		'''Value of variable W_P_RATE'''
		return self._instance.WPRate

	@property
	def residual_err(self) -> float:
		'''Value of variable RESIDUAL_ERR'''
		return self._instance.ResidualErr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FdotVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
