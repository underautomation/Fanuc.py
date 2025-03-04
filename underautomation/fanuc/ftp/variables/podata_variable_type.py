import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PodataVariableType as podata_variable_type

class PodataVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = podata_variable_type()
		else:
			self._instance = _internal
	@property
	def overrun_cnt(self) -> int:
		return self._instance.OverrunCnt
	@property
	def cur_index(self) -> int:
		return self._instance.CurIndex
	@property
	def program_id(self) -> typing.List[int]:
		return self._instance.ProgramId
	@property
	def line_no(self) -> typing.List[int]:
		return self._instance.LineNo
	@property
	def overrun_itp(self) -> typing.List[int]:
		return self._instance.OverrunItp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
