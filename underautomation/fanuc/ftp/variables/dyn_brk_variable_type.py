import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DynBrkVariableType as dyn_brk_variable_type

class DynBrkVariableType(GenericVariableType):
	'''Describes the Fanuc type DYN_BRK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dyn_brk_variable_type()
		else:
			self._instance = _internal

	@property
	def di_idx(self) -> int:
		'''Value of variable $DI_IDX'''
		return self._instance.DiIdx

	@property
	def do_idx(self) -> int:
		'''Value of variable $DO_IDX'''
		return self._instance.DoIdx

	@property
	def brk_msk(self) -> int:
		'''Value of variable $BRK_MSK'''
		return self._instance.BrkMsk

	@property
	def fltr_if(self) -> int:
		'''Value of variable $FLTR_IF'''
		return self._instance.FltrIf

	@property
	def use_opdi(self) -> bool:
		'''Value of variable $USE_OPDI'''
		return self._instance.UseOpdi

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DynBrkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
