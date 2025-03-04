import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UserInfoVariableType as user_info_variable_type

class UserInfoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_info_variable_type()
		else:
			self._instance = _internal
	@property
	def usr_prog(self) -> str:
		return self._instance.UsrProg
	@property
	def task_id(self) -> int:
		return self._instance.TaskId
	@property
	def usr_posidx(self) -> int:
		return self._instance.UsrPosidx
	@property
	def usr_pr_use(self) -> bool:
		return self._instance.UsrPrUse
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
