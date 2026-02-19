import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ItemNameVariableType as item_name_variable_type

class ItemNameVariableType(GenericVariableType):
	'''Describes the Fanuc type ITEM_NAME_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = item_name_variable_type()
		else:
			self._instance = _internal

	@property
	def item_name(self) -> str:
		'''Value of variable $ITEM_NAME'''
		return self._instance.ItemName

	@property
	def on_label(self) -> str:
		'''Value of variable $ON_LABEL'''
		return self._instance.OnLabel

	@property
	def off_label(self) -> str:
		'''Value of variable $OFF_LABEL'''
		return self._instance.OffLabel

	@property
	def unit(self) -> str:
		'''Value of variable $UNIT'''
		return self._instance.Unit

	@property
	def item_entity(self) -> int:
		'''Value of variable $ITEM_ENTITY'''
		return self._instance.ItemEntity

	@property
	def item_type(self) -> int:
		'''Value of variable $ITEM_TYPE'''
		return self._instance.ItemType

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ItemNameVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
