import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DtrecVariableType as dtrec_variable_type

class DtrecVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dtrec_variable_type()
		else:
			self._instance = _internal
	@property
	def dtrec_enb(self) -> int:
		return self._instance.DtrecEnb
	@property
	def sample_itp(self) -> int:
		return self._instance.SampleItp
	@property
	def buf_size(self) -> int:
		return self._instance.BufSize
	@property
	def file_size(self) -> int:
		return self._instance.FileSize
	@property
	def device_nam(self) -> str:
		return self._instance.DeviceNam
	@property
	def subbuf_siz(self) -> int:
		return self._instance.SubbufSiz
	@property
	def spc_file(self) -> int:
		return self._instance.SpcFile
	@property
	def dtrec_on(self) -> int:
		return self._instance.DtrecOn
	@property
	def dtsav_on(self) -> int:
		return self._instance.DtsavOn
	@property
	def file_access(self) -> int:
		return self._instance.FileAccess
	@property
	def pc_access(self) -> int:
		return self._instance.PcAccess
	@property
	def systime(self) -> typing.List[int]:
		return self._instance.Systime
	@property
	def dtsav_enb(self) -> int:
		return self._instance.DtsavEnb
	@property
	def order(self) -> int:
		return self._instance.Order
	@property
	def dsb_bufsiz(self) -> int:
		return self._instance.DsbBufsiz
	@property
	def enb_bufsiz(self) -> int:
		return self._instance.EnbBufsiz
	@property
	def ottask_mod(self) -> int:
		return self._instance.OttaskMod
	@property
	def dp_alm_id(self) -> int:
		return self._instance.DpAlmId
	@property
	def dp_alm_grp(self) -> int:
		return self._instance.DpAlmGrp
	@property
	def dp_alm_axs(self) -> int:
		return self._instance.DpAlmAxs
	@property
	def def_maxbuf(self) -> float:
		return self._instance.DefMaxbuf
	@property
	def systime_g0(self) -> typing.List[int]:
		return self._instance.SystimeG0
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
