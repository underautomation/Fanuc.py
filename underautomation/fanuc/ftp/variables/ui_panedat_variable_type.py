import typing
from underautomation.fanuc.ftp.variables.mouse_variable_type import MouseVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiPanedatVariableType as ui_panedat_variable_type

class UiPanedatVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_PANEDAT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_panedat_variable_type()
		else:
			self._instance = _internal

	@property
	def pageurl(self) -> str:
		'''Value of variable $PAGEURL'''
		return self._instance.Pageurl

	@property
	def frame(self) -> str:
		'''Value of variable $FRAME'''
		return self._instance.Frame

	@property
	def helpurl(self) -> str:
		'''Value of variable $HELPURL'''
		return self._instance.Helpurl

	@property
	def parameter1(self) -> str:
		'''Value of variable $PARAMETER1'''
		return self._instance.Parameter1

	@property
	def parameter2(self) -> str:
		'''Value of variable $PARAMETER2'''
		return self._instance.Parameter2

	@property
	def parameter3(self) -> str:
		'''Value of variable $PARAMETER3'''
		return self._instance.Parameter3

	@property
	def parameter4(self) -> str:
		'''Value of variable $PARAMETER4'''
		return self._instance.Parameter4

	@property
	def parameter5(self) -> str:
		'''Value of variable $PARAMETER5'''
		return self._instance.Parameter5

	@property
	def parameter6(self) -> str:
		'''Value of variable $PARAMETER6'''
		return self._instance.Parameter6

	@property
	def parameter7(self) -> str:
		'''Value of variable $PARAMETER7'''
		return self._instance.Parameter7

	@property
	def parameter8(self) -> str:
		'''Value of variable $PARAMETER8'''
		return self._instance.Parameter8

	@property
	def interval(self) -> int:
		'''Value of variable $INTERVAL'''
		return self._instance.Interval

	@property
	def panestate(self) -> int:
		'''Value of variable $PANESTATE'''
		return self._instance.Panestate

	@property
	def dummy14(self) -> int:
		'''Value of variable $DUMMY14'''
		return self._instance.Dummy14

	@property
	def mouse(self) -> MouseVariableType:
		'''Value of variable $MOUSE'''
		return MouseVariableType(self._instance.Mouse)

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiPanedatVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
