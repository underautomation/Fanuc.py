import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UiMenhisVariableType as ui_menhis_variable_type

class UiMenhisVariableType(GenericVariableType):
	'''Describes the Fanuc type UI_MENHIS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_menhis_variable_type()
		else:
			self._instance = _internal

	@property
	def hist_head(self) -> int:
		'''Value of variable $HIST_HEAD'''
		return self._instance.HistHead

	@property
	def hist_entry(self) -> typing.List[str]:
		'''Value of variable $HIST_ENTRY'''
		return self._instance.HistEntry

	@property
	def dummy2(self) -> int:
		'''Value of variable $DUMMY2'''
		return self._instance.Dummy2

	@property
	def dummy3(self) -> int:
		'''Value of variable $DUMMY3'''
		return self._instance.Dummy3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UiMenhisVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
