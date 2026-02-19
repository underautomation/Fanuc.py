import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UserWorkVariableType as user_work_variable_type

class UserWorkVariableType(GenericVariableType):
	'''Describes the Fanuc type USER_WORK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_work_variable_type()
		else:
			self._instance = _internal

	@property
	def task_id(self) -> typing.List[int]:
		'''Value of variable $TASK_ID'''
		return self._instance.TaskId

	@property
	def wait_usradv(self) -> typing.List[int]:
		'''Value of variable $WAIT_USRADV'''
		return self._instance.WaitUsradv

	@property
	def adv_db_id(self) -> typing.List[int]:
		'''Value of variable $ADV_DB_ID'''
		return self._instance.AdvDbId

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UserWorkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
