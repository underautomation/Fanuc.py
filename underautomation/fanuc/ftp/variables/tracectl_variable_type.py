import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TracectlVariableType as tracectl_variable_type

class TracectlVariableType(GenericVariableType):
	'''Describes the Fanuc type TRACECTL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tracectl_variable_type()
		else:
			self._instance = _internal

	@property
	def task_status(self) -> int:
		'''Value of variable $TASK_STATUS'''
		return self._instance.TaskStatus

	@property
	def trc_top_idx(self) -> int:
		'''Value of variable $TRC_TOP_IDX'''
		return self._instance.TrcTopIdx

	@property
	def trc_btm_idx(self) -> int:
		'''Value of variable $TRC_BTM_IDX'''
		return self._instance.TrcBtmIdx

	@property
	def task_id(self) -> int:
		'''Value of variable $TASK_ID'''
		return self._instance.TaskId

	@property
	def dummy4(self) -> int:
		'''Value of variable $DUMMY4'''
		return self._instance.Dummy4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TracectlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
