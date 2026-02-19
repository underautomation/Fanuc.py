import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import GemdataFile as gemdata_file

class GemdataFile(GenericVariableFile):
	'''Describes the Fanuc variable file gemdata.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gemdata_file()
		else:
			self._instance = _internal

	@property
	def answer_delay(self) -> int:
		'''Value of variable ANSWER_DELAY'''
		return self._instance.AnswerDelay

	@property
	def debug_msg(self) -> bool:
		'''Value of variable DEBUG_MSG'''
		return self._instance.DebugMsg

	@property
	def wait_act(self) -> int:
		'''Value of variable WAIT_ACT'''
		return self._instance.WaitAct

	@property
	def wait_time(self) -> int:
		'''Value of variable WAIT_TIME'''
		return self._instance.WaitTime

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GemdataFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
