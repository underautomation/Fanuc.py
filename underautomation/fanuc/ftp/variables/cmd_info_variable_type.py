import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CmdInfoVariableType as cmd_info_variable_type

class CmdInfoVariableType(GenericVariableType):
	'''Describes the Fanuc type CMD_INFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cmd_info_variable_type()
		else:
			self._instance = _internal

	@property
	def trq_cmd(self) -> typing.List[float]:
		'''Value of variable $TRQ_CMD'''
		return self._instance.TrqCmd

	@property
	def jnt_pos(self) -> typing.List[float]:
		'''Value of variable $JNT_POS'''
		return self._instance.JntPos

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
		if not isinstance(other, CmdInfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
