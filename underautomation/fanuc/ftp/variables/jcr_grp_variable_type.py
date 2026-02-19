import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import JcrGrpVariableType as jcr_grp_variable_type

class JcrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type JCR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jcr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def jog_wrstjnt(self) -> bool:
		'''Value of variable $JOG_WRSTJNT'''
		return self._instance.JogWrstjnt

	@property
	def jog_fine_md(self) -> bool:
		'''Value of variable $JOG_FINE_MD'''
		return self._instance.JogFineMd

	@property
	def jog_v_fine(self) -> bool:
		'''Value of variable $JOG_V_FINE'''
		return self._instance.JogVFine

	@property
	def prg_run(self) -> bool:
		'''Value of variable $PRG_RUN'''
		return self._instance.PrgRun

	@property
	def jog_coord(self) -> int:
		'''Value of variable $JOG_COORD'''
		return self._instance.JogCoord

	@property
	def cd_jog(self) -> bool:
		'''Value of variable $CD_JOG'''
		return self._instance.CdJog

	@property
	def follower(self) -> int:
		'''Value of variable $FOLLOWER'''
		return self._instance.Follower

	@property
	def jog_rtcp(self) -> bool:
		'''Value of variable $JOG_RTCP'''
		return self._instance.JogRtcp

	@property
	def jog_sgavd(self) -> bool:
		'''Value of variable $JOG_SGAVD'''
		return self._instance.JogSgavd

	@property
	def jog_subgrp(self) -> bool:
		'''Value of variable $JOG_SUBGRP'''
		return self._instance.JogSubgrp

	@property
	def rrmc_jog(self) -> bool:
		'''Value of variable $RRMC_JOG'''
		return self._instance.RrmcJog

	@property
	def leader(self) -> int:
		'''Value of variable $LEADER'''
		return self._instance.Leader

	@property
	def fix_ornt(self) -> bool:
		'''Value of variable $FIX_ORNT'''
		return self._instance.FixOrnt

	@property
	def keyorder(self) -> typing.List[int]:
		'''Value of variable $KEYORDER'''
		return self._instance.Keyorder

	@property
	def spath_rdy(self) -> bool:
		'''Value of variable $SPATH_RDY'''
		return self._instance.SpathRdy

	@property
	def track_jog(self) -> bool:
		'''Value of variable $TRACK_JOG'''
		return self._instance.TrackJog

	@property
	def tjog_ldr(self) -> int:
		'''Value of variable $TJOG_LDR'''
		return self._instance.TjogLdr

	@property
	def tjog_flwr(self) -> int:
		'''Value of variable $TJOG_FLWR'''
		return self._instance.TjogFlwr

	@property
	def tjog_mode(self) -> int:
		'''Value of variable $TJOG_MODE'''
		return self._instance.TjogMode

	@property
	def tjog_cntr(self) -> int:
		'''Value of variable $TJOG_CNTR'''
		return self._instance.TjogCntr

	@property
	def spjog_gmsk(self) -> int:
		'''Value of variable $SPJOG_GMSK'''
		return self._instance.SpjogGmsk

	@property
	def spjog_mode(self) -> int:
		'''Value of variable $SPJOG_MODE'''
		return self._instance.SpjogMode

	@property
	def fix_ornt_wr(self) -> bool:
		'''Value of variable $FIX_ORNT_WR'''
		return self._instance.FixOrntWr

	@property
	def ldr_frm_num(self) -> int:
		'''Value of variable $LDR_FRM_NUM'''
		return self._instance.LdrFrmNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JcrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
