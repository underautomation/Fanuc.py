import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UndoCfgVariableType as undo_cfg_variable_type

class UndoCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type UNDO_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = undo_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def undo_enb(self) -> bool:
		'''Value of variable $UNDO_ENB'''
		return self._instance.UndoEnb

	@property
	def warn_enb(self) -> bool:
		'''Value of variable $WARN_ENB'''
		return self._instance.WarnEnb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UndoCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
