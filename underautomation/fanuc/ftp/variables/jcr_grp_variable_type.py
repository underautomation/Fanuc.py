import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import JcrGrpVariableType as jcr_grp_variable_type

class JcrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jcr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def jog_wrstjnt(self) -> bool:
		return self._instance.JogWrstjnt
	@property
	def jog_fine_md(self) -> bool:
		return self._instance.JogFineMd
	@property
	def jog_v_fine(self) -> bool:
		return self._instance.JogVFine
	@property
	def prg_run(self) -> bool:
		return self._instance.PrgRun
	@property
	def jog_coord(self) -> int:
		return self._instance.JogCoord
	@property
	def cd_jog(self) -> bool:
		return self._instance.CdJog
	@property
	def follower(self) -> int:
		return self._instance.Follower
	@property
	def jog_rtcp(self) -> bool:
		return self._instance.JogRtcp
	@property
	def jog_sgavd(self) -> bool:
		return self._instance.JogSgavd
	@property
	def jog_subgrp(self) -> bool:
		return self._instance.JogSubgrp
	@property
	def rrmc_jog(self) -> bool:
		return self._instance.RrmcJog
	@property
	def leader(self) -> int:
		return self._instance.Leader
	@property
	def fix_ornt(self) -> bool:
		return self._instance.FixOrnt
	@property
	def keyorder(self) -> typing.List[int]:
		return self._instance.Keyorder
	@property
	def spath_rdy(self) -> bool:
		return self._instance.SpathRdy
	@property
	def track_jog(self) -> bool:
		return self._instance.TrackJog
	@property
	def tjog_ldr(self) -> int:
		return self._instance.TjogLdr
	@property
	def tjog_flwr(self) -> int:
		return self._instance.TjogFlwr
	@property
	def tjog_mode(self) -> int:
		return self._instance.TjogMode
	@property
	def tjog_cntr(self) -> int:
		return self._instance.TjogCntr
	@property
	def spjog_gmsk(self) -> int:
		return self._instance.SpjogGmsk
	@property
	def spjog_mode(self) -> int:
		return self._instance.SpjogMode
	@property
	def fix_ornt_wr(self) -> bool:
		return self._instance.FixOrntWr
	@property
	def ldr_frm_num(self) -> int:
		return self._instance.LdrFrmNum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
