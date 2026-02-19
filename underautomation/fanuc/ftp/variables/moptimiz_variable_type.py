import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MoptimizVariableType as moptimiz_variable_type

class MoptimizVariableType(GenericVariableType):
	'''Describes the Fanuc type MOPTIMIZ_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = moptimiz_variable_type()
		else:
			self._instance = _internal

	@property
	def data_out(self) -> bool:
		'''Value of variable $DATA_OUT'''
		return self._instance.DataOut

	@property
	def cnt_dyn_acc(self) -> typing.List[bool]:
		'''Value of variable $CNT_DYN_ACC'''
		return self._instance.CntDynAcc

	@property
	def dd_motor1(self) -> typing.List[bool]:
		'''Value of variable $DD_MOTOR1'''
		return self._instance.DdMotor1

	@property
	def update_map3(self) -> typing.List[bool]:
		'''Value of variable $UPDATE_MAP3'''
		return self._instance.UpdateMap3

	@property
	def update_map7(self) -> bool:
		'''Value of variable $UPDATE_MAP7'''
		return self._instance.UpdateMap7

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MoptimizVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
