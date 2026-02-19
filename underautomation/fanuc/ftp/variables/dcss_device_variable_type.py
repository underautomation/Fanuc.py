import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssDeviceVariableType as dcss_device_variable_type

class DcssDeviceVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_DEVICE_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_device_variable_type()
		else:
			self._instance = _internal

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def rbt_num(self) -> int:
		'''Value of variable $RBT_NUM'''
		return self._instance.RbtNum

	@property
	def spi_idx(self) -> int:
		'''Value of variable $SPI_IDX'''
		return self._instance.SpiIdx

	@property
	def spo_idx(self) -> int:
		'''Value of variable $SPO_IDX'''
		return self._instance.SpoIdx

	@property
	def spi_byte(self) -> int:
		'''Value of variable $SPI_BYTE'''
		return self._instance.SpiByte

	@property
	def spo_byte(self) -> int:
		'''Value of variable $SPO_BYTE'''
		return self._instance.SpoByte

	@property
	def sto(self) -> int:
		'''Value of variable $STO'''
		return self._instance.Sto

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssDeviceVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
