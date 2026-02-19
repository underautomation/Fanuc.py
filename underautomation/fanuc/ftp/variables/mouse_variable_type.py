import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MouseVariableType as mouse_variable_type

class MouseVariableType(GenericVariableType):
	'''Describes the Fanuc type $MOUSE'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mouse_variable_type()
		else:
			self._instance = _internal

	@property
	def action(self) -> int:
		'''Value of variable $ACTION'''
		return self._instance.Action

	@property
	def button(self) -> int:
		'''Value of variable $BUTTON'''
		return self._instance.Button

	@property
	def row(self) -> int:
		'''Value of variable $ROW'''
		return self._instance.Row

	@property
	def column(self) -> int:
		'''Value of variable $COLUMN'''
		return self._instance.Column

	@property
	def time(self) -> int:
		'''Value of variable $TIME'''
		return self._instance.Time

	@property
	def reserved(self) -> int:
		'''Value of variable $RESERVED'''
		return self._instance.Reserved

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MouseVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
