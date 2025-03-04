import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import McrGrpVariableType as mcr_grp_variable_type

class McrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def calibrate(self) -> bool:
		return self._instance.Calibrate
	@property
	def crc_rsm_tol(self) -> float:
		return self._instance.CrcRsmTol
	@property
	def hold(self) -> bool:
		return self._instance.Hold
	@property
	def hard_hold(self) -> bool:
		return self._instance.HardHold
	@property
	def machinelock(self) -> bool:
		return self._instance.Machinelock
	@property
	def master(self) -> bool:
		return self._instance.Master
	@property
	def prgoverride(self) -> float:
		return self._instance.Prgoverride
	@property
	def dry_run_spd(self) -> float:
		return self._instance.DryRunSpd
	@property
	def dryrun_jspd(self) -> float:
		return self._instance.DryrunJspd
	@property
	def dry_jog_ovr(self) -> float:
		return self._instance.DryJogOvr
	@property
	def rsm_speed(self) -> float:
		return self._instance.RsmSpeed
	@property
	def rsm_motype(self) -> int:
		return self._instance.RsmMotype
	@property
	def rsm_termtyp(self) -> int:
		return self._instance.RsmTermtyp
	@property
	def jnt_prc_enb(self) -> bool:
		return self._instance.JntPrcEnb
	@property
	def soft_alarm(self) -> bool:
		return self._instance.SoftAlarm
	@property
	def syn_adj_mod(self) -> bool:
		return self._instance.SynAdjMod
	@property
	def syn_adj_sel(self) -> bool:
		return self._instance.SynAdjSel
	@property
	def turn_on_srv(self) -> bool:
		return self._instance.TurnOnSrv
	@property
	def rsm_offset(self) -> float:
		return self._instance.RsmOffset
	@property
	def set_ref(self) -> bool:
		return self._instance.SetRef
	@property
	def master_type(self) -> int:
		return self._instance.MasterType
	@property
	def intr_debug(self) -> int:
		return self._instance.IntrDebug
	@property
	def plan_debug(self) -> int:
		return self._instance.PlanDebug
	@property
	def chk_jnt_spd(self) -> typing.List[bool]:
		return self._instance.ChkJntSpd
	@property
	def dsp_upd_blk(self) -> typing.List[int]:
		return self._instance.DspUpdBlk
	@property
	def dummy66(self) -> int:
		return self._instance.Dummy66
	@property
	def dsp_update(self) -> typing.List[int]:
		return self._instance.DspUpdate
	@property
	def dummy67(self) -> int:
		return self._instance.Dummy67
	@property
	def servo_disbl(self) -> typing.List[bool]:
		return self._instance.ServoDisbl
	@property
	def intplockhol(self) -> bool:
		return self._instance.Intplockhol
	@property
	def qck_stp_enb(self) -> bool:
		return self._instance.QckStpEnb
	@property
	def otf_speed(self) -> float:
		return self._instance.OtfSpeed
	@property
	def otf_org_spd(self) -> float:
		return self._instance.OtfOrgSpd
	@property
	def otf_spd_chg(self) -> int:
		return self._instance.OtfSpdChg
	@property
	def otf_spd_upd(self) -> bool:
		return self._instance.OtfSpdUpd
	@property
	def tsmod_on(self) -> bool:
		return self._instance.TsmodOn
	@property
	def uop_imstp(self) -> bool:
		return self._instance.UopImstp
	@property
	def lch_edm_enb(self) -> bool:
		return self._instance.LchEdmEnb
	@property
	def eachmst_sel(self) -> typing.List[bool]:
		return self._instance.EachmstSel
	@property
	def fjog_enb(self) -> bool:
		return self._instance.FjogEnb
	@property
	def sflt_enb(self) -> typing.List[bool]:
		return self._instance.SfltEnb
	@property
	def sflt_val(self) -> typing.List[int]:
		return self._instance.SfltVal
	@property
	def sflt_fup(self) -> bool:
		return self._instance.SfltFup
	@property
	def rsm_orient(self) -> int:
		return self._instance.RsmOrient
	@property
	def rsm_cmd_pth(self) -> bool:
		return self._instance.RsmCmdPth
	@property
	def pos_estblsh(self) -> bool:
		return self._instance.PosEstblsh
	@property
	def pos_can_req(self) -> bool:
		return self._instance.PosCanReq
	@property
	def srvo_q_stop(self) -> int:
		return self._instance.SrvoQStop
	@property
	def dummy68(self) -> int:
		return self._instance.Dummy68
	@property
	def pg_org_rsm(self) -> bool:
		return self._instance.PgOrgRsm
	@property
	def fltr_flush(self) -> int:
		return self._instance.FltrFlush
	@property
	def dummy69(self) -> int:
		return self._instance.Dummy69
	@property
	def forceupdate(self) -> int:
		return self._instance.Forceupdate
	@property
	def lckd_caldon(self) -> bool:
		return self._instance.LckdCaldon
	@property
	def fltr_debug1(self) -> int:
		return self._instance.FltrDebug1
	@property
	def fltr_debug2(self) -> int:
		return self._instance.FltrDebug2
	@property
	def fltr_debug3(self) -> int:
		return self._instance.FltrDebug3
	@property
	def fltr_debug4(self) -> int:
		return self._instance.FltrDebug4
	@property
	def fltr_func(self) -> int:
		return self._instance.FltrFunc
	@property
	def frcebrkrel(self) -> int:
		return self._instance.Frcebrkrel
	@property
	def hold2(self) -> int:
		return self._instance.Hold2
	@property
	def hard_hold2(self) -> int:
		return self._instance.HardHold2
	@property
	def qstop_ecc(self) -> bool:
		return self._instance.QstopEcc
	@property
	def mpdt_enb(self) -> typing.List[bool]:
		return self._instance.MpdtEnb
	@property
	def mpdt_start(self) -> typing.List[bool]:
		return self._instance.MpdtStart
	@property
	def mpdt_status(self) -> typing.List[int]:
		return self._instance.MpdtStatus
	@property
	def mpdt_done(self) -> typing.List[bool]:
		return self._instance.MpdtDone
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
