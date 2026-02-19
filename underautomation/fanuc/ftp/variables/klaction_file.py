import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import KlactionFile as klaction_file

class KlactionFile(GenericVariableFile):
	'''Describes the Fanuc variable file klaction.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = klaction_file()
		else:
			self._instance = _internal

	@property
	def data_type(self) -> int:
		'''Value of variable DATA_TYPE'''
		return self._instance.DataType

	@property
	def int_value(self) -> int:
		'''Value of variable INT_VALUE'''
		return self._instance.IntValue

	@property
	def real_value(self) -> float:
		'''Value of variable REAL_VALUE'''
		return self._instance.RealValue

	@property
	def string_value(self) -> str:
		'''Value of variable STRING_VALUE'''
		return self._instance.StringValue

	@property
	def status(self) -> int:
		'''Value of variable STATUS'''
		return self._instance.Status

	@property
	def param_ok(self) -> bool:
		'''Value of variable PARAM_OK'''
		return self._instance.ParamOk

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KlactionFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
