import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiFkeydatVariableType as ui_fkeydat_variable_type

class UiFkeydatVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_FKEYDAT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_fkeydat_variable_type()
		else:
			self._instance = _internal

	@property
	def enb_color(self) -> typing.List[int]:
		'''Value of variable $ENB_COLOR'''
		return self._instance.EnbColor

	@property
	def ps_backcolo(self) -> int:
		'''Value of variable $PS_BACKCOLO'''
		return self._instance.PsBackcolo

	@property
	def backcolor(self) -> typing.List[int]:
		'''Value of variable $BACKCOLOR'''
		return self._instance.Backcolor

	@property
	def forecolor(self) -> typing.List[int]:
		'''Value of variable $FORECOLOR'''
		return self._instance.Forecolor

	@property
	def label(self) -> typing.List[str]:
		'''Value of variable $LABEL'''
		return self._instance.Label

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
		if not isinstance(other, UiFkeydatVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
