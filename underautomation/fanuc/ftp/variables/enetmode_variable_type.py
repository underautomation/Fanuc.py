import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EnetmodeVariableType as enetmode_variable_type

class EnetmodeVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enetmode_variable_type()
		else:
			self._instance = _internal
	@property
	def full_duplex(self) -> bool:
		return self._instance.FullDuplex
	@property
	def speed(self) -> int:
		return self._instance.Speed
	@property
	def acd_enable(self) -> bool:
		return self._instance.AcdEnable
	@property
	def throttle(self) -> bool:
		return self._instance.Throttle
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
