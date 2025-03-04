import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PmonQueVariableType as pmon_que_variable_type

class PmonQueVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pmon_que_variable_type()
		else:
			self._instance = _internal
	@property
	def qcount(self) -> int:
		return self._instance.Qcount
	@property
	def qthreshold(self) -> int:
		return self._instance.Qthreshold
	@property
	def qhysteresis(self) -> int:
		return self._instance.Qhysteresis
	@property
	def queue_up(self) -> bool:
		return self._instance.QueueUp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
