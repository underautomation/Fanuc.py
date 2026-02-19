import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DryrunPortVariableType as dryrun_port_variable_type

class DryrunPortVariableType(GenericVariableType):
	'''Describes the Fanuc type DRYRUN_PORT_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dryrun_port_variable_type()
		else:
			self._instance = _internal

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def fst_idx(self) -> int:
		'''Value of variable $FST_IDX'''
		return self._instance.FstIdx

	@property
	def lst_idx(self) -> int:
		'''Value of variable $LST_IDX'''
		return self._instance.LstIdx

	@property
	def static_port(self) -> bool:
		'''Value of variable $STATIC_PORT'''
		return self._instance.StaticPort

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DryrunPortVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
