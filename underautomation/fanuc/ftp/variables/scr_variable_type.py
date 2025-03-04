import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ScrVariableType as scr_variable_type

class ScrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = scr_variable_type()
		else:
			self._instance = _internal
	@property
	def itp_time(self) -> int:
		return self._instance.ItpTime
	@property
	def num_group(self) -> int:
		return self._instance.NumGroup
	@property
	def num_tot_axs(self) -> int:
		return self._instance.NumTotAxs
	@property
	def num_dsp_axs(self) -> int:
		return self._instance.NumDspAxs
	@property
	def joglim(self) -> int:
		return self._instance.Joglim
	@property
	def fine_pcnt(self) -> int:
		return self._instance.FinePcnt
	@property
	def cond_time(self) -> int:
		return self._instance.CondTime
	@property
	def maxnumtask(self) -> int:
		return self._instance.Maxnumtask
	@property
	def kept_mirlim(self) -> int:
		return self._instance.KeptMirlim
	@property
	def maxpremtn(self) -> int:
		return self._instance.Maxpremtn
	@property
	def maxpreapl(self) -> int:
		return self._instance.Maxpreapl
	@property
	def pre_exe_enb(self) -> bool:
		return self._instance.PreExeEnb
	@property
	def num_sys_mir(self) -> int:
		return self._instance.NumSysMir
	@property
	def num_pg_mir(self) -> int:
		return self._instance.NumPgMir
	@property
	def brkhold_enb(self) -> bool:
		return self._instance.BrkholdEnb
	@property
	def enc_axis(self) -> typing.List[int]:
		return self._instance.EncAxis
	@property
	def enc_type(self) -> typing.List[int]:
		return self._instance.EncType
	@property
	def num_gp_made(self) -> int:
		return self._instance.NumGpMade
	@property
	def num_rlibsoc(self) -> int:
		return self._instance.NumRlibsoc
	@property
	def num_motnsoc(self) -> int:
		return self._instance.NumMotnsoc
	@property
	def dummy164(self) -> int:
		return self._instance.Dummy164
	@property
	def sv_code_opt(self) -> int:
		return self._instance.SvCodeOpt
	@property
	def sfspd_ovrd(self) -> typing.List[int]:
		return self._instance.SfspdOvrd
	@property
	def coldovrd(self) -> int:
		return self._instance.Coldovrd
	@property
	def coordovrd(self) -> int:
		return self._instance.Coordovrd
	@property
	def tpenbleovrd(self) -> int:
		return self._instance.Tpenbleovrd
	@property
	def fenceovrd(self) -> int:
		return self._instance.Fenceovrd
	@property
	def jogovlim(self) -> int:
		return self._instance.Jogovlim
	@property
	def sfjogovlim(self) -> int:
		return self._instance.Sfjogovlim
	@property
	def runovlim(self) -> int:
		return self._instance.Runovlim
	@property
	def sfrunovlim(self) -> int:
		return self._instance.Sfrunovlim
	@property
	def maxnumufram(self) -> int:
		return self._instance.Maxnumufram
	@property
	def maxnumutool(self) -> int:
		return self._instance.Maxnumutool
	@property
	def lchdly_time(self) -> int:
		return self._instance.LchdlyTime
	@property
	def recov_ovrd(self) -> bool:
		return self._instance.RecovOvrd
	@property
	def jogwst_mode(self) -> bool:
		return self._instance.JogwstMode
	@property
	def joglimrot(self) -> int:
		return self._instance.Joglimrot
	@property
	def motn_pc_run(self) -> typing.List[int]:
		return self._instance.MotnPcRun
	@property
	def resetinvert(self) -> bool:
		return self._instance.Resetinvert
	@property
	def ofstincval(self) -> int:
		return self._instance.Ofstincval
	@property
	def fwdenblovrd(self) -> int:
		return self._instance.Fwdenblovrd
	@property
	def tpmotnenabl(self) -> int:
		return self._instance.Tpmotnenabl
	@property
	def prev_ctrl(self) -> bool:
		return self._instance.PrevCtrl
	@property
	def max_pre_fdo(self) -> int:
		return self._instance.MaxPreFdo
	@property
	def pre_mb_cmp(self) -> bool:
		return self._instance.PreMbCmp
	@property
	def mb_dsbl_msk(self) -> int:
		return self._instance.MbDsblMsk
	@property
	def mb_dsb_msk2(self) -> int:
		return self._instance.MbDsbMsk2
	@property
	def svstat(self) -> int:
		return self._instance.Svstat
	@property
	def update_time(self) -> int:
		return self._instance.UpdateTime
	@property
	def jg_dsbl_msk(self) -> int:
		return self._instance.JgDsblMsk
	@property
	def num_pg_amr(self) -> int:
		return self._instance.NumPgAmr
	@property
	def mb_ld_msk(self) -> int:
		return self._instance.MbLdMsk
	@property
	def motn_ld_msk(self) -> int:
		return self._instance.MotnLdMsk
	@property
	def motn_ld_mk2(self) -> int:
		return self._instance.MotnLdMk2
	@property
	def amp_type(self) -> typing.List[int]:
		return self._instance.AmpType
	@property
	def cap_amp_dis(self) -> typing.List[float]:
		return self._instance.CapAmpDis
	@property
	def hbk_map_enb(self) -> bool:
		return self._instance.HbkMapEnb
	@property
	def hbk_io_type(self) -> int:
		return self._instance.HbkIoType
	@property
	def hbk_io_idx(self) -> int:
		return self._instance.HbkIoIdx
	@property
	def ppa_map_enb(self) -> bool:
		return self._instance.PpaMapEnb
	@property
	def ppa_io_type(self) -> int:
		return self._instance.PpaIoType
	@property
	def ppa_io_idx(self) -> int:
		return self._instance.PpaIoIdx
	@property
	def motn_ld_idx(self) -> typing.List[int]:
		return self._instance.MotnLdIdx
	@property
	def dvc_dbg(self) -> int:
		return self._instance.DvcDbg
	@property
	def dvc_enb(self) -> bool:
		return self._instance.DvcEnb
	@property
	def dvc_mode(self) -> int:
		return self._instance.DvcMode
	@property
	def dvc_mode1(self) -> int:
		return self._instance.DvcMode1
	@property
	def dvc_mode2(self) -> int:
		return self._instance.DvcMode2
	@property
	def dvc_mode3(self) -> int:
		return self._instance.DvcMode3
	@property
	def dvc_c_ratio(self) -> float:
		return self._instance.DvcCRatio
	@property
	def intask_ovru(self) -> int:
		return self._instance.IntaskOvru
	@property
	def dsp_type(self) -> int:
		return self._instance.DspType
	@property
	def cabinet_typ(self) -> int:
		return self._instance.CabinetTyp
	@property
	def ne_mode(self) -> int:
		return self._instance.NeMode
	@property
	def pg_dsbl_msk(self) -> int:
		return self._instance.PgDsblMsk
	@property
	def jog_aux_enb(self) -> bool:
		return self._instance.JogAuxEnb
	@property
	def subcpu(self) -> bool:
		return self._instance.Subcpu
	@property
	def ne_sin_reso(self) -> int:
		return self._instance.NeSinReso
	@property
	def update_map1(self) -> int:
		return self._instance.UpdateMap1
	@property
	def update_map2(self) -> int:
		return self._instance.UpdateMap2
	@property
	def update_flag(self) -> typing.List[int]:
		return self._instance.UpdateFlag
	@property
	def hw_c1_time1(self) -> int:
		return self._instance.HwC1Time1
	@property
	def hw_c1_time2(self) -> int:
		return self._instance.HwC1Time2
	@property
	def atr(self) -> typing.List[int]:
		return self._instance.Atr
	@property
	def unittype(self) -> typing.List[int]:
		return self._instance.Unittype
	@property
	def atrattrib(self) -> typing.List[int]:
		return self._instance.Atrattrib
	@property
	def ne_cycle(self) -> int:
		return self._instance.NeCycle
	@property
	def neca_ovrun(self) -> int:
		return self._instance.NecaOvrun
	@property
	def fltr2_fix(self) -> int:
		return self._instance.Fltr2Fix
	@property
	def startup_cnd(self) -> int:
		return self._instance.StartupCnd
	@property
	def dsb_signal(self) -> int:
		return self._instance.DsbSignal
	@property
	def lpcond_time(self) -> int:
		return self._instance.LpcondTime
	@property
	def chk_ch_sctm(self) -> int:
		return self._instance.ChkChSctm
	@property
	def f_atr(self) -> typing.List[int]:
		return self._instance.FAtr
	@property
	def f_unittype(self) -> typing.List[int]:
		return self._instance.FUnittype
	@property
	def f_atrattrib(self) -> typing.List[int]:
		return self._instance.FAtrattrib
	@property
	def fssb_stat(self) -> typing.List[int]:
		return self._instance.FssbStat
	@property
	def chain_time(self) -> int:
		return self._instance.ChainTime
	@property
	def chain_stat(self) -> int:
		return self._instance.ChainStat
	@property
	def chain_rsdn(self) -> bool:
		return self._instance.ChainRsdn
	@property
	def dsp_map_enb(self) -> bool:
		return self._instance.DspMapEnb
	@property
	def idx_tbl_msk(self) -> int:
		return self._instance.IdxTblMsk
	@property
	def proc_ctrl(self) -> int:
		return self._instance.ProcCtrl
	@property
	def temper_lims(self) -> typing.List[int]:
		return self._instance.TemperLims
	@property
	def fssb1(self) -> typing.List[int]:
		return self._instance.Fssb1
	@property
	def fssb2(self) -> typing.List[int]:
		return self._instance.Fssb2
	@property
	def fssbdiagenb(self) -> bool:
		return self._instance.Fssbdiagenb
	@property
	def railacc_enb(self) -> bool:
		return self._instance.RailaccEnb
	@property
	def smcr_loaded(self) -> int:
		return self._instance.SmcrLoaded
	@property
	def dummy165(self) -> int:
		return self._instance.Dummy165
	@property
	def dsp_type2(self) -> int:
		return self._instance.DspType2
	@property
	def prc_dsp(self) -> typing.List[bool]:
		return self._instance.PrcDsp
	@property
	def prc_cd_id(self) -> str:
		return self._instance.PrcCdId
	@property
	def motn_func(self) -> typing.List[int]:
		return self._instance.MotnFunc
	@property
	def intrins_tp(self) -> bool:
		return self._instance.IntrinsTp
	@property
	def diag_func(self) -> int:
		return self._instance.DiagFunc
	@property
	def trans_num(self) -> typing.List[int]:
		return self._instance.TransNum
	@property
	def trans_max(self) -> typing.List[float]:
		return self._instance.TransMax
	@property
	def trans_warn(self) -> typing.List[float]:
		return self._instance.TransWarn
	@property
	def cblcur_max(self) -> typing.List[float]:
		return self._instance.CblcurMax
	@property
	def cblcur_a(self) -> typing.List[float]:
		return self._instance.CblcurA
	@property
	def cblcur_b(self) -> typing.List[float]:
		return self._instance.CblcurB
	@property
	def cblcur_warn(self) -> typing.List[float]:
		return self._instance.CblcurWarn
	@property
	def dac_trans(self) -> typing.List[float]:
		return self._instance.DacTrans
	@property
	def dac_cblcur(self) -> typing.List[float]:
		return self._instance.DacCblcur
	@property
	def cldet_pt(self) -> int:
		return self._instance.CldetPt
	@property
	def cldet_axs(self) -> typing.List[int]:
		return self._instance.CldetAxs
	@property
	def cldet_time(self) -> typing.List[int]:
		return self._instance.CldetTime
	@property
	def ce_ria_sw(self) -> int:
		return self._instance.CeRiaSw
	@property
	def safe_spd(self) -> float:
		return self._instance.SafeSpd
	@property
	def safe_rotspd(self) -> float:
		return self._instance.SafeRotspd
	@property
	def t2_lock_enb(self) -> int:
		return self._instance.T2LockEnb
	@property
	def dsb_moinit(self) -> bool:
		return self._instance.DsbMoinit
	@property
	def max_df_len(self) -> int:
		return self._instance.MaxDfLen
	@property
	def mpdt_timlmt(self) -> int:
		return self._instance.MpdtTimlmt
	@property
	def fast_hrdyon(self) -> bool:
		return self._instance.FastHrdyon
	@property
	def org_pth_rsm(self) -> bool:
		return self._instance.OrgPthRsm
	@property
	def dac_lmt(self) -> int:
		return self._instance.DacLmt
	@property
	def mulselenb(self) -> bool:
		return self._instance.Mulselenb
	@property
	def update_map3(self) -> typing.List[int]:
		return self._instance.UpdateMap3
	@property
	def jcoldovrd(self) -> int:
		return self._instance.Jcoldovrd
	@property
	def jtpenbovrd(self) -> int:
		return self._instance.Jtpenbovrd
	@property
	def jfenceovrd(self) -> int:
		return self._instance.Jfenceovrd
	@property
	def fan_almlvl(self) -> int:
		return self._instance.FanAlmlvl
	@property
	def fan_wrnlvl(self) -> int:
		return self._instance.FanWrnlvl
	@property
	def hardtyp_map(self) -> int:
		return self._instance.HardtypMap
	@property
	def comp_sw(self) -> typing.List[int]:
		return self._instance.CompSw
	@property
	def fanstop_tim(self) -> int:
		return self._instance.FanstopTim
	@property
	def brk_eco_enb(self) -> bool:
		return self._instance.BrkEcoEnb
	@property
	def autatr_stat(self) -> int:
		return self._instance.AutatrStat
	@property
	def auto_sbridx(self) -> int:
		return self._instance.AutoSbridx
	@property
	def auto_dspidx(self) -> int:
		return self._instance.AutoDspidx
	@property
	def auto_atridx(self) -> typing.List[int]:
		return self._instance.AutoAtridx
	@property
	def auto_ampinf(self) -> typing.List[int]:
		return self._instance.AutoAmpinf
	@property
	def auto_ampcur(self) -> typing.List[int]:
		return self._instance.AutoAmpcur
	@property
	def regtype(self) -> int:
		return self._instance.Regtype
	@property
	def nvdt_enable(self) -> bool:
		return self._instance.NvdtEnable
	@property
	def enc_dal_no(self) -> int:
		return self._instance.EncDalNo
	@property
	def pfl_c1_time(self) -> typing.List[int]:
		return self._instance.PflC1Time
	@property
	def mcurchk(self) -> bool:
		return self._instance.Mcurchk
	@property
	def fan_almlvl2(self) -> typing.List[int]:
		return self._instance.FanAlmlvl2
	@property
	def fan_wrnlvl2(self) -> typing.List[int]:
		return self._instance.FanWrnlvl2
	@property
	def cmd_inf_cyc(self) -> int:
		return self._instance.CmdInfCyc
	@property
	def nonax_atr(self) -> int:
		return self._instance.NonaxAtr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
