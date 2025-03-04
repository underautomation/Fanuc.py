import typing
from underautomation.fanuc.ftp.variables.sbr_variable_type import SbrVariableType
from underautomation.fanuc.ftp.variables.sbr2_variable_type import Sbr2VariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysservoFile as sysservo_file

class SysservoFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysservo_file()
		else:
			self._instance = _internal
	@property
	def sbr(self) -> typing.List[SbrVariableType]:
		return [SbrVariableType(x) for x in self._instance.Sbr]
	@property
	def sbr2(self) -> typing.List[Sbr2VariableType]:
		return [Sbr2VariableType(x) for x in self._instance.Sbr2]
