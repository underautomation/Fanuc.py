import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiFctnfavVariableType as ui_fctnfav_variable_type

class UiFctnfavVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_FCTNFAV_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_fctnfav_variable_type()
		else:
			self._instance = _internal

	@property
	def pwd_spid(self) -> int:
		'''Value of variable $PWD_SPID'''
		return self._instance.PwdSpid

	@property
	def pwd_scid(self) -> int:
		'''Value of variable $PWD_SCID'''
		return self._instance.PwdScid

	@property
	def press_text(self) -> str:
		'''Value of variable $PRESS_TEXT'''
		return self._instance.PressText

	@property
	def press_icon(self) -> str:
		'''Value of variable $PRESS_ICON'''
		return self._instance.PressIcon

	@property
	def press_ptr(self) -> int:
		'''Value of variable $PRESS_PTR'''
		return self._instance.PressPtr

	@property
	def releas_text(self) -> str:
		'''Value of variable $RELEAS_TEXT'''
		return self._instance.ReleasText

	@property
	def releas_icon(self) -> str:
		'''Value of variable $RELEAS_ICON'''
		return self._instance.ReleasIcon

	@property
	def releas_ptr(self) -> int:
		'''Value of variable $RELEAS_PTR'''
		return self._instance.ReleasPtr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiFctnfavVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
