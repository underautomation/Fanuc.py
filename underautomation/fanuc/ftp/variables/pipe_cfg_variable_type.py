import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PipeCfgVariableType as pipe_cfg_variable_type

class PipeCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PIPE_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pipe_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def sectors(self) -> int:
		'''Value of variable $SECTORS'''
		return self._instance.Sectors

	@property
	def formatter(self) -> int:
		'''Value of variable $FORMATTER'''
		return self._instance.Formatter

	@property
	def recordsize(self) -> int:
		'''Value of variable $RECORDSIZE'''
		return self._instance.Recordsize

	@property
	def memtype(self) -> int:
		'''Value of variable $MEMTYPE'''
		return self._instance.Memtype

	@property
	def format(self) -> int:
		'''Value of variable $FORMAT'''
		return self._instance.Format

	@property
	def auxword(self) -> int:
		'''Value of variable $AUXWORD'''
		return self._instance.Auxword

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PipeCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
