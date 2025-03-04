import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CrcfgVariableType as crcfg_variable_type

class CrcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = crcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def group_mask(self) -> int:
		return self._instance.GroupMask
	@property
	def mb_conflict(self) -> int:
		return self._instance.MbConflict
	@property
	def mb_required(self) -> int:
		return self._instance.MbRequired
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def pgdebug(self) -> int:
		return self._instance.Pgdebug
	@property
	def cr_enhanced(self) -> bool:
		return self._instance.CrEnhanced
	@property
	def lgorn_enbl(self) -> bool:
		return self._instance.LgornEnbl
	@property
	def blend_enb(self) -> bool:
		return self._instance.BlendEnb
	@property
	def max_arc_ang(self) -> float:
		return self._instance.MaxArcAng
	@property
	def rsm_rspd_lm(self) -> float:
		return self._instance.RsmRspdLm
	@property
	def lgorn_meth(self) -> int:
		return self._instance.LgornMeth
	@property
	def lgorn_dbg(self) -> bool:
		return self._instance.LgornDbg
	@property
	def lgorn_rad(self) -> int:
		return self._instance.LgornRad
	@property
	def lgorn_az_sp(self) -> int:
		return self._instance.LgornAzSp
	@property
	def lgorn_eltol(self) -> int:
		return self._instance.LgornEltol
	@property
	def rotspdfctr(self) -> float:
		return self._instance.Rotspdfctr
	@property
	def max_fp_spd(self) -> float:
		return self._instance.MaxFpSpd
	@property
	def smcrc_radi(self) -> float:
		return self._instance.SmcrcRadi
	@property
	def smcrc_rado(self) -> float:
		return self._instance.SmcrcRado
	@property
	def smcrc_arc(self) -> float:
		return self._instance.SmcrcArc
	@property
	def arcanglim(self) -> float:
		return self._instance.Arcanglim
	@property
	def maxorntchg(self) -> float:
		return self._instance.Maxorntchg
	@property
	def maxsgratio(self) -> float:
		return self._instance.Maxsgratio
	@property
	def chkbmp(self) -> int:
		return self._instance.Chkbmp
	@property
	def rsm_typ(self) -> int:
		return self._instance.RsmTyp
	@property
	def chk_msk(self) -> int:
		return self._instance.ChkMsk
	@property
	def aes_singtol(self) -> float:
		return self._instance.AesSingtol
	@property
	def sw_orntbase(self) -> int:
		return self._instance.SwOrntbase
	@property
	def xyzwpr_tol(self) -> typing.List[float]:
		return self._instance.XyzwprTol
	@property
	def ang_tol(self) -> typing.List[float]:
		return self._instance.AngTol
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
