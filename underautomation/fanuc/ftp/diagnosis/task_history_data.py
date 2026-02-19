import typing
from underautomation.fanuc.common.program_type import ProgramType
from UnderAutomation.Fanuc.Ftp.Diagnosis import TaskHistoryData as task_history_data
from UnderAutomation.Fanuc.Common import ProgramType as program_type

class TaskHistoryData:
	'''Represents one frame in the task's call stack.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_history_data()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def routine_depth(self) -> int:
		'''Depth of the routine in the call stack.'''
		return self._instance.RoutineDepth

	@routine_depth.setter
	def routine_depth(self, value: int):
		self._instance.RoutineDepth = value

	@property
	def routine_name(self) -> str:
		'''Name of the routine.'''
		return self._instance.RoutineName

	@routine_name.setter
	def routine_name(self, value: str):
		self._instance.RoutineName = value

	@property
	def line_number(self) -> int:
		'''Line number currently being executed.'''
		return self._instance.LineNumber

	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value

	@property
	def program_name(self) -> str:
		'''Name of the program containing the routine.'''
		return self._instance.ProgramName

	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value

	@property
	def program_type(self) -> ProgramType:
		'''Type of the program (TP, Karel, etc.).'''
		return ProgramType(int(self._instance.ProgramType))

	@program_type.setter
	def program_type(self, value: ProgramType):
		self._instance.ProgramType = program_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TaskHistoryData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
