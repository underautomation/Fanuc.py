import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ItemNameVariableType as item_name_variable_type

class ItemNameVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = item_name_variable_type()
		else:
			self._instance = _internal
	@property
	def item_name(self) -> str:
		return self._instance.ItemName
	@property
	def on_label(self) -> str:
		return self._instance.OnLabel
	@property
	def off_label(self) -> str:
		return self._instance.OffLabel
	@property
	def unit(self) -> str:
		return self._instance.Unit
	@property
	def item_entity(self) -> int:
		return self._instance.ItemEntity
	@property
	def item_type(self) -> int:
		return self._instance.ItemType
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
