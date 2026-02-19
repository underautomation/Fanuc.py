import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import McrVariableType as mcr_variable_type

class McrVariableType(GenericVariableType):
	'''Describes the Fanuc type MCR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcr_variable_type()
		else:
			self._instance = _internal

	@property
	def enbl(self) -> bool:
		'''Value of variable $ENBL'''
		return self._instance.Enbl

	@property
	def sfspd(self) -> bool:
		'''Value of variable $SFSPD'''
		return self._instance.Sfspd

	@property
	def brk_out_enb(self) -> bool:
		'''Value of variable $BRK_OUT_ENB'''
		return self._instance.BrkOutEnb

	@property
	def brk_output(self) -> typing.List[bool]:
		'''Value of variable $BRK_OUTPUT'''
		return self._instance.BrkOutput

	@property
	def ot_release(self) -> bool:
		'''Value of variable $OT_RELEASE'''
		return self._instance.OtRelease

	@property
	def dry_run(self) -> bool:
		'''Value of variable $DRY_RUN'''
		return self._instance.DryRun

	@property
	def genoverride(self) -> int:
		'''Value of variable $GENOVERRIDE'''
		return self._instance.Genoverride

	@property
	def fltr_debug(self) -> int:
		'''Value of variable $FLTR_DEBUG'''
		return self._instance.FltrDebug

	@property
	def mmgr_debug(self) -> int:
		'''Value of variable $MMGR_DEBUG'''
		return self._instance.MmgrDebug

	@property
	def mjog_debug(self) -> int:
		'''Value of variable $MJOG_DEBUG'''
		return self._instance.MjogDebug

	@property
	def otf_prg_id(self) -> int:
		'''Value of variable $OTF_PRG_ID'''
		return self._instance.OtfPrgId

	@property
	def otf_lin_no(self) -> int:
		'''Value of variable $OTF_LIN_NO'''
		return self._instance.OtfLinNo

	@property
	def otf_ofst(self) -> int:
		'''Value of variable $OTF_OFST'''
		return self._instance.OtfOfst

	@property
	def spc_reset(self) -> bool:
		'''Value of variable $SPC_RESET'''
		return self._instance.SpcReset

	@property
	def mo_warn_enb(self) -> bool:
		'''Value of variable $MO_WARN_ENB'''
		return self._instance.MoWarnEnb

	@property
	def cld_release(self) -> bool:
		'''Value of variable $CLD_RELEASE'''
		return self._instance.CldRelease

	@property
	def ovrdslow(self) -> int:
		'''Value of variable $OVRDSLOW'''
		return self._instance.Ovrdslow

	@property
	def ovrdfast(self) -> int:
		'''Value of variable $OVRDFAST'''
		return self._instance.Ovrdfast

	@property
	def fast_rate(self) -> int:
		'''Value of variable $FAST_RATE'''
		return self._instance.FastRate

	@property
	def slow_rate(self) -> int:
		'''Value of variable $SLOW_RATE'''
		return self._instance.SlowRate

	@property
	def slow_max(self) -> int:
		'''Value of variable $SLOW_MAX'''
		return self._instance.SlowMax

	@property
	def chain_reset(self) -> bool:
		'''Value of variable $CHAIN_RESET'''
		return self._instance.ChainReset

	@property
	def shft_rst_pr(self) -> bool:
		'''Value of variable $SHFT_RST_PR'''
		return self._instance.ShftRstPr

	@property
	def actoverride(self) -> int:
		'''Value of variable $ACTOVERRIDE'''
		return self._instance.Actoverride

	@property
	def jogoverride(self) -> int:
		'''Value of variable $JOGOVERRIDE'''
		return self._instance.Jogoverride

	@property
	def ovr_zero(self) -> bool:
		'''Value of variable $OVR_ZERO'''
		return self._instance.OvrZero

	@property
	def ovrzero_enb(self) -> bool:
		'''Value of variable $OVRZERO_ENB'''
		return self._instance.OvrzeroEnb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, McrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
