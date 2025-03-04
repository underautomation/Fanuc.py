import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HwrConfigVariableType as hwr_config_variable_type

class HwrConfigVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hwr_config_variable_type()
		else:
			self._instance = _internal
	@property
	def maincpu(self) -> int:
		return self._instance.Maincpu
	@property
	def visioncpu(self) -> int:
		return self._instance.Visioncpu
	@property
	def spare1(self) -> int:
		return self._instance.Spare1
	@property
	def spare2(self) -> int:
		return self._instance.Spare2
	@property
	def spare3(self) -> int:
		return self._instance.Spare3
	@property
	def spare4(self) -> int:
		return self._instance.Spare4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
