import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GemdataFile as gemdata_file

class GemdataFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gemdata_file()
		else:
			self._instance = _internal
	@property
	def answer_delay(self) -> int:
		return self._instance.AnswerDelay
	@property
	def debug_msg(self) -> bool:
		return self._instance.DebugMsg
	@property
	def wait_act(self) -> int:
		return self._instance.WaitAct
	@property
	def wait_time(self) -> int:
		return self._instance.WaitTime
