import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TscfgVariableType as tscfg_variable_type

class TscfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tscfg_variable_type()
		else:
			self._instance = _internal
	@property
	def grp_mask(self) -> int:
		return self._instance.GrpMask
	@property
	def mode_mask(self) -> int:
		return self._instance.ModeMask
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def opt_val(self) -> float:
		return self._instance.OptVal
	@property
	def size(self) -> int:
		return self._instance.Size
	@property
	def fname_type(self) -> int:
		return self._instance.FnameType
	@property
	def proc(self) -> bool:
		return self._instance.Proc
	@property
	def output(self) -> bool:
		return self._instance.Output
	@property
	def output_done(self) -> bool:
		return self._instance.OutputDone
	@property
	def axs_msk_enb(self) -> bool:
		return self._instance.AxsMskEnb
	@property
	def axis_mask(self) -> typing.List[int]:
		return self._instance.AxisMask
	@property
	def cur_rectime(self) -> int:
		return self._instance.CurRectime
	@property
	def tot_chn_num(self) -> int:
		return self._instance.TotChnNum
	@property
	def minfreq_us(self) -> int:
		return self._instance.MinfreqUs
	@property
	def setfreq_pow(self) -> int:
		return self._instance.SetfreqPow
	@property
	def lparam(self) -> typing.List[int]:
		return self._instance.Lparam
	@property
	def fparam(self) -> typing.List[float]:
		return self._instance.Fparam
	@property
	def path_nam(self) -> str:
		return self._instance.PathNam
	@property
	def dummy19(self) -> int:
		return self._instance.Dummy19
	@property
	def dummy20(self) -> int:
		return self._instance.Dummy20
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
