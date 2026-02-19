import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import LogBuffVariableType as log_buff_variable_type

class LogBuffVariableType(GenericVariableType):
	'''Describes the Fanuc type LOG_BUFF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_buff_variable_type()
		else:
			self._instance = _internal

	@property
	def title(self) -> str:
		'''Value of variable $TITLE'''
		return self._instance.Title

	@property
	def size(self) -> int:
		'''Value of variable $SIZE'''
		return self._instance.Size

	@property
	def mem_type(self) -> int:
		'''Value of variable $MEM_TYPE'''
		return self._instance.MemType

	@property
	def visible(self) -> bool:
		'''Value of variable $VISIBLE'''
		return self._instance.Visible

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogBuffVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
