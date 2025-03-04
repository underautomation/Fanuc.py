import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MndsppstlVariableType as mndsppstl_variable_type

class MndsppstlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mndsppstl_variable_type()
		else:
			self._instance = _internal
	@property
	def loctol(self) -> float:
		return self._instance.Loctol
	@property
	def orienttol(self) -> float:
		return self._instance.Orienttol
	@property
	def exttol(self) -> float:
		return self._instance.Exttol
	@property
	def angtol(self) -> typing.List[float]:
		return self._instance.Angtol
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
