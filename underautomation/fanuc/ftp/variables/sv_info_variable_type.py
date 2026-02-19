import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SvInfoVariableType as sv_info_variable_type

class SvInfoVariableType(GenericVariableType):
	'''Describes the Fanuc type SV_INFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sv_info_variable_type()
		else:
			self._instance = _internal

	@property
	def torque_cmd(self) -> typing.List[float]:
		'''Value of variable $TORQUE_CMD'''
		return self._instance.TorqueCmd

	@property
	def motor_speed(self) -> typing.List[float]:
		'''Value of variable $MOTOR_SPEED'''
		return self._instance.MotorSpeed

	@property
	def q_current(self) -> typing.List[float]:
		'''Value of variable $Q_CURRENT'''
		return self._instance.QCurrent

	@property
	def axis_pos(self) -> typing.List[float]:
		'''Value of variable $AXIS_POS'''
		return self._instance.AxisPos

	@property
	def sq_current(self) -> typing.List[float]:
		'''Value of variable $SQ_CURRENT'''
		return self._instance.SqCurrent

	@property
	def cart_pos(self) -> typing.List[float]:
		'''Value of variable $CART_POS'''
		return self._instance.CartPos

	@property
	def cart_pos_uf(self) -> typing.List[float]:
		'''Value of variable $CART_POS_UF'''
		return self._instance.CartPosUf

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SvInfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
