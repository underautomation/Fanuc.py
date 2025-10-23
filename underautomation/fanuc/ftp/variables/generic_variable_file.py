import typing
from underautomation.fanuc.ftp.variables.i_generic_variable_type import IGenericVariableType
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.variables.generic_variable import GenericVariable
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GenericVariableFile as generic_variable_file

class GenericVariableFile(IGenericVariableType, IFanucContent):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = generic_variable_file()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	def get_field(self, name: str) -> GenericVariable:
		return GenericVariable(self._instance.GetField(name))
	def generate_va(self, stream: typing.Any) -> None:
		self._instance.GenerateVa(stream)
	def generated_va(self) -> str:
		return self._instance.GeneratedVa()
	@property
	def variables(self) -> typing.List[GenericVariable]:
		return [GenericVariable(x) for x in self._instance.Variables]
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def parent(self) -> IGenericVariableType:
		return IGenericVariableType(self._instance.Parent)
	@parent.setter
	def parent(self, value: IGenericVariableType):
		self._instance.Parent = value
