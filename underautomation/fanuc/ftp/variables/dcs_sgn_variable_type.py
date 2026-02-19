import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcsSgnVariableType as dcs_sgn_variable_type

class DcsSgnVariableType(GenericVariableType):
	'''Describes the Fanuc type DCS_SGN_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcs_sgn_variable_type()
		else:
			self._instance = _internal

	@property
	def curr_signat(self) -> int:
		'''Value of variable $CURR_SIGNAT'''
		return self._instance.CurrSignat

	@property
	def curr_date(self) -> str:
		'''Value of variable $CURR_DATE'''
		return self._instance.CurrDate

	@property
	def prev_signat(self) -> int:
		'''Value of variable $PREV_SIGNAT'''
		return self._instance.PrevSignat

	@property
	def prev_date(self) -> str:
		'''Value of variable $PREV_DATE'''
		return self._instance.PrevDate

	@property
	def annunc_typ(self) -> int:
		'''Value of variable $ANNUNC_TYP'''
		return self._instance.AnnuncTyp

	@property
	def annunc_idx(self) -> int:
		'''Value of variable $ANNUNC_IDX'''
		return self._instance.AnnuncIdx

	@property
	def cur_time(self) -> typing.List[int]:
		'''Value of variable $CUR_TIME'''
		return self._instance.CurTime

	@property
	def latch_time(self) -> typing.List[int]:
		'''Value of variable $LATCH_TIME'''
		return self._instance.LatchTime

	@property
	def cur_crc(self) -> typing.List[int]:
		'''Value of variable $CUR_CRC'''
		return self._instance.CurCrc

	@property
	def latch_crc(self) -> typing.List[int]:
		'''Value of variable $LATCH_CRC'''
		return self._instance.LatchCrc

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcsSgnVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
