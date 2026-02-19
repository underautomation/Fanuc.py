import typing
from underautomation.fanuc.ftp.variables.user_tool_variable_type import UserToolVariableType
from underautomation.fanuc.ftp.variables.user_ufram_variable_type import UserUframVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UserOffstVariableType as user_offst_variable_type

class UserOffstVariableType(GenericVariableType):
	'''Describes the Fanuc type USER_OFFST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_offst_variable_type()
		else:
			self._instance = _internal

	@property
	def tool_ofst(self) -> typing.List[UserToolVariableType]:
		'''Value of variable $TOOL_OFST'''
		return [UserToolVariableType(x) for x in self._instance.ToolOfst]

	@property
	def uframe_ofst(self) -> typing.List[UserUframVariableType]:
		'''Value of variable $UFRAME_OFST'''
		return [UserUframVariableType(x) for x in self._instance.UframeOfst]

	@property
	def gun_tip_ofs(self) -> typing.List[float]:
		'''Value of variable $GUN_TIP_OFS'''
		return self._instance.GunTipOfs

	@property
	def gun_cyc_ofs(self) -> typing.List[float]:
		'''Value of variable $GUN_CYC_OFS'''
		return self._instance.GunCycOfs

	@property
	def enb_subnum(self) -> typing.List[bool]:
		'''Value of variable $ENB_SUBNUM'''
		return self._instance.EnbSubnum

	@property
	def pre_exe_adv(self) -> bool:
		'''Value of variable $PRE_EXE_ADV'''
		return self._instance.PreExeAdv

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UserOffstVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
