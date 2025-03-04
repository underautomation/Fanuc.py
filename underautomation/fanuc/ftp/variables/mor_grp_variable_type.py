import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.current_pos_variable_type import CurrentPosVariableType
from underautomation.fanuc.ftp.variables.tune_variable_type import TuneVariableType
from underautomation.fanuc.ftp.variables.pulco_idata_variable_type import PulcoIdataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MorGrpVariableType as mor_grp_variable_type

class MorGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mor_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def nilpos(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Nilpos)
	@property
	def overrun_cnt(self) -> int:
		return self._instance.OverrunCnt
	@property
	def current_pos(self) -> CurrentPosVariableType:
		return CurrentPosVariableType(self._instance.CurrentPos)
	@property
	def segmovedist(self) -> float:
		return self._instance.Segmovedist
	@property
	def segmovetime(self) -> float:
		return self._instance.Segmovetime
	@property
	def segfraction(self) -> float:
		return self._instance.Segfraction
	@property
	def path_node(self) -> int:
		return self._instance.PathNode
	@property
	def cur_seg_id(self) -> int:
		return self._instance.CurSegId
	@property
	def currentline(self) -> int:
		return self._instance.Currentline
	@property
	def cur_prog_id(self) -> int:
		return self._instance.CurProgId
	@property
	def line_offset(self) -> int:
		return self._instance.LineOffset
	@property
	def apc_done(self) -> bool:
		return self._instance.ApcDone
	@property
	def atperch(self) -> bool:
		return self._instance.Atperch
	@property
	def cur_acctime(self) -> int:
		return self._instance.CurAcctime
	@property
	def cal_done(self) -> bool:
		return self._instance.CalDone
	@property
	def filter_empt(self) -> bool:
		return self._instance.FilterEmpt
	@property
	def fltr_nc_emp(self) -> bool:
		return self._instance.FltrNcEmp
	@property
	def servo_ready(self) -> bool:
		return self._instance.ServoReady
	@property
	def syn_err_cnt(self) -> int:
		return self._instance.SynErrCnt
	@property
	def apc_counter(self) -> typing.List[int]:
		return self._instance.ApcCounter
	@property
	def in_position(self) -> typing.List[bool]:
		return self._instance.InPosition
	@property
	def current_ang(self) -> typing.List[float]:
		return self._instance.CurrentAng
	@property
	def dsp_stat(self) -> typing.List[int]:
		return self._instance.DspStat
	@property
	def error_cnt(self) -> typing.List[int]:
		return self._instance.ErrorCnt
	@property
	def torque(self) -> typing.List[int]:
		return self._instance.Torque
	@property
	def max_torque(self) -> typing.List[int]:
		return self._instance.MaxTorque
	@property
	def cur_torque(self) -> typing.List[int]:
		return self._instance.CurTorque
	@property
	def machine_pls(self) -> typing.List[int]:
		return self._instance.MachinePls
	@property
	def spc_stat(self) -> typing.List[int]:
		return self._instance.SpcStat
	@property
	def line_er_cnt(self) -> typing.List[int]:
		return self._instance.LineErCnt
	@property
	def motion_cmnd(self) -> typing.List[int]:
		return self._instance.MotionCmnd
	@property
	def cur_axs_acc(self) -> typing.List[int]:
		return self._instance.CurAxsAcc
	@property
	def cur_dis_trq(self) -> typing.List[int]:
		return self._instance.CurDisTrq
	@property
	def min_dis_trq(self) -> typing.List[int]:
		return self._instance.MinDisTrq
	@property
	def max_dis_trq(self) -> typing.List[int]:
		return self._instance.MaxDisTrq
	@property
	def jogged(self) -> bool:
		return self._instance.Jogged
	@property
	def curpthacc(self) -> int:
		return self._instance.Curpthacc
	@property
	def curtimeacc(self) -> int:
		return self._instance.Curtimeacc
	@property
	def cartfltremp(self) -> bool:
		return self._instance.Cartfltremp
	@property
	def filter_type(self) -> int:
		return self._instance.FilterType
	@property
	def dvc_axes(self) -> int:
		return self._instance.DvcAxes
	@property
	def dvc_delay(self) -> int:
		return self._instance.DvcDelay
	@property
	def dvc_reduce(self) -> float:
		return self._instance.DvcReduce
	@property
	def error_cnt2(self) -> typing.List[int]:
		return self._instance.ErrorCnt2
	@property
	def error_cnt3(self) -> typing.List[int]:
		return self._instance.ErrorCnt3
	@property
	def torsion_cnt(self) -> typing.List[int]:
		return self._instance.TorsionCnt
	@property
	def temperature(self) -> typing.List[int]:
		return self._instance.Temperature
	@property
	def dischg_vlt(self) -> typing.List[int]:
		return self._instance.DischgVlt
	@property
	def dischg_mntr(self) -> typing.List[int]:
		return self._instance.DischgMntr
	@property
	def ansback_sig(self) -> typing.List[int]:
		return self._instance.AnsbackSig
	@property
	def ignore_alm(self) -> bool:
		return self._instance.IgnoreAlm
	@property
	def max_dischg(self) -> typing.List[int]:
		return self._instance.MaxDischg
	@property
	def ovc_value(self) -> typing.List[float]:
		return self._instance.OvcValue
	@property
	def max_error(self) -> typing.List[int]:
		return self._instance.MaxError
	@property
	def fb_comp_cnt(self) -> typing.List[int]:
		return self._instance.FbCompCnt
	@property
	def pccomer_cnt(self) -> typing.List[int]:
		return self._instance.PccomerCnt
	@property
	def err_value(self) -> typing.List[float]:
		return self._instance.ErrValue
	@property
	def tune(self) -> typing.List[TuneVariableType]:
		return [TuneVariableType(x) for x in self._instance.Tune]
	@property
	def tune_val(self) -> int:
		return self._instance.TuneVal
	@property
	def ogdst_ratio(self) -> float:
		return self._instance.OgdstRatio
	@property
	def whileqstop(self) -> bool:
		return self._instance.Whileqstop
	@property
	def dsp_stat2(self) -> typing.List[int]:
		return self._instance.DspStat2
	@property
	def sv_int_data(self) -> typing.List[int]:
		return self._instance.SvIntData
	@property
	def dac_stat(self) -> typing.List[int]:
		return self._instance.DacStat
	@property
	def dac_rate(self) -> typing.List[float]:
		return self._instance.DacRate
	@property
	def ms_diag(self) -> typing.List[float]:
		return self._instance.MsDiag
	@property
	def ne_mcmd(self) -> typing.List[int]:
		return self._instance.NeMcmd
	@property
	def bzal_detect(self) -> typing.List[bool]:
		return self._instance.BzalDetect
	@property
	def torque_cmd(self) -> typing.List[int]:
		return self._instance.TorqueCmd
	@property
	def psy_tmo_ctr(self) -> int:
		return self._instance.PsyTmoCtr
	@property
	def q_current(self) -> typing.List[float]:
		return self._instance.QCurrent
	@property
	def sv_int_dat2(self) -> typing.List[int]:
		return self._instance.SvIntDat2
	@property
	def sv_int_dat3(self) -> typing.List[int]:
		return self._instance.SvIntDat3
	@property
	def sv_int_dat4(self) -> typing.List[int]:
		return self._instance.SvIntDat4
	@property
	def sv_int_dat5(self) -> typing.List[int]:
		return self._instance.SvIntDat5
	@property
	def sv_int_dat6(self) -> typing.List[int]:
		return self._instance.SvIntDat6
	@property
	def pulco_idata(self) -> PulcoIdataVariableType:
		return PulcoIdataVariableType(self._instance.PulcoIdata)
	@property
	def cur_nom_ang(self) -> typing.List[float]:
		return self._instance.CurNomAng
	@property
	def move_cnt(self) -> int:
		return self._instance.MoveCnt
	@property
	def still_cnt(self) -> int:
		return self._instance.StillCnt
	@property
	def mv_st_reset(self) -> bool:
		return self._instance.MvStReset
	@property
	def rob_move(self) -> bool:
		return self._instance.RobMove
	@property
	def mvst_enb(self) -> bool:
		return self._instance.MvstEnb
	@property
	def amp_alarm(self) -> typing.List[int]:
		return self._instance.AmpAlarm
	@property
	def jog_motion(self) -> bool:
		return self._instance.JogMotion
	@property
	def cur_prognam(self) -> str:
		return self._instance.CurPrognam
	@property
	def cur_tcp(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CurTcp)
	@property
	def mch_pls_grv(self) -> typing.List[int]:
		return self._instance.MchPlsGrv
	@property
	def ovc_mntr(self) -> typing.List[float]:
		return self._instance.OvcMntr
	@property
	def ovc2_mntr(self) -> typing.List[float]:
		return self._instance.Ovc2Mntr
	@property
	def servo_err(self) -> typing.List[int]:
		return self._instance.ServoErr
	@property
	def maxservocmp(self) -> typing.List[int]:
		return self._instance.Maxservocmp
	@property
	def aftfltrang(self) -> typing.List[float]:
		return self._instance.Aftfltrang
	@property
	def distrq_org(self) -> typing.List[int]:
		return self._instance.DistrqOrg
	@property
	def sv_cmnd_ang(self) -> typing.List[float]:
		return self._instance.SvCmndAng
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
