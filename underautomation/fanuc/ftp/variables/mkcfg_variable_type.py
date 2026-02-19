import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MkcfgVariableType as mkcfg_variable_type

class MkcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type MKCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mkcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def group_mask(self) -> int:
		'''Value of variable $GROUP_MASK'''
		return self._instance.GroupMask

	@property
	def mb_conflict(self) -> int:
		'''Value of variable $MB_CONFLICT'''
		return self._instance.MbConflict

	@property
	def mb_required(self) -> int:
		'''Value of variable $MB_REQUIRED'''
		return self._instance.MbRequired

	@property
	def mo_conflict(self) -> int:
		'''Value of variable $MO_CONFLICT'''
		return self._instance.MoConflict

	@property
	def mo_required(self) -> int:
		'''Value of variable $MO_REQUIRED'''
		return self._instance.MoRequired

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MkcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
