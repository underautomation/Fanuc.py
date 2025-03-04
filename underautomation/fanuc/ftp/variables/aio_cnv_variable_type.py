import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AioCnvVariableType as aio_cnv_variable_type

class AioCnvVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aio_cnv_variable_type()
		else:
			self._instance = _internal
	@property
	def rack(self) -> int:
		return self._instance.Rack
	@property
	def slot(self) -> int:
		return self._instance.Slot
	@property
	def mod_type(self) -> int:
		return self._instance.ModType
	@property
	def first_ch(self) -> int:
		return self._instance.FirstCh
	@property
	def last_ch(self) -> int:
		return self._instance.LastCh
	@property
	def in_out(self) -> int:
		return self._instance.InOut
	@property
	def factor(self) -> float:
		return self._instance.Factor
	@property
	def intercept(self) -> float:
		return self._instance.Intercept
	@property
	def bit_size(self) -> int:
		return self._instance.BitSize
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
