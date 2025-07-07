import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VariableFileList as variable_file_list

class VariableFileList:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_file_list()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value

