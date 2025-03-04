import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SvInfoVariableType as sv_info_variable_type

class SvInfoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sv_info_variable_type()
		else:
			self._instance = _internal
	@property
	def torque_cmd(self) -> typing.List[float]:
		return self._instance.TorqueCmd
	@property
	def motor_speed(self) -> typing.List[float]:
		return self._instance.MotorSpeed
	@property
	def q_current(self) -> typing.List[float]:
		return self._instance.QCurrent
	@property
	def axis_pos(self) -> typing.List[float]:
		return self._instance.AxisPos
	@property
	def sq_current(self) -> typing.List[float]:
		return self._instance.SqCurrent
	@property
	def cart_pos(self) -> typing.List[float]:
		return self._instance.CartPos
	@property
	def cart_pos_uf(self) -> typing.List[float]:
		return self._instance.CartPosUf
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
