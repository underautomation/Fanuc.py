import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IoUopCfgVariableType as io_uop_cfg_variable_type

class IoUopCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_uop_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def uop_type(self) -> int:
		return self._instance.UopType
	@property
	def in_rack(self) -> int:
		return self._instance.InRack
	@property
	def in_slot(self) -> int:
		return self._instance.InSlot
	@property
	def in_strtpt(self) -> int:
		return self._instance.InStrtpt
	@property
	def out_rack(self) -> int:
		return self._instance.OutRack
	@property
	def out_slot(self) -> int:
		return self._instance.OutSlot
	@property
	def out_strtpt(self) -> int:
		return self._instance.OutStrtpt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
