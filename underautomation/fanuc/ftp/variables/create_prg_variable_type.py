import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CreatePrgVariableType as create_prg_variable_type

class CreatePrgVariableType(GenericVariableType):
	'''Describes the Fanuc type $CREATE_PRG'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = create_prg_variable_type()
		else:
			self._instance = _internal

	@property
	def axis_flag(self) -> typing.List[bool]:
		'''Value of variable $AXIS_FLAG'''
		return self._instance.AxisFlag

	@property
	def num_axs_rep(self) -> int:
		'''Value of variable $NUM_AXS_REP'''
		return self._instance.NumAxsRep

	@property
	def swing_ang(self) -> typing.List[float]:
		'''Value of variable $SWING_ANG'''
		return self._instance.SwingAng

	@property
	def num_ms_pose(self) -> int:
		'''Value of variable $NUM_MS_POSE'''
		return self._instance.NumMsPose

	@property
	def base_pose(self) -> typing.List[float]:
		'''Value of variable $BASE_POSE'''
		return self._instance.BasePose

	@property
	def evalue_idx(self) -> typing.List[float]:
		'''Value of variable $EVALUE_IDX'''
		return self._instance.EvalueIdx

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CreatePrgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
