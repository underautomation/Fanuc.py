import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import InteractVariableType as interact_variable_type

class InteractVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = interact_variable_type()
		else:
			self._instance = _internal
	@property
	def interaction(self) -> typing.List[float]:
		return self._instance.Interaction
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
