import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SbrVariableType as sbr_variable_type

class SbrVariableType(GenericVariableType):
	'''Describes the Fanuc type SBR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sbr_variable_type()
		else:
			self._instance = _internal

	@property
	def svmtr_id(self) -> int:
		'''Value of variable $SVMTR_ID'''
		return self._instance.SvmtrId

	@property
	def robot_id(self) -> str:
		'''Value of variable $ROBOT_ID'''
		return self._instance.RobotId

	@property
	def grp_num(self) -> int:
		'''Value of variable $GRP_NUM'''
		return self._instance.GrpNum

	@property
	def axis_num(self) -> int:
		'''Value of variable $AXIS_NUM'''
		return self._instance.AxisNum

	@property
	def mtr_id(self) -> str:
		'''Value of variable $MTR_ID'''
		return self._instance.MtrId

	@property
	def mtr_inf_id(self) -> str:
		'''Value of variable $MTR_INF_ID'''
		return self._instance.MtrInfId

	@property
	def sv_param_id(self) -> str:
		'''Value of variable $SV_PARAM_ID'''
		return self._instance.SvParamId

	@property
	def param(self) -> typing.List[int]:
		'''Value of variable $PARAM'''
		return self._instance.Param

	@property
	def mot_spd_lim(self) -> int:
		'''Value of variable $MOT_SPD_LIM'''
		return self._instance.MotSpdLim

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SbrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
