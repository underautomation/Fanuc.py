import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcsSgnVariableType as dcs_sgn_variable_type

class DcsSgnVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcs_sgn_variable_type()
		else:
			self._instance = _internal
	@property
	def curr_signat(self) -> int:
		return self._instance.CurrSignat
	@property
	def curr_date(self) -> str:
		return self._instance.CurrDate
	@property
	def prev_signat(self) -> int:
		return self._instance.PrevSignat
	@property
	def prev_date(self) -> str:
		return self._instance.PrevDate
	@property
	def annunc_typ(self) -> int:
		return self._instance.AnnuncTyp
	@property
	def annunc_idx(self) -> int:
		return self._instance.AnnuncIdx
	@property
	def cur_time(self) -> typing.List[int]:
		return self._instance.CurTime
	@property
	def latch_time(self) -> typing.List[int]:
		return self._instance.LatchTime
	@property
	def cur_crc(self) -> typing.List[int]:
		return self._instance.CurCrc
	@property
	def latch_crc(self) -> typing.List[int]:
		return self._instance.LatchCrc
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
