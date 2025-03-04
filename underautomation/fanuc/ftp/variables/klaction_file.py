import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import KlactionFile as klaction_file

class KlactionFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = klaction_file()
		else:
			self._instance = _internal
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def int_value(self) -> int:
		return self._instance.IntValue
	@property
	def real_value(self) -> float:
		return self._instance.RealValue
	@property
	def string_value(self) -> str:
		return self._instance.StringValue
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def param_ok(self) -> bool:
		return self._instance.ParamOk
