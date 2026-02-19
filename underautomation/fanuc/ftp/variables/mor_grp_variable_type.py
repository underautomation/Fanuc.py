import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.current_pos_variable_type import CurrentPosVariableType
from underautomation.fanuc.ftp.variables.tune_variable_type import TuneVariableType
from underautomation.fanuc.ftp.variables.pulco_idata_variable_type import PulcoIdataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MorGrpVariableType as mor_grp_variable_type

class MorGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MOR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mor_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def nilpos(self) -> CartesianPositionVariable:
		'''Value of variable $NILPOS'''
		return CartesianPositionVariable(self._instance.Nilpos)

	@property
	def overrun_cnt(self) -> int:
		'''Value of variable $OVERRUN_CNT'''
		return self._instance.OverrunCnt

	@property
	def current_pos(self) -> CurrentPosVariableType:
		'''Value of variable $CURRENT_POS'''
		return CurrentPosVariableType(self._instance.CurrentPos)

	@property
	def segmovedist(self) -> float:
		'''Value of variable $SEGMOVEDIST'''
		return self._instance.Segmovedist

	@property
	def segmovetime(self) -> float:
		'''Value of variable $SEGMOVETIME'''
		return self._instance.Segmovetime

	@property
	def segfraction(self) -> float:
		'''Value of variable $SEGFRACTION'''
		return self._instance.Segfraction

	@property
	def path_node(self) -> int:
		'''Value of variable $PATH_NODE'''
		return self._instance.PathNode

	@property
	def cur_seg_id(self) -> int:
		'''Value of variable $CUR_SEG_ID'''
		return self._instance.CurSegId

	@property
	def currentline(self) -> int:
		'''Value of variable $CURRENTLINE'''
		return self._instance.Currentline

	@property
	def cur_prog_id(self) -> int:
		'''Value of variable $CUR_PROG_ID'''
		return self._instance.CurProgId

	@property
	def line_offset(self) -> int:
		'''Value of variable $LINE_OFFSET'''
		return self._instance.LineOffset

	@property
	def apc_done(self) -> bool:
		'''Value of variable $APC_DONE'''
		return self._instance.ApcDone

	@property
	def atperch(self) -> bool:
		'''Value of variable $ATPERCH'''
		return self._instance.Atperch

	@property
	def cur_acctime(self) -> int:
		'''Value of variable $CUR_ACCTIME'''
		return self._instance.CurAcctime

	@property
	def cal_done(self) -> bool:
		'''Value of variable $CAL_DONE'''
		return self._instance.CalDone

	@property
	def filter_empt(self) -> bool:
		'''Value of variable $FILTER_EMPT'''
		return self._instance.FilterEmpt

	@property
	def fltr_nc_emp(self) -> bool:
		'''Value of variable $FLTR_NC_EMP'''
		return self._instance.FltrNcEmp

	@property
	def servo_ready(self) -> bool:
		'''Value of variable $SERVO_READY'''
		return self._instance.ServoReady

	@property
	def syn_err_cnt(self) -> int:
		'''Value of variable $SYN_ERR_CNT'''
		return self._instance.SynErrCnt

	@property
	def apc_counter(self) -> typing.List[int]:
		'''Value of variable $APC_COUNTER'''
		return self._instance.ApcCounter

	@property
	def in_position(self) -> typing.List[bool]:
		'''Value of variable $IN_POSITION'''
		return self._instance.InPosition

	@property
	def current_ang(self) -> typing.List[float]:
		'''Value of variable $CURRENT_ANG'''
		return self._instance.CurrentAng

	@property
	def dsp_stat(self) -> typing.List[int]:
		'''Value of variable $DSP_STAT'''
		return self._instance.DspStat

	@property
	def error_cnt(self) -> typing.List[int]:
		'''Value of variable $ERROR_CNT'''
		return self._instance.ErrorCnt

	@property
	def torque(self) -> typing.List[int]:
		'''Value of variable $TORQUE'''
		return self._instance.Torque

	@property
	def max_torque(self) -> typing.List[int]:
		'''Value of variable $MAX_TORQUE'''
		return self._instance.MaxTorque

	@property
	def cur_torque(self) -> typing.List[int]:
		'''Value of variable $CUR_TORQUE'''
		return self._instance.CurTorque

	@property
	def machine_pls(self) -> typing.List[int]:
		'''Value of variable $MACHINE_PLS'''
		return self._instance.MachinePls

	@property
	def spc_stat(self) -> typing.List[int]:
		'''Value of variable $SPC_STAT'''
		return self._instance.SpcStat

	@property
	def line_er_cnt(self) -> typing.List[int]:
		'''Value of variable $LINE_ER_CNT'''
		return self._instance.LineErCnt

	@property
	def motion_cmnd(self) -> typing.List[int]:
		'''Value of variable $MOTION_CMND'''
		return self._instance.MotionCmnd

	@property
	def cur_axs_acc(self) -> typing.List[int]:
		'''Value of variable $CUR_AXS_ACC'''
		return self._instance.CurAxsAcc

	@property
	def cur_dis_trq(self) -> typing.List[int]:
		'''Value of variable $CUR_DIS_TRQ'''
		return self._instance.CurDisTrq

	@property
	def min_dis_trq(self) -> typing.List[int]:
		'''Value of variable $MIN_DIS_TRQ'''
		return self._instance.MinDisTrq

	@property
	def max_dis_trq(self) -> typing.List[int]:
		'''Value of variable $MAX_DIS_TRQ'''
		return self._instance.MaxDisTrq

	@property
	def jogged(self) -> bool:
		'''Value of variable $JOGGED'''
		return self._instance.Jogged

	@property
	def curpthacc(self) -> int:
		'''Value of variable $CURPTHACC'''
		return self._instance.Curpthacc

	@property
	def curtimeacc(self) -> int:
		'''Value of variable $CURTIMEACC'''
		return self._instance.Curtimeacc

	@property
	def cartfltremp(self) -> bool:
		'''Value of variable $CARTFLTREMP'''
		return self._instance.Cartfltremp

	@property
	def filter_type(self) -> int:
		'''Value of variable $FILTER_TYPE'''
		return self._instance.FilterType

	@property
	def dvc_axes(self) -> int:
		'''Value of variable $DVC_AXES'''
		return self._instance.DvcAxes

	@property
	def dvc_delay(self) -> int:
		'''Value of variable $DVC_DELAY'''
		return self._instance.DvcDelay

	@property
	def dvc_reduce(self) -> float:
		'''Value of variable $DVC_REDUCE'''
		return self._instance.DvcReduce

	@property
	def error_cnt2(self) -> typing.List[int]:
		'''Value of variable $ERROR_CNT2'''
		return self._instance.ErrorCnt2

	@property
	def error_cnt3(self) -> typing.List[int]:
		'''Value of variable $ERROR_CNT3'''
		return self._instance.ErrorCnt3

	@property
	def torsion_cnt(self) -> typing.List[int]:
		'''Value of variable $TORSION_CNT'''
		return self._instance.TorsionCnt

	@property
	def temperature(self) -> typing.List[int]:
		'''Value of variable $TEMPERATURE'''
		return self._instance.Temperature

	@property
	def dischg_vlt(self) -> typing.List[int]:
		'''Value of variable $DISCHG_VLT'''
		return self._instance.DischgVlt

	@property
	def dischg_mntr(self) -> typing.List[int]:
		'''Value of variable $DISCHG_MNTR'''
		return self._instance.DischgMntr

	@property
	def ansback_sig(self) -> typing.List[int]:
		'''Value of variable $ANSBACK_SIG'''
		return self._instance.AnsbackSig

	@property
	def ignore_alm(self) -> bool:
		'''Value of variable $IGNORE_ALM'''
		return self._instance.IgnoreAlm

	@property
	def max_dischg(self) -> typing.List[int]:
		'''Value of variable $MAX_DISCHG'''
		return self._instance.MaxDischg

	@property
	def ovc_value(self) -> typing.List[float]:
		'''Value of variable $OVC_VALUE'''
		return self._instance.OvcValue

	@property
	def max_error(self) -> typing.List[int]:
		'''Value of variable $MAX_ERROR'''
		return self._instance.MaxError

	@property
	def fb_comp_cnt(self) -> typing.List[int]:
		'''Value of variable $FB_COMP_CNT'''
		return self._instance.FbCompCnt

	@property
	def pccomer_cnt(self) -> typing.List[int]:
		'''Value of variable $PCCOMER_CNT'''
		return self._instance.PccomerCnt

	@property
	def err_value(self) -> typing.List[float]:
		'''Value of variable $ERR_VALUE'''
		return self._instance.ErrValue

	@property
	def tune(self) -> typing.List[TuneVariableType]:
		'''Value of variable $TUNE'''
		return [TuneVariableType(x) for x in self._instance.Tune]

	@property
	def tune_val(self) -> int:
		'''Value of variable $TUNE_VAL'''
		return self._instance.TuneVal

	@property
	def ogdst_ratio(self) -> float:
		'''Value of variable $OGDST_RATIO'''
		return self._instance.OgdstRatio

	@property
	def whileqstop(self) -> bool:
		'''Value of variable $WHILEQSTOP'''
		return self._instance.Whileqstop

	@property
	def dsp_stat2(self) -> typing.List[int]:
		'''Value of variable $DSP_STAT2'''
		return self._instance.DspStat2

	@property
	def sv_int_data(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DATA'''
		return self._instance.SvIntData

	@property
	def dac_stat(self) -> typing.List[int]:
		'''Value of variable $DAC_STAT'''
		return self._instance.DacStat

	@property
	def dac_rate(self) -> typing.List[float]:
		'''Value of variable $DAC_RATE'''
		return self._instance.DacRate

	@property
	def ms_diag(self) -> typing.List[float]:
		'''Value of variable $MS_DIAG'''
		return self._instance.MsDiag

	@property
	def ne_mcmd(self) -> typing.List[int]:
		'''Value of variable $NE_MCMD'''
		return self._instance.NeMcmd

	@property
	def bzal_detect(self) -> typing.List[bool]:
		'''Value of variable $BZAL_DETECT'''
		return self._instance.BzalDetect

	@property
	def torque_cmd(self) -> typing.List[int]:
		'''Value of variable $TORQUE_CMD'''
		return self._instance.TorqueCmd

	@property
	def psy_tmo_ctr(self) -> int:
		'''Value of variable $PSY_TMO_CTR'''
		return self._instance.PsyTmoCtr

	@property
	def q_current(self) -> typing.List[float]:
		'''Value of variable $Q_CURRENT'''
		return self._instance.QCurrent

	@property
	def sv_int_dat2(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DAT2'''
		return self._instance.SvIntDat2

	@property
	def sv_int_dat3(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DAT3'''
		return self._instance.SvIntDat3

	@property
	def sv_int_dat4(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DAT4'''
		return self._instance.SvIntDat4

	@property
	def sv_int_dat5(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DAT5'''
		return self._instance.SvIntDat5

	@property
	def sv_int_dat6(self) -> typing.List[int]:
		'''Value of variable $SV_INT_DAT6'''
		return self._instance.SvIntDat6

	@property
	def pulco_idata(self) -> PulcoIdataVariableType:
		'''Value of variable $PULCO_IDATA'''
		return PulcoIdataVariableType(self._instance.PulcoIdata)

	@property
	def cur_nom_ang(self) -> typing.List[float]:
		'''Value of variable $CUR_NOM_ANG'''
		return self._instance.CurNomAng

	@property
	def move_cnt(self) -> int:
		'''Value of variable $MOVE_CNT'''
		return self._instance.MoveCnt

	@property
	def still_cnt(self) -> int:
		'''Value of variable $STILL_CNT'''
		return self._instance.StillCnt

	@property
	def mv_st_reset(self) -> bool:
		'''Value of variable $MV_ST_RESET'''
		return self._instance.MvStReset

	@property
	def rob_move(self) -> bool:
		'''Value of variable $ROB_MOVE'''
		return self._instance.RobMove

	@property
	def mvst_enb(self) -> bool:
		'''Value of variable $MVST_ENB'''
		return self._instance.MvstEnb

	@property
	def amp_alarm(self) -> typing.List[int]:
		'''Value of variable $AMP_ALARM'''
		return self._instance.AmpAlarm

	@property
	def jog_motion(self) -> bool:
		'''Value of variable $JOG_MOTION'''
		return self._instance.JogMotion

	@property
	def cur_prognam(self) -> str:
		'''Value of variable $CUR_PROGNAM'''
		return self._instance.CurPrognam

	@property
	def cur_tcp(self) -> CartesianPositionVariable:
		'''Value of variable $CUR_TCP'''
		return CartesianPositionVariable(self._instance.CurTcp)

	@property
	def mch_pls_grv(self) -> typing.List[int]:
		'''Value of variable $MCH_PLS_GRV'''
		return self._instance.MchPlsGrv

	@property
	def ovc_mntr(self) -> typing.List[float]:
		'''Value of variable $OVC_MNTR'''
		return self._instance.OvcMntr

	@property
	def ovc2_mntr(self) -> typing.List[float]:
		'''Value of variable $OVC2_MNTR'''
		return self._instance.Ovc2Mntr

	@property
	def servo_err(self) -> typing.List[int]:
		'''Value of variable $SERVO_ERR'''
		return self._instance.ServoErr

	@property
	def maxservocmp(self) -> typing.List[int]:
		'''Value of variable $MAXSERVOCMP'''
		return self._instance.Maxservocmp

	@property
	def aftfltrang(self) -> typing.List[float]:
		'''Value of variable $AFTFLTRANG'''
		return self._instance.Aftfltrang

	@property
	def distrq_org(self) -> typing.List[int]:
		'''Value of variable $DISTRQ_ORG'''
		return self._instance.DistrqOrg

	@property
	def sv_cmnd_ang(self) -> typing.List[float]:
		'''Value of variable $SV_CMND_ANG'''
		return self._instance.SvCmndAng

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MorGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
