import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AioCnvVariableType as aio_cnv_variable_type

class AioCnvVariableType(GenericVariableType):
	'''Describes the Fanuc type AIO_CNV_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = aio_cnv_variable_type()
		else:
			self._instance = _internal

	@property
	def rack(self) -> int:
		'''Value of variable $RACK'''
		return self._instance.Rack

	@property
	def slot(self) -> int:
		'''Value of variable $SLOT'''
		return self._instance.Slot

	@property
	def mod_type(self) -> int:
		'''Value of variable $MOD_TYPE'''
		return self._instance.ModType

	@property
	def first_ch(self) -> int:
		'''Value of variable $FIRST_CH'''
		return self._instance.FirstCh

	@property
	def last_ch(self) -> int:
		'''Value of variable $LAST_CH'''
		return self._instance.LastCh

	@property
	def in_out(self) -> int:
		'''Value of variable $IN_OUT'''
		return self._instance.InOut

	@property
	def factor(self) -> float:
		'''Value of variable $FACTOR'''
		return self._instance.Factor

	@property
	def intercept(self) -> float:
		'''Value of variable $INTERCEPT'''
		return self._instance.Intercept

	@property
	def bit_size(self) -> int:
		'''Value of variable $BIT_SIZE'''
		return self._instance.BitSize

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AioCnvVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
