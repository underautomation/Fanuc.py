import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ChkResultVariableType as chk_result_variable_type

class ChkResultVariableType(GenericVariableType):
	'''Describes the Fanuc type $CHK_RESULT'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = chk_result_variable_type()
		else:
			self._instance = _internal

	@property
	def evalue_idx(self) -> float:
		'''Value of variable $EVALUE_IDX'''
		return self._instance.EvalueIdx

	@property
	def max_ms_err(self) -> float:
		'''Value of variable $MAX_MS_ERR'''
		return self._instance.MaxMsErr

	@property
	def mean_ms_err(self) -> float:
		'''Value of variable $MEAN_MS_ERR'''
		return self._instance.MeanMsErr

	@property
	def worst_pose(self) -> int:
		'''Value of variable $WORST_POSE'''
		return self._instance.WorstPose

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ChkResultVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
