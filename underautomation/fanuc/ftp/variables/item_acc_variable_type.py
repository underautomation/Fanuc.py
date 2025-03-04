import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ItemAccVariableType as item_acc_variable_type

class ItemAccVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = item_acc_variable_type()
		else:
			self._instance = _internal
	@property
	def time_stamp(self) -> int:
		return self._instance.TimeStamp
	@property
	def last_tick(self) -> int:
		return self._instance.LastTick
	@property
	def on_acc(self) -> int:
		return self._instance.OnAcc
	@property
	def off_acc(self) -> int:
		return self._instance.OffAcc
	@property
	def elaps_acc(self) -> int:
		return self._instance.ElapsAcc
	@property
	def buff_idx(self) -> int:
		return self._instance.BuffIdx
	@property
	def hist_idx(self) -> int:
		return self._instance.HistIdx
	@property
	def rep_idx(self) -> int:
		return self._instance.RepIdx
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
