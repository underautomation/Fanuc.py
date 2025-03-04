import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PslgsetVariableType as pslgset_variable_type

class PslgsetVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pslgset_variable_type()
		else:
			self._instance = _internal
	@property
	def ps_size(self) -> int:
		return self._instance.PsSize
	@property
	def ps_mode(self) -> int:
		return self._instance.PsMode
	@property
	def timesent(self) -> int:
		return self._instance.Timesent
	@property
	def lastdev(self) -> str:
		return self._instance.Lastdev
	@property
	def ps_debug(self) -> int:
		return self._instance.PsDebug
	@property
	def timesent2(self) -> int:
		return self._instance.Timesent2
	@property
	def lastdev2(self) -> str:
		return self._instance.Lastdev2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
