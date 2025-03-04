import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import McrVariableType as mcr_variable_type

class McrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcr_variable_type()
		else:
			self._instance = _internal
	@property
	def enbl(self) -> bool:
		return self._instance.Enbl
	@property
	def sfspd(self) -> bool:
		return self._instance.Sfspd
	@property
	def brk_out_enb(self) -> bool:
		return self._instance.BrkOutEnb
	@property
	def brk_output(self) -> typing.List[bool]:
		return self._instance.BrkOutput
	@property
	def ot_release(self) -> bool:
		return self._instance.OtRelease
	@property
	def dry_run(self) -> bool:
		return self._instance.DryRun
	@property
	def genoverride(self) -> int:
		return self._instance.Genoverride
	@property
	def fltr_debug(self) -> int:
		return self._instance.FltrDebug
	@property
	def mmgr_debug(self) -> int:
		return self._instance.MmgrDebug
	@property
	def mjog_debug(self) -> int:
		return self._instance.MjogDebug
	@property
	def otf_prg_id(self) -> int:
		return self._instance.OtfPrgId
	@property
	def otf_lin_no(self) -> int:
		return self._instance.OtfLinNo
	@property
	def otf_ofst(self) -> int:
		return self._instance.OtfOfst
	@property
	def spc_reset(self) -> bool:
		return self._instance.SpcReset
	@property
	def mo_warn_enb(self) -> bool:
		return self._instance.MoWarnEnb
	@property
	def cld_release(self) -> bool:
		return self._instance.CldRelease
	@property
	def ovrdslow(self) -> int:
		return self._instance.Ovrdslow
	@property
	def ovrdfast(self) -> int:
		return self._instance.Ovrdfast
	@property
	def fast_rate(self) -> int:
		return self._instance.FastRate
	@property
	def slow_rate(self) -> int:
		return self._instance.SlowRate
	@property
	def slow_max(self) -> int:
		return self._instance.SlowMax
	@property
	def chain_reset(self) -> bool:
		return self._instance.ChainReset
	@property
	def shft_rst_pr(self) -> bool:
		return self._instance.ShftRstPr
	@property
	def actoverride(self) -> int:
		return self._instance.Actoverride
	@property
	def jogoverride(self) -> int:
		return self._instance.Jogoverride
	@property
	def ovr_zero(self) -> bool:
		return self._instance.OvrZero
	@property
	def ovrzero_enb(self) -> bool:
		return self._instance.OvrzeroEnb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
