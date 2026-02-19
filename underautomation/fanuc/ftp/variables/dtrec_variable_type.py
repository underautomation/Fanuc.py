import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DtrecVariableType as dtrec_variable_type

class DtrecVariableType(GenericVariableType):
	'''Describes the Fanuc type DTREC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dtrec_variable_type()
		else:
			self._instance = _internal

	@property
	def dtrec_enb(self) -> int:
		'''Value of variable $DTREC_ENB'''
		return self._instance.DtrecEnb

	@property
	def sample_itp(self) -> int:
		'''Value of variable $SAMPLE_ITP'''
		return self._instance.SampleItp

	@property
	def buf_size(self) -> int:
		'''Value of variable $BUF_SIZE'''
		return self._instance.BufSize

	@property
	def file_size(self) -> int:
		'''Value of variable $FILE_SIZE'''
		return self._instance.FileSize

	@property
	def device_nam(self) -> str:
		'''Value of variable $DEVICE_NAM'''
		return self._instance.DeviceNam

	@property
	def subbuf_siz(self) -> int:
		'''Value of variable $SUBBUF_SIZ'''
		return self._instance.SubbufSiz

	@property
	def spc_file(self) -> int:
		'''Value of variable $SPC_FILE'''
		return self._instance.SpcFile

	@property
	def dtrec_on(self) -> int:
		'''Value of variable $DTREC_ON'''
		return self._instance.DtrecOn

	@property
	def dtsav_on(self) -> int:
		'''Value of variable $DTSAV_ON'''
		return self._instance.DtsavOn

	@property
	def file_access(self) -> int:
		'''Value of variable $FILE_ACCESS'''
		return self._instance.FileAccess

	@property
	def pc_access(self) -> int:
		'''Value of variable $PC_ACCESS'''
		return self._instance.PcAccess

	@property
	def systime(self) -> typing.List[int]:
		'''Value of variable $SYSTIME'''
		return self._instance.Systime

	@property
	def dtsav_enb(self) -> int:
		'''Value of variable $DTSAV_ENB'''
		return self._instance.DtsavEnb

	@property
	def order(self) -> int:
		'''Value of variable $ORDER'''
		return self._instance.Order

	@property
	def dsb_bufsiz(self) -> int:
		'''Value of variable $DSB_BUFSIZ'''
		return self._instance.DsbBufsiz

	@property
	def enb_bufsiz(self) -> int:
		'''Value of variable $ENB_BUFSIZ'''
		return self._instance.EnbBufsiz

	@property
	def ottask_mod(self) -> int:
		'''Value of variable $OTTASK_MOD'''
		return self._instance.OttaskMod

	@property
	def dp_alm_id(self) -> int:
		'''Value of variable $DP_ALM_ID'''
		return self._instance.DpAlmId

	@property
	def dp_alm_grp(self) -> int:
		'''Value of variable $DP_ALM_GRP'''
		return self._instance.DpAlmGrp

	@property
	def dp_alm_axs(self) -> int:
		'''Value of variable $DP_ALM_AXS'''
		return self._instance.DpAlmAxs

	@property
	def def_maxbuf(self) -> float:
		'''Value of variable $DEF_MAXBUF'''
		return self._instance.DefMaxbuf

	@property
	def systime_g0(self) -> typing.List[int]:
		'''Value of variable $SYSTIME_G0'''
		return self._instance.SystimeG0

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DtrecVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
