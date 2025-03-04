import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FeatureVariableType as feature_variable_type

class FeatureVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = feature_variable_type()
		else:
			self._instance = _internal
	@property
	def nam(self) -> typing.List[str]:
		return self._instance.Nam
	@property
	def mod(self) -> typing.List[str]:
		return self._instance.Mod
	@property
	def ver(self) -> typing.List[str]:
		return self._instance.Ver
	@property
	def mec(self) -> typing.List[str]:
		return self._instance.Mec
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
