import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SwiupdtFile as swiupdt_file

class SwiupdtFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = swiupdt_file()
		else:
			self._instance = _internal
	@property
	def run_once(self) -> int:
		return self._instance.RunOnce
