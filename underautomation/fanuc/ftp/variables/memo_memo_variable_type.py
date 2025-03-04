import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MemoMemoVariableType as memo_memo_variable_type

class MemoMemoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = memo_memo_variable_type()
		else:
			self._instance = _internal
	@property
	def tpe_area(self) -> int:
		return self._instance.TpeArea
	@property
	def tskwrk_area(self) -> int:
		return self._instance.TskwrkArea
	@property
	def wrk_buf_siz(self) -> int:
		return self._instance.WrkBufSiz
	@property
	def prc_tbl_siz(self) -> int:
		return self._instance.PrcTblSiz
	@property
	def tmp_alc_sum(self) -> int:
		return self._instance.TmpAlcSum
	@property
	def open_size(self) -> int:
		return self._instance.OpenSize
	@property
	def revive_prog(self) -> str:
		return self._instance.ReviveProg
	@property
	def mm_dsbl_msk(self) -> int:
		return self._instance.MmDsblMsk
	@property
	def recv_mode(self) -> int:
		return self._instance.RecvMode
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
