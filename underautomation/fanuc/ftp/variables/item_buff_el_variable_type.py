import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ItemBuffElVariableType as item_buff_el_variable_type

class ItemBuffElVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = item_buff_el_variable_type()
		else:
			self._instance = _internal
	@property
	def time_stamp(self) -> int:
		return self._instance.TimeStamp
	@property
	def elaps_tick(self) -> int:
		return self._instance.ElapsTick
	@property
	def on_tick(self) -> int:
		return self._instance.OnTick
	@property
	def off_tick(self) -> int:
		return self._instance.OffTick
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
