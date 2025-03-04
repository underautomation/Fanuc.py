import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ArgStrVariableType as arg_str_variable_type

class ArgStrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = arg_str_variable_type()
		else:
			self._instance = _internal
	@property
	def title(self) -> str:
		return self._instance.Title
	@property
	def item1(self) -> str:
		return self._instance.Item1
	@property
	def item2(self) -> str:
		return self._instance.Item2
	@property
	def item3(self) -> str:
		return self._instance.Item3
	@property
	def item4(self) -> str:
		return self._instance.Item4
	@property
	def item5(self) -> str:
		return self._instance.Item5
	@property
	def item6(self) -> str:
		return self._instance.Item6
	@property
	def item7(self) -> str:
		return self._instance.Item7
	@property
	def item8(self) -> str:
		return self._instance.Item8
	@property
	def item9(self) -> str:
		return self._instance.Item9
	@property
	def item10(self) -> str:
		return self._instance.Item10
	@property
	def item11(self) -> str:
		return self._instance.Item11
	@property
	def item12(self) -> str:
		return self._instance.Item12
	@property
	def item13(self) -> str:
		return self._instance.Item13
	@property
	def item14(self) -> str:
		return self._instance.Item14
	@property
	def item15(self) -> str:
		return self._instance.Item15
	@property
	def item16(self) -> str:
		return self._instance.Item16
	@property
	def item17(self) -> str:
		return self._instance.Item17
	@property
	def item18(self) -> str:
		return self._instance.Item18
	@property
	def item19(self) -> str:
		return self._instance.Item19
	@property
	def item20(self) -> str:
		return self._instance.Item20
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
