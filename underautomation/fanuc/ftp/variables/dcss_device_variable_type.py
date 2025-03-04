import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcssDeviceVariableType as dcss_device_variable_type

class DcssDeviceVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_device_variable_type()
		else:
			self._instance = _internal
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def rbt_num(self) -> int:
		return self._instance.RbtNum
	@property
	def spi_idx(self) -> int:
		return self._instance.SpiIdx
	@property
	def spo_idx(self) -> int:
		return self._instance.SpoIdx
	@property
	def spi_byte(self) -> int:
		return self._instance.SpiByte
	@property
	def spo_byte(self) -> int:
		return self._instance.SpoByte
	@property
	def sto(self) -> int:
		return self._instance.Sto
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
