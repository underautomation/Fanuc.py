import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import LnDispVariableType as ln_disp_variable_type

class LnDispVariableType(GenericVariableType):
	'''Describes the Fanuc type LN_DISP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ln_disp_variable_type()
		else:
			self._instance = _internal

	@property
	def hide_line_n(self) -> bool:
		'''Value of variable $HIDE_LINE_N'''
		return self._instance.HideLineN

	@property
	def disp_menu(self) -> bool:
		'''Value of variable $DISP_MENU'''
		return self._instance.DispMenu

	@property
	def hide_parln(self) -> bool:
		'''Value of variable $HIDE_PARLN'''
		return self._instance.HideParln

	@property
	def hide_dauln(self) -> bool:
		'''Value of variable $HIDE_DAULN'''
		return self._instance.HideDauln

	@property
	def head_parent(self) -> str:
		'''Value of variable $HEAD_PARENT'''
		return self._instance.HeadParent

	@property
	def head_daught(self) -> str:
		'''Value of variable $HEAD_DAUGHT'''
		return self._instance.HeadDaught

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LnDispVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
