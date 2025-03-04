import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ClhistVariableType as clhist_variable_type

class ClhistVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = clhist_variable_type()
		else:
			self._instance = _internal
	@property
	def cldet_axs(self) -> int:
		return self._instance.CldetAxs
	@property
	def ps_cldet_ti(self) -> int:
		return self._instance.PsCldetTi
	@property
	def cldet_time(self) -> int:
		return self._instance.CldetTime
	@property
	def jpos_cmd(self) -> typing.List[float]:
		return self._instance.JposCmd
	@property
	def jpos_fb(self) -> typing.List[float]:
		return self._instance.JposFb
	@property
	def vel_fb(self) -> typing.List[float]:
		return self._instance.VelFb
	@property
	def cl_ovr(self) -> int:
		return self._instance.ClOvr
	@property
	def cl_frmz(self) -> int:
		return self._instance.ClFrmz
	@property
	def cldept_idx(self) -> int:
		return self._instance.CldeptIdx
	@property
	def clname(self) -> str:
		return self._instance.Clname
	@property
	def clcurline(self) -> int:
		return self._instance.Clcurline
	@property
	def wnt_cnt(self) -> int:
		return self._instance.WntCnt
	@property
	def stck_cnt(self) -> int:
		return self._instance.StckCnt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
