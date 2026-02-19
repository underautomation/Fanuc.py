import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ScrVariableType as scr_variable_type

class ScrVariableType(GenericVariableType):
	'''Describes the Fanuc type SCR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = scr_variable_type()
		else:
			self._instance = _internal

	@property
	def itp_time(self) -> int:
		'''Value of variable $ITP_TIME'''
		return self._instance.ItpTime

	@property
	def num_group(self) -> int:
		'''Value of variable $NUM_GROUP'''
		return self._instance.NumGroup

	@property
	def num_tot_axs(self) -> int:
		'''Value of variable $NUM_TOT_AXS'''
		return self._instance.NumTotAxs

	@property
	def num_dsp_axs(self) -> int:
		'''Value of variable $NUM_DSP_AXS'''
		return self._instance.NumDspAxs

	@property
	def joglim(self) -> int:
		'''Value of variable $JOGLIM'''
		return self._instance.Joglim

	@property
	def fine_pcnt(self) -> int:
		'''Value of variable $FINE_PCNT'''
		return self._instance.FinePcnt

	@property
	def cond_time(self) -> int:
		'''Value of variable $COND_TIME'''
		return self._instance.CondTime

	@property
	def maxnumtask(self) -> int:
		'''Value of variable $MAXNUMTASK'''
		return self._instance.Maxnumtask

	@property
	def kept_mirlim(self) -> int:
		'''Value of variable $KEPT_MIRLIM'''
		return self._instance.KeptMirlim

	@property
	def maxpremtn(self) -> int:
		'''Value of variable $MAXPREMTN'''
		return self._instance.Maxpremtn

	@property
	def maxpreapl(self) -> int:
		'''Value of variable $MAXPREAPL'''
		return self._instance.Maxpreapl

	@property
	def pre_exe_enb(self) -> bool:
		'''Value of variable $PRE_EXE_ENB'''
		return self._instance.PreExeEnb

	@property
	def num_sys_mir(self) -> int:
		'''Value of variable $NUM_SYS_MIR'''
		return self._instance.NumSysMir

	@property
	def num_pg_mir(self) -> int:
		'''Value of variable $NUM_PG_MIR'''
		return self._instance.NumPgMir

	@property
	def brkhold_enb(self) -> bool:
		'''Value of variable $BRKHOLD_ENB'''
		return self._instance.BrkholdEnb

	@property
	def enc_axis(self) -> typing.List[int]:
		'''Value of variable $ENC_AXIS'''
		return self._instance.EncAxis

	@property
	def enc_type(self) -> typing.List[int]:
		'''Value of variable $ENC_TYPE'''
		return self._instance.EncType

	@property
	def num_gp_made(self) -> int:
		'''Value of variable $NUM_GP_MADE'''
		return self._instance.NumGpMade

	@property
	def num_rlibsoc(self) -> int:
		'''Value of variable $NUM_RLIBSOC'''
		return self._instance.NumRlibsoc

	@property
	def num_motnsoc(self) -> int:
		'''Value of variable $NUM_MOTNSOC'''
		return self._instance.NumMotnsoc

	@property
	def dummy164(self) -> int:
		'''Value of variable $DUMMY164'''
		return self._instance.Dummy164

	@property
	def sv_code_opt(self) -> int:
		'''Value of variable $SV_CODE_OPT'''
		return self._instance.SvCodeOpt

	@property
	def sfspd_ovrd(self) -> typing.List[int]:
		'''Value of variable $SFSPD_OVRD'''
		return self._instance.SfspdOvrd

	@property
	def coldovrd(self) -> int:
		'''Value of variable $COLDOVRD'''
		return self._instance.Coldovrd

	@property
	def coordovrd(self) -> int:
		'''Value of variable $COORDOVRD'''
		return self._instance.Coordovrd

	@property
	def tpenbleovrd(self) -> int:
		'''Value of variable $TPENBLEOVRD'''
		return self._instance.Tpenbleovrd

	@property
	def fenceovrd(self) -> int:
		'''Value of variable $FENCEOVRD'''
		return self._instance.Fenceovrd

	@property
	def jogovlim(self) -> int:
		'''Value of variable $JOGOVLIM'''
		return self._instance.Jogovlim

	@property
	def sfjogovlim(self) -> int:
		'''Value of variable $SFJOGOVLIM'''
		return self._instance.Sfjogovlim

	@property
	def runovlim(self) -> int:
		'''Value of variable $RUNOVLIM'''
		return self._instance.Runovlim

	@property
	def sfrunovlim(self) -> int:
		'''Value of variable $SFRUNOVLIM'''
		return self._instance.Sfrunovlim

	@property
	def maxnumufram(self) -> int:
		'''Value of variable $MAXNUMUFRAM'''
		return self._instance.Maxnumufram

	@property
	def maxnumutool(self) -> int:
		'''Value of variable $MAXNUMUTOOL'''
		return self._instance.Maxnumutool

	@property
	def lchdly_time(self) -> int:
		'''Value of variable $LCHDLY_TIME'''
		return self._instance.LchdlyTime

	@property
	def recov_ovrd(self) -> bool:
		'''Value of variable $RECOV_OVRD'''
		return self._instance.RecovOvrd

	@property
	def jogwst_mode(self) -> bool:
		'''Value of variable $JOGWST_MODE'''
		return self._instance.JogwstMode

	@property
	def joglimrot(self) -> int:
		'''Value of variable $JOGLIMROT'''
		return self._instance.Joglimrot

	@property
	def motn_pc_run(self) -> typing.List[int]:
		'''Value of variable $MOTN_PC_RUN'''
		return self._instance.MotnPcRun

	@property
	def resetinvert(self) -> bool:
		'''Value of variable $RESETINVERT'''
		return self._instance.Resetinvert

	@property
	def ofstincval(self) -> int:
		'''Value of variable $OFSTINCVAL'''
		return self._instance.Ofstincval

	@property
	def fwdenblovrd(self) -> int:
		'''Value of variable $FWDENBLOVRD'''
		return self._instance.Fwdenblovrd

	@property
	def tpmotnenabl(self) -> int:
		'''Value of variable $TPMOTNENABL'''
		return self._instance.Tpmotnenabl

	@property
	def prev_ctrl(self) -> bool:
		'''Value of variable $PREV_CTRL'''
		return self._instance.PrevCtrl

	@property
	def max_pre_fdo(self) -> int:
		'''Value of variable $MAX_PRE_FDO'''
		return self._instance.MaxPreFdo

	@property
	def pre_mb_cmp(self) -> bool:
		'''Value of variable $PRE_MB_CMP'''
		return self._instance.PreMbCmp

	@property
	def mb_dsbl_msk(self) -> int:
		'''Value of variable $MB_DSBL_MSK'''
		return self._instance.MbDsblMsk

	@property
	def mb_dsb_msk2(self) -> int:
		'''Value of variable $MB_DSB_MSK2'''
		return self._instance.MbDsbMsk2

	@property
	def svstat(self) -> int:
		'''Value of variable $SVSTAT'''
		return self._instance.Svstat

	@property
	def update_time(self) -> int:
		'''Value of variable $UPDATE_TIME'''
		return self._instance.UpdateTime

	@property
	def jg_dsbl_msk(self) -> int:
		'''Value of variable $JG_DSBL_MSK'''
		return self._instance.JgDsblMsk

	@property
	def num_pg_amr(self) -> int:
		'''Value of variable $NUM_PG_AMR'''
		return self._instance.NumPgAmr

	@property
	def mb_ld_msk(self) -> int:
		'''Value of variable $MB_LD_MSK'''
		return self._instance.MbLdMsk

	@property
	def motn_ld_msk(self) -> int:
		'''Value of variable $MOTN_LD_MSK'''
		return self._instance.MotnLdMsk

	@property
	def motn_ld_mk2(self) -> int:
		'''Value of variable $MOTN_LD_MK2'''
		return self._instance.MotnLdMk2

	@property
	def amp_type(self) -> typing.List[int]:
		'''Value of variable $AMP_TYPE'''
		return self._instance.AmpType

	@property
	def cap_amp_dis(self) -> typing.List[float]:
		'''Value of variable $CAP_AMP_DIS'''
		return self._instance.CapAmpDis

	@property
	def hbk_map_enb(self) -> bool:
		'''Value of variable $HBK_MAP_ENB'''
		return self._instance.HbkMapEnb

	@property
	def hbk_io_type(self) -> int:
		'''Value of variable $HBK_IO_TYPE'''
		return self._instance.HbkIoType

	@property
	def hbk_io_idx(self) -> int:
		'''Value of variable $HBK_IO_IDX'''
		return self._instance.HbkIoIdx

	@property
	def ppa_map_enb(self) -> bool:
		'''Value of variable $PPA_MAP_ENB'''
		return self._instance.PpaMapEnb

	@property
	def ppa_io_type(self) -> int:
		'''Value of variable $PPA_IO_TYPE'''
		return self._instance.PpaIoType

	@property
	def ppa_io_idx(self) -> int:
		'''Value of variable $PPA_IO_IDX'''
		return self._instance.PpaIoIdx

	@property
	def motn_ld_idx(self) -> typing.List[int]:
		'''Value of variable $MOTN_LD_IDX'''
		return self._instance.MotnLdIdx

	@property
	def dvc_dbg(self) -> int:
		'''Value of variable $DVC_DBG'''
		return self._instance.DvcDbg

	@property
	def dvc_enb(self) -> bool:
		'''Value of variable $DVC_ENB'''
		return self._instance.DvcEnb

	@property
	def dvc_mode(self) -> int:
		'''Value of variable $DVC_MODE'''
		return self._instance.DvcMode

	@property
	def dvc_mode1(self) -> int:
		'''Value of variable $DVC_MODE1'''
		return self._instance.DvcMode1

	@property
	def dvc_mode2(self) -> int:
		'''Value of variable $DVC_MODE2'''
		return self._instance.DvcMode2

	@property
	def dvc_mode3(self) -> int:
		'''Value of variable $DVC_MODE3'''
		return self._instance.DvcMode3

	@property
	def dvc_c_ratio(self) -> float:
		'''Value of variable $DVC_C_RATIO'''
		return self._instance.DvcCRatio

	@property
	def intask_ovru(self) -> int:
		'''Value of variable $INTASK_OVRU'''
		return self._instance.IntaskOvru

	@property
	def dsp_type(self) -> int:
		'''Value of variable $DSP_TYPE'''
		return self._instance.DspType

	@property
	def cabinet_typ(self) -> int:
		'''Value of variable $CABINET_TYP'''
		return self._instance.CabinetTyp

	@property
	def ne_mode(self) -> int:
		'''Value of variable $NE_MODE'''
		return self._instance.NeMode

	@property
	def pg_dsbl_msk(self) -> int:
		'''Value of variable $PG_DSBL_MSK'''
		return self._instance.PgDsblMsk

	@property
	def jog_aux_enb(self) -> bool:
		'''Value of variable $JOG_AUX_ENB'''
		return self._instance.JogAuxEnb

	@property
	def subcpu(self) -> bool:
		'''Value of variable $SUBCPU'''
		return self._instance.Subcpu

	@property
	def ne_sin_reso(self) -> int:
		'''Value of variable $NE_SIN_RESO'''
		return self._instance.NeSinReso

	@property
	def update_map1(self) -> int:
		'''Value of variable $UPDATE_MAP1'''
		return self._instance.UpdateMap1

	@property
	def update_map2(self) -> int:
		'''Value of variable $UPDATE_MAP2'''
		return self._instance.UpdateMap2

	@property
	def update_flag(self) -> typing.List[int]:
		'''Value of variable $UPDATE_FLAG'''
		return self._instance.UpdateFlag

	@property
	def hw_c1_time1(self) -> int:
		'''Value of variable $HW_C1_TIME1'''
		return self._instance.HwC1Time1

	@property
	def hw_c1_time2(self) -> int:
		'''Value of variable $HW_C1_TIME2'''
		return self._instance.HwC1Time2

	@property
	def atr(self) -> typing.List[int]:
		'''Value of variable $ATR'''
		return self._instance.Atr

	@property
	def unittype(self) -> typing.List[int]:
		'''Value of variable $UNITTYPE'''
		return self._instance.Unittype

	@property
	def atrattrib(self) -> typing.List[int]:
		'''Value of variable $ATRATTRIB'''
		return self._instance.Atrattrib

	@property
	def ne_cycle(self) -> int:
		'''Value of variable $NE_CYCLE'''
		return self._instance.NeCycle

	@property
	def neca_ovrun(self) -> int:
		'''Value of variable $NECA_OVRUN'''
		return self._instance.NecaOvrun

	@property
	def fltr2_fix(self) -> int:
		'''Value of variable $FLTR_2_FIX'''
		return self._instance.Fltr2Fix

	@property
	def startup_cnd(self) -> int:
		'''Value of variable $STARTUP_CND'''
		return self._instance.StartupCnd

	@property
	def dsb_signal(self) -> int:
		'''Value of variable $DSB_SIGNAL'''
		return self._instance.DsbSignal

	@property
	def lpcond_time(self) -> int:
		'''Value of variable $LPCOND_TIME'''
		return self._instance.LpcondTime

	@property
	def chk_ch_sctm(self) -> int:
		'''Value of variable $CHK_CH_SCTM'''
		return self._instance.ChkChSctm

	@property
	def f_atr(self) -> typing.List[int]:
		'''Value of variable $F_ATR'''
		return self._instance.FAtr

	@property
	def f_unittype(self) -> typing.List[int]:
		'''Value of variable $F_UNITTYPE'''
		return self._instance.FUnittype

	@property
	def f_atrattrib(self) -> typing.List[int]:
		'''Value of variable $F_ATRATTRIB'''
		return self._instance.FAtrattrib

	@property
	def fssb_stat(self) -> typing.List[int]:
		'''Value of variable $FSSB_STAT'''
		return self._instance.FssbStat

	@property
	def chain_time(self) -> int:
		'''Value of variable $CHAIN_TIME'''
		return self._instance.ChainTime

	@property
	def chain_stat(self) -> int:
		'''Value of variable $CHAIN_STAT'''
		return self._instance.ChainStat

	@property
	def chain_rsdn(self) -> bool:
		'''Value of variable $CHAIN_RSDN'''
		return self._instance.ChainRsdn

	@property
	def dsp_map_enb(self) -> bool:
		'''Value of variable $DSP_MAP_ENB'''
		return self._instance.DspMapEnb

	@property
	def idx_tbl_msk(self) -> int:
		'''Value of variable $IDX_TBL_MSK'''
		return self._instance.IdxTblMsk

	@property
	def proc_ctrl(self) -> int:
		'''Value of variable $PROC_CTRL'''
		return self._instance.ProcCtrl

	@property
	def temper_lims(self) -> typing.List[int]:
		'''Value of variable $TEMPER_LIMS'''
		return self._instance.TemperLims

	@property
	def fssb1(self) -> typing.List[int]:
		'''Value of variable $FSSB1'''
		return self._instance.Fssb1

	@property
	def fssb2(self) -> typing.List[int]:
		'''Value of variable $FSSB2'''
		return self._instance.Fssb2

	@property
	def fssbdiagenb(self) -> bool:
		'''Value of variable $FSSBDIAGENB'''
		return self._instance.Fssbdiagenb

	@property
	def railacc_enb(self) -> bool:
		'''Value of variable $RAILACC_ENB'''
		return self._instance.RailaccEnb

	@property
	def smcr_loaded(self) -> int:
		'''Value of variable $SMCR_LOADED'''
		return self._instance.SmcrLoaded

	@property
	def dummy165(self) -> int:
		'''Value of variable $DUMMY165'''
		return self._instance.Dummy165

	@property
	def dsp_type2(self) -> int:
		'''Value of variable $DSP_TYPE2'''
		return self._instance.DspType2

	@property
	def prc_dsp(self) -> typing.List[bool]:
		'''Value of variable $PRC_DSP'''
		return self._instance.PrcDsp

	@property
	def prc_cd_id(self) -> str:
		'''Value of variable $PRC_CD_ID'''
		return self._instance.PrcCdId

	@property
	def motn_func(self) -> typing.List[int]:
		'''Value of variable $MOTN_FUNC'''
		return self._instance.MotnFunc

	@property
	def intrins_tp(self) -> bool:
		'''Value of variable $INTRINS_TP'''
		return self._instance.IntrinsTp

	@property
	def diag_func(self) -> int:
		'''Value of variable $DIAG_FUNC'''
		return self._instance.DiagFunc

	@property
	def trans_num(self) -> typing.List[int]:
		'''Value of variable $TRANS_NUM'''
		return self._instance.TransNum

	@property
	def trans_max(self) -> typing.List[float]:
		'''Value of variable $TRANS_MAX'''
		return self._instance.TransMax

	@property
	def trans_warn(self) -> typing.List[float]:
		'''Value of variable $TRANS_WARN'''
		return self._instance.TransWarn

	@property
	def cblcur_max(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_MAX'''
		return self._instance.CblcurMax

	@property
	def cblcur_a(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_A'''
		return self._instance.CblcurA

	@property
	def cblcur_b(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_B'''
		return self._instance.CblcurB

	@property
	def cblcur_warn(self) -> typing.List[float]:
		'''Value of variable $CBLCUR_WARN'''
		return self._instance.CblcurWarn

	@property
	def dac_trans(self) -> typing.List[float]:
		'''Value of variable $DAC_TRANS'''
		return self._instance.DacTrans

	@property
	def dac_cblcur(self) -> typing.List[float]:
		'''Value of variable $DAC_CBLCUR'''
		return self._instance.DacCblcur

	@property
	def cldet_pt(self) -> int:
		'''Value of variable $CLDET_PT'''
		return self._instance.CldetPt

	@property
	def cldet_axs(self) -> typing.List[int]:
		'''Value of variable $CLDET_AXS'''
		return self._instance.CldetAxs

	@property
	def cldet_time(self) -> typing.List[int]:
		'''Value of variable $CLDET_TIME'''
		return self._instance.CldetTime

	@property
	def ce_ria_sw(self) -> int:
		'''Value of variable $CE_RIA_SW'''
		return self._instance.CeRiaSw

	@property
	def safe_spd(self) -> float:
		'''Value of variable $SAFE_SPD'''
		return self._instance.SafeSpd

	@property
	def safe_rotspd(self) -> float:
		'''Value of variable $SAFE_ROTSPD'''
		return self._instance.SafeRotspd

	@property
	def t2_lock_enb(self) -> int:
		'''Value of variable $T2_LOCK_ENB'''
		return self._instance.T2LockEnb

	@property
	def dsb_moinit(self) -> bool:
		'''Value of variable $DSB_MOINIT'''
		return self._instance.DsbMoinit

	@property
	def max_df_len(self) -> int:
		'''Value of variable $MAX_DF_LEN'''
		return self._instance.MaxDfLen

	@property
	def mpdt_timlmt(self) -> int:
		'''Value of variable $MPDT_TIMLMT'''
		return self._instance.MpdtTimlmt

	@property
	def fast_hrdyon(self) -> bool:
		'''Value of variable $FAST_HRDYON'''
		return self._instance.FastHrdyon

	@property
	def org_pth_rsm(self) -> bool:
		'''Value of variable $ORG_PTH_RSM'''
		return self._instance.OrgPthRsm

	@property
	def dac_lmt(self) -> int:
		'''Value of variable $DAC_LMT'''
		return self._instance.DacLmt

	@property
	def mulselenb(self) -> bool:
		'''Value of variable $MULSELENB'''
		return self._instance.Mulselenb

	@property
	def update_map3(self) -> typing.List[int]:
		'''Value of variable $UPDATE_MAP3'''
		return self._instance.UpdateMap3

	@property
	def jcoldovrd(self) -> int:
		'''Value of variable $JCOLDOVRD'''
		return self._instance.Jcoldovrd

	@property
	def jtpenbovrd(self) -> int:
		'''Value of variable $JTPENBOVRD'''
		return self._instance.Jtpenbovrd

	@property
	def jfenceovrd(self) -> int:
		'''Value of variable $JFENCEOVRD'''
		return self._instance.Jfenceovrd

	@property
	def fan_almlvl(self) -> int:
		'''Value of variable $FAN_ALMLVL'''
		return self._instance.FanAlmlvl

	@property
	def fan_wrnlvl(self) -> int:
		'''Value of variable $FAN_WRNLVL'''
		return self._instance.FanWrnlvl

	@property
	def hardtyp_map(self) -> int:
		'''Value of variable $HARDTYP_MAP'''
		return self._instance.HardtypMap

	@property
	def comp_sw(self) -> typing.List[int]:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def fanstop_tim(self) -> int:
		'''Value of variable $FANSTOP_TIM'''
		return self._instance.FanstopTim

	@property
	def brk_eco_enb(self) -> bool:
		'''Value of variable $BRK_ECO_ENB'''
		return self._instance.BrkEcoEnb

	@property
	def autatr_stat(self) -> int:
		'''Value of variable $AUTATR_STAT'''
		return self._instance.AutatrStat

	@property
	def auto_sbridx(self) -> int:
		'''Value of variable $AUTO_SBRIDX'''
		return self._instance.AutoSbridx

	@property
	def auto_dspidx(self) -> int:
		'''Value of variable $AUTO_DSPIDX'''
		return self._instance.AutoDspidx

	@property
	def auto_atridx(self) -> typing.List[int]:
		'''Value of variable $AUTO_ATRIDX'''
		return self._instance.AutoAtridx

	@property
	def auto_ampinf(self) -> typing.List[int]:
		'''Value of variable $AUTO_AMPINF'''
		return self._instance.AutoAmpinf

	@property
	def auto_ampcur(self) -> typing.List[int]:
		'''Value of variable $AUTO_AMPCUR'''
		return self._instance.AutoAmpcur

	@property
	def regtype(self) -> int:
		'''Value of variable $REGTYPE'''
		return self._instance.Regtype

	@property
	def nvdt_enable(self) -> bool:
		'''Value of variable $NVDT_ENABLE'''
		return self._instance.NvdtEnable

	@property
	def enc_dal_no(self) -> int:
		'''Value of variable $ENC_DAL_NO'''
		return self._instance.EncDalNo

	@property
	def pfl_c1_time(self) -> typing.List[int]:
		'''Value of variable $PFL_C1_TIME'''
		return self._instance.PflC1Time

	@property
	def mcurchk(self) -> bool:
		'''Value of variable $MCURCHK'''
		return self._instance.Mcurchk

	@property
	def fan_almlvl2(self) -> typing.List[int]:
		'''Value of variable $FAN_ALMLVL2'''
		return self._instance.FanAlmlvl2

	@property
	def fan_wrnlvl2(self) -> typing.List[int]:
		'''Value of variable $FAN_WRNLVL2'''
		return self._instance.FanWrnlvl2

	@property
	def cmd_inf_cyc(self) -> int:
		'''Value of variable $CMD_INF_CYC'''
		return self._instance.CmdInfCyc

	@property
	def nonax_atr(self) -> int:
		'''Value of variable $NONAX_ATR'''
		return self._instance.NonaxAtr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ScrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
