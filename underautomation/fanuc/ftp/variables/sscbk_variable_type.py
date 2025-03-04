import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SscbkVariableType as sscbk_variable_type

class SscbkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sscbk_variable_type()
		else:
			self._instance = _internal
	@property
	def frommx(self) -> int:
		return self._instance.Frommx
	@property
	def cmosmx(self) -> int:
		return self._instance.Cmosmx
	@property
	def startmd(self) -> int:
		return self._instance.Startmd
	@property
	def clflag(self) -> int:
		return self._instance.Clflag
	@property
	def smdx(self) -> int:
		return self._instance.Smdx
	@property
	def herr(self) -> int:
		return self._instance.Herr
	@property
	def ifpoint(self) -> int:
		return self._instance.Ifpoint
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
