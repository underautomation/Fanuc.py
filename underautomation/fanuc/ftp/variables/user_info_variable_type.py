import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UserInfoVariableType as user_info_variable_type

class UserInfoVariableType(GenericVariableType):
	'''Describes the Fanuc type USER_INFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_info_variable_type()
		else:
			self._instance = _internal

	@property
	def usr_prog(self) -> str:
		'''Value of variable $USR_PROG'''
		return self._instance.UsrProg

	@property
	def task_id(self) -> int:
		'''Value of variable $TASK_ID'''
		return self._instance.TaskId

	@property
	def usr_posidx(self) -> int:
		'''Value of variable $USR_POSIDX'''
		return self._instance.UsrPosidx

	@property
	def usr_pr_use(self) -> bool:
		'''Value of variable $USR_PR_USE'''
		return self._instance.UsrPrUse

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UserInfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
