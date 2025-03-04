import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DemoInitVariableType as demo_init_variable_type

class DemoInitVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = demo_init_variable_type()
		else:
			self._instance = _internal
	@property
	def demo_enb(self) -> bool:
		return self._instance.DemoEnb
	@property
	def demo_au(self) -> bool:
		return self._instance.DemoAu
	@property
	def demo_days(self) -> int:
		return self._instance.DemoDays
	@property
	def load_num(self) -> int:
		return self._instance.LoadNum
	@property
	def dummy4(self) -> int:
		return self._instance.Dummy4
	@property
	def dummy5(self) -> int:
		return self._instance.Dummy5
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
