import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiTopmenuVariableType as ui_topmenu_variable_type

class UiTopmenuVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_TOPMENU_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_topmenu_variable_type()
		else:
			self._instance = _internal

	@property
	def pwd_access(self) -> int:
		'''Value of variable $PWD_ACCESS'''
		return self._instance.PwdAccess

	@property
	def dummy8(self) -> int:
		'''Value of variable $DUMMY8'''
		return self._instance.Dummy8

	@property
	def dummy(self) -> int:
		'''Value of variable $DUMMY'''
		return self._instance.Dummy

	@property
	def title(self) -> str:
		'''Value of variable $TITLE'''
		return self._instance.Title

	@property
	def label(self) -> str:
		'''Value of variable $LABEL'''
		return self._instance.Label

	@property
	def text(self) -> typing.List[str]:
		'''Value of variable $TEXT'''
		return self._instance.Text

	@property
	def icon(self) -> typing.List[str]:
		'''Value of variable $ICON'''
		return self._instance.Icon

	@property
	def url(self) -> typing.List[str]:
		'''Value of variable $URL'''
		return self._instance.Url

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiTopmenuVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
