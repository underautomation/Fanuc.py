import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiPanelnkVariableType as ui_panelnk_variable_type

class UiPanelnkVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_PANELNK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_panelnk_variable_type()
		else:
			self._instance = _internal

	@property
	def help_url(self) -> typing.List[str]:
		'''Value of variable $HELP_URL'''
		return self._instance.HelpUrl

	@property
	def hlp_context(self) -> typing.List[int]:
		'''Value of variable $HLP_CONTEXT'''
		return self._instance.HlpContext

	@property
	def help_flag(self) -> typing.List[int]:
		'''Value of variable $HELP_FLAG'''
		return self._instance.HelpFlag

	@property
	def relv_index(self) -> int:
		'''Value of variable $RELV_INDEX'''
		return self._instance.RelvIndex

	@property
	def relv_url(self) -> typing.List[str]:
		'''Value of variable $RELV_URL'''
		return self._instance.RelvUrl

	@property
	def relv_mtext(self) -> typing.List[str]:
		'''Value of variable $RELV_MTEXT'''
		return self._instance.RelvMtext

	@property
	def relv_contex(self) -> typing.List[int]:
		'''Value of variable $RELV_CONTEX'''
		return self._instance.RelvContex

	@property
	def relv_flags(self) -> typing.List[int]:
		'''Value of variable $RELV_FLAGS'''
		return self._instance.RelvFlags

	@property
	def relv_spid(self) -> typing.List[int]:
		'''Value of variable $RELV_SPID'''
		return self._instance.RelvSpid

	@property
	def relv_scid(self) -> typing.List[int]:
		'''Value of variable $RELV_SCID'''
		return self._instance.RelvScid

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiPanelnkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
