import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CrcfgVariableType as crcfg_variable_type

class CrcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type CRCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = crcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def group_mask(self) -> int:
		'''Value of variable $GROUP_MASK'''
		return self._instance.GroupMask

	@property
	def mb_conflict(self) -> int:
		'''Value of variable $MB_CONFLICT'''
		return self._instance.MbConflict

	@property
	def mb_required(self) -> int:
		'''Value of variable $MB_REQUIRED'''
		return self._instance.MbRequired

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def pgdebug(self) -> int:
		'''Value of variable $PGDEBUG'''
		return self._instance.Pgdebug

	@property
	def cr_enhanced(self) -> bool:
		'''Value of variable $CR_ENHANCED'''
		return self._instance.CrEnhanced

	@property
	def lgorn_enbl(self) -> bool:
		'''Value of variable $LGORN_ENBL'''
		return self._instance.LgornEnbl

	@property
	def blend_enb(self) -> bool:
		'''Value of variable $BLEND_ENB'''
		return self._instance.BlendEnb

	@property
	def max_arc_ang(self) -> float:
		'''Value of variable $MAX_ARC_ANG'''
		return self._instance.MaxArcAng

	@property
	def rsm_rspd_lm(self) -> float:
		'''Value of variable $RSM_RSPD_LM'''
		return self._instance.RsmRspdLm

	@property
	def lgorn_meth(self) -> int:
		'''Value of variable $LGORN_METH'''
		return self._instance.LgornMeth

	@property
	def lgorn_dbg(self) -> bool:
		'''Value of variable $LGORN_DBG'''
		return self._instance.LgornDbg

	@property
	def lgorn_rad(self) -> int:
		'''Value of variable $LGORN_RAD'''
		return self._instance.LgornRad

	@property
	def lgorn_az_sp(self) -> int:
		'''Value of variable $LGORN_AZ_SP'''
		return self._instance.LgornAzSp

	@property
	def lgorn_eltol(self) -> int:
		'''Value of variable $LGORN_ELTOL'''
		return self._instance.LgornEltol

	@property
	def rotspdfctr(self) -> float:
		'''Value of variable $ROTSPDFCTR'''
		return self._instance.Rotspdfctr

	@property
	def max_fp_spd(self) -> float:
		'''Value of variable $MAX_FP_SPD'''
		return self._instance.MaxFpSpd

	@property
	def smcrc_radi(self) -> float:
		'''Value of variable $SMCRC_RADI'''
		return self._instance.SmcrcRadi

	@property
	def smcrc_rado(self) -> float:
		'''Value of variable $SMCRC_RADO'''
		return self._instance.SmcrcRado

	@property
	def smcrc_arc(self) -> float:
		'''Value of variable $SMCRC_ARC'''
		return self._instance.SmcrcArc

	@property
	def arcanglim(self) -> float:
		'''Value of variable $ARCANGLIM'''
		return self._instance.Arcanglim

	@property
	def maxorntchg(self) -> float:
		'''Value of variable $MAXORNTCHG'''
		return self._instance.Maxorntchg

	@property
	def maxsgratio(self) -> float:
		'''Value of variable $MAXSGRATIO'''
		return self._instance.Maxsgratio

	@property
	def chkbmp(self) -> int:
		'''Value of variable $CHKBMP'''
		return self._instance.Chkbmp

	@property
	def rsm_typ(self) -> int:
		'''Value of variable $RSM_TYP'''
		return self._instance.RsmTyp

	@property
	def chk_msk(self) -> int:
		'''Value of variable $CHK_MSK'''
		return self._instance.ChkMsk

	@property
	def aes_singtol(self) -> float:
		'''Value of variable $AES_SINGTOL'''
		return self._instance.AesSingtol

	@property
	def sw_orntbase(self) -> int:
		'''Value of variable $SW_ORNTBASE'''
		return self._instance.SwOrntbase

	@property
	def xyzwpr_tol(self) -> typing.List[float]:
		'''Value of variable $XYZWPR_TOL'''
		return self._instance.XyzwprTol

	@property
	def ang_tol(self) -> typing.List[float]:
		'''Value of variable $ANG_TOL'''
		return self._instance.AngTol

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CrcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
