import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MemoMemoVariableType as memo_memo_variable_type

class MemoMemoVariableType(GenericVariableType):
	'''Describes the Fanuc type MEMO_MEMO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = memo_memo_variable_type()
		else:
			self._instance = _internal

	@property
	def tpe_area(self) -> int:
		'''Value of variable $TPE_AREA'''
		return self._instance.TpeArea

	@property
	def tskwrk_area(self) -> int:
		'''Value of variable $TSKWRK_AREA'''
		return self._instance.TskwrkArea

	@property
	def wrk_buf_siz(self) -> int:
		'''Value of variable $WRK_BUF_SIZ'''
		return self._instance.WrkBufSiz

	@property
	def prc_tbl_siz(self) -> int:
		'''Value of variable $PRC_TBL_SIZ'''
		return self._instance.PrcTblSiz

	@property
	def tmp_alc_sum(self) -> int:
		'''Value of variable $TMP_ALC_SUM'''
		return self._instance.TmpAlcSum

	@property
	def open_size(self) -> int:
		'''Value of variable $OPEN_SIZE'''
		return self._instance.OpenSize

	@property
	def revive_prog(self) -> str:
		'''Value of variable $REVIVE_PROG'''
		return self._instance.ReviveProg

	@property
	def mm_dsbl_msk(self) -> int:
		'''Value of variable $MM_DSBL_MSK'''
		return self._instance.MmDsblMsk

	@property
	def recv_mode(self) -> int:
		'''Value of variable $RECV_MODE'''
		return self._instance.RecvMode

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MemoMemoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
