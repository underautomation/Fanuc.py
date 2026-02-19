import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SscbkVariableType as sscbk_variable_type

class SscbkVariableType(GenericVariableType):
	'''Describes the Fanuc type SSCBK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sscbk_variable_type()
		else:
			self._instance = _internal

	@property
	def frommx(self) -> int:
		'''Value of variable $FROMMX'''
		return self._instance.Frommx

	@property
	def cmosmx(self) -> int:
		'''Value of variable $CMOSMX'''
		return self._instance.Cmosmx

	@property
	def startmd(self) -> int:
		'''Value of variable $STARTMD'''
		return self._instance.Startmd

	@property
	def clflag(self) -> int:
		'''Value of variable $CLFLAG'''
		return self._instance.Clflag

	@property
	def smdx(self) -> int:
		'''Value of variable $SMDX'''
		return self._instance.Smdx

	@property
	def herr(self) -> int:
		'''Value of variable $HERR'''
		return self._instance.Herr

	@property
	def ifpoint(self) -> int:
		'''Value of variable $IFPOINT'''
		return self._instance.Ifpoint

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SscbkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
