import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VrtdFiltVariableType as vrtd_filt_variable_type

class VrtdFiltVariableType(GenericVariableType):
	'''Describes the Fanuc type VRTD_FILT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vrtd_filt_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def dummy4(self) -> int:
		'''Value of variable $DUMMY4'''
		return self._instance.Dummy4

	@property
	def tool_type(self) -> int:
		'''Value of variable $TOOL_TYPE'''
		return self._instance.ToolType

	@property
	def words(self) -> str:
		'''Value of variable $WORDS'''
		return self._instance.Words

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VrtdFiltVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
