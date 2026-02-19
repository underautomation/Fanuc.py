import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TsscbVariableType as tsscb_variable_type

class TsscbVariableType(GenericVariableType):
	'''Describes the Fanuc type TSSCB_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tsscb_variable_type()
		else:
			self._instance = _internal

	@property
	def dsp_no(self) -> int:
		'''Value of variable $DSP_NO'''
		return self._instance.DspNo

	@property
	def dspax_no(self) -> int:
		'''Value of variable $DSPAX_NO'''
		return self._instance.DspaxNo

	@property
	def data_sel(self) -> int:
		'''Value of variable $DATA_SEL'''
		return self._instance.DataSel

	@property
	def out_channel(self) -> int:
		'''Value of variable $OUT_CHANNEL'''
		return self._instance.OutChannel

	@property
	def address(self) -> int:
		'''Value of variable $ADDRESS'''
		return self._instance.Address

	@property
	def bit_shift(self) -> int:
		'''Value of variable $BIT_SHIFT'''
		return self._instance.BitShift

	@property
	def use2ch(self) -> int:
		'''Value of variable $USE_2CH'''
		return self._instance.Use2ch

	@property
	def monitor(self) -> int:
		'''Value of variable $MONITOR'''
		return self._instance.Monitor

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TsscbVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
