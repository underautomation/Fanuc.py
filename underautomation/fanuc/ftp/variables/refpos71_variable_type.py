import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Refpos71VariableType as refpos71_variable_type

class Refpos71VariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = refpos71_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def atperch(self) -> bool:
		return self._instance.Atperch
	@property
	def dout_type(self) -> int:
		return self._instance.DoutType
	@property
	def dout_indx(self) -> int:
		return self._instance.DoutIndx
	@property
	def perchpos(self) -> typing.List[float]:
		return self._instance.Perchpos
	@property
	def perchtol(self) -> typing.List[float]:
		return self._instance.Perchtol
	@property
	def homepos(self) -> bool:
		return self._instance.Homepos
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
