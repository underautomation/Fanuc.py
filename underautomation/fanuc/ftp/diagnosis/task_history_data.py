import typing
from underautomation.fanuc.common.program_type import ProgramType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Diagnosis import TaskHistoryData as task_history_data

class TaskHistoryData:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_history_data()
		else:
			self._instance = _internal
	@property
	def routine_depth(self) -> int:
		return self._instance.RoutineDepth
	@routine_depth.setter
	def routine_depth(self, value: int):
		self._instance.RoutineDepth = value
	@property
	def routine_name(self) -> str:
		return self._instance.RoutineName
	@routine_name.setter
	def routine_name(self, value: str):
		self._instance.RoutineName = value
	@property
	def line_number(self) -> int:
		return self._instance.LineNumber
	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value
	@property
	def program_name(self) -> str:
		return self._instance.ProgramName
	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value
	@property
	def program_type(self) -> ProgramType:
		return ProgramType(self._instance.ProgramType)
	@program_type.setter
	def program_type(self, value: ProgramType):
		self._instance.ProgramType = value
