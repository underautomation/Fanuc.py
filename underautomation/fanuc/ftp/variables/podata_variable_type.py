import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PodataVariableType as podata_variable_type

class PodataVariableType(GenericVariableType):
	'''Describes the Fanuc type PODATA_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = podata_variable_type()
		else:
			self._instance = _internal

	@property
	def overrun_cnt(self) -> int:
		'''Value of variable $OVERRUN_CNT'''
		return self._instance.OverrunCnt

	@property
	def cur_index(self) -> int:
		'''Value of variable $CUR_INDEX'''
		return self._instance.CurIndex

	@property
	def program_id(self) -> typing.List[int]:
		'''Value of variable $PROGRAM_ID'''
		return self._instance.ProgramId

	@property
	def line_no(self) -> typing.List[int]:
		'''Value of variable $LINE_NO'''
		return self._instance.LineNo

	@property
	def overrun_itp(self) -> typing.List[int]:
		'''Value of variable $OVERRUN_ITP'''
		return self._instance.OverrunItp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PodataVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
