import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import McrGrpVariableType as mcr_grp_variable_type

class McrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MCR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def calibrate(self) -> bool:
		'''Value of variable $CALIBRATE'''
		return self._instance.Calibrate

	@property
	def crc_rsm_tol(self) -> float:
		'''Value of variable $CRC_RSM_TOL'''
		return self._instance.CrcRsmTol

	@property
	def hold(self) -> bool:
		'''Value of variable $HOLD'''
		return self._instance.Hold

	@property
	def hard_hold(self) -> bool:
		'''Value of variable $HARD_HOLD'''
		return self._instance.HardHold

	@property
	def machinelock(self) -> bool:
		'''Value of variable $MACHINELOCK'''
		return self._instance.Machinelock

	@property
	def master(self) -> bool:
		'''Value of variable $MASTER'''
		return self._instance.Master

	@property
	def prgoverride(self) -> float:
		'''Value of variable $PRGOVERRIDE'''
		return self._instance.Prgoverride

	@property
	def dry_run_spd(self) -> float:
		'''Value of variable $DRY_RUN_SPD'''
		return self._instance.DryRunSpd

	@property
	def dryrun_jspd(self) -> float:
		'''Value of variable $DRYRUN_JSPD'''
		return self._instance.DryrunJspd

	@property
	def dry_jog_ovr(self) -> float:
		'''Value of variable $DRY_JOG_OVR'''
		return self._instance.DryJogOvr

	@property
	def rsm_speed(self) -> float:
		'''Value of variable $RSM_SPEED'''
		return self._instance.RsmSpeed

	@property
	def rsm_motype(self) -> int:
		'''Value of variable $RSM_MOTYPE'''
		return self._instance.RsmMotype

	@property
	def rsm_termtyp(self) -> int:
		'''Value of variable $RSM_TERMTYP'''
		return self._instance.RsmTermtyp

	@property
	def jnt_prc_enb(self) -> bool:
		'''Value of variable $JNT_PRC_ENB'''
		return self._instance.JntPrcEnb

	@property
	def soft_alarm(self) -> bool:
		'''Value of variable $SOFT_ALARM'''
		return self._instance.SoftAlarm

	@property
	def syn_adj_mod(self) -> bool:
		'''Value of variable $SYN_ADJ_MOD'''
		return self._instance.SynAdjMod

	@property
	def syn_adj_sel(self) -> bool:
		'''Value of variable $SYN_ADJ_SEL'''
		return self._instance.SynAdjSel

	@property
	def turn_on_srv(self) -> bool:
		'''Value of variable $TURN_ON_SRV'''
		return self._instance.TurnOnSrv

	@property
	def rsm_offset(self) -> float:
		'''Value of variable $RSM_OFFSET'''
		return self._instance.RsmOffset

	@property
	def set_ref(self) -> bool:
		'''Value of variable $SET_REF'''
		return self._instance.SetRef

	@property
	def master_type(self) -> int:
		'''Value of variable $MASTER_TYPE'''
		return self._instance.MasterType

	@property
	def intr_debug(self) -> int:
		'''Value of variable $INTR_DEBUG'''
		return self._instance.IntrDebug

	@property
	def plan_debug(self) -> int:
		'''Value of variable $PLAN_DEBUG'''
		return self._instance.PlanDebug

	@property
	def chk_jnt_spd(self) -> typing.List[bool]:
		'''Value of variable $CHK_JNT_SPD'''
		return self._instance.ChkJntSpd

	@property
	def dsp_upd_blk(self) -> typing.List[int]:
		'''Value of variable $DSP_UPD_BLK'''
		return self._instance.DspUpdBlk

	@property
	def dummy66(self) -> int:
		'''Value of variable $DUMMY66'''
		return self._instance.Dummy66

	@property
	def dsp_update(self) -> typing.List[int]:
		'''Value of variable $DSP_UPDATE'''
		return self._instance.DspUpdate

	@property
	def dummy67(self) -> int:
		'''Value of variable $DUMMY67'''
		return self._instance.Dummy67

	@property
	def servo_disbl(self) -> typing.List[bool]:
		'''Value of variable $SERVO_DISBL'''
		return self._instance.ServoDisbl

	@property
	def intplockhol(self) -> bool:
		'''Value of variable $INTPLOCKHOL'''
		return self._instance.Intplockhol

	@property
	def qck_stp_enb(self) -> bool:
		'''Value of variable $QCK_STP_ENB'''
		return self._instance.QckStpEnb

	@property
	def otf_speed(self) -> float:
		'''Value of variable $OTF_SPEED'''
		return self._instance.OtfSpeed

	@property
	def otf_org_spd(self) -> float:
		'''Value of variable $OTF_ORG_SPD'''
		return self._instance.OtfOrgSpd

	@property
	def otf_spd_chg(self) -> int:
		'''Value of variable $OTF_SPD_CHG'''
		return self._instance.OtfSpdChg

	@property
	def otf_spd_upd(self) -> bool:
		'''Value of variable $OTF_SPD_UPD'''
		return self._instance.OtfSpdUpd

	@property
	def tsmod_on(self) -> bool:
		'''Value of variable $TSMOD_ON'''
		return self._instance.TsmodOn

	@property
	def uop_imstp(self) -> bool:
		'''Value of variable $UOP_IMSTP'''
		return self._instance.UopImstp

	@property
	def lch_edm_enb(self) -> bool:
		'''Value of variable $LCH_EDM_ENB'''
		return self._instance.LchEdmEnb

	@property
	def eachmst_sel(self) -> typing.List[bool]:
		'''Value of variable $EACHMST_SEL'''
		return self._instance.EachmstSel

	@property
	def fjog_enb(self) -> bool:
		'''Value of variable $FJOG_ENB'''
		return self._instance.FjogEnb

	@property
	def sflt_enb(self) -> typing.List[bool]:
		'''Value of variable $SFLT_ENB'''
		return self._instance.SfltEnb

	@property
	def sflt_val(self) -> typing.List[int]:
		'''Value of variable $SFLT_VAL'''
		return self._instance.SfltVal

	@property
	def sflt_fup(self) -> bool:
		'''Value of variable $SFLT_FUP'''
		return self._instance.SfltFup

	@property
	def rsm_orient(self) -> int:
		'''Value of variable $RSM_ORIENT'''
		return self._instance.RsmOrient

	@property
	def rsm_cmd_pth(self) -> bool:
		'''Value of variable $RSM_CMD_PTH'''
		return self._instance.RsmCmdPth

	@property
	def pos_estblsh(self) -> bool:
		'''Value of variable $POS_ESTBLSH'''
		return self._instance.PosEstblsh

	@property
	def pos_can_req(self) -> bool:
		'''Value of variable $POS_CAN_REQ'''
		return self._instance.PosCanReq

	@property
	def srvo_q_stop(self) -> int:
		'''Value of variable $SRVO_Q_STOP'''
		return self._instance.SrvoQStop

	@property
	def dummy68(self) -> int:
		'''Value of variable $DUMMY68'''
		return self._instance.Dummy68

	@property
	def pg_org_rsm(self) -> bool:
		'''Value of variable $PG_ORG_RSM'''
		return self._instance.PgOrgRsm

	@property
	def fltr_flush(self) -> int:
		'''Value of variable $FLTR_FLUSH'''
		return self._instance.FltrFlush

	@property
	def dummy69(self) -> int:
		'''Value of variable $DUMMY69'''
		return self._instance.Dummy69

	@property
	def forceupdate(self) -> int:
		'''Value of variable $FORCEUPDATE'''
		return self._instance.Forceupdate

	@property
	def lckd_caldon(self) -> bool:
		'''Value of variable $LCKD_CALDON'''
		return self._instance.LckdCaldon

	@property
	def fltr_debug1(self) -> int:
		'''Value of variable $FLTR_DEBUG1'''
		return self._instance.FltrDebug1

	@property
	def fltr_debug2(self) -> int:
		'''Value of variable $FLTR_DEBUG2'''
		return self._instance.FltrDebug2

	@property
	def fltr_debug3(self) -> int:
		'''Value of variable $FLTR_DEBUG3'''
		return self._instance.FltrDebug3

	@property
	def fltr_debug4(self) -> int:
		'''Value of variable $FLTR_DEBUG4'''
		return self._instance.FltrDebug4

	@property
	def fltr_func(self) -> int:
		'''Value of variable $FLTR_FUNC'''
		return self._instance.FltrFunc

	@property
	def frcebrkrel(self) -> int:
		'''Value of variable $FRCEBRKREL'''
		return self._instance.Frcebrkrel

	@property
	def hold2(self) -> int:
		'''Value of variable $HOLD2'''
		return self._instance.Hold2

	@property
	def hard_hold2(self) -> int:
		'''Value of variable $HARD_HOLD2'''
		return self._instance.HardHold2

	@property
	def qstop_ecc(self) -> bool:
		'''Value of variable $QSTOP_ECC'''
		return self._instance.QstopEcc

	@property
	def mpdt_enb(self) -> typing.List[bool]:
		'''Value of variable $MPDT_ENB'''
		return self._instance.MpdtEnb

	@property
	def mpdt_start(self) -> typing.List[bool]:
		'''Value of variable $MPDT_START'''
		return self._instance.MpdtStart

	@property
	def mpdt_status(self) -> typing.List[int]:
		'''Value of variable $MPDT_STATUS'''
		return self._instance.MpdtStatus

	@property
	def mpdt_done(self) -> typing.List[bool]:
		'''Value of variable $MPDT_DONE'''
		return self._instance.MpdtDone

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, McrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
