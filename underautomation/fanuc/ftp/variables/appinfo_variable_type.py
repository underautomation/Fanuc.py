import typing
from underautomation.fanuc.ftp.variables.appinfoeq_variable_type import AppinfoeqVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AppinfoVariableType as appinfo_variable_type

class AppinfoVariableType(GenericVariableType):
	'''Describes the Fanuc type APPINFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = appinfo_variable_type()
		else:
			self._instance = _internal

	@property
	def data(self) -> typing.List[int]:
		'''Value of variable $DATA'''
		return self._instance.Data

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def equip(self) -> typing.List[AppinfoeqVariableType]:
		'''Value of variable $EQUIP'''
		return [AppinfoeqVariableType(x) for x in self._instance.Equip]

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def name_ovrd(self) -> bool:
		'''Value of variable $NAME_OVRD'''
		return self._instance.NameOvrd

	@property
	def version(self) -> int:
		'''Value of variable $VERSION'''
		return self._instance.Version

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AppinfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
