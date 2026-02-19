import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TvOutputVariableType as tv_output_variable_type

class TvOutputVariableType(GenericVariableType):
	'''Describes the Fanuc type TV_OUTPUT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tv_output_variable_type()
		else:
			self._instance = _internal

	@property
	def selected(self) -> typing.List[str]:
		'''Value of variable $SELECTED'''
		return self._instance.Selected

	@property
	def datatype(self) -> typing.List[int]:
		'''Value of variable $DATATYPE'''
		return self._instance.Datatype

	@property
	def state(self) -> typing.List[str]:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def cmd_status(self) -> typing.List[int]:
		'''Value of variable $CMD_STATUS'''
		return self._instance.CmdStatus

	@property
	def tempint(self) -> typing.List[int]:
		'''Value of variable $TEMPINT'''
		return self._instance.Tempint

	@property
	def selectedmod(self) -> typing.List[str]:
		'''Value of variable $SELECTEDMOD'''
		return self._instance.Selectedmod

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TvOutputVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
