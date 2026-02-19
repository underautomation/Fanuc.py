import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ArgStrVariableType as arg_str_variable_type

class ArgStrVariableType(GenericVariableType):
	'''Describes the Fanuc type ARG_STR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = arg_str_variable_type()
		else:
			self._instance = _internal

	@property
	def title(self) -> str:
		'''Value of variable $TITLE'''
		return self._instance.Title

	@property
	def item1(self) -> str:
		'''Value of variable $ITEM1'''
		return self._instance.Item1

	@property
	def item2(self) -> str:
		'''Value of variable $ITEM2'''
		return self._instance.Item2

	@property
	def item3(self) -> str:
		'''Value of variable $ITEM3'''
		return self._instance.Item3

	@property
	def item4(self) -> str:
		'''Value of variable $ITEM4'''
		return self._instance.Item4

	@property
	def item5(self) -> str:
		'''Value of variable $ITEM5'''
		return self._instance.Item5

	@property
	def item6(self) -> str:
		'''Value of variable $ITEM6'''
		return self._instance.Item6

	@property
	def item7(self) -> str:
		'''Value of variable $ITEM7'''
		return self._instance.Item7

	@property
	def item8(self) -> str:
		'''Value of variable $ITEM8'''
		return self._instance.Item8

	@property
	def item9(self) -> str:
		'''Value of variable $ITEM9'''
		return self._instance.Item9

	@property
	def item10(self) -> str:
		'''Value of variable $ITEM10'''
		return self._instance.Item10

	@property
	def item11(self) -> str:
		'''Value of variable $ITEM11'''
		return self._instance.Item11

	@property
	def item12(self) -> str:
		'''Value of variable $ITEM12'''
		return self._instance.Item12

	@property
	def item13(self) -> str:
		'''Value of variable $ITEM13'''
		return self._instance.Item13

	@property
	def item14(self) -> str:
		'''Value of variable $ITEM14'''
		return self._instance.Item14

	@property
	def item15(self) -> str:
		'''Value of variable $ITEM15'''
		return self._instance.Item15

	@property
	def item16(self) -> str:
		'''Value of variable $ITEM16'''
		return self._instance.Item16

	@property
	def item17(self) -> str:
		'''Value of variable $ITEM17'''
		return self._instance.Item17

	@property
	def item18(self) -> str:
		'''Value of variable $ITEM18'''
		return self._instance.Item18

	@property
	def item19(self) -> str:
		'''Value of variable $ITEM19'''
		return self._instance.Item19

	@property
	def item20(self) -> str:
		'''Value of variable $ITEM20'''
		return self._instance.Item20

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ArgStrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
