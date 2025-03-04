import typing
from underautomation.fanuc.ftp.variables.interact_variable_type import InteractVariableType
from underautomation.fanuc.ftp.variables.intrac_n_variable_type import IntracNVariableType
from underautomation.fanuc.ftp.variables.intrac_d_variable_type import IntracDVariableType
from underautomation.fanuc.ftp.variables.dh_extra_variable_type import DhExtraVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MrrGrpVariableType as mrr_grp_variable_type

class MrrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mrr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def belt_enable(self) -> bool:
		return self._instance.BeltEnable
	@property
	def cart_accel1(self) -> int:
		return self._instance.CartAccel1
	@property
	def cart_accel2(self) -> int:
		return self._instance.CartAccel2
	@property
	def circ_rate(self) -> int:
		return self._instance.CircRate
	@property
	def contaxisnum(self) -> int:
		return self._instance.Contaxisnum
	@property
	def ps_exp_enbl(self) -> int:
		return self._instance.PsExpEnbl
	@property
	def exp_enbl(self) -> bool:
		return self._instance.ExpEnbl
	@property
	def joint_rate(self) -> int:
		return self._instance.JointRate
	@property
	def linear_rate(self) -> int:
		return self._instance.LinearRate
	@property
	def path_accel1(self) -> int:
		return self._instance.PathAccel1
	@property
	def path_accel2(self) -> int:
		return self._instance.PathAccel2
	@property
	def path_accel3(self) -> int:
		return self._instance.PathAccel3
	@property
	def process_spd(self) -> float:
		return self._instance.ProcessSpd
	@property
	def proc_spdlim(self) -> float:
		return self._instance.ProcSpdlim
	@property
	def cnt_acc_mgn(self) -> float:
		return self._instance.CntAccMgn
	@property
	def ddacc_ratio(self) -> float:
		return self._instance.DdaccRatio
	@property
	def fwp_time1(self) -> int:
		return self._instance.FwpTime1
	@property
	def fwp_time2(self) -> int:
		return self._instance.FwpTime2
	@property
	def accel_ratio(self) -> float:
		return self._instance.AccelRatio
	@property
	def decel_ratio(self) -> float:
		return self._instance.DecelRatio
	@property
	def ppabn_enbl(self) -> bool:
		return self._instance.PpabnEnbl
	@property
	def rotspeedlim(self) -> float:
		return self._instance.Rotspeedlim
	@property
	def speedlim(self) -> float:
		return self._instance.Speedlim
	@property
	def speedlimjnt(self) -> float:
		return self._instance.Speedlimjnt
	@property
	def def_maxacce(self) -> bool:
		return self._instance.DefMaxacce
	@property
	def use_cal(self) -> bool:
		return self._instance.UseCal
	@property
	def spin_ctrl(self) -> bool:
		return self._instance.SpinCtrl
	@property
	def syn_err_lim(self) -> int:
		return self._instance.SynErrLim
	@property
	def sync_gain(self) -> int:
		return self._instance.SyncGain
	@property
	def sync_offset(self) -> int:
		return self._instance.SyncOffset
	@property
	def mount_angle(self) -> float:
		return self._instance.MountAngle
	@property
	def collinear(self) -> float:
		return self._instance.Collinear
	@property
	def coincident(self) -> float:
		return self._instance.Coincident
	@property
	def accel_time1(self) -> typing.List[int]:
		return self._instance.AccelTime1
	@property
	def accel_time2(self) -> typing.List[int]:
		return self._instance.AccelTime2
	@property
	def encscales(self) -> typing.List[float]:
		return self._instance.Encscales
	@property
	def exp_accel(self) -> typing.List[int]:
		return self._instance.ExpAccel
	@property
	def ps_inpos_ti(self) -> int:
		return self._instance.PsInposTi
	@property
	def inpos_time(self) -> typing.List[int]:
		return self._instance.InposTime
	@property
	def jntvellim(self) -> typing.List[float]:
		return self._instance.Jntvellim
	@property
	def jnt23_uplim(self) -> float:
		return self._instance.Jnt23Uplim
	@property
	def jnt23_lowli(self) -> float:
		return self._instance.Jnt23Lowli
	@property
	def lowerlims(self) -> typing.List[float]:
		return self._instance.Lowerlims
	@property
	def lowerlimsdf(self) -> typing.List[float]:
		return self._instance.Lowerlimsdf
	@property
	def master_pos(self) -> typing.List[float]:
		return self._instance.MasterPos
	@property
	def min_acctime(self) -> typing.List[int]:
		return self._instance.MinAcctime
	@property
	def mosign(self) -> typing.List[bool]:
		return self._instance.Mosign
	@property
	def mot_spd_lim(self) -> typing.List[int]:
		return self._instance.MotSpdLim
	@property
	def perch(self) -> typing.List[float]:
		return self._instance.Perch
	@property
	def moverrlim(self) -> typing.List[int]:
		return self._instance.Moverrlim
	@property
	def perchtol(self) -> typing.List[float]:
		return self._instance.Perchtol
	@property
	def stoperlim(self) -> typing.List[int]:
		return self._instance.Stoperlim
	@property
	def stoptol(self) -> typing.List[int]:
		return self._instance.Stoptol
	@property
	def servo_ctrl(self) -> int:
		return self._instance.ServoCtrl
	@property
	def ps_sv_off_a(self) -> int:
		return self._instance.PsSvOffA
	@property
	def sv_off_all(self) -> bool:
		return self._instance.SvOffAll
	@property
	def sv_off_enb(self) -> typing.List[bool]:
		return self._instance.SvOffEnb
	@property
	def sv_off_time(self) -> typing.List[int]:
		return self._instance.SvOffTime
	@property
	def upperlims(self) -> typing.List[float]:
		return self._instance.Upperlims
	@property
	def upperlimsdf(self) -> typing.List[float]:
		return self._instance.Upperlimsdf
	@property
	def trkerrlim(self) -> int:
		return self._instance.Trkerrlim
	@property
	def payload(self) -> int:
		return self._instance.Payload
	@property
	def ps_max_payl(self) -> int:
		return self._instance.PsMaxPayl
	@property
	def max_payload(self) -> float:
		return self._instance.MaxPayload
	@property
	def axisinertia(self) -> typing.List[int]:
		return self._instance.Axisinertia
	@property
	def axismoment(self) -> typing.List[int]:
		return self._instance.Axismoment
	@property
	def max_amp_cur(self) -> typing.List[float]:
		return self._instance.MaxAmpCur
	@property
	def accel_param(self) -> typing.List[float]:
		return self._instance.AccelParam
	@property
	def max_pth_acc(self) -> float:
		return self._instance.MaxPthAcc
	@property
	def mrrdum2(self) -> int:
		return self._instance.Mrrdum2
	@property
	def ps_bcklsh_c(self) -> int:
		return self._instance.PsBcklshC
	@property
	def bcklsh_coun(self) -> typing.List[int]:
		return self._instance.BcklshCoun
	@property
	def mover_gain(self) -> typing.List[float]:
		return self._instance.MoverGain
	@property
	def mover_scale(self) -> typing.List[float]:
		return self._instance.MoverScale
	@property
	def mover_offst(self) -> typing.List[int]:
		return self._instance.MoverOffst
	@property
	def clalm_time(self) -> int:
		return self._instance.ClalmTime
	@property
	def tsmod_time(self) -> int:
		return self._instance.TsmodTime
	@property
	def chklimtyp(self) -> int:
		return self._instance.Chklimtyp
	@property
	def snglrty_stp(self) -> bool:
		return self._instance.SnglrtyStp
	@property
	def inpos_type(self) -> int:
		return self._instance.InposType
	@property
	def jog_time_m(self) -> int:
		return self._instance.JogTimeM
	@property
	def min_acc_uma(self) -> int:
		return self._instance.MinAccUma
	@property
	def min_acc_uca(self) -> int:
		return self._instance.MinAccUca
	@property
	def acc_scl_uca(self) -> float:
		return self._instance.AccSclUca
	@property
	def slmt_j1_lw(self) -> typing.List[float]:
		return self._instance.SlmtJ1Lw
	@property
	def slmt_j1_up(self) -> typing.List[float]:
		return self._instance.SlmtJ1Up
	@property
	def slmt_e1_lw(self) -> typing.List[float]:
		return self._instance.SlmtE1Lw
	@property
	def slmt_e1_up(self) -> typing.List[float]:
		return self._instance.SlmtE1Up
	@property
	def slmt_j1_num(self) -> int:
		return self._instance.SlmtJ1Num
	@property
	def slmt_e1_num(self) -> int:
		return self._instance.SlmtE1Num
	@property
	def ps_spccount(self) -> int:
		return self._instance.PsSpccount
	@property
	def spccounttol(self) -> typing.List[int]:
		return self._instance.Spccounttol
	@property
	def spcmovetol(self) -> typing.List[int]:
		return self._instance.Spcmovetol
	@property
	def shortmo_mgn(self) -> float:
		return self._instance.ShortmoMgn
	@property
	def min_acc_cmc(self) -> int:
		return self._instance.MinAccCmc
	@property
	def extaccratio(self) -> float:
		return self._instance.Extaccratio
	@property
	def cn_gear_n1(self) -> int:
		return self._instance.CnGearN1
	@property
	def cn_gear_n2(self) -> int:
		return self._instance.CnGearN2
	@property
	def sflt_erlim(self) -> typing.List[int]:
		return self._instance.SfltErlim
	@property
	def sv_ctrl_typ(self) -> typing.List[int]:
		return self._instance.SvCtrlTyp
	@property
	def ps_cartmo_m(self) -> int:
		return self._instance.PsCartmoM
	@property
	def cartmo_mgn(self) -> float:
		return self._instance.CartmoMgn
	@property
	def min_cat_uma(self) -> int:
		return self._instance.MinCatUma
	@property
	def min_acc_shm(self) -> int:
		return self._instance.MinAccShm
	@property
	def gear_ratio(self) -> typing.List[float]:
		return self._instance.GearRatio
	@property
	def exp_jog_acc(self) -> typing.List[int]:
		return self._instance.ExpJogAcc
	@property
	def ps_armload(self) -> int:
		return self._instance.PsArmload
	@property
	def armload(self) -> typing.List[float]:
		return self._instance.Armload
	@property
	def acc_pa_uma(self) -> float:
		return self._instance.AccPaUma
	@property
	def acc_pc_uma(self) -> float:
		return self._instance.AccPcUma
	@property
	def axis_im_scl(self) -> int:
		return self._instance.AxisImScl
	@property
	def ps_mot_lim(self) -> int:
		return self._instance.PsMotLim
	@property
	def mot_lim_stp(self) -> bool:
		return self._instance.MotLimStp
	@property
	def jg_fltr_scl(self) -> float:
		return self._instance.JgFltrScl
	@property
	def jogaccratio(self) -> typing.List[float]:
		return self._instance.Jogaccratio
	@property
	def torque_cons(self) -> typing.List[float]:
		return self._instance.TorqueCons
	@property
	def min_payload(self) -> float:
		return self._instance.MinPayload
	@property
	def decoup_mgn(self) -> typing.List[float]:
		return self._instance.DecoupMgn
	@property
	def decp_mgn_wr(self) -> typing.List[float]:
		return self._instance.DecpMgnWr
	@property
	def payload_x(self) -> float:
		return self._instance.PayloadX
	@property
	def payload_y(self) -> float:
		return self._instance.PayloadY
	@property
	def payload_z(self) -> float:
		return self._instance.PayloadZ
	@property
	def payload_ix(self) -> float:
		return self._instance.PayloadIx
	@property
	def payload_iy(self) -> float:
		return self._instance.PayloadIy
	@property
	def payload_iz(self) -> float:
		return self._instance.PayloadIz
	@property
	def ffg_mgn_j2(self) -> float:
		return self._instance.FfgMgnJ2
	@property
	def ffg_mgn_j3(self) -> float:
		return self._instance.FfgMgnJ3
	@property
	def dvc_ac0_max(self) -> typing.List[float]:
		return self._instance.DvcAc0Max
	@property
	def dvc_ac1_max(self) -> typing.List[float]:
		return self._instance.DvcAc1Max
	@property
	def dvc_acc_max(self) -> typing.List[float]:
		return self._instance.DvcAccMax
	@property
	def dvc_acc_min(self) -> typing.List[float]:
		return self._instance.DvcAccMin
	@property
	def dvc_jrk_max(self) -> typing.List[float]:
		return self._instance.DvcJrkMax
	@property
	def dvc_jrk_min(self) -> typing.List[float]:
		return self._instance.DvcJrkMin
	@property
	def sv_dbl_smt(self) -> bool:
		return self._instance.SvDblSmt
	@property
	def sv_mcmd_dly(self) -> bool:
		return self._instance.SvMcmdDly
	@property
	def sv_grv_x(self) -> float:
		return self._instance.SvGrvX
	@property
	def sv_grv_y(self) -> float:
		return self._instance.SvGrvY
	@property
	def sv_grv_z(self) -> float:
		return self._instance.SvGrvZ
	@property
	def sv_dh_d(self) -> typing.List[float]:
		return self._instance.SvDhD
	@property
	def sv_dh_a(self) -> typing.List[float]:
		return self._instance.SvDhA
	@property
	def sv_dh_cosa(self) -> typing.List[float]:
		return self._instance.SvDhCosa
	@property
	def sv_dh_sina(self) -> typing.List[float]:
		return self._instance.SvDhSina
	@property
	def sv_lnk_m(self) -> typing.List[float]:
		return self._instance.SvLnkM
	@property
	def sv_lnk_x(self) -> typing.List[float]:
		return self._instance.SvLnkX
	@property
	def sv_lnk_y(self) -> typing.List[float]:
		return self._instance.SvLnkY
	@property
	def sv_lnk_z(self) -> typing.List[float]:
		return self._instance.SvLnkZ
	@property
	def sv_lnk_ix(self) -> typing.List[float]:
		return self._instance.SvLnkIx
	@property
	def sv_lnk_iy(self) -> typing.List[float]:
		return self._instance.SvLnkIy
	@property
	def sv_lnk_iz(self) -> typing.List[float]:
		return self._instance.SvLnkIz
	@property
	def sv_z_sign(self) -> typing.List[bool]:
		return self._instance.SvZSign
	@property
	def sv_dmy_lnk(self) -> typing.List[bool]:
		return self._instance.SvDmyLnk
	@property
	def sv_dh_costh(self) -> typing.List[float]:
		return self._instance.SvDhCosth
	@property
	def sv_dh_sinth(self) -> typing.List[float]:
		return self._instance.SvDhSinth
	@property
	def sv_thet0(self) -> typing.List[float]:
		return self._instance.SvThet0
	@property
	def lnk23z(self) -> float:
		return self._instance.Lnk23z
	@property
	def lnk23x(self) -> float:
		return self._instance.Lnk23x
	@property
	def lnkcbz(self) -> float:
		return self._instance.Lnkcbz
	@property
	def lnkcbx(self) -> float:
		return self._instance.Lnkcbx
	@property
	def cb_mass(self) -> float:
		return self._instance.CbMass
	@property
	def cb_ix(self) -> float:
		return self._instance.CbIx
	@property
	def cb_iy(self) -> float:
		return self._instance.CbIy
	@property
	def cb_iz(self) -> float:
		return self._instance.CbIz
	@property
	def lnksby(self) -> float:
		return self._instance.Lnksby
	@property
	def lnksbx(self) -> float:
		return self._instance.Lnksbx
	@property
	def lngtsb(self) -> float:
		return self._instance.Lngtsb
	@property
	def spcns(self) -> float:
		return self._instance.Spcns
	@property
	def armload_x(self) -> typing.List[float]:
		return self._instance.ArmloadX
	@property
	def armload_y(self) -> typing.List[float]:
		return self._instance.ArmloadY
	@property
	def armload_z(self) -> typing.List[float]:
		return self._instance.ArmloadZ
	@property
	def duty_enb(self) -> typing.List[bool]:
		return self._instance.DutyEnb
	@property
	def duty_param1(self) -> typing.List[float]:
		return self._instance.DutyParam1
	@property
	def duty_param2(self) -> typing.List[float]:
		return self._instance.DutyParam2
	@property
	def qstop_tol(self) -> typing.List[float]:
		return self._instance.QstopTol
	@property
	def ne_enb(self) -> int:
		return self._instance.NeEnb
	@property
	def link_type(self) -> typing.List[int]:
		return self._instance.LinkType
	@property
	def armload_num(self) -> typing.List[int]:
		return self._instance.ArmloadNum
	@property
	def dh_theta0(self) -> typing.List[float]:
		return self._instance.DhTheta0
	@property
	def dh_theta(self) -> typing.List[float]:
		return self._instance.DhTheta
	@property
	def dh_d(self) -> typing.List[float]:
		return self._instance.DhD
	@property
	def dh_a(self) -> typing.List[float]:
		return self._instance.DhA
	@property
	def dh_alpha(self) -> typing.List[float]:
		return self._instance.DhAlpha
	@property
	def link_m(self) -> typing.List[float]:
		return self._instance.LinkM
	@property
	def link_sx(self) -> typing.List[float]:
		return self._instance.LinkSx
	@property
	def link_sy(self) -> typing.List[float]:
		return self._instance.LinkSy
	@property
	def link_sz(self) -> typing.List[float]:
		return self._instance.LinkSz
	@property
	def link_ix(self) -> typing.List[float]:
		return self._instance.LinkIx
	@property
	def link_iy(self) -> typing.List[float]:
		return self._instance.LinkIy
	@property
	def link_iz(self) -> typing.List[float]:
		return self._instance.LinkIz
	@property
	def dh_vd(self) -> typing.List[float]:
		return self._instance.DhVd
	@property
	def dh_va(self) -> typing.List[float]:
		return self._instance.DhVa
	@property
	def dh_valpha(self) -> typing.List[float]:
		return self._instance.DhValpha
	@property
	def link_vm(self) -> typing.List[float]:
		return self._instance.LinkVm
	@property
	def link_vsx(self) -> typing.List[float]:
		return self._instance.LinkVsx
	@property
	def link_vsy(self) -> typing.List[float]:
		return self._instance.LinkVsy
	@property
	def link_vsz(self) -> typing.List[float]:
		return self._instance.LinkVsz
	@property
	def link_vix(self) -> typing.List[float]:
		return self._instance.LinkVix
	@property
	def link_viy(self) -> typing.List[float]:
		return self._instance.LinkViy
	@property
	def link_viz(self) -> typing.List[float]:
		return self._instance.LinkViz
	@property
	def dh_hd(self) -> typing.List[float]:
		return self._instance.DhHd
	@property
	def dh_ha(self) -> typing.List[float]:
		return self._instance.DhHa
	@property
	def dh_halpha(self) -> typing.List[float]:
		return self._instance.DhHalpha
	@property
	def link_hm(self) -> typing.List[float]:
		return self._instance.LinkHm
	@property
	def link_hsx(self) -> typing.List[float]:
		return self._instance.LinkHsx
	@property
	def link_hsy(self) -> typing.List[float]:
		return self._instance.LinkHsy
	@property
	def link_hsz(self) -> typing.List[float]:
		return self._instance.LinkHsz
	@property
	def link_hix(self) -> typing.List[float]:
		return self._instance.LinkHix
	@property
	def link_hiy(self) -> typing.List[float]:
		return self._instance.LinkHiy
	@property
	def link_hiz(self) -> typing.List[float]:
		return self._instance.LinkHiz
	@property
	def dh_otheta(self) -> typing.List[float]:
		return self._instance.DhOtheta
	@property
	def dh_od(self) -> typing.List[float]:
		return self._instance.DhOd
	@property
	def dh_oa(self) -> typing.List[float]:
		return self._instance.DhOa
	@property
	def dh_oalpha(self) -> typing.List[float]:
		return self._instance.DhOalpha
	@property
	def link_om(self) -> typing.List[float]:
		return self._instance.LinkOm
	@property
	def link_osx(self) -> typing.List[float]:
		return self._instance.LinkOsx
	@property
	def link_osy(self) -> typing.List[float]:
		return self._instance.LinkOsy
	@property
	def link_osz(self) -> typing.List[float]:
		return self._instance.LinkOsz
	@property
	def link_oix(self) -> typing.List[float]:
		return self._instance.LinkOix
	@property
	def link_oiy(self) -> typing.List[float]:
		return self._instance.LinkOiy
	@property
	def link_oiz(self) -> typing.List[float]:
		return self._instance.LinkOiz
	@property
	def flink_bx(self) -> typing.List[float]:
		return self._instance.FlinkBx
	@property
	def flink_by(self) -> typing.List[float]:
		return self._instance.FlinkBy
	@property
	def flink_beta(self) -> typing.List[float]:
		return self._instance.FlinkBeta
	@property
	def spbalance_k(self) -> typing.List[float]:
		return self._instance.SpbalanceK
	@property
	def splength0(self) -> typing.List[float]:
		return self._instance.Splength0
	@property
	def spact_x(self) -> typing.List[float]:
		return self._instance.SpactX
	@property
	def spact_y(self) -> typing.List[float]:
		return self._instance.SpactY
	@property
	def spact_z(self) -> typing.List[float]:
		return self._instance.SpactZ
	@property
	def spfulc_x(self) -> typing.List[float]:
		return self._instance.SpfulcX
	@property
	def spfulc_y(self) -> typing.List[float]:
		return self._instance.SpfulcY
	@property
	def spfulc_z(self) -> typing.List[float]:
		return self._instance.SpfulcZ
	@property
	def interaction(self) -> typing.List[InteractVariableType]:
		return [InteractVariableType(x) for x in self._instance.Interaction]
	@property
	def auto_sngstp(self) -> bool:
		return self._instance.AutoSngstp
	@property
	def t1t2_sngstp(self) -> bool:
		return self._instance.T1t2Sngstp
	@property
	def cart2nd_ti(self) -> int:
		return self._instance.Cart2ndTi
	@property
	def jnt2nd_tim(self) -> typing.List[int]:
		return self._instance.Jnt2ndTim
	@property
	def lc_qstp_enb(self) -> bool:
		return self._instance.LcQstpEnb
	@property
	def cp_cutoffov(self) -> int:
		return self._instance.CpCutoffov
	@property
	def cp_minseg(self) -> int:
		return self._instance.CpMinseg
	@property
	def mastrev_enb(self) -> bool:
		return self._instance.MastrevEnb
	@property
	def maspos_diff(self) -> typing.List[float]:
		return self._instance.MasposDiff
	@property
	def intrac_num(self) -> typing.List[IntracNVariableType]:
		return [IntracNVariableType(x) for x in self._instance.IntracNum]
	@property
	def intrac_div(self) -> typing.List[IntracDVariableType]:
		return [IntracDVariableType(x) for x in self._instance.IntracDiv]
	@property
	def obs_dist(self) -> float:
		return self._instance.ObsDist
	@property
	def sv_param(self) -> typing.List[float]:
		return self._instance.SvParam
	@property
	def mijntchklmt(self) -> bool:
		return self._instance.Mijntchklmt
	@property
	def lchwarn_enb(self) -> bool:
		return self._instance.LchwarnEnb
	@property
	def abc_param(self) -> typing.List[float]:
		return self._instance.AbcParam
	@property
	def mech_mask(self) -> int:
		return self._instance.MechMask
	@property
	def mech_type(self) -> int:
		return self._instance.MechType
	@property
	def axs_map_num(self) -> int:
		return self._instance.AxsMapNum
	@property
	def axs_map(self) -> typing.List[int]:
		return self._instance.AxsMap
	@property
	def dh_extra(self) -> typing.List[DhExtraVariableType]:
		return [DhExtraVariableType(x) for x in self._instance.DhExtra]
	@property
	def axs_couple(self) -> typing.List[int]:
		return self._instance.AxsCouple
	@property
	def ps_robot_cr(self) -> int:
		return self._instance.PsRobotCr
	@property
	def robot_crc(self) -> int:
		return self._instance.RobotCrc
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
