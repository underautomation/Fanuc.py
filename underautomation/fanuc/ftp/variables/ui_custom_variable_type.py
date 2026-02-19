import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiCustomVariableType as ui_custom_variable_type

class UiCustomVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_CUSTOM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_custom_variable_type()
		else:
			self._instance = _internal

	@property
	def start_spid(self) -> int:
		'''Value of variable $START_SPID'''
		return self._instance.StartSpid

	@property
	def start_scid(self) -> int:
		'''Value of variable $START_SCID'''
		return self._instance.StartScid

	@property
	def config_page(self) -> typing.List[str]:
		'''Value of variable $CONFIG_PAGE'''
		return self._instance.ConfigPage

	@property
	def device_page(self) -> typing.List[str]:
		'''Value of variable $DEVICE_PAGE'''
		return self._instance.DevicePage

	@property
	def screen_def(self) -> typing.List[int]:
		'''Value of variable $SCREEN_DEF'''
		return self._instance.ScreenDef

	@property
	def config_pane(self) -> typing.List[int]:
		'''Value of variable $CONFIG_PANE'''
		return self._instance.ConfigPane

	@property
	def flags(self) -> typing.List[int]:
		'''Value of variable $FLAGS'''
		return self._instance.Flags

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiCustomVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
