import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiUsrviewVariableType as ui_usrview_variable_type

class UiUsrviewVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_USRVIEW_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_usrview_variable_type()
		else:
			self._instance = _internal

	@property
	def menu(self) -> str:
		'''Value of variable $MENU'''
		return self._instance.Menu

	@property
	def config(self) -> str:
		'''Value of variable $CONFIG'''
		return self._instance.Config

	@property
	def focus(self) -> str:
		'''Value of variable $FOCUS'''
		return self._instance.Focus

	@property
	def prim(self) -> str:
		'''Value of variable $PRIM'''
		return self._instance.Prim

	@property
	def dual(self) -> str:
		'''Value of variable $DUAL'''
		return self._instance.Dual

	@property
	def triple(self) -> str:
		'''Value of variable $TRIPLE'''
		return self._instance.Triple

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiUsrviewVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
