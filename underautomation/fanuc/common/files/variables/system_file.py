from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.aavm_wrk_variable_type import AavmWrkVariableType
from underautomation.fanuc.common.files.variables.abspos_grp_variable_type import AbsposGrpVariableType
from underautomation.fanuc.common.files.variables.aio_cnv_variable_type import AioCnvVariableType
from underautomation.fanuc.common.files.variables.almdg_variable_type import AlmdgVariableType
from underautomation.fanuc.common.files.variables.alm_if_variable_type import AlmIfVariableType
from underautomation.fanuc.common.files.variables.appinfo_variable_type import AppinfoVariableType
from underautomation.fanuc.common.files.variables.apcoupled_variable_type import ApcoupledVariableType
from underautomation.fanuc.common.files.variables.apcureq_variable_type import ApcureqVariableType
from underautomation.fanuc.common.files.variables.arg_str_variable_type import ArgStrVariableType
from underautomation.fanuc.common.files.variables.asbn_cfg_variable_type import AsbnCfgVariableType
from underautomation.fanuc.common.files.variables.at_cellsetup_variable_type import AtCellsetupVariableType
from underautomation.fanuc.common.files.variables.autobackup_variable_type import AutobackupVariableType
from underautomation.fanuc.common.joint_position_variable import JointPositionVariable
from underautomation.fanuc.common.files.variables.axscrdcfg_variable_type import AxscrdcfgVariableType
from underautomation.fanuc.common.files.variables.back_edit_variable_type import BackEditVariableType
from underautomation.fanuc.common.files.variables.bigallow_variable_type import BigallowVariableType
from underautomation.fanuc.common.files.variables.blal_out_variable_type import BlalOutVariableType
from underautomation.fanuc.common.files.variables.cfcfg_variable_type import CfcfgVariableType
from underautomation.fanuc.common.files.variables.chg_pri_variable_type import ChgPriVariableType
from underautomation.fanuc.common.files.variables.chkpos_variable_type import ChkposVariableType
from underautomation.fanuc.common.files.variables.cmd_info_variable_type import CmdInfoVariableType
from underautomation.fanuc.common.files.variables.cocfg_variable_type import CocfgVariableType
from underautomation.fanuc.common.files.variables.collect_variable_type import CollectVariableType
from underautomation.fanuc.common.files.variables.condet_cfg_variable_type import CondetCfgVariableType
from underautomation.fanuc.common.files.variables.condet_grp_variable_type import CondetGrpVariableType
from underautomation.fanuc.common.files.variables.condet_io_variable_type import CondetIoVariableType
from underautomation.fanuc.common.files.variables.condet_trgp_variable_type import CondetTrgpVariableType
from underautomation.fanuc.common.files.variables.condet_trig_variable_type import CondetTrigVariableType
from underautomation.fanuc.common.files.variables.co_morgrp_variable_type import CoMorgrpVariableType
from underautomation.fanuc.common.files.variables.co_paramgp_variable_type import CoParamgpVariableType
from underautomation.fanuc.common.files.variables.cpcfg_variable_type import CpcfgVariableType
from underautomation.fanuc.common.files.variables.cpdbg_variable_type import CpdbgVariableType
from underautomation.fanuc.common.files.variables.cp_mcrgrp_variable_type import CpMcrgrpVariableType
from underautomation.fanuc.common.files.variables.cp_morgrp_variable_type import CpMorgrpVariableType
from underautomation.fanuc.common.files.variables.cp_paramgp_variable_type import CpParamgpVariableType
from underautomation.fanuc.common.files.variables.cp_t1_grp_variable_type import CpT1GrpVariableType
from underautomation.fanuc.common.files.variables.cp_t1_mode_variable_type import CpT1ModeVariableType
from underautomation.fanuc.common.files.variables.custommenu_variable_type import CustommenuVariableType
from underautomation.fanuc.common.files.variables.dbg_errlog_variable_type import DbgErrlogVariableType
from underautomation.fanuc.common.files.variables.dbpxwork_variable_type import DbpxworkVariableType
from underautomation.fanuc.common.files.variables.dbtb_ctrl_variable_type import DbtbCtrlVariableType
from underautomation.fanuc.common.files.variables.db_dbg_variable_type import DbDbgVariableType
from underautomation.fanuc.common.files.variables.db_record_variable_type import DbRecordVariableType
from underautomation.fanuc.common.files.variables.dcss_cnstcy_variable_type import DcssCnstcyVariableType
from underautomation.fanuc.common.files.variables.dcss_device_variable_type import DcssDeviceVariableType
from underautomation.fanuc.common.files.variables.dcss_hndgd_variable_type import DcssHndgdVariableType
from underautomation.fanuc.common.files.variables.dcss_ls_variable_type import DcssLsVariableType
from underautomation.fanuc.common.files.variables.dcss_param_variable_type import DcssParamVariableType
from underautomation.fanuc.common.files.variables.dcss_slave_variable_type import DcssSlaveVariableType
from underautomation.fanuc.common.files.variables.dcs_cfg_variable_type import DcsCfgVariableType
from underautomation.fanuc.common.files.variables.dcs_crc_out_variable_type import DcsCrcOutVariableType
from underautomation.fanuc.common.files.variables.dcs_nocode_variable_type import DcsNocodeVariableType
from underautomation.fanuc.common.files.variables.dcs_sgn_variable_type import DcsSgnVariableType
from underautomation.fanuc.common.files.variables.deflogic_variable_type import DeflogicVariableType
from underautomation.fanuc.common.files.variables.demo_init_variable_type import DemoInitVariableType
from underautomation.fanuc.common.files.variables.diag_grp_variable_type import DiagGrpVariableType
from underautomation.fanuc.common.files.variables.dict_cfg_variable_type import DictCfgVariableType
from underautomation.fanuc.common.files.variables.dmsw_cfg_variable_type import DmswCfgVariableType
from underautomation.fanuc.common.files.variables.docviewer_variable_type import DocviewerVariableType
from underautomation.fanuc.common.files.variables.drc_cfg_variable_type import DrcCfgVariableType
from underautomation.fanuc.common.files.variables.dsbl_fault_variable_type import DsblFaultVariableType
from underautomation.fanuc.common.files.variables.dtrec_variable_type import DtrecVariableType
from underautomation.fanuc.common.files.variables.dyn_brk_variable_type import DynBrkVariableType
from underautomation.fanuc.common.files.variables.edt_recent_variable_type import EdtRecentVariableType
from underautomation.fanuc.common.files.variables.enc_info_variable_type import EncInfoVariableType
from underautomation.fanuc.common.files.variables.enetmode_variable_type import EnetmodeVariableType
from underautomation.fanuc.common.files.variables.eoatcfg_variable_type import EoatcfgVariableType
from underautomation.fanuc.common.files.variables.eoatdata_variable_type import EoatdataVariableType
from underautomation.fanuc.common.files.variables.erpost_log_variable_type import ErpostLogVariableType
from underautomation.fanuc.common.files.variables.er_noauto_variable_type import ErNoautoVariableType
from underautomation.fanuc.common.files.variables.er_noalm_variable_type import ErNoalmVariableType
from underautomation.fanuc.common.files.variables.ext_set_variable_type import ExtSetVariableType
from underautomation.fanuc.common.files.variables.fdr_grp_variable_type import FdrGrpVariableType
from underautomation.fanuc.common.files.variables.feature_variable_type import FeatureVariableType
from underautomation.fanuc.common.files.variables.filecomp_variable_type import FilecompVariableType
from underautomation.fanuc.common.files.variables.file_setup2_variable_type import FileSetup2VariableType
from underautomation.fanuc.common.files.variables.file_back_variable_type import FileBackVariableType
from underautomation.fanuc.common.files.variables.flui_cfg_variable_type import FluiCfgVariableType
from underautomation.fanuc.common.files.variables.flui_data_variable_type import FluiDataVariableType
from underautomation.fanuc.common.files.variables.flui_res_variable_type import FluiResVariableType
from underautomation.fanuc.common.files.variables.fmr_cfg_variable_type import FmrCfgVariableType
from underautomation.fanuc.common.files.variables.fssb_cfg_variable_type import FssbCfgVariableType
from underautomation.fanuc.common.files.variables.gravc_grp_variable_type import GravcGrpVariableType
from underautomation.fanuc.common.files.variables.grsmt_grp_variable_type import GrsmtGrpVariableType
from underautomation.fanuc.common.files.variables.host_cfg_variable_type import HostCfgVariableType
from underautomation.fanuc.common.files.variables.hostent_variable_type import HostentVariableType
from underautomation.fanuc.common.files.variables.err_mask_variable_type import ErrMaskVariableType
from underautomation.fanuc.common.files.variables.hscd_mng_variable_type import HscdMngVariableType
from underautomation.fanuc.common.files.variables.http_auth_variable_type import HttpAuthVariableType
from underautomation.fanuc.common.files.variables.http_variable_type import HttpVariableType
from underautomation.fanuc.common.files.variables.hwr_config_variable_type import HwrConfigVariableType
from underautomation.fanuc.common.files.variables.iolnk_variable_type import IolnkVariableType
from underautomation.fanuc.common.files.variables.ioslave_variable_type import IoslaveVariableType
from underautomation.fanuc.common.files.variables.io_def_asg_variable_type import IoDefAsgVariableType
from underautomation.fanuc.common.files.variables.io_uop_cfg_variable_type import IoUopCfgVariableType
from underautomation.fanuc.common.files.variables.item_acc_variable_type import ItemAccVariableType
from underautomation.fanuc.common.files.variables.item_buff_el_variable_type import ItemBuffElVariableType
from underautomation.fanuc.common.files.variables.irca_cnf_variable_type import IrcaCnfVariableType
from underautomation.fanuc.common.files.variables.hist_day_variable_type import HistDayVariableType
from underautomation.fanuc.common.files.variables.item_name_variable_type import ItemNameVariableType
from underautomation.fanuc.common.files.variables.irprog_cfg_variable_type import IrprogCfgVariableType
from underautomation.fanuc.common.files.variables.jinc_variable_type import JincVariableType
from underautomation.fanuc.common.files.variables.karelmon_variable_type import KarelmonVariableType
from underautomation.fanuc.common.files.variables.karel_cfg_variable_type import KarelCfgVariableType
from underautomation.fanuc.common.files.variables.lgcfg_variable_type import LgcfgVariableType
from underautomation.fanuc.common.files.variables.ln_disp_variable_type import LnDispVariableType
from underautomation.fanuc.common.files.variables.logbook_variable_type import LogbookVariableType
from underautomation.fanuc.common.files.variables.log_buff_variable_type import LogBuffVariableType
from underautomation.fanuc.common.files.variables.log_dcs_variable_type import LogDcsVariableType
from underautomation.fanuc.common.files.variables.log_dio_variable_type import LogDioVariableType
from underautomation.fanuc.common.files.variables.log_scrn_fl_variable_type import LogScrnFlVariableType
from underautomation.fanuc.common.files.variables.mcsp_variable_type import McspVariableType
from underautomation.fanuc.common.files.variables.mcsp_grp_variable_type import McspGrpVariableType
from underautomation.fanuc.common.files.variables.mfrq_cfg_variable_type import MfrqCfgVariableType
from underautomation.fanuc.common.files.variables.mfrq_grp_variable_type import MfrqGrpVariableType
from underautomation.fanuc.common.files.variables.misc_mstr_variable_type import MiscMstrVariableType
from underautomation.fanuc.common.files.variables.misc_scd_variable_type import MiscScdVariableType
from underautomation.fanuc.common.files.variables.mkcfg_variable_type import MkcfgVariableType
from underautomation.fanuc.common.files.variables.mltarm_cfg_variable_type import MltarmCfgVariableType
from underautomation.fanuc.common.files.variables.mndsp_mst_variable_type import MndspMstVariableType
from underautomation.fanuc.common.files.variables.mndsppstl_variable_type import MndsppstlVariableType
from underautomation.fanuc.common.files.variables.modaq_cfg_variable_type import ModaqCfgVariableType
from underautomation.fanuc.common.files.variables.fx_trigger_variable_type import FxTriggerVariableType
from underautomation.fanuc.common.files.variables.modem_inf_variable_type import ModemInfVariableType
from underautomation.fanuc.common.files.variables.mor_grp_sv_variable_type import MorGrpSvVariableType
from underautomation.fanuc.common.files.variables.motion_dbg_variable_type import MotionDbgVariableType
from underautomation.fanuc.common.files.variables.mr_hist_variable_type import MrHistVariableType
from underautomation.fanuc.common.files.variables.msk_ce_grp_variable_type import MskCeGrpVariableType
from underautomation.fanuc.common.files.variables.mtcom_cfg_variable_type import MtcomCfgVariableType
from underautomation.fanuc.common.files.variables.opwork_variable_type import OpworkVariableType
from underautomation.fanuc.common.files.variables.ovrdslct_variable_type import OvrdslctVariableType
from underautomation.fanuc.common.files.variables.ovrd_setup_variable_type import OvrdSetupVariableType
from underautomation.fanuc.common.files.variables.plcfg_variable_type import PlcfgVariableType
from underautomation.fanuc.common.files.variables.tracectl_variable_type import TracectlVariableType
from underautomation.fanuc.common.files.variables.tracedt_variable_type import TracedtVariableType
from underautomation.fanuc.common.files.variables.traceup_variable_type import TraceupVariableType
from underautomation.fanuc.common.files.variables.pg_cfg_variable_type import PgCfgVariableType
from underautomation.fanuc.common.files.variables.pg_defspd_variable_type import PgDefspdVariableType
from underautomation.fanuc.common.files.variables.ping_variable_type import PingVariableType
from underautomation.fanuc.common.files.variables.pipe_cfg_variable_type import PipeCfgVariableType
from underautomation.fanuc.common.files.variables.plid_cfg_variable_type import PlidCfgVariableType
from underautomation.fanuc.common.files.variables.plid_cllb_variable_type import PlidCllbVariableType
from underautomation.fanuc.common.files.variables.plim_grp_variable_type import PlimGrpVariableType
from underautomation.fanuc.common.files.variables.plmr_grp_variable_type import PlmrGrpVariableType
from underautomation.fanuc.common.files.variables.plst_grp_variable_type import PlstGrpVariableType
from underautomation.fanuc.common.files.variables.pl_res_g_variable_type import PlResGVariableType
from underautomation.fanuc.common.files.variables.pmon_que_variable_type import PmonQueVariableType
from underautomation.fanuc.common.files.variables.pocfg_variable_type import PocfgVariableType
from underautomation.fanuc.common.files.variables.pos_edit_variable_type import PosEditVariableType
from underautomation.fanuc.common.files.variables.prgadj_variable_type import PrgadjVariableType
from underautomation.fanuc.common.files.variables.prgns_cfg_variable_type import PrgnsCfgVariableType
from underautomation.fanuc.common.files.variables.prgns_grp_variable_type import PrgnsGrpVariableType
from underautomation.fanuc.common.files.variables.prgns_pref_variable_type import PrgnsPrefVariableType
from underautomation.fanuc.common.files.variables.protoent_variable_type import ProtoentVariableType
from underautomation.fanuc.common.files.variables.proxy_cfg_variable_type import ProxyCfgVariableType
from underautomation.fanuc.common.files.variables.pf_cfg_variable_type import PfCfgVariableType
from underautomation.fanuc.common.files.variables.pf_enhance_variable_type import PfEnhanceVariableType
from underautomation.fanuc.common.files.variables.pf_pref_variable_type import PfPrefVariableType
from underautomation.fanuc.common.files.variables.pslgset_variable_type import PslgsetVariableType
from underautomation.fanuc.common.files.variables.pslgtemp_variable_type import PslgtempVariableType
from underautomation.fanuc.common.files.variables.pssave_variable_type import PssaveVariableType
from underautomation.fanuc.common.files.variables.pwrup_dly_variable_type import PwrupDlyVariableType
from underautomation.fanuc.common.files.variables.qskip_grp_variable_type import QskipGrpVariableType
from underautomation.fanuc.common.files.variables.rdcr_grp_variable_type import RdcrGrpVariableType
from underautomation.fanuc.common.files.variables.redprot_cfg_variable_type import RedprotCfgVariableType
from underautomation.fanuc.common.files.variables.redprot_grp_variable_type import RedprotGrpVariableType
from underautomation.fanuc.common.files.variables.refpos11_variable_type import Refpos11VariableType
from underautomation.fanuc.common.files.variables.refpos21_variable_type import Refpos21VariableType
from underautomation.fanuc.common.files.variables.refpos31_variable_type import Refpos31VariableType
from underautomation.fanuc.common.files.variables.refpos41_variable_type import Refpos41VariableType
from underautomation.fanuc.common.files.variables.refpos51_variable_type import Refpos51VariableType
from underautomation.fanuc.common.files.variables.refpos61_variable_type import Refpos61VariableType
from underautomation.fanuc.common.files.variables.refpos71_variable_type import Refpos71VariableType
from underautomation.fanuc.common.files.variables.refpos81_variable_type import Refpos81VariableType
from underautomation.fanuc.common.files.variables.refpsmsk_variable_type import RefpsmskVariableType
from underautomation.fanuc.common.files.variables.remote_cfg_variable_type import RemoteCfgVariableType
from underautomation.fanuc.common.files.variables.repower_variable_type import RepowerVariableType
from underautomation.fanuc.common.files.variables.restart_variable_type import RestartVariableType
from underautomation.fanuc.common.files.variables.rs232_cfg_variable_type import Rs232CfgVariableType
from underautomation.fanuc.common.files.variables.rsch_variable_type import RschVariableType
from underautomation.fanuc.common.files.variables.rspace_variable_type import RspaceVariableType
from underautomation.fanuc.common.files.variables.rspaceg_variable_type import RspacegVariableType
from underautomation.fanuc.common.files.variables.rspacesr_variable_type import RspacesrVariableType
from underautomation.fanuc.common.files.variables.servent_variable_type import ServentVariableType
from underautomation.fanuc.common.files.variables.sfzn_cfg_variable_type import SfznCfgVariableType
from underautomation.fanuc.common.files.variables.sfzn_grp_variable_type import SfznGrpVariableType
from underautomation.fanuc.common.files.variables.shell_cfg_variable_type import ShellCfgVariableType
from underautomation.fanuc.common.files.variables.shell_chk_variable_type import ShellChkVariableType
from underautomation.fanuc.common.files.variables.shell_comm_variable_type import ShellCommVariableType
from underautomation.fanuc.common.files.variables.simiofwdlm_variable_type import SimiofwdlmVariableType
from underautomation.fanuc.common.files.variables.snpx_asg_variable_type import SnpxAsgVariableType
from underautomation.fanuc.common.files.variables.snpx_param_variable_type import SnpxParamVariableType
from underautomation.fanuc.common.files.variables.ssr_variable_type import SsrVariableType
from underautomation.fanuc.common.files.variables.svdt_grp_variable_type import SvdtGrpVariableType
from underautomation.fanuc.common.files.variables.svprm_upd_variable_type import SvprmUpdVariableType
from underautomation.fanuc.common.files.variables.sv_info_variable_type import SvInfoVariableType
from underautomation.fanuc.common.files.variables.syslog_variable_type import SyslogVariableType
from underautomation.fanuc.common.files.variables.syslog_sav_variable_type import SyslogSavVariableType
from underautomation.fanuc.common.files.variables.system_timer_variable_type import SystemTimerVariableType
from underautomation.fanuc.common.files.variables.t2mode_lim_variable_type import T2modeLimVariableType
from underautomation.fanuc.common.files.variables.t2spdlim_variable_type import T2spdlimVariableType
from underautomation.fanuc.common.files.variables.tbc2_grp_variable_type import Tbc2GrpVariableType
from underautomation.fanuc.common.files.variables.tbcsg_grp_variable_type import TbcsgGrpVariableType
from underautomation.fanuc.common.files.variables.tbj2_grp_variable_type import Tbj2GrpVariableType
from underautomation.fanuc.common.files.variables.tbjop_grp_variable_type import TbjopGrpVariableType
from underautomation.fanuc.common.files.variables.tp_thr_table_variable_type import TpThrTableVariableType
from underautomation.fanuc.common.files.variables.thr_cfg_variable_type import ThrCfgVariableType
from underautomation.fanuc.common.files.variables.timer_variable_type import TimerVariableType
from underautomation.fanuc.common.files.variables.tpgl_conf_variable_type import TpglConfVariableType
from underautomation.fanuc.common.files.variables.tpgl_out_variable_type import TpglOutVariableType
from underautomation.fanuc.common.files.variables.tpp_mon_variable_type import TppMonVariableType
from underautomation.fanuc.common.files.variables.tpstrtchk_variable_type import TpstrtchkVariableType
from underautomation.fanuc.common.files.variables.tpvwvar_variable_type import TpvwvarVariableType
from underautomation.fanuc.common.files.variables.trace_cfg_variable_type import TraceCfgVariableType
from underautomation.fanuc.common.files.variables.trace_chnl_variable_type import TraceChnlVariableType
from underautomation.fanuc.common.files.variables.trace_item_variable_type import TraceItemVariableType
from underautomation.fanuc.common.files.variables.tscfg_variable_type import TscfgVariableType
from underautomation.fanuc.common.files.variables.tsscb_variable_type import TsscbVariableType
from underautomation.fanuc.common.files.variables.tutorial_variable_type import TutorialVariableType
from underautomation.fanuc.common.files.variables.tv_config_variable_type import TvConfigVariableType
from underautomation.fanuc.common.files.variables.tv_output_variable_type import TvOutputVariableType
from underautomation.fanuc.common.files.variables.txscreen_variable_type import TxscreenVariableType
from underautomation.fanuc.common.files.variables.uecfg_variable_type import UecfgVariableType
from underautomation.fanuc.common.files.variables.uegrp_variable_type import UegrpVariableType
from underautomation.fanuc.common.files.variables.bbl_nt_wnd_variable_type import BblNtWndVariableType
from underautomation.fanuc.common.files.variables.ui_fkeydat_variable_type import UiFkeydatVariableType
from underautomation.fanuc.common.files.variables.ui_menhis_variable_type import UiMenhisVariableType
from underautomation.fanuc.common.files.variables.ui_panedat_variable_type import UiPanedatVariableType
from underautomation.fanuc.common.files.variables.ui_usrview_variable_type import UiUsrviewVariableType
from underautomation.fanuc.common.files.variables.undo_cfg_variable_type import UndoCfgVariableType
from underautomation.fanuc.common.files.variables.user_info_variable_type import UserInfoVariableType
from underautomation.fanuc.common.files.variables.user_offst_variable_type import UserOffstVariableType
from underautomation.fanuc.common.files.variables.user_work_variable_type import UserWorkVariableType
from underautomation.fanuc.common.files.variables.usrtol_grp_variable_type import UsrtolGrpVariableType
from underautomation.fanuc.common.files.variables.usr_ev_cfg_variable_type import UsrEvCfgVariableType
from underautomation.fanuc.common.files.variables.usr_ev_wrk_variable_type import UsrEvWrkVariableType
from underautomation.fanuc.common.files.variables.vars_config_variable_type import VarsConfigVariableType
from underautomation.fanuc.common.files.variables.vcmr_grp_variable_type import VcmrGrpVariableType
from underautomation.fanuc.common.files.variables.via_work_variable_type import ViaWorkVariableType
from underautomation.fanuc.common.files.variables.vision_cfg_variable_type import VisionCfgVariableType
from underautomation.fanuc.common.files.variables.vision_grp_variable_type import VisionGrpVariableType
from underautomation.fanuc.common.files.variables.vis_ge_cfg_variable_type import VisGeCfgVariableType
from underautomation.fanuc.common.files.variables.vis_logreg_variable_type import VisLogregVariableType
from underautomation.fanuc.common.files.variables.vlexe_cfg_variable_type import VlexeCfgVariableType
from underautomation.fanuc.common.files.variables.vrtd_filt_variable_type import VrtdFiltVariableType
from underautomation.fanuc.common.files.variables.vsft_cfg_variable_type import VsftCfgVariableType
from underautomation.fanuc.common.files.variables.vsmo_cfg_variable_type import VsmoCfgVariableType
from underautomation.fanuc.common.files.variables.vzdt_cfg_variable_type import VzdtCfgVariableType
from underautomation.fanuc.common.files.variables.wait_data_variable_type import WaitDataVariableType
from underautomation.fanuc.common.files.variables.xvrcfg_variable_type import XvrcfgVariableType
from underautomation.fanuc.common.files.variables.zabc_grp_variable_type import ZabcGrpVariableType
from underautomation.fanuc.common.files.variables.zdt_actvspt_variable_type import ZdtActvsptVariableType
from underautomation.fanuc.common.files.variables.zdt_dcschg_variable_type import ZdtDcschgVariableType
from underautomation.fanuc.common.files.variables.zip_cfg_variable_type import ZipCfgVariableType
from underautomation.fanuc.common.files.variables.zmpcf_grp_variable_type import ZmpcfGrpVariableType
from underautomation.fanuc.common.files.variables.zmpos_grp_variable_type import ZmposGrpVariableType
from underautomation.fanuc.common.files.variables.zp_cfg_variable_type import ZpCfgVariableType
from underautomation.fanuc.common.files.variables.zp_cylinder_variable_type import ZpCylinderVariableType
from underautomation.fanuc.common.files.variables.zp_grp_variable_type import ZpGrpVariableType
from underautomation.fanuc.common.files.variables.zp_sphere_variable_type import ZpSphereVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SystemFile as system_file

class SystemFile(GenericVariableFile):
	'''Describes the Fanuc variable file system.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = system_file()
		else:
			self._instance = _internal

	@property
	def aavm_wrk(self) -> typing.List[AavmWrkVariableType]:
		'''Value of variable $AAVM_WRK'''
		__r = self._instance.AavmWrk
		return None if __r is None else [None if x is None else AavmWrkVariableType(x) for x in __r]

	@property
	def abspos_grp(self) -> typing.List[AbsposGrpVariableType]:
		'''Value of variable $ABSPOS_GRP'''
		__r = self._instance.AbsposGrp
		return None if __r is None else [None if x is None else AbsposGrpVariableType(x) for x in __r]

	@property
	def acc_maxlmt(self) -> int:
		'''Value of variable $ACC_MAXLMT'''
		return self._instance.AccMaxlmt

	@property
	def acc_minlmt(self) -> int:
		'''Value of variable $ACC_MINLMT'''
		return self._instance.AccMinlmt

	@property
	def acc_pre_exe(self) -> int:
		'''Value of variable $ACC_PRE_EXE'''
		return self._instance.AccPreExe

	@property
	def ac_update(self) -> int:
		'''Value of variable $AC_UPDATE'''
		return self._instance.AcUpdate

	@property
	def aiocnv_num(self) -> int:
		'''Value of variable $AIOCNV_NUM'''
		return self._instance.AiocnvNum

	@property
	def aiocnv_use(self) -> int:
		'''Value of variable $AIOCNV_USE'''
		return self._instance.AiocnvUse

	@property
	def aio_cnv(self) -> typing.List[AioCnvVariableType]:
		'''Value of variable $AIO_CNV'''
		__r = self._instance.AioCnv
		return None if __r is None else [None if x is None else AioCnvVariableType(x) for x in __r]

	@property
	def almdg(self) -> AlmdgVariableType:
		'''Value of variable $ALMDG'''
		__r = self._instance.Almdg
		return None if __r is None else AlmdgVariableType(__r)

	@property
	def alm_if(self) -> AlmIfVariableType:
		'''Value of variable $ALM_IF'''
		__r = self._instance.AlmIf
		return None if __r is None else AlmIfVariableType(__r)

	@property
	def angtol(self) -> typing.List[float]:
		'''Value of variable $ANGTOL'''
		return self._instance.Angtol

	@property
	def appinfo(self) -> AppinfoVariableType:
		'''Value of variable $APPINFO'''
		__r = self._instance.Appinfo
		return None if __r is None else AppinfoVariableType(__r)

	@property
	def application(self) -> typing.List[str]:
		'''Value of variable $APPLICATION'''
		return self._instance.Application

	@property
	def ap_active(self) -> int:
		'''Value of variable $AP_ACTIVE'''
		return self._instance.ApActive

	@property
	def ap_automode(self) -> bool:
		'''Value of variable $AP_AUTOMODE'''
		return self._instance.ApAutomode

	@property
	def ap_chgaponl(self) -> bool:
		'''Value of variable $AP_CHGAPONL'''
		return self._instance.ApChgaponl

	@property
	def ap_coupled(self) -> typing.List[ApcoupledVariableType]:
		'''Value of variable $AP_COUPLED'''
		__r = self._instance.ApCoupled
		return None if __r is None else [None if x is None else ApcoupledVariableType(x) for x in __r]

	@property
	def ap_cureq(self) -> typing.List[ApcureqVariableType]:
		'''Value of variable $AP_CUREQ'''
		__r = self._instance.ApCureq
		return None if __r is None else [None if x is None else ApcureqVariableType(x) for x in __r]

	@property
	def ap_curtool(self) -> int:
		'''Value of variable $AP_CURTOOL'''
		return self._instance.ApCurtool

	@property
	def ap_do_clean(self) -> bool:
		'''Value of variable $AP_DO_CLEAN'''
		return self._instance.ApDoClean

	@property
	def ap_do_clenm(self) -> typing.List[bool]:
		'''Value of variable $AP_DO_CLENM'''
		return self._instance.ApDoClenm

	@property
	def ap_dspdryrn(self) -> bool:
		'''Value of variable $AP_DSPDRYRN'''
		return self._instance.ApDspdryrn

	@property
	def ap_hide(self) -> typing.List[bool]:
		'''Value of variable $AP_HIDE'''
		return self._instance.ApHide

	@property
	def ap_maxapp(self) -> int:
		'''Value of variable $AP_MAXAPP'''
		return self._instance.ApMaxapp

	@property
	def ap_maxax(self) -> int:
		'''Value of variable $AP_MAXAX'''
		return self._instance.ApMaxax

	@property
	def ap_plugged(self) -> int:
		'''Value of variable $AP_PLUGGED'''
		return self._instance.ApPlugged

	@property
	def ap_prc_dsbm(self) -> typing.List[int]:
		'''Value of variable $AP_PRC_DSBM'''
		return self._instance.ApPrcDsbm

	@property
	def ap_proc_dsb(self) -> bool:
		'''Value of variable $AP_PROC_DSB'''
		return self._instance.ApProcDsb

	@property
	def ap_segf_chk(self) -> bool:
		'''Value of variable $AP_SEGF_CHK'''
		return self._instance.ApSegfChk

	@property
	def ap_seg_chkm(self) -> typing.List[bool]:
		'''Value of variable $AP_SEG_CHKM'''
		return self._instance.ApSegChkm

	@property
	def ap_selap(self) -> typing.List[bool]:
		'''Value of variable $AP_SELAP'''
		return self._instance.ApSelap

	@property
	def ap_totalax(self) -> int:
		'''Value of variable $AP_TOTALAX'''
		return self._instance.ApTotalax

	@property
	def ap_usenum(self) -> typing.List[int]:
		'''Value of variable $AP_USENUM'''
		return self._instance.ApUsenum

	@property
	def argdispmmck(self) -> float:
		'''Value of variable $ARGDISPMMCK'''
		return self._instance.Argdispmmck

	@property
	def argdispmode(self) -> int:
		'''Value of variable $ARGDISPMODE'''
		return self._instance.Argdispmode

	@property
	def arg_string(self) -> typing.List[ArgStrVariableType]:
		'''Value of variable $ARG_STRING'''
		__r = self._instance.ArgString
		return None if __r is None else [None if x is None else ArgStrVariableType(x) for x in __r]

	@property
	def arg_word(self) -> typing.List[str]:
		'''Value of variable $ARG_WORD'''
		return self._instance.ArgWord

	@property
	def asbn_config(self) -> AsbnCfgVariableType:
		'''Value of variable $ASBN_CONFIG'''
		__r = self._instance.AsbnConfig
		return None if __r is None else AsbnCfgVariableType(__r)

	@property
	def atcellsetup(self) -> AtCellsetupVariableType:
		'''Value of variable $ATCELLSETUP'''
		__r = self._instance.Atcellsetup
		return None if __r is None else AtCellsetupVariableType(__r)

	@property
	def autobackup(self) -> AutobackupVariableType:
		'''Value of variable $AUTOBACKUP'''
		__r = self._instance.Autobackup
		return None if __r is None else AutobackupVariableType(__r)

	@property
	def autoinit(self) -> int:
		'''Value of variable $AUTOINIT'''
		return self._instance.Autoinit

	@property
	def automessage(self) -> int:
		'''Value of variable $AUTOMESSAGE'''
		return self._instance.Automessage

	@property
	def automode_do(self) -> bool:
		'''Value of variable $AUTOMODE_DO'''
		return self._instance.AutomodeDo

	@property
	def automode_ov(self) -> bool:
		'''Value of variable $AUTOMODE_OV'''
		return self._instance.AutomodeOv

	@property
	def autopauspos(self) -> typing.List[JointPositionVariable]:
		'''Value of variable $AUTOPAUSPOS'''
		__r = self._instance.Autopauspos
		return None if __r is None else [None if x is None else JointPositionVariable(None, None, x) for x in __r]

	@property
	def autoppostsk(self) -> typing.List[int]:
		'''Value of variable $AUTOPPOSTSK'''
		return self._instance.Autoppostsk

	@property
	def autoupdtmod(self) -> int:
		'''Value of variable $AUTOUPDTMOD'''
		return self._instance.Autoupdtmod

	@property
	def auxwzd_enb(self) -> int:
		'''Value of variable $AUXWZD_ENB'''
		return self._instance.AuxwzdEnb

	@property
	def auxwzd_stat(self) -> int:
		'''Value of variable $AUXWZD_STAT'''
		return self._instance.AuxwzdStat

	@property
	def axscrdcfg(self) -> typing.List[AxscrdcfgVariableType]:
		'''Value of variable $AXSCRDCFG'''
		__r = self._instance.Axscrdcfg
		return None if __r is None else [None if x is None else AxscrdcfgVariableType(x) for x in __r]

	@property
	def background(self) -> bool:
		'''Value of variable $BACKGROUND'''
		return self._instance.Background

	@property
	def backup_name(self) -> str:
		'''Value of variable $BACKUP_NAME'''
		return self._instance.BackupName

	@property
	def back_edit(self) -> typing.List[BackEditVariableType]:
		'''Value of variable $BACK_EDIT'''
		__r = self._instance.BackEdit
		return None if __r is None else [None if x is None else BackEditVariableType(x) for x in __r]

	@property
	def bck_no_del(self) -> bool:
		'''Value of variable $BCK_NO_DEL'''
		return self._instance.BckNoDel

	@property
	def bge_unusend(self) -> bool:
		'''Value of variable $BGE_UNUSEND'''
		return self._instance.BgeUnusend

	@property
	def bigallow(self) -> typing.List[BigallowVariableType]:
		'''Value of variable $BIGALLOW'''
		__r = self._instance.Bigallow
		return None if __r is None else [None if x is None else BigallowVariableType(x) for x in __r]

	@property
	def blal_out(self) -> BlalOutVariableType:
		'''Value of variable $BLAL_OUT'''
		__r = self._instance.BlalOut
		return None if __r is None else BlalOutVariableType(__r)

	@property
	def bwd_abort(self) -> bool:
		'''Value of variable $BWD_ABORT'''
		return self._instance.BwdAbort

	@property
	def bwd_itr_rtn(self) -> int:
		'''Value of variable $BWD_ITR_RTN'''
		return self._instance.BwdItrRtn

	@property
	def bwd_nonstop(self) -> int:
		'''Value of variable $BWD_NONSTOP'''
		return self._instance.BwdNonstop

	@property
	def ce_option(self) -> int:
		'''Value of variable $CE_OPTION'''
		return self._instance.CeOption

	@property
	def ce_ria_id(self) -> int:
		'''Value of variable $CE_RIA_ID'''
		return self._instance.CeRiaId

	@property
	def cfcfg(self) -> CfcfgVariableType:
		'''Value of variable $CFCFG'''
		__r = self._instance.Cfcfg
		return None if __r is None else CfcfgVariableType(__r)

	@property
	def checkconfig(self) -> bool:
		'''Value of variable $CHECKCONFIG'''
		return self._instance.Checkconfig

	@property
	def chg_pri(self) -> typing.List[ChgPriVariableType]:
		'''Value of variable $CHG_PRI'''
		__r = self._instance.ChgPri
		return None if __r is None else [None if x is None else ChgPriVariableType(x) for x in __r]

	@property
	def chkpauspos(self) -> typing.List[ChkposVariableType]:
		'''Value of variable $CHKPAUSPOS'''
		__r = self._instance.Chkpauspos
		return None if __r is None else [None if x is None else ChkposVariableType(x) for x in __r]

	@property
	def cmd_info(self) -> typing.List[CmdInfoVariableType]:
		'''Value of variable $CMD_INFO'''
		__r = self._instance.CmdInfo
		return None if __r is None else [None if x is None else CmdInfoVariableType(x) for x in __r]

	@property
	def cocfg(self) -> CocfgVariableType:
		'''Value of variable $COCFG'''
		__r = self._instance.Cocfg
		return None if __r is None else CocfgVariableType(__r)

	@property
	def collect_cfg(self) -> CollectVariableType:
		'''Value of variable $COLLECT_CFG'''
		__r = self._instance.CollectCfg
		return None if __r is None else CollectVariableType(__r)

	@property
	def collect_enb(self) -> int:
		'''Value of variable $COLLECT_ENB'''
		return self._instance.CollectEnb

	@property
	def condet_cfg(self) -> CondetCfgVariableType:
		'''Value of variable $CONDET_CFG'''
		__r = self._instance.CondetCfg
		return None if __r is None else CondetCfgVariableType(__r)

	@property
	def condet_grp(self) -> typing.List[CondetGrpVariableType]:
		'''Value of variable $CONDET_GRP'''
		__r = self._instance.CondetGrp
		return None if __r is None else [None if x is None else CondetGrpVariableType(x) for x in __r]

	@property
	def condet_io(self) -> CondetIoVariableType:
		'''Value of variable $CONDET_IO'''
		__r = self._instance.CondetIo
		return None if __r is None else CondetIoVariableType(__r)

	@property
	def condet_trgp(self) -> typing.List[CondetTrgpVariableType]:
		'''Value of variable $CONDET_TRGP'''
		__r = self._instance.CondetTrgp
		return None if __r is None else [None if x is None else CondetTrgpVariableType(x) for x in __r]

	@property
	def condet_trig(self) -> CondetTrigVariableType:
		'''Value of variable $CONDET_TRIG'''
		__r = self._instance.CondetTrig
		return None if __r is None else CondetTrigVariableType(__r)

	@property
	def co_morgrp(self) -> typing.List[CoMorgrpVariableType]:
		'''Value of variable $CO_MORGRP'''
		__r = self._instance.CoMorgrp
		return None if __r is None else [None if x is None else CoMorgrpVariableType(x) for x in __r]

	@property
	def co_paramgrp(self) -> typing.List[CoParamgpVariableType]:
		'''Value of variable $CO_PARAMGRP'''
		__r = self._instance.CoParamgrp
		return None if __r is None else [None if x is None else CoParamgpVariableType(x) for x in __r]

	@property
	def cpcfg(self) -> CpcfgVariableType:
		'''Value of variable $CPCFG'''
		__r = self._instance.Cpcfg
		return None if __r is None else CpcfgVariableType(__r)

	@property
	def cpdbg(self) -> CpdbgVariableType:
		'''Value of variable $CPDBG'''
		__r = self._instance.Cpdbg
		return None if __r is None else CpdbgVariableType(__r)

	@property
	def cp_mcrgrp(self) -> typing.List[CpMcrgrpVariableType]:
		'''Value of variable $CP_MCRGRP'''
		__r = self._instance.CpMcrgrp
		return None if __r is None else [None if x is None else CpMcrgrpVariableType(x) for x in __r]

	@property
	def cp_morgrp(self) -> typing.List[CpMorgrpVariableType]:
		'''Value of variable $CP_MORGRP'''
		__r = self._instance.CpMorgrp
		return None if __r is None else [None if x is None else CpMorgrpVariableType(x) for x in __r]

	@property
	def cp_paramgrp(self) -> typing.List[CpParamgpVariableType]:
		'''Value of variable $CP_PARAMGRP'''
		__r = self._instance.CpParamgrp
		return None if __r is None else [None if x is None else CpParamgpVariableType(x) for x in __r]

	@property
	def cp_t1_grp(self) -> typing.List[CpT1GrpVariableType]:
		'''Value of variable $CP_T1_GRP'''
		__r = self._instance.CpT1Grp
		return None if __r is None else [None if x is None else CpT1GrpVariableType(x) for x in __r]

	@property
	def cp_t1_mode(self) -> CpT1ModeVariableType:
		'''Value of variable $CP_T1_MODE'''
		__r = self._instance.CpT1Mode
		return None if __r is None else CpT1ModeVariableType(__r)

	@property
	def crt_defprog(self) -> str:
		'''Value of variable $CRT_DEFPROG'''
		return self._instance.CrtDefprog

	@property
	def crt_inuser(self) -> bool:
		'''Value of variable $CRT_INUSER'''
		return self._instance.CrtInuser

	@property
	def crt_key_tbl(self) -> typing.List[int]:
		'''Value of variable $CRT_KEY_TBL'''
		return self._instance.CrtKeyTbl

	@property
	def crt_lckuser(self) -> bool:
		'''Value of variable $CRT_LCKUSER'''
		return self._instance.CrtLckuser

	@property
	def crt_usestat(self) -> bool:
		'''Value of variable $CRT_USESTAT'''
		return self._instance.CrtUsestat

	@property
	def cr_auto_do(self) -> int:
		'''Value of variable $CR_AUTO_DO'''
		return self._instance.CrAutoDo

	@property
	def cr_indt_enb(self) -> bool:
		'''Value of variable $CR_INDT_ENB'''
		return self._instance.CrIndtEnb

	@property
	def cr_t1_do(self) -> int:
		'''Value of variable $CR_T1_DO'''
		return self._instance.CrT1Do

	@property
	def cr_t2_do(self) -> int:
		'''Value of variable $CR_T2_DO'''
		return self._instance.CrT2Do

	@property
	def cstop(self) -> bool:
		'''Value of variable $CSTOP'''
		return self._instance.Cstop

	@property
	def ctrl_delete(self) -> int:
		'''Value of variable $CTRL_DELETE'''
		return self._instance.CtrlDelete

	@property
	def ct_screen(self) -> str:
		'''Value of variable $CT_SCREEN'''
		return self._instance.CtScreen

	@property
	def custommenu(self) -> typing.List[CustommenuVariableType]:
		'''Value of variable $CUSTOMMENU'''
		__r = self._instance.Custommenu
		return None if __r is None else [None if x is None else CustommenuVariableType(x) for x in __r]

	@property
	def cust_manual(self) -> bool:
		'''Value of variable $CUST_MANUAL'''
		return self._instance.CustManual

	@property
	def dbcondtrig(self) -> int:
		'''Value of variable $DBCONDTRIG'''
		return self._instance.Dbcondtrig

	@property
	def dbg_errlog(self) -> DbgErrlogVariableType:
		'''Value of variable $DBG_ERRLOG'''
		__r = self._instance.DbgErrlog
		return None if __r is None else DbgErrlogVariableType(__r)

	@property
	def dbnumlim(self) -> int:
		'''Value of variable $DBNUMLIM'''
		return self._instance.Dbnumlim

	@property
	def dbpxwork(self) -> typing.List[DbpxworkVariableType]:
		'''Value of variable $DBPXWORK'''
		__r = self._instance.Dbpxwork
		return None if __r is None else [None if x is None else DbpxworkVariableType(x) for x in __r]

	@property
	def dbtb_ctrl(self) -> DbtbCtrlVariableType:
		'''Value of variable $DBTB_CTRL'''
		__r = self._instance.DbtbCtrl
		return None if __r is None else DbtbCtrlVariableType(__r)

	@property
	def db_awaytrig(self) -> float:
		'''Value of variable $DB_AWAYTRIG'''
		return self._instance.DbAwaytrig

	@property
	def db_away_alm(self) -> bool:
		'''Value of variable $DB_AWAY_ALM'''
		return self._instance.DbAwayAlm

	@property
	def db_condtyp(self) -> int:
		'''Value of variable $DB_CONDTYP'''
		return self._instance.DbCondtyp

	@property
	def db_dbg(self) -> typing.List[DbDbgVariableType]:
		'''Value of variable $DB_DBG'''
		__r = self._instance.DbDbg
		return None if __r is None else [None if x is None else DbDbgVariableType(x) for x in __r]

	@property
	def db_mindist(self) -> float:
		'''Value of variable $DB_MINDIST'''
		return self._instance.DbMindist

	@property
	def db_montime(self) -> int:
		'''Value of variable $DB_MONTIME'''
		return self._instance.DbMontime

	@property
	def db_montyp(self) -> int:
		'''Value of variable $DB_MONTYP'''
		return self._instance.DbMontyp

	@property
	def db_motnend(self) -> bool:
		'''Value of variable $DB_MOTNEND'''
		return self._instance.DbMotnend

	@property
	def db_record(self) -> typing.List[DbRecordVariableType]:
		'''Value of variable $DB_RECORD'''
		__r = self._instance.DbRecord
		return None if __r is None else [None if x is None else DbRecordVariableType(x) for x in __r]

	@property
	def db_tolerenc(self) -> float:
		'''Value of variable $DB_TOLERENC'''
		return self._instance.DbTolerenc

	@property
	def dcss_cnstcy(self) -> typing.List[DcssCnstcyVariableType]:
		'''Value of variable $DCSS_CNSTCY'''
		__r = self._instance.DcssCnstcy
		return None if __r is None else [None if x is None else DcssCnstcyVariableType(x) for x in __r]

	@property
	def dcss_device(self) -> typing.List[DcssDeviceVariableType]:
		'''Value of variable $DCSS_DEVICE'''
		__r = self._instance.DcssDevice
		return None if __r is None else [None if x is None else DcssDeviceVariableType(x) for x in __r]

	@property
	def dcss_hndgd(self) -> DcssHndgdVariableType:
		'''Value of variable $DCSS_HNDGD'''
		__r = self._instance.DcssHndgd
		return None if __r is None else DcssHndgdVariableType(__r)

	@property
	def dcss_ls(self) -> typing.List[DcssLsVariableType]:
		'''Value of variable $DCSS_LS'''
		__r = self._instance.DcssLs
		return None if __r is None else [None if x is None else DcssLsVariableType(x) for x in __r]

	@property
	def dcss_param(self) -> DcssParamVariableType:
		'''Value of variable $DCSS_PARAM'''
		__r = self._instance.DcssParam
		return None if __r is None else DcssParamVariableType(__r)

	@property
	def dcss_slave(self) -> DcssSlaveVariableType:
		'''Value of variable $DCSS_SLAVE'''
		__r = self._instance.DcssSlave
		return None if __r is None else DcssSlaveVariableType(__r)

	@property
	def dcs_cfg(self) -> DcsCfgVariableType:
		'''Value of variable $DCS_CFG'''
		__r = self._instance.DcsCfg
		return None if __r is None else DcsCfgVariableType(__r)

	@property
	def dcs_crc_out(self) -> DcsCrcOutVariableType:
		'''Value of variable $DCS_CRC_OUT'''
		__r = self._instance.DcsCrcOut
		return None if __r is None else DcsCrcOutVariableType(__r)

	@property
	def dcs_nocode(self) -> DcsNocodeVariableType:
		'''Value of variable $DCS_NOCODE'''
		__r = self._instance.DcsNocode
		return None if __r is None else DcsNocodeVariableType(__r)

	@property
	def dcs_sgn(self) -> DcsSgnVariableType:
		'''Value of variable $DCS_SGN'''
		__r = self._instance.DcsSgn
		return None if __r is None else DcsSgnVariableType(__r)

	@property
	def dcs_version(self) -> str:
		'''Value of variable $DCS_VERSION'''
		return self._instance.DcsVersion

	@property
	def deflogic(self) -> typing.List[DeflogicVariableType]:
		'''Value of variable $DEFLOGIC'''
		__r = self._instance.Deflogic
		return None if __r is None else [None if x is None else DeflogicVariableType(x) for x in __r]

	@property
	def defprog_enb(self) -> bool:
		'''Value of variable $DEFPROG_ENB'''
		return self._instance.DefprogEnb

	@property
	def defpulse(self) -> int:
		'''Value of variable $DEFPULSE'''
		return self._instance.Defpulse

	@property
	def def_acclim(self) -> int:
		'''Value of variable $DEF_ACCLIM'''
		return self._instance.DefAcclim

	@property
	def def_wrstjnt(self) -> int:
		'''Value of variable $DEF_WRSTJNT'''
		return self._instance.DefWrstjnt

	@property
	def demo_init(self) -> DemoInitVariableType:
		'''Value of variable $DEMO_INIT'''
		__r = self._instance.DemoInit
		return None if __r is None else DemoInitVariableType(__r)

	@property
	def dev_index(self) -> int:
		'''Value of variable $DEV_INDEX'''
		return self._instance.DevIndex

	@property
	def dev_path(self) -> str:
		'''Value of variable $DEV_PATH'''
		return self._instance.DevPath

	@property
	def dhcp_clntid(self) -> typing.List[str]:
		'''Value of variable $DHCP_CLNTID'''
		return self._instance.DhcpClntid

	@property
	def diag_grp(self) -> typing.List[DiagGrpVariableType]:
		'''Value of variable $DIAG_GRP'''
		__r = self._instance.DiagGrp
		return None if __r is None else [None if x is None else DiagGrpVariableType(x) for x in __r]

	@property
	def dict_config(self) -> DictCfgVariableType:
		'''Value of variable $DICT_CONFIG'''
		__r = self._instance.DictConfig
		return None if __r is None else DictCfgVariableType(__r)

	@property
	def distbf_tts(self) -> int:
		'''Value of variable $DISTBF_TTS'''
		return self._instance.DistbfTts

	@property
	def distbf_ver(self) -> int:
		'''Value of variable $DISTBF_VER'''
		return self._instance.DistbfVer

	@property
	def dmaurst(self) -> bool:
		'''Value of variable $DMAURST'''
		return self._instance.Dmaurst

	@property
	def dmsw_cfg(self) -> DmswCfgVariableType:
		'''Value of variable $DMSW_CFG'''
		__r = self._instance.DmswCfg
		return None if __r is None else DmswCfgVariableType(__r)

	@property
	def docviewer(self) -> DocviewerVariableType:
		'''Value of variable $DOCVIEWER'''
		__r = self._instance.Docviewer
		return None if __r is None else DocviewerVariableType(__r)

	@property
	def drc_cfg(self) -> DrcCfgVariableType:
		'''Value of variable $DRC_CFG'''
		__r = self._instance.DrcCfg
		return None if __r is None else DrcCfgVariableType(__r)

	@property
	def dsbl_fault(self) -> DsblFaultVariableType:
		'''Value of variable $DSBL_FAULT'''
		__r = self._instance.DsblFault
		return None if __r is None else DsblFaultVariableType(__r)

	@property
	def dsbl_gpmsk(self) -> int:
		'''Value of variable $DSBL_GPMSK'''
		return self._instance.DsblGpmsk

	@property
	def dtdiag(self) -> DtrecVariableType:
		'''Value of variable $DTDIAG'''
		__r = self._instance.Dtdiag
		return None if __r is None else DtrecVariableType(__r)

	@property
	def dtrecp(self) -> DtrecVariableType:
		'''Value of variable $DTRECP'''
		__r = self._instance.Dtrecp
		return None if __r is None else DtrecVariableType(__r)

	@property
	def dump_option(self) -> int:
		'''Value of variable $DUMP_OPTION'''
		return self._instance.DumpOption

	@property
	def dutr_cfg(self) -> int:
		'''Value of variable $DUTR_CFG'''
		return self._instance.DutrCfg

	@property
	def dutr_cpmes(self) -> int:
		'''Value of variable $DUTR_CPMES'''
		return self._instance.DutrCpmes

	@property
	def duty_temp(self) -> float:
		'''Value of variable $DUTY_TEMP'''
		return self._instance.DutyTemp

	@property
	def duty_unit(self) -> int:
		'''Value of variable $DUTY_UNIT'''
		return self._instance.DutyUnit

	@property
	def dyn_brk(self) -> DynBrkVariableType:
		'''Value of variable $DYN_BRK'''
		__r = self._instance.DynBrk
		return None if __r is None else DynBrkVariableType(__r)

	@property
	def editor_optn(self) -> int:
		'''Value of variable $EDITOR_OPTN'''
		return self._instance.EditorOptn

	@property
	def edit_recent(self) -> typing.List[EdtRecentVariableType]:
		'''Value of variable $EDIT_RECENT'''
		__r = self._instance.EditRecent
		return None if __r is None else [None if x is None else EdtRecentVariableType(x) for x in __r]

	@property
	def emgdi_stat(self) -> int:
		'''Value of variable $EMGDI_STAT'''
		return self._instance.EmgdiStat

	@property
	def enc_info(self) -> typing.List[EncInfoVariableType]:
		'''Value of variable $ENC_INFO'''
		__r = self._instance.EncInfo
		return None if __r is None else [None if x is None else EncInfoVariableType(x) for x in __r]

	@property
	def enetmode(self) -> typing.List[EnetmodeVariableType]:
		'''Value of variable $ENETMODE'''
		__r = self._instance.Enetmode
		return None if __r is None else [None if x is None else EnetmodeVariableType(x) for x in __r]

	@property
	def eoatcfg(self) -> EoatcfgVariableType:
		'''Value of variable $EOATCFG'''
		__r = self._instance.Eoatcfg
		return None if __r is None else EoatcfgVariableType(__r)

	@property
	def eoatdata(self) -> typing.List[EoatdataVariableType]:
		'''Value of variable $EOATDATA'''
		__r = self._instance.Eoatdata
		return None if __r is None else [None if x is None else EoatdataVariableType(x) for x in __r]

	@property
	def erpost_log(self) -> ErpostLogVariableType:
		'''Value of variable $ERPOST_LOG'''
		__r = self._instance.ErpostLog
		return None if __r is None else ErpostLogVariableType(__r)

	@property
	def error_prog(self) -> str:
		'''Value of variable $ERROR_PROG'''
		return self._instance.ErrorProg

	@property
	def error_table(self) -> typing.List[int]:
		'''Value of variable $ERROR_TABLE'''
		return self._instance.ErrorTable

	@property
	def errsev_num(self) -> int:
		'''Value of variable $ERRSEV_NUM'''
		return self._instance.ErrsevNum

	@property
	def er_auto_enb(self) -> bool:
		'''Value of variable $ER_AUTO_ENB'''
		return self._instance.ErAutoEnb

	@property
	def er_noauto(self) -> ErNoautoVariableType:
		'''Value of variable $ER_NOAUTO'''
		__r = self._instance.ErNoauto
		return None if __r is None else ErNoautoVariableType(__r)

	@property
	def er_nofltr(self) -> bool:
		'''Value of variable $ER_NOFLTR'''
		return self._instance.ErNofltr

	@property
	def er_nohis(self) -> int:
		'''Value of variable $ER_NOHIS'''
		return self._instance.ErNohis

	@property
	def er_no_alm(self) -> typing.List[ErNoalmVariableType]:
		'''Value of variable $ER_NO_ALM'''
		__r = self._instance.ErNoAlm
		return None if __r is None else [None if x is None else ErNoalmVariableType(x) for x in __r]

	@property
	def er_sev_noau(self) -> typing.List[bool]:
		'''Value of variable $ER_SEV_NOAU'''
		return self._instance.ErSevNoau

	@property
	def etcp_ver(self) -> str:
		'''Value of variable $ETCP_VER'''
		return self._instance.EtcpVer

	@property
	def extlog_req(self) -> int:
		'''Value of variable $EXTLOG_REQ'''
		return self._instance.ExtlogReq

	@property
	def extlog_siz(self) -> int:
		'''Value of variable $EXTLOG_SIZ'''
		return self._instance.ExtlogSiz

	@property
	def extstksiz(self) -> int:
		'''Value of variable $EXTSTKSIZ'''
		return self._instance.Extstksiz

	@property
	def exttol(self) -> float:
		'''Value of variable $EXTTOL'''
		return self._instance.Exttol

	@property
	def ext_bwd_sel(self) -> bool:
		'''Value of variable $EXT_BWD_SEL'''
		return self._instance.ExtBwdSel

	@property
	def ext_di_bwd(self) -> ExtSetVariableType:
		'''Value of variable $EXT_DI_BWD'''
		__r = self._instance.ExtDiBwd
		return None if __r is None else ExtSetVariableType(__r)

	@property
	def ext_di_step(self) -> ExtSetVariableType:
		'''Value of variable $EXT_DI_STEP'''
		__r = self._instance.ExtDiStep
		return None if __r is None else ExtSetVariableType(__r)

	@property
	def e_stop_do(self) -> int:
		'''Value of variable $E_STOP_DO'''
		return self._instance.EStopDo

	@property
	def factory_tun(self) -> int:
		'''Value of variable $FACTORY_TUN'''
		return self._instance.FactoryTun

	@property
	def fdr_grp(self) -> typing.List[FdrGrpVariableType]:
		'''Value of variable $FDR_GRP'''
		__r = self._instance.FdrGrp
		return None if __r is None else [None if x is None else FdrGrpVariableType(x) for x in __r]

	@property
	def feature(self) -> FeatureVariableType:
		'''Value of variable $FEATURE'''
		__r = self._instance.Feature
		return None if __r is None else FeatureVariableType(__r)

	@property
	def feat_add(self) -> typing.List[str]:
		'''Value of variable $FEAT_ADD'''
		return self._instance.FeatAdd

	@property
	def feat_demo(self) -> FeatureVariableType:
		'''Value of variable $FEAT_DEMO'''
		__r = self._instance.FeatDemo
		return None if __r is None else FeatureVariableType(__r)

	@property
	def feat_demoin(self) -> int:
		'''Value of variable $FEAT_DEMOIN'''
		return self._instance.FeatDemoin

	@property
	def feat_index(self) -> int:
		'''Value of variable $FEAT_INDEX'''
		return self._instance.FeatIndex

	@property
	def filecomp(self) -> FilecompVariableType:
		'''Value of variable $FILECOMP'''
		__r = self._instance.Filecomp
		return None if __r is None else FilecompVariableType(__r)

	@property
	def filesetup2(self) -> FileSetup2VariableType:
		'''Value of variable $FILESETUP2'''
		__r = self._instance.Filesetup2
		return None if __r is None else FileSetup2VariableType(__r)

	@property
	def file_ap2bck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_AP2BCK'''
		__r = self._instance.FileAp2bck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def file_appbck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_APPBCK'''
		__r = self._instance.FileAppbck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def file_dgbck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_DGBCK'''
		__r = self._instance.FileDgbck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def file_frsprt(self) -> bool:
		'''Value of variable $FILE_FRSPRT'''
		return self._instance.FileFrsprt

	@property
	def file_visbck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_VISBCK'''
		__r = self._instance.FileVisbck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def flui_config(self) -> FluiCfgVariableType:
		'''Value of variable $FLUI_CONFIG'''
		__r = self._instance.FluiConfig
		return None if __r is None else FluiCfgVariableType(__r)

	@property
	def flui_data(self) -> FluiDataVariableType:
		'''Value of variable $FLUI_DATA'''
		__r = self._instance.FluiData
		return None if __r is None else FluiDataVariableType(__r)

	@property
	def flui_result(self) -> typing.List[FluiResVariableType]:
		'''Value of variable $FLUI_RESULT'''
		__r = self._instance.FluiResult
		return None if __r is None else [None if x is None else FluiResVariableType(x) for x in __r]

	@property
	def fmr_cfg(self) -> FmrCfgVariableType:
		'''Value of variable $FMR_CFG'''
		__r = self._instance.FmrCfg
		return None if __r is None else FmrCfgVariableType(__r)

	@property
	def fno(self) -> str:
		'''Value of variable $FNO'''
		return self._instance.Fno

	@property
	def frm_chktyp(self) -> int:
		'''Value of variable $FRM_CHKTYP'''
		return self._instance.FrmChktyp

	@property
	def fromchk_min(self) -> int:
		'''Value of variable $FROMCHK_MIN'''
		return self._instance.FromchkMin

	@property
	def fssb_cfg(self) -> FssbCfgVariableType:
		'''Value of variable $FSSB_CFG'''
		__r = self._instance.FssbCfg
		return None if __r is None else FssbCfgVariableType(__r)

	@property
	def ftp_def_ow(self) -> bool:
		'''Value of variable $FTP_DEF_OW'''
		return self._instance.FtpDefOw

	@property
	def ftp_dircomp(self) -> bool:
		'''Value of variable $FTP_DIRCOMP'''
		return self._instance.FtpDircomp

	@property
	def genov_enb(self) -> bool:
		'''Value of variable $GENOV_ENB'''
		return self._instance.GenovEnb

	@property
	def gravc_grp(self) -> typing.List[GravcGrpVariableType]:
		'''Value of variable $GRAVC_GRP'''
		__r = self._instance.GravcGrp
		return None if __r is None else [None if x is None else GravcGrpVariableType(x) for x in __r]

	@property
	def grsmt_grp(self) -> typing.List[GrsmtGrpVariableType]:
		'''Value of variable $GRSMT_GRP'''
		__r = self._instance.GrsmtGrp
		return None if __r is None else [None if x is None else GrsmtGrpVariableType(x) for x in __r]

	@property
	def hostc_cfg(self) -> typing.List[HostCfgVariableType]:
		'''Value of variable $HOSTC_CFG'''
		__r = self._instance.HostcCfg
		return None if __r is None else [None if x is None else HostCfgVariableType(x) for x in __r]

	@property
	def hostent(self) -> typing.List[HostentVariableType]:
		'''Value of variable $HOSTENT'''
		__r = self._instance.Hostent
		return None if __r is None else [None if x is None else HostentVariableType(x) for x in __r]

	@property
	def hostname(self) -> str:
		'''Value of variable $HOSTNAME'''
		return self._instance.Hostname

	@property
	def hosts_cfg(self) -> typing.List[HostCfgVariableType]:
		'''Value of variable $HOSTS_CFG'''
		__r = self._instance.HostsCfg
		return None if __r is None else [None if x is None else HostCfgVariableType(x) for x in __r]

	@property
	def host_err(self) -> ErrMaskVariableType:
		'''Value of variable $HOST_ERR'''
		__r = self._instance.HostErr
		return None if __r is None else ErrMaskVariableType(__r)

	@property
	def host_pdusiz(self) -> int:
		'''Value of variable $HOST_PDUSIZ'''
		return self._instance.HostPdusiz

	@property
	def hscdmngrp(self) -> typing.List[HscdMngVariableType]:
		'''Value of variable $HSCDMNGRP'''
		__r = self._instance.Hscdmngrp
		return None if __r is None else [None if x is None else HscdMngVariableType(x) for x in __r]

	@property
	def hscd_qupd(self) -> bool:
		'''Value of variable $HSCD_QUPD'''
		return self._instance.HscdQupd

	@property
	def hscd_updtyp(self) -> int:
		'''Value of variable $HSCD_UPDTYP'''
		return self._instance.HscdUpdtyp

	@property
	def http_auth(self) -> typing.List[HttpAuthVariableType]:
		'''Value of variable $HTTP_AUTH'''
		__r = self._instance.HttpAuth
		return None if __r is None else [None if x is None else HttpAuthVariableType(x) for x in __r]

	@property
	def http_ctrl(self) -> HttpVariableType:
		'''Value of variable $HTTP_CTRL'''
		__r = self._instance.HttpCtrl
		return None if __r is None else HttpVariableType(__r)

	@property
	def hwr_config(self) -> HwrConfigVariableType:
		'''Value of variable $HWR_CONFIG'''
		__r = self._instance.HwrConfig
		return None if __r is None else HwrConfigVariableType(__r)

	@property
	def idl_cpu_pct(self) -> float:
		'''Value of variable $IDL_CPU_PCT'''
		return self._instance.IdlCpuPct

	@property
	def idl_min_pct(self) -> float:
		'''Value of variable $IDL_MIN_PCT'''
		return self._instance.IdlMinPct

	@property
	def ignr_ioerr(self) -> int:
		'''Value of variable $IGNR_IOERR'''
		return self._instance.IgnrIoerr

	@property
	def inpt_sim_do(self) -> int:
		'''Value of variable $INPT_SIM_DO'''
		return self._instance.InptSimDo

	@property
	def instal_scrn(self) -> int:
		'''Value of variable $INSTAL_SCRN'''
		return self._instance.InstalScrn

	@property
	def intpmodntol(self) -> int:
		'''Value of variable $INTPMODNTOL'''
		return self._instance.Intpmodntol

	@property
	def intp_prty(self) -> int:
		'''Value of variable $INTP_PRTY'''
		return self._instance.IntpPrty

	@property
	def invistp_enb(self) -> int:
		'''Value of variable $INVISTP_ENB'''
		return self._instance.InvistpEnb

	@property
	def iolnk(self) -> typing.List[IolnkVariableType]:
		'''Value of variable $IOLNK'''
		__r = self._instance.Iolnk
		return None if __r is None else [None if x is None else IolnkVariableType(x) for x in __r]

	@property
	def iomaster(self) -> bool:
		'''Value of variable $IOMASTER'''
		return self._instance.Iomaster

	@property
	def ioslave(self) -> IoslaveVariableType:
		'''Value of variable $IOSLAVE'''
		__r = self._instance.Ioslave
		return None if __r is None else IoslaveVariableType(__r)

	@property
	def iosramcache(self) -> bool:
		'''Value of variable $IOSRAMCACHE'''
		return self._instance.Iosramcache

	@property
	def io_auto_cfg(self) -> bool:
		'''Value of variable $IO_AUTO_CFG'''
		return self._instance.IoAutoCfg

	@property
	def io_auto_uop(self) -> bool:
		'''Value of variable $IO_AUTO_UOP'''
		return self._instance.IoAutoUop

	@property
	def io_cmt_opt(self) -> int:
		'''Value of variable $IO_CMT_OPT'''
		return self._instance.IoCmtOpt

	@property
	def io_cycle(self) -> bool:
		'''Value of variable $IO_CYCLE'''
		return self._instance.IoCycle

	@property
	def io_def_asg(self) -> typing.List[IoDefAsgVariableType]:
		'''Value of variable $IO_DEF_ASG'''
		__r = self._instance.IoDefAsg
		return None if __r is None else [None if x is None else IoDefAsgVariableType(x) for x in __r]

	@property
	def io_def_num(self) -> int:
		'''Value of variable $IO_DEF_NUM'''
		return self._instance.IoDefNum

	@property
	def io_ipche(self) -> bool:
		'''Value of variable $IO_IPCHE'''
		return self._instance.IoIpche

	@property
	def io_rtry_cnt(self) -> int:
		'''Value of variable $IO_RTRY_CNT'''
		return self._instance.IoRtryCnt

	@property
	def io_scrn_upd(self) -> int:
		'''Value of variable $IO_SCRN_UPD'''
		return self._instance.IoScrnUpd

	@property
	def io_uop_cfg(self) -> IoUopCfgVariableType:
		'''Value of variable $IO_UOP_CFG'''
		__r = self._instance.IoUopCfg
		return None if __r is None else IoUopCfgVariableType(__r)

	@property
	def irca_acc(self) -> typing.List[ItemAccVariableType]:
		'''Value of variable $IRCA_ACC'''
		__r = self._instance.IrcaAcc
		return None if __r is None else [None if x is None else ItemAccVariableType(x) for x in __r]

	@property
	def irca_buf001(self) -> typing.List[ItemBuffElVariableType]:
		'''Value of variable $IRCA_BUF001'''
		__r = self._instance.IrcaBuf001
		return None if __r is None else [None if x is None else ItemBuffElVariableType(x) for x in __r]

	@property
	def irca_buf002(self) -> typing.List[ItemBuffElVariableType]:
		'''Value of variable $IRCA_BUF002'''
		__r = self._instance.IrcaBuf002
		return None if __r is None else [None if x is None else ItemBuffElVariableType(x) for x in __r]

	@property
	def irca_buf003(self) -> typing.List[ItemBuffElVariableType]:
		'''Value of variable $IRCA_BUF003'''
		__r = self._instance.IrcaBuf003
		return None if __r is None else [None if x is None else ItemBuffElVariableType(x) for x in __r]

	@property
	def irca_cfg(self) -> typing.List[IrcaCnfVariableType]:
		'''Value of variable $IRCA_CFG'''
		__r = self._instance.IrcaCfg
		return None if __r is None else [None if x is None else IrcaCnfVariableType(x) for x in __r]

	@property
	def irca_his001(self) -> typing.List[HistDayVariableType]:
		'''Value of variable $IRCA_HIS001'''
		__r = self._instance.IrcaHis001
		return None if __r is None else [None if x is None else HistDayVariableType(x) for x in __r]

	@property
	def irca_his002(self) -> typing.List[HistDayVariableType]:
		'''Value of variable $IRCA_HIS002'''
		__r = self._instance.IrcaHis002
		return None if __r is None else [None if x is None else HistDayVariableType(x) for x in __r]

	@property
	def irca_his003(self) -> typing.List[HistDayVariableType]:
		'''Value of variable $IRCA_HIS003'''
		__r = self._instance.IrcaHis003
		return None if __r is None else [None if x is None else HistDayVariableType(x) for x in __r]

	@property
	def irca_i_cfg(self) -> typing.List[ItemNameVariableType]:
		'''Value of variable $IRCA_I_CFG'''
		__r = self._instance.IrcaICfg
		return None if __r is None else [None if x is None else ItemNameVariableType(x) for x in __r]

	@property
	def irprog_cfg(self) -> IrprogCfgVariableType:
		'''Value of variable $IRPROG_CFG'''
		__r = self._instance.IrprogCfg
		return None if __r is None else IrprogCfgVariableType(__r)

	@property
	def isdt_isolc(self) -> typing.List[int]:
		'''Value of variable $ISDT_ISOLC'''
		return self._instance.IsdtIsolc

	@property
	def j23_dsp_enb(self) -> bool:
		'''Value of variable $J23_DSP_ENB'''
		return self._instance.J23DspEnb

	@property
	def jinc(self) -> JincVariableType:
		'''Value of variable $JINC'''
		__r = self._instance.Jinc
		return None if __r is None else JincVariableType(__r)

	@property
	def jobproc_enb(self) -> int:
		'''Value of variable $JOBPROC_ENB'''
		return self._instance.JobprocEnb

	@property
	def jog_in_auto(self) -> int:
		'''Value of variable $JOG_IN_AUTO'''
		return self._instance.JogInAuto

	@property
	def jposrec_enb(self) -> int:
		'''Value of variable $JPOSREC_ENB'''
		return self._instance.JposrecEnb

	@property
	def kanji_mask(self) -> int:
		'''Value of variable $KANJI_MASK'''
		return self._instance.KanjiMask

	@property
	def karelmon(self) -> KarelmonVariableType:
		'''Value of variable $KARELMON'''
		__r = self._instance.Karelmon
		return None if __r is None else KarelmonVariableType(__r)

	@property
	def karel_cfg(self) -> KarelCfgVariableType:
		'''Value of variable $KAREL_CFG'''
		__r = self._instance.KarelCfg
		return None if __r is None else KarelCfgVariableType(__r)

	@property
	def karel_enb(self) -> int:
		'''Value of variable $KAREL_ENB'''
		return self._instance.KarelEnb

	@property
	def kcl_lin_num(self) -> bool:
		'''Value of variable $KCL_LIN_NUM'''
		return self._instance.KclLinNum

	@property
	def keylogging(self) -> int:
		'''Value of variable $KEYLOGGING'''
		return self._instance.Keylogging

	@property
	def language(self) -> str:
		'''Value of variable $LANGUAGE'''
		return self._instance.Language

	@property
	def lgcfg(self) -> LgcfgVariableType:
		'''Value of variable $LGCFG'''
		__r = self._instance.Lgcfg
		return None if __r is None else LgcfgVariableType(__r)

	@property
	def ln_disp(self) -> LnDispVariableType:
		'''Value of variable $LN_DISP'''
		__r = self._instance.LnDisp
		return None if __r is None else LnDispVariableType(__r)

	@property
	def loctol(self) -> float:
		'''Value of variable $LOCTOL'''
		return self._instance.Loctol

	@property
	def logbook(self) -> LogbookVariableType:
		'''Value of variable $LOGBOOK'''
		__r = self._instance.Logbook
		return None if __r is None else LogbookVariableType(__r)

	@property
	def log_buff(self) -> typing.List[LogBuffVariableType]:
		'''Value of variable $LOG_BUFF'''
		__r = self._instance.LogBuff
		return None if __r is None else [None if x is None else LogBuffVariableType(x) for x in __r]

	@property
	def log_dcs(self) -> LogDcsVariableType:
		'''Value of variable $LOG_DCS'''
		__r = self._instance.LogDcs
		return None if __r is None else LogDcsVariableType(__r)

	@property
	def log_dio(self) -> typing.List[LogDioVariableType]:
		'''Value of variable $LOG_DIO'''
		__r = self._instance.LogDio
		return None if __r is None else [None if x is None else LogDioVariableType(x) for x in __r]

	@property
	def log_er_itm(self) -> typing.List[int]:
		'''Value of variable $LOG_ER_ITM'''
		return self._instance.LogErItm

	@property
	def log_er_sev(self) -> int:
		'''Value of variable $LOG_ER_SEV'''
		return self._instance.LogErSev

	@property
	def log_er_typ(self) -> typing.List[int]:
		'''Value of variable $LOG_ER_TYP'''
		return self._instance.LogErTyp

	@property
	def log_rec_rst(self) -> bool:
		'''Value of variable $LOG_REC_RST'''
		return self._instance.LogRecRst

	@property
	def log_scrn_fl(self) -> typing.List[LogScrnFlVariableType]:
		'''Value of variable $LOG_SCRN_FL'''
		__r = self._instance.LogScrnFl
		return None if __r is None else [None if x is None else LogScrnFlVariableType(x) for x in __r]

	@property
	def log_tpkey(self) -> typing.List[int]:
		'''Value of variable $LOG_TPKEY'''
		return self._instance.LogTpkey

	@property
	def longnam_enb(self) -> bool:
		'''Value of variable $LONGNAM_ENB'''
		return self._instance.LongnamEnb

	@property
	def lups_digit(self) -> int:
		'''Value of variable $LUPS_DIGIT'''
		return self._instance.LupsDigit

	@property
	def lu_loadprog(self) -> str:
		'''Value of variable $LU_LOADPROG'''
		return self._instance.LuLoadprog

	@property
	def maxualrmnum(self) -> int:
		'''Value of variable $MAXUALRMNUM'''
		return self._instance.Maxualrmnum

	@property
	def max_dig_prt(self) -> int:
		'''Value of variable $MAX_DIG_PRT'''
		return self._instance.MaxDigPrt

	@property
	def mcsp(self) -> McspVariableType:
		'''Value of variable $MCSP'''
		__r = self._instance.Mcsp
		return None if __r is None else McspVariableType(__r)

	@property
	def mcsp_grp(self) -> typing.List[McspGrpVariableType]:
		'''Value of variable $MCSP_GRP'''
		__r = self._instance.McspGrp
		return None if __r is None else [None if x is None else McspGrpVariableType(x) for x in __r]

	@property
	def md_ldxdisab(self) -> int:
		'''Value of variable $MD_LDXDISAB'''
		return self._instance.MdLdxdisab

	@property
	def memo_apname(self) -> typing.List[str]:
		'''Value of variable $MEMO_APNAME'''
		return self._instance.MemoApname

	@property
	def mfrq_cfg(self) -> MfrqCfgVariableType:
		'''Value of variable $MFRQ_CFG'''
		__r = self._instance.MfrqCfg
		return None if __r is None else MfrqCfgVariableType(__r)

	@property
	def mfrq_grp(self) -> typing.List[MfrqGrpVariableType]:
		'''Value of variable $MFRQ_GRP'''
		__r = self._instance.MfrqGrp
		return None if __r is None else [None if x is None else MfrqGrpVariableType(x) for x in __r]

	@property
	def misc_mstr(self) -> MiscMstrVariableType:
		'''Value of variable $MISC_MSTR'''
		__r = self._instance.MiscMstr
		return None if __r is None else MiscMstrVariableType(__r)

	@property
	def misc_scd(self) -> typing.List[MiscScdVariableType]:
		'''Value of variable $MISC_SCD'''
		__r = self._instance.MiscScd
		return None if __r is None else [None if x is None else MiscScdVariableType(x) for x in __r]

	@property
	def mkcfg(self) -> MkcfgVariableType:
		'''Value of variable $MKCFG'''
		__r = self._instance.Mkcfg
		return None if __r is None else MkcfgVariableType(__r)

	@property
	def mltarm_cfg(self) -> MltarmCfgVariableType:
		'''Value of variable $MLTARM_CFG'''
		__r = self._instance.MltarmCfg
		return None if __r is None else MltarmCfgVariableType(__r)

	@property
	def mmetpu(self) -> int:
		'''Value of variable $MMETPU'''
		return self._instance.Mmetpu

	@property
	def mndsp_adcol(self) -> int:
		'''Value of variable $MNDSP_ADCOL'''
		return self._instance.MndspAdcol

	@property
	def mndsp_cmnt(self) -> int:
		'''Value of variable $MNDSP_CMNT'''
		return self._instance.MndspCmnt

	@property
	def mndsp_fncmn(self) -> int:
		'''Value of variable $MNDSP_FNCMN'''
		return self._instance.MndspFncmn

	@property
	def mndsp_fstli(self) -> int:
		'''Value of variable $MNDSP_FSTLI'''
		return self._instance.MndspFstli

	@property
	def mndsp_mst(self) -> MndspMstVariableType:
		'''Value of variable $MNDSP_MST'''
		__r = self._instance.MndspMst
		return None if __r is None else MndspMstVariableType(__r)

	@property
	def mndsp_poscf(self) -> int:
		'''Value of variable $MNDSP_POSCF'''
		return self._instance.MndspPoscf

	@property
	def mndsp_prpmt(self) -> int:
		'''Value of variable $MNDSP_PRPMT'''
		return self._instance.MndspPrpmt

	@property
	def mndsp_pstol(self) -> typing.List[MndsppstlVariableType]:
		'''Value of variable $MNDSP_PSTOL'''
		__r = self._instance.MndspPstol
		return None if __r is None else [None if x is None else MndsppstlVariableType(x) for x in __r]

	@property
	def mnsing_chk(self) -> bool:
		'''Value of variable $MNSING_CHK'''
		return self._instance.MnsingChk

	@property
	def modaq_cfg(self) -> ModaqCfgVariableType:
		'''Value of variable $MODAQ_CFG'''
		__r = self._instance.ModaqCfg
		return None if __r is None else ModaqCfgVariableType(__r)

	@property
	def modaq_dev(self) -> str:
		'''Value of variable $MODAQ_DEV'''
		return self._instance.ModaqDev

	@property
	def modaq_hsize(self) -> int:
		'''Value of variable $MODAQ_HSIZE'''
		return self._instance.ModaqHsize

	@property
	def modaq_task(self) -> str:
		'''Value of variable $MODAQ_TASK'''
		return self._instance.ModaqTask

	@property
	def modaq_trig(self) -> typing.List[FxTriggerVariableType]:
		'''Value of variable $MODAQ_TRIG'''
		__r = self._instance.ModaqTrig
		return None if __r is None else [None if x is None else FxTriggerVariableType(x) for x in __r]

	@property
	def modaq_type(self) -> int:
		'''Value of variable $MODAQ_TYPE'''
		return self._instance.ModaqType

	@property
	def modem_inf(self) -> typing.List[ModemInfVariableType]:
		'''Value of variable $MODEM_INF'''
		__r = self._instance.ModemInf
		return None if __r is None else [None if x is None else ModemInfVariableType(x) for x in __r]

	@property
	def monitor_msg(self) -> typing.List[str]:
		'''Value of variable $MONITOR_MSG'''
		return self._instance.MonitorMsg

	@property
	def mor_grp_sv(self) -> typing.List[MorGrpSvVariableType]:
		'''Value of variable $MOR_GRP_SV'''
		__r = self._instance.MorGrpSv
		return None if __r is None else [None if x is None else MorGrpSvVariableType(x) for x in __r]

	@property
	def motion_dbg(self) -> MotionDbgVariableType:
		'''Value of variable $MOTION_DBG'''
		__r = self._instance.MotionDbg
		return None if __r is None else MotionDbgVariableType(__r)

	@property
	def mpl_name(self) -> str:
		'''Value of variable $MPL_NAME'''
		return self._instance.MplName

	@property
	def mr_hist(self) -> typing.List[MrHistVariableType]:
		'''Value of variable $MR_HIST'''
		__r = self._instance.MrHist
		return None if __r is None else [None if x is None else MrHistVariableType(x) for x in __r]

	@property
	def mskcfmap(self) -> typing.List[int]:
		'''Value of variable $MSKCFMAP'''
		return self._instance.Mskcfmap

	@property
	def mskconrel(self) -> int:
		'''Value of variable $MSKCONREL'''
		return self._instance.Mskconrel

	@property
	def mskexcfenb(self) -> int:
		'''Value of variable $MSKEXCFENB'''
		return self._instance.Mskexcfenb

	@property
	def mskexcffnc(self) -> int:
		'''Value of variable $MSKEXCFFNC'''
		return self._instance.Mskexcffnc

	@property
	def mskjogovlim(self) -> int:
		'''Value of variable $MSKJOGOVLIM'''
		return self._instance.Mskjogovlim

	@property
	def mskkey(self) -> int:
		'''Value of variable $MSKKEY'''
		return self._instance.Mskkey

	@property
	def mskkey_panl(self) -> int:
		'''Value of variable $MSKKEY_PANL'''
		return self._instance.MskkeyPanl

	@property
	def mskrunovlim(self) -> int:
		'''Value of variable $MSKRUNOVLIM'''
		return self._instance.Mskrunovlim

	@property
	def msksfspdtyp(self) -> int:
		'''Value of variable $MSKSFSPDTYP'''
		return self._instance.Msksfspdtyp

	@property
	def msksign(self) -> int:
		'''Value of variable $MSKSIGN'''
		return self._instance.Msksign

	@property
	def mskt1motlim(self) -> int:
		'''Value of variable $MSKT1MOTLIM'''
		return self._instance.Mskt1motlim

	@property
	def msk_ce_grp(self) -> typing.List[MskCeGrpVariableType]:
		'''Value of variable $MSK_CE_GRP'''
		__r = self._instance.MskCeGrp
		return None if __r is None else [None if x is None else MskCeGrpVariableType(x) for x in __r]

	@property
	def msqz_edit(self) -> int:
		'''Value of variable $MSQZ_EDIT'''
		return self._instance.MsqzEdit

	@property
	def mtcom_cfg(self) -> typing.List[MtcomCfgVariableType]:
		'''Value of variable $MTCOM_CFG'''
		__r = self._instance.MtcomCfg
		return None if __r is None else [None if x is None else MtcomCfgVariableType(x) for x in __r]

	@property
	def mt_arc_enb(self) -> bool:
		'''Value of variable $MT_ARC_ENB'''
		return self._instance.MtArcEnb

	@property
	def mt_mn_mode(self) -> int:
		'''Value of variable $MT_MN_MODE'''
		return self._instance.MtMnMode

	@property
	def mt_spl_enb(self) -> bool:
		'''Value of variable $MT_SPL_ENB'''
		return self._instance.MtSplEnb

	@property
	def muap_cplenb(self) -> bool:
		'''Value of variable $MUAP_CPLENB'''
		return self._instance.MuapCplenb

	@property
	def nocheck(self) -> typing.List[str]:
		'''Value of variable $NOCHECK'''
		return self._instance.Nocheck

	@property
	def no_wait_ln(self) -> int:
		'''Value of variable $NO_WAIT_LN'''
		return self._instance.NoWaitLn

	@property
	def num_rspace(self) -> typing.List[int]:
		'''Value of variable $NUM_RSPACE'''
		return self._instance.NumRspace

	@property
	def odrdsp_enb(self) -> int:
		'''Value of variable $ODRDSP_ENB'''
		return self._instance.OdrdspEnb

	@property
	def offset_cart(self) -> bool:
		'''Value of variable $OFFSET_CART'''
		return self._instance.OffsetCart

	@property
	def offset_dis(self) -> bool:
		'''Value of variable $OFFSET_DIS'''
		return self._instance.OffsetDis

	@property
	def ofs_at_mark(self) -> int:
		'''Value of variable $OFS_AT_MARK'''
		return self._instance.OfsAtMark

	@property
	def open_files(self) -> int:
		'''Value of variable $OPEN_FILES'''
		return self._instance.OpenFiles

	@property
	def option_io(self) -> int:
		'''Value of variable $OPTION_IO'''
		return self._instance.OptionIo

	@property
	def optm_prg(self) -> str:
		'''Value of variable $OPTM_PRG'''
		return self._instance.OptmPrg

	@property
	def opwork(self) -> OpworkVariableType:
		'''Value of variable $OPWORK'''
		__r = self._instance.Opwork
		return None if __r is None else OpworkVariableType(__r)

	@property
	def org_dsbl(self) -> typing.List[int]:
		'''Value of variable $ORG_DSBL'''
		return self._instance.OrgDsbl

	@property
	def orienttol(self) -> float:
		'''Value of variable $ORIENTTOL'''
		return self._instance.Orienttol

	@property
	def out_sim_do(self) -> int:
		'''Value of variable $OUT_SIM_DO'''
		return self._instance.OutSimDo

	@property
	def ovrdslct(self) -> OvrdslctVariableType:
		'''Value of variable $OVRDSLCT'''
		__r = self._instance.Ovrdslct
		return None if __r is None else OvrdslctVariableType(__r)

	@property
	def ovrd_pexe(self) -> bool:
		'''Value of variable $OVRD_PEXE'''
		return self._instance.OvrdPexe

	@property
	def ovrd_rate(self) -> int:
		'''Value of variable $OVRD_RATE'''
		return self._instance.OvrdRate

	@property
	def ovrd_setup(self) -> OvrdSetupVariableType:
		'''Value of variable $OVRD_SETUP'''
		__r = self._instance.OvrdSetup
		return None if __r is None else OvrdSetupVariableType(__r)

	@property
	def palcfg(self) -> PlcfgVariableType:
		'''Value of variable $PALCFG'''
		__r = self._instance.Palcfg
		return None if __r is None else PlcfgVariableType(__r)

	@property
	def pal_pos_chk(self) -> bool:
		'''Value of variable $PAL_POS_CHK'''
		return self._instance.PalPosChk

	@property
	def param_menu(self) -> typing.List[str]:
		'''Value of variable $PARAM_MENU'''
		return self._instance.ParamMenu

	@property
	def pause_prog(self) -> str:
		'''Value of variable $PAUSE_PROG'''
		return self._instance.PauseProg

	@property
	def pccrt(self) -> int:
		'''Value of variable $PCCRT'''
		return self._instance.Pccrt

	@property
	def pccrt_host(self) -> str:
		'''Value of variable $PCCRT_HOST'''
		return self._instance.PccrtHost

	@property
	def pctp(self) -> int:
		'''Value of variable $PCTP'''
		return self._instance.Pctp

	@property
	def pctp_host(self) -> str:
		'''Value of variable $PCTP_HOST'''
		return self._instance.PctpHost

	@property
	def pc_timeout(self) -> int:
		'''Value of variable $PC_TIMEOUT'''
		return self._instance.PcTimeout

	@property
	def pgdebug(self) -> int:
		'''Value of variable $PGDEBUG'''
		return self._instance.Pgdebug

	@property
	def pginp_flmsk(self) -> int:
		'''Value of variable $PGINP_FLMSK'''
		return self._instance.PginpFlmsk

	@property
	def pginp_fltr(self) -> int:
		'''Value of variable $PGINP_FLTR'''
		return self._instance.PginpFltr

	@property
	def pginp_pgatr(self) -> typing.List[int]:
		'''Value of variable $PGINP_PGATR'''
		return self._instance.PginpPgatr

	@property
	def pginp_pgchk(self) -> int:
		'''Value of variable $PGINP_PGCHK'''
		return self._instance.PginpPgchk

	@property
	def pginp_type(self) -> typing.List[str]:
		'''Value of variable $PGINP_TYPE'''
		return self._instance.PginpType

	@property
	def pginp_word(self) -> typing.List[str]:
		'''Value of variable $PGINP_WORD'''
		return self._instance.PginpWord

	@property
	def pglog(self) -> int:
		'''Value of variable $PGLOG'''
		return self._instance.Pglog

	@property
	def pgtracectl(self) -> typing.List[TracectlVariableType]:
		'''Value of variable $PGTRACECTL'''
		__r = self._instance.Pgtracectl
		return None if __r is None else [None if x is None else TracectlVariableType(x) for x in __r]

	@property
	def pgtracedt(self) -> typing.List[TracedtVariableType]:
		'''Value of variable $PGTRACEDT'''
		__r = self._instance.Pgtracedt
		return None if __r is None else [None if x is None else TracedtVariableType(x) for x in __r]

	@property
	def pgtracelen(self) -> int:
		'''Value of variable $PGTRACELEN'''
		return self._instance.Pgtracelen

	@property
	def pgtrace_up(self) -> TraceupVariableType:
		'''Value of variable $PGTRACE_UP'''
		__r = self._instance.PgtraceUp
		return None if __r is None else TraceupVariableType(__r)

	@property
	def pg_cfg(self) -> PgCfgVariableType:
		'''Value of variable $PG_CFG'''
		__r = self._instance.PgCfg
		return None if __r is None else PgCfgVariableType(__r)

	@property
	def pg_defspd(self) -> PgDefspdVariableType:
		'''Value of variable $PG_DEFSPD'''
		__r = self._instance.PgDefspd
		return None if __r is None else PgDefspdVariableType(__r)

	@property
	def ping_ctrl(self) -> PingVariableType:
		'''Value of variable $PING_CTRL'''
		__r = self._instance.PingCtrl
		return None if __r is None else PingVariableType(__r)

	@property
	def pipe_config(self) -> PipeCfgVariableType:
		'''Value of variable $PIPE_CONFIG'''
		__r = self._instance.PipeConfig
		return None if __r is None else PipeCfgVariableType(__r)

	@property
	def plid_cfg(self) -> PlidCfgVariableType:
		'''Value of variable $PLID_CFG'''
		__r = self._instance.PlidCfg
		return None if __r is None else PlidCfgVariableType(__r)

	@property
	def plid_cllb(self) -> typing.List[PlidCllbVariableType]:
		'''Value of variable $PLID_CLLB'''
		__r = self._instance.PlidCllb
		return None if __r is None else [None if x is None else PlidCllbVariableType(x) for x in __r]

	@property
	def plid_know_m(self) -> bool:
		'''Value of variable $PLID_KNOW_M'''
		return self._instance.PlidKnowM

	@property
	def plim_grp(self) -> typing.List[PlimGrpVariableType]:
		'''Value of variable $PLIM_GRP'''
		__r = self._instance.PlimGrp
		return None if __r is None else [None if x is None else PlimGrpVariableType(x) for x in __r]

	@property
	def plmr_grp(self) -> typing.List[PlmrGrpVariableType]:
		'''Value of variable $PLMR_GRP'''
		__r = self._instance.PlmrGrp
		return None if __r is None else [None if x is None else PlmrGrpVariableType(x) for x in __r]

	@property
	def ploadbanfwd(self) -> bool:
		'''Value of variable $PLOADBANFWD'''
		return self._instance.Ploadbanfwd

	@property
	def plst_grp6(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP6'''
		__r = self._instance.PlstGrp6
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp7(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP7'''
		__r = self._instance.PlstGrp7
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_grp8(self) -> typing.List[PlstGrpVariableType]:
		'''Value of variable $PLST_GRP8'''
		__r = self._instance.PlstGrp8
		return None if __r is None else [None if x is None else PlstGrpVariableType(x) for x in __r]

	@property
	def plst_ovld(self) -> typing.List[bool]:
		'''Value of variable $PLST_OVLD'''
		return self._instance.PlstOvld

	@property
	def pls_cmp_lim(self) -> int:
		'''Value of variable $PLS_CMP_LIM'''
		return self._instance.PlsCmpLim

	@property
	def pls_er_chk(self) -> int:
		'''Value of variable $PLS_ER_CHK'''
		return self._instance.PlsErChk

	@property
	def pls_er_lim(self) -> int:
		'''Value of variable $PLS_ER_LIM'''
		return self._instance.PlsErLim

	@property
	def pls_er_rst(self) -> bool:
		'''Value of variable $PLS_ER_RST'''
		return self._instance.PlsErRst

	@property
	def pl_mod(self) -> bool:
		'''Value of variable $PL_MOD'''
		return self._instance.PlMod

	@property
	def pl_mod_st(self) -> bool:
		'''Value of variable $PL_MOD_ST'''
		return self._instance.PlModSt

	@property
	def pl_res_g1(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G1'''
		__r = self._instance.PlResG1
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g2(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G2'''
		__r = self._instance.PlResG2
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g3(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G3'''
		__r = self._instance.PlResG3
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g4(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G4'''
		__r = self._instance.PlResG4
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g5(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G5'''
		__r = self._instance.PlResG5
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g6(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G6'''
		__r = self._instance.PlResG6
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g7(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G7'''
		__r = self._instance.PlResG7
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_res_g8(self) -> typing.List[PlResGVariableType]:
		'''Value of variable $PL_RES_G8'''
		__r = self._instance.PlResG8
		return None if __r is None else [None if x is None else PlResGVariableType(x) for x in __r]

	@property
	def pl_thr_inrt(self) -> int:
		'''Value of variable $PL_THR_INRT'''
		return self._instance.PlThrInrt

	@property
	def pl_thr_mass(self) -> int:
		'''Value of variable $PL_THR_MASS'''
		return self._instance.PlThrMass

	@property
	def pl_thr_mmnt(self) -> int:
		'''Value of variable $PL_THR_MMNT'''
		return self._instance.PlThrMmnt

	@property
	def pmon_queue(self) -> PmonQueVariableType:
		'''Value of variable $PMON_QUEUE'''
		__r = self._instance.PmonQueue
		return None if __r is None else PmonQueVariableType(__r)

	@property
	def pns_cur_lin(self) -> int:
		'''Value of variable $PNS_CUR_LIN'''
		return self._instance.PnsCurLin

	@property
	def pns_end_cur(self) -> bool:
		'''Value of variable $PNS_END_CUR'''
		return self._instance.PnsEndCur

	@property
	def pns_end_exe(self) -> bool:
		'''Value of variable $PNS_END_EXE'''
		return self._instance.PnsEndExe

	@property
	def pns_number(self) -> int:
		'''Value of variable $PNS_NUMBER'''
		return self._instance.PnsNumber

	@property
	def pns_option(self) -> int:
		'''Value of variable $PNS_OPTION'''
		return self._instance.PnsOption

	@property
	def pns_program(self) -> str:
		'''Value of variable $PNS_PROGRAM'''
		return self._instance.PnsProgram

	@property
	def pns_task_id(self) -> int:
		'''Value of variable $PNS_TASK_ID'''
		return self._instance.PnsTaskId

	@property
	def pocfg(self) -> PocfgVariableType:
		'''Value of variable $POCFG'''
		__r = self._instance.Pocfg
		return None if __r is None else PocfgVariableType(__r)

	@property
	def pos_edit(self) -> PosEditVariableType:
		'''Value of variable $POS_EDIT'''
		__r = self._instance.PosEdit
		return None if __r is None else PosEditVariableType(__r)

	@property
	def prgadj(self) -> PrgadjVariableType:
		'''Value of variable $PRGADJ'''
		__r = self._instance.Prgadj
		return None if __r is None else PrgadjVariableType(__r)

	@property
	def prgns_cfg(self) -> PrgnsCfgVariableType:
		'''Value of variable $PRGNS_CFG'''
		__r = self._instance.PrgnsCfg
		return None if __r is None else PrgnsCfgVariableType(__r)

	@property
	def prgns_grp(self) -> typing.List[PrgnsGrpVariableType]:
		'''Value of variable $PRGNS_GRP'''
		__r = self._instance.PrgnsGrp
		return None if __r is None else [None if x is None else PrgnsGrpVariableType(x) for x in __r]

	@property
	def prgns_pref(self) -> PrgnsPrefVariableType:
		'''Value of variable $PRGNS_PREF'''
		__r = self._instance.PrgnsPref
		return None if __r is None else PrgnsPrefVariableType(__r)

	@property
	def priority(self) -> int:
		'''Value of variable $PRIORITY'''
		return self._instance.Priority

	@property
	def product_id(self) -> str:
		'''Value of variable $PRODUCT_ID'''
		return self._instance.ProductId

	@property
	def proggrp_tgl(self) -> int:
		'''Value of variable $PROGGRP_TGL'''
		return self._instance.ProggrpTgl

	@property
	def prohibit_do(self) -> bool:
		'''Value of variable $PROHIBIT_DO'''
		return self._instance.ProhibitDo

	@property
	def protoent(self) -> typing.List[ProtoentVariableType]:
		'''Value of variable $PROTOENT'''
		__r = self._instance.Protoent
		return None if __r is None else [None if x is None else ProtoentVariableType(x) for x in __r]

	@property
	def proxy_cfg(self) -> ProxyCfgVariableType:
		'''Value of variable $PROXY_CFG'''
		__r = self._instance.ProxyCfg
		return None if __r is None else ProxyCfgVariableType(__r)

	@property
	def pro_cfg(self) -> PfCfgVariableType:
		'''Value of variable $PRO_CFG'''
		__r = self._instance.ProCfg
		return None if __r is None else PfCfgVariableType(__r)

	@property
	def pro_enhance(self) -> PfEnhanceVariableType:
		'''Value of variable $PRO_ENHANCE'''
		__r = self._instance.ProEnhance
		return None if __r is None else PfEnhanceVariableType(__r)

	@property
	def pro_pref(self) -> PfPrefVariableType:
		'''Value of variable $PRO_PREF'''
		__r = self._instance.ProPref
		return None if __r is None else PfPrefVariableType(__r)

	@property
	def prport_num(self) -> int:
		'''Value of variable $PRPORT_NUM'''
		return self._instance.PrportNum

	@property
	def pr_cartrep(self) -> bool:
		'''Value of variable $PR_CARTREP'''
		return self._instance.PrCartrep

	@property
	def pskstat(self) -> int:
		'''Value of variable $PSKSTAT'''
		return self._instance.Pskstat

	@property
	def pslgset(self) -> PslgsetVariableType:
		'''Value of variable $PSLGSET'''
		__r = self._instance.Pslgset
		return None if __r is None else PslgsetVariableType(__r)

	@property
	def pslgtemp(self) -> PslgtempVariableType:
		'''Value of variable $PSLGTEMP'''
		__r = self._instance.Pslgtemp
		return None if __r is None else PslgtempVariableType(__r)

	@property
	def pslgversion(self) -> str:
		'''Value of variable $PSLGVERSION'''
		return self._instance.Pslgversion

	@property
	def pssave(self) -> PssaveVariableType:
		'''Value of variable $PSSAVE'''
		__r = self._instance.Pssave
		return None if __r is None else PssaveVariableType(__r)

	@property
	def purge_enbl(self) -> bool:
		'''Value of variable $PURGE_ENBL'''
		return self._instance.PurgeEnbl

	@property
	def pwf_io(self) -> int:
		'''Value of variable $PWF_IO'''
		return self._instance.PwfIo

	@property
	def pwrup_delay(self) -> PwrupDlyVariableType:
		'''Value of variable $PWRUP_DELAY'''
		__r = self._instance.PwrupDelay
		return None if __r is None else PwrupDlyVariableType(__r)

	@property
	def pwr_normal(self) -> str:
		'''Value of variable $PWR_NORMAL'''
		return self._instance.PwrNormal

	@property
	def pwr_semi(self) -> str:
		'''Value of variable $PWR_SEMI'''
		return self._instance.PwrSemi

	@property
	def qskip_grp(self) -> typing.List[QskipGrpVariableType]:
		'''Value of variable $QSKIP_GRP'''
		__r = self._instance.QskipGrp
		return None if __r is None else [None if x is None else QskipGrpVariableType(x) for x in __r]

	@property
	def rbtif(self) -> int:
		'''Value of variable $RBTIF'''
		return self._instance.Rbtif

	@property
	def rcvtmout(self) -> int:
		'''Value of variable $RCVTMOUT'''
		return self._instance.Rcvtmout

	@property
	def rdcr_grp(self) -> typing.List[RdcrGrpVariableType]:
		'''Value of variable $RDCR_GRP'''
		__r = self._instance.RdcrGrp
		return None if __r is None else [None if x is None else RdcrGrpVariableType(x) for x in __r]

	@property
	def rdio_type(self) -> typing.List[int]:
		'''Value of variable $RDIO_TYPE'''
		return self._instance.RdioType

	@property
	def redprot_cfg(self) -> RedprotCfgVariableType:
		'''Value of variable $REDPROT_CFG'''
		__r = self._instance.RedprotCfg
		return None if __r is None else RedprotCfgVariableType(__r)

	@property
	def redprot_grp(self) -> typing.List[RedprotGrpVariableType]:
		'''Value of variable $REDPROT_GRP'''
		__r = self._instance.RedprotGrp
		return None if __r is None else [None if x is None else RedprotGrpVariableType(x) for x in __r]

	@property
	def refpos1(self) -> typing.List[Refpos11VariableType]:
		'''Value of variable $REFPOS1'''
		__r = self._instance.Refpos1
		return None if __r is None else [None if x is None else Refpos11VariableType(x) for x in __r]

	@property
	def refpos2(self) -> typing.List[Refpos21VariableType]:
		'''Value of variable $REFPOS2'''
		__r = self._instance.Refpos2
		return None if __r is None else [None if x is None else Refpos21VariableType(x) for x in __r]

	@property
	def refpos3(self) -> typing.List[Refpos31VariableType]:
		'''Value of variable $REFPOS3'''
		__r = self._instance.Refpos3
		return None if __r is None else [None if x is None else Refpos31VariableType(x) for x in __r]

	@property
	def refpos4(self) -> typing.List[Refpos41VariableType]:
		'''Value of variable $REFPOS4'''
		__r = self._instance.Refpos4
		return None if __r is None else [None if x is None else Refpos41VariableType(x) for x in __r]

	@property
	def refpos5(self) -> typing.List[Refpos51VariableType]:
		'''Value of variable $REFPOS5'''
		__r = self._instance.Refpos5
		return None if __r is None else [None if x is None else Refpos51VariableType(x) for x in __r]

	@property
	def refpos6(self) -> typing.List[Refpos61VariableType]:
		'''Value of variable $REFPOS6'''
		__r = self._instance.Refpos6
		return None if __r is None else [None if x is None else Refpos61VariableType(x) for x in __r]

	@property
	def refpos7(self) -> typing.List[Refpos71VariableType]:
		'''Value of variable $REFPOS7'''
		__r = self._instance.Refpos7
		return None if __r is None else [None if x is None else Refpos71VariableType(x) for x in __r]

	@property
	def refpos8(self) -> typing.List[Refpos81VariableType]:
		'''Value of variable $REFPOS8'''
		__r = self._instance.Refpos8
		return None if __r is None else [None if x is None else Refpos81VariableType(x) for x in __r]

	@property
	def refposmask(self) -> typing.List[RefpsmskVariableType]:
		'''Value of variable $REFPOSMASK'''
		__r = self._instance.Refposmask
		return None if __r is None else [None if x is None else RefpsmskVariableType(x) for x in __r]

	@property
	def refposmaxno(self) -> typing.List[int]:
		'''Value of variable $REFPOSMAXNO'''
		return self._instance.Refposmaxno

	@property
	def remote(self) -> int:
		'''Value of variable $REMOTE'''
		return self._instance.Remote

	@property
	def remote_cfg(self) -> RemoteCfgVariableType:
		'''Value of variable $REMOTE_CFG'''
		__r = self._instance.RemoteCfg
		return None if __r is None else RemoteCfgVariableType(__r)

	@property
	def repl_range(self) -> int:
		'''Value of variable $REPL_RANGE'''
		return self._instance.ReplRange

	@property
	def repower(self) -> RepowerVariableType:
		'''Value of variable $REPOWER'''
		__r = self._instance.Repower
		return None if __r is None else RepowerVariableType(__r)

	@property
	def resm_dryprg(self) -> str:
		'''Value of variable $RESM_DRYPRG'''
		return self._instance.ResmDryprg

	@property
	def restart(self) -> RestartVariableType:
		'''Value of variable $RESTART'''
		__r = self._instance.Restart
		return None if __r is None else RestartVariableType(__r)

	@property
	def resume_prog(self) -> str:
		'''Value of variable $RESUME_PROG'''
		return self._instance.ResumeProg

	@property
	def re_exec_enb(self) -> bool:
		'''Value of variable $RE_EXEC_ENB'''
		return self._instance.ReExecEnb

	@property
	def rgspd_prexe(self) -> bool:
		'''Value of variable $RGSPD_PREXE'''
		return self._instance.RgspdPrexe

	@property
	def rgtdb_prexe(self) -> bool:
		'''Value of variable $RGTDB_PREXE'''
		return self._instance.RgtdbPrexe

	@property
	def rgtrm_prexe(self) -> bool:
		'''Value of variable $RGTRM_PREXE'''
		return self._instance.RgtrmPrexe

	@property
	def ri_airpurge(self) -> typing.List[bool]:
		'''Value of variable $RI_AIRPURGE'''
		return self._instance.RiAirpurge

	@property
	def rmt_master(self) -> int:
		'''Value of variable $RMT_MASTER'''
		return self._instance.RmtMaster

	@property
	def robot_isolc(self) -> typing.List[int]:
		'''Value of variable $ROBOT_ISOLC'''
		return self._instance.RobotIsolc

	@property
	def robot_name(self) -> str:
		'''Value of variable $ROBOT_NAME'''
		return self._instance.RobotName

	@property
	def rob_categ(self) -> typing.List[int]:
		'''Value of variable $ROB_CATEG'''
		return self._instance.RobCateg

	@property
	def rob_ord_num(self) -> typing.List[str]:
		'''Value of variable $ROB_ORD_NUM'''
		return self._instance.RobOrdNum

	@property
	def rpc_timeout(self) -> int:
		'''Value of variable $RPC_TIMEOUT'''
		return self._instance.RpcTimeout

	@property
	def rs232_cfg(self) -> typing.List[Rs232CfgVariableType]:
		'''Value of variable $RS232_CFG'''
		__r = self._instance.Rs232Cfg
		return None if __r is None else [None if x is None else Rs232CfgVariableType(x) for x in __r]

	@property
	def rs232_nport(self) -> int:
		'''Value of variable $RS232_NPORT'''
		return self._instance.Rs232Nport

	@property
	def rsch_log(self) -> RschVariableType:
		'''Value of variable $RSCH_LOG'''
		__r = self._instance.RschLog
		return None if __r is None else RschVariableType(__r)

	@property
	def rsmavailnum(self) -> int:
		'''Value of variable $RSMAVAILNUM'''
		return self._instance.Rsmavailnum

	@property
	def rspace1(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE1'''
		__r = self._instance.Rspace1
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace2(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE2'''
		__r = self._instance.Rspace2
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace3(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE3'''
		__r = self._instance.Rspace3
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace4(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE4'''
		__r = self._instance.Rspace4
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace5(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE5'''
		__r = self._instance.Rspace5
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace6(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE6'''
		__r = self._instance.Rspace6
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace7(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE7'''
		__r = self._instance.Rspace7
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspace8(self) -> typing.List[RspaceVariableType]:
		'''Value of variable $RSPACE8'''
		__r = self._instance.Rspace8
		return None if __r is None else [None if x is None else RspaceVariableType(x) for x in __r]

	@property
	def rspaceg(self) -> RspacegVariableType:
		'''Value of variable $RSPACEG'''
		__r = self._instance.Rspaceg
		return None if __r is None else RspacegVariableType(__r)

	@property
	def rspace_mode(self) -> int:
		'''Value of variable $RSPACE_MODE'''
		return self._instance.RspaceMode

	@property
	def rspace_s(self) -> RspacesrVariableType:
		'''Value of variable $RSPACE_S'''
		__r = self._instance.RspaceS
		return None if __r is None else RspacesrVariableType(__r)

	@property
	def rspcwork_ad(self) -> int:
		'''Value of variable $RSPCWORK_AD'''
		return self._instance.RspcworkAd

	@property
	def rsr(self) -> typing.List[int]:
		'''Value of variable $RSR'''
		return self._instance.Rsr

	@property
	def rsr_intval(self) -> int:
		'''Value of variable $RSR_INTVAL'''
		return self._instance.RsrIntval

	@property
	def rsr_option(self) -> int:
		'''Value of variable $RSR_OPTION'''
		return self._instance.RsrOption

	@property
	def saf_do_puls(self) -> int:
		'''Value of variable $SAF_DO_PULS'''
		return self._instance.SafDoPuls

	@property
	def scan_time(self) -> int:
		'''Value of variable $SCAN_TIME'''
		return self._instance.ScanTime

	@property
	def sel_default(self) -> int:
		'''Value of variable $SEL_DEFAULT'''
		return self._instance.SelDefault

	@property
	def sel_hotstrt(self) -> int:
		'''Value of variable $SEL_HOTSTRT'''
		return self._instance.SelHotstrt

	@property
	def semipowerfl(self) -> bool:
		'''Value of variable $SEMIPOWERFL'''
		return self._instance.Semipowerfl

	@property
	def semipwfdo(self) -> int:
		'''Value of variable $SEMIPWFDO'''
		return self._instance.Semipwfdo

	@property
	def servent(self) -> typing.List[ServentVariableType]:
		'''Value of variable $SERVENT'''
		__r = self._instance.Servent
		return None if __r is None else [None if x is None else ServentVariableType(x) for x in __r]

	@property
	def service_kl(self) -> typing.List[str]:
		'''Value of variable $SERVICE_KL'''
		return self._instance.ServiceKl

	@property
	def service_prg(self) -> typing.List[str]:
		'''Value of variable $SERVICE_PRG'''
		return self._instance.ServicePrg

	@property
	def serv_dev(self) -> str:
		'''Value of variable $SERV_DEV'''
		return self._instance.ServDev

	@property
	def serv_mail(self) -> int:
		'''Value of variable $SERV_MAIL'''
		return self._instance.ServMail

	@property
	def serv_output(self) -> int:
		'''Value of variable $SERV_OUTPUT'''
		return self._instance.ServOutput

	@property
	def serv_save(self) -> int:
		'''Value of variable $SERV_SAVE'''
		return self._instance.ServSave

	@property
	def serv_type(self) -> int:
		'''Value of variable $SERV_TYPE'''
		return self._instance.ServType

	@property
	def sfzn_cfg(self) -> SfznCfgVariableType:
		'''Value of variable $SFZN_CFG'''
		__r = self._instance.SfznCfg
		return None if __r is None else SfznCfgVariableType(__r)

	@property
	def sfzn_grp(self) -> typing.List[SfznGrpVariableType]:
		'''Value of variable $SFZN_GRP'''
		__r = self._instance.SfznGrp
		return None if __r is None else [None if x is None else SfznGrpVariableType(x) for x in __r]

	@property
	def shell_cfg(self) -> ShellCfgVariableType:
		'''Value of variable $SHELL_CFG'''
		__r = self._instance.ShellCfg
		return None if __r is None else ShellCfgVariableType(__r)

	@property
	def shell_chk(self) -> typing.List[ShellChkVariableType]:
		'''Value of variable $SHELL_CHK'''
		__r = self._instance.ShellChk
		return None if __r is None else [None if x is None else ShellChkVariableType(x) for x in __r]

	@property
	def shell_comm(self) -> ShellCommVariableType:
		'''Value of variable $SHELL_COMM'''
		__r = self._instance.ShellComm
		return None if __r is None else ShellCommVariableType(__r)

	@property
	def shftov_enb(self) -> int:
		'''Value of variable $SHFTOV_ENB'''
		return self._instance.ShftovEnb

	@property
	def show_reg_ui(self) -> int:
		'''Value of variable $SHOW_REG_UI'''
		return self._instance.ShowRegUi

	@property
	def simiofwdlm(self) -> SimiofwdlmVariableType:
		'''Value of variable $SIMIOFWDLM'''
		__r = self._instance.Simiofwdlm
		return None if __r is None else SimiofwdlmVariableType(__r)

	@property
	def si_unit_enb(self) -> bool:
		'''Value of variable $SI_UNIT_ENB'''
		return self._instance.SiUnitEnb

	@property
	def slc_retry(self) -> int:
		'''Value of variable $SLC_RETRY'''
		return self._instance.SlcRetry

	@property
	def smon_alias(self) -> typing.List[str]:
		'''Value of variable $SMON_ALIAS'''
		return self._instance.SmonAlias

	@property
	def smon_defprog(self) -> str:
		'''Value of variable $SMON_DEFPROG'''
		return self._instance.SmonDefprog

	@property
	def smon_recall(self) -> typing.List[str]:
		'''Value of variable $SMON_RECALL'''
		return self._instance.SmonRecall

	@property
	def snpx_asg(self) -> typing.List[SnpxAsgVariableType]:
		'''Value of variable $SNPX_ASG'''
		__r = self._instance.SnpxAsg
		return None if __r is None else [None if x is None else SnpxAsgVariableType(x) for x in __r]

	@property
	def snpx_param(self) -> SnpxParamVariableType:
		'''Value of variable $SNPX_PARAM'''
		__r = self._instance.SnpxParam
		return None if __r is None else SnpxParamVariableType(__r)

	@property
	def soft_kb_cfg(self) -> int:
		'''Value of variable $SOFT_KB_CFG'''
		return self._instance.SoftKbCfg

	@property
	def sopin_sim(self) -> typing.List[int]:
		'''Value of variable $SOPIN_SIM'''
		return self._instance.SopinSim

	@property
	def srvnordy_do(self) -> bool:
		'''Value of variable $SRVNORDY_DO'''
		return self._instance.SrvnordyDo

	@property
	def srvqstp_dsb(self) -> typing.List[int]:
		'''Value of variable $SRVQSTP_DSB'''
		return self._instance.SrvqstpDsb

	@property
	def ssr(self) -> SsrVariableType:
		'''Value of variable $SSR'''
		__r = self._instance.Ssr
		return None if __r is None else SsrVariableType(__r)

	@property
	def stop_on_err(self) -> bool:
		'''Value of variable $STOP_ON_ERR'''
		return self._instance.StopOnErr

	@property
	def stop_ptn(self) -> str:
		'''Value of variable $STOP_PTN'''
		return self._instance.StopPtn

	@property
	def string_prm(self) -> bool:
		'''Value of variable $STRING_PRM'''
		return self._instance.StringPrm

	@property
	def svdt_grp(self) -> typing.List[SvdtGrpVariableType]:
		'''Value of variable $SVDT_GRP'''
		__r = self._instance.SvdtGrp
		return None if __r is None else [None if x is None else SvdtGrpVariableType(x) for x in __r]

	@property
	def svprg_count(self) -> int:
		'''Value of variable $SVPRG_COUNT'''
		return self._instance.SvprgCount

	@property
	def svprg_enb(self) -> bool:
		'''Value of variable $SVPRG_ENB'''
		return self._instance.SvprgEnb

	@property
	def svprm_enb(self) -> int:
		'''Value of variable $SVPRM_ENB'''
		return self._instance.SvprmEnb

	@property
	def svprm_upd(self) -> typing.List[SvprmUpdVariableType]:
		'''Value of variable $SVPRM_UPD'''
		__r = self._instance.SvprmUpd
		return None if __r is None else [None if x is None else SvprmUpdVariableType(x) for x in __r]

	@property
	def sv_info(self) -> typing.List[SvInfoVariableType]:
		'''Value of variable $SV_INFO'''
		__r = self._instance.SvInfo
		return None if __r is None else [None if x is None else SvInfoVariableType(x) for x in __r]

	@property
	def sysdebug(self) -> int:
		'''Value of variable $SYSDEBUG'''
		return self._instance.Sysdebug

	@property
	def sysdsp_pass(self) -> int:
		'''Value of variable $SYSDSP_PASS'''
		return self._instance.SysdspPass

	@property
	def syslog(self) -> SyslogVariableType:
		'''Value of variable $SYSLOG'''
		__r = self._instance.Syslog
		return None if __r is None else SyslogVariableType(__r)

	@property
	def syslog_mpc(self) -> SyslogVariableType:
		'''Value of variable $SYSLOG_MPC'''
		__r = self._instance.SyslogMpc
		return None if __r is None else SyslogVariableType(__r)

	@property
	def syslog_sav(self) -> SyslogSavVariableType:
		'''Value of variable $SYSLOG_SAV'''
		__r = self._instance.SyslogSav
		return None if __r is None else SyslogSavVariableType(__r)

	@property
	def system_time(self) -> typing.List[SystemTimerVariableType]:
		'''Value of variable $SYSTEM_TIME'''
		__r = self._instance.SystemTime
		return None if __r is None else [None if x is None else SystemTimerVariableType(x) for x in __r]

	@property
	def systskmem(self) -> typing.List[int]:
		'''Value of variable $SYSTSKMEM'''
		return self._instance.Systskmem

	@property
	def t1svgunspd(self) -> int:
		'''Value of variable $T1SVGUNSPD'''
		return self._instance.T1svgunspd

	@property
	def t2mode_lim(self) -> T2modeLimVariableType:
		'''Value of variable $T2MODE_LIM'''
		__r = self._instance.T2modeLim
		return None if __r is None else T2modeLimVariableType(__r)

	@property
	def t2spdlim(self) -> T2spdlimVariableType:
		'''Value of variable $T2SPDLIM'''
		__r = self._instance.T2spdlim
		return None if __r is None else T2spdlimVariableType(__r)

	@property
	def ta_disp_enb(self) -> bool:
		'''Value of variable $TA_DISP_ENB'''
		return self._instance.TaDispEnb

	@property
	def tbc2_grp(self) -> typing.List[Tbc2GrpVariableType]:
		'''Value of variable $TBC2_GRP'''
		__r = self._instance.Tbc2Grp
		return None if __r is None else [None if x is None else Tbc2GrpVariableType(x) for x in __r]

	@property
	def tbcsg_grp(self) -> typing.List[TbcsgGrpVariableType]:
		'''Value of variable $TBCSG_GRP'''
		__r = self._instance.TbcsgGrp
		return None if __r is None else [None if x is None else TbcsgGrpVariableType(x) for x in __r]

	@property
	def tbj2_grp(self) -> typing.List[Tbj2GrpVariableType]:
		'''Value of variable $TBJ2_GRP'''
		__r = self._instance.Tbj2Grp
		return None if __r is None else [None if x is None else Tbj2GrpVariableType(x) for x in __r]

	@property
	def tbjop_grp(self) -> typing.List[TbjopGrpVariableType]:
		'''Value of variable $TBJOP_GRP'''
		__r = self._instance.TbjopGrp
		return None if __r is None else [None if x is None else TbjopGrpVariableType(x) for x in __r]

	@property
	def threstable(self) -> typing.List[TpThrTableVariableType]:
		'''Value of variable $THRESTABLE'''
		__r = self._instance.Threstable
		return None if __r is None else [None if x is None else TpThrTableVariableType(x) for x in __r]

	@property
	def thrrditable(self) -> typing.List[TpThrTableVariableType]:
		'''Value of variable $THRRDITABLE'''
		__r = self._instance.Thrrditable
		return None if __r is None else [None if x is None else TpThrTableVariableType(x) for x in __r]

	@property
	def thrrdotable(self) -> typing.List[TpThrTableVariableType]:
		'''Value of variable $THRRDOTABLE'''
		__r = self._instance.Thrrdotable
		return None if __r is None else [None if x is None else TpThrTableVariableType(x) for x in __r]

	@property
	def thrsditable(self) -> typing.List[TpThrTableVariableType]:
		'''Value of variable $THRSDITABLE'''
		__r = self._instance.Thrsditable
		return None if __r is None else [None if x is None else TpThrTableVariableType(x) for x in __r]

	@property
	def thrsitable(self) -> typing.List[TpThrTableVariableType]:
		'''Value of variable $THRSITABLE'''
		__r = self._instance.Thrsitable
		return None if __r is None else [None if x is None else TpThrTableVariableType(x) for x in __r]

	@property
	def thrtablenum(self) -> typing.List[int]:
		'''Value of variable $THRTABLENUM'''
		return self._instance.Thrtablenum

	@property
	def thr_cfg(self) -> ThrCfgVariableType:
		'''Value of variable $THR_CFG'''
		__r = self._instance.ThrCfg
		return None if __r is None else ThrCfgVariableType(__r)

	@property
	def timebf_tts(self) -> int:
		'''Value of variable $TIMEBF_TTS'''
		return self._instance.TimebfTts

	@property
	def timebf_ver(self) -> int:
		'''Value of variable $TIMEBF_VER'''
		return self._instance.TimebfVer

	@property
	def timer(self) -> typing.List[TimerVariableType]:
		'''Value of variable $TIMER'''
		__r = self._instance.Timer
		return None if __r is None else [None if x is None else TimerVariableType(x) for x in __r]

	@property
	def timer_num(self) -> int:
		'''Value of variable $TIMER_NUM'''
		return self._instance.TimerNum

	@property
	def tmi_chan(self) -> int:
		'''Value of variable $TMI_CHAN'''
		return self._instance.TmiChan

	@property
	def tmi_dbglvl(self) -> int:
		'''Value of variable $TMI_DBGLVL'''
		return self._instance.TmiDbglvl

	@property
	def tmi_etherad(self) -> typing.List[str]:
		'''Value of variable $TMI_ETHERAD'''
		return self._instance.TmiEtherad

	@property
	def tmi_router(self) -> str:
		'''Value of variable $TMI_ROUTER'''
		return self._instance.TmiRouter

	@property
	def tmi_snmask(self) -> typing.List[str]:
		'''Value of variable $TMI_SNMASK'''
		return self._instance.TmiSnmask

	@property
	def toolofs_dis(self) -> bool:
		'''Value of variable $TOOLOFS_DIS'''
		return self._instance.ToolofsDis

	@property
	def tpe_detail(self) -> int:
		'''Value of variable $TPE_DETAIL'''
		return self._instance.TpeDetail

	@property
	def tpgl_config(self) -> TpglConfVariableType:
		'''Value of variable $TPGL_CONFIG'''
		__r = self._instance.TpglConfig
		return None if __r is None else TpglConfVariableType(__r)

	@property
	def tpgl_output(self) -> TpglOutVariableType:
		'''Value of variable $TPGL_OUTPUT'''
		__r = self._instance.TpglOutput
		return None if __r is None else TpglOutVariableType(__r)

	@property
	def tpoff_lim(self) -> int:
		'''Value of variable $TPOFF_LIM'''
		return self._instance.TpoffLim

	@property
	def tpon_svoff(self) -> bool:
		'''Value of variable $TPON_SVOFF'''
		return self._instance.TponSvoff

	@property
	def tpp_mon(self) -> TppMonVariableType:
		'''Value of variable $TPP_MON'''
		__r = self._instance.TppMon
		return None if __r is None else TppMonVariableType(__r)

	@property
	def tpstrtchk(self) -> TpstrtchkVariableType:
		'''Value of variable $TPSTRTCHK'''
		__r = self._instance.Tpstrtchk
		return None if __r is None else TpstrtchkVariableType(__r)

	@property
	def tpvtcompat(self) -> bool:
		'''Value of variable $TPVTCOMPAT'''
		return self._instance.Tpvtcompat

	@property
	def tpvwvar(self) -> TpvwvarVariableType:
		'''Value of variable $TPVWVAR'''
		__r = self._instance.Tpvwvar
		return None if __r is None else TpvwvarVariableType(__r)

	@property
	def tp_defprog(self) -> str:
		'''Value of variable $TP_DEFPROG'''
		return self._instance.TpDefprog

	@property
	def tp_display(self) -> int:
		'''Value of variable $TP_DISPLAY'''
		return self._instance.TpDisplay

	@property
	def tp_inst_msk(self) -> typing.List[int]:
		'''Value of variable $TP_INST_MSK'''
		return self._instance.TpInstMsk

	@property
	def tp_inuser(self) -> bool:
		'''Value of variable $TP_INUSER'''
		return self._instance.TpInuser

	@property
	def tp_lckuser(self) -> bool:
		'''Value of variable $TP_LCKUSER'''
		return self._instance.TpLckuser

	@property
	def tp_quickmen(self) -> bool:
		'''Value of variable $TP_QUICKMEN'''
		return self._instance.TpQuickmen

	@property
	def tp_screen(self) -> str:
		'''Value of variable $TP_SCREEN'''
		return self._instance.TpScreen

	@property
	def tp_userscrn(self) -> str:
		'''Value of variable $TP_USERSCRN'''
		return self._instance.TpUserscrn

	@property
	def tp_usestat(self) -> bool:
		'''Value of variable $TP_USESTAT'''
		return self._instance.TpUsestat

	@property
	def trace_cfg(self) -> TraceCfgVariableType:
		'''Value of variable $TRACE_CFG'''
		__r = self._instance.TraceCfg
		return None if __r is None else TraceCfgVariableType(__r)

	@property
	def trace_chnl(self) -> typing.List[TraceChnlVariableType]:
		'''Value of variable $TRACE_CHNL'''
		__r = self._instance.TraceChnl
		return None if __r is None else [None if x is None else TraceChnlVariableType(x) for x in __r]

	@property
	def trace_item(self) -> typing.List[TraceItemVariableType]:
		'''Value of variable $TRACE_ITEM'''
		__r = self._instance.TraceItem
		return None if __r is None else [None if x is None else TraceItemVariableType(x) for x in __r]

	@property
	def tscfg(self) -> TscfgVariableType:
		'''Value of variable $TSCFG'''
		__r = self._instance.Tscfg
		return None if __r is None else TscfgVariableType(__r)

	@property
	def tsscb(self) -> typing.List[TsscbVariableType]:
		'''Value of variable $TSSCB'''
		__r = self._instance.Tsscb
		return None if __r is None else [None if x is None else TsscbVariableType(x) for x in __r]

	@property
	def tutorial(self) -> TutorialVariableType:
		'''Value of variable $TUTORIAL'''
		__r = self._instance.Tutorial
		return None if __r is None else TutorialVariableType(__r)

	@property
	def tv_config(self) -> TvConfigVariableType:
		'''Value of variable $TV_CONFIG'''
		__r = self._instance.TvConfig
		return None if __r is None else TvConfigVariableType(__r)

	@property
	def tv_output(self) -> TvOutputVariableType:
		'''Value of variable $TV_OUTPUT'''
		__r = self._instance.TvOutput
		return None if __r is None else TvOutputVariableType(__r)

	@property
	def tx_screen(self) -> typing.List[TxscreenVariableType]:
		'''Value of variable $TX_SCREEN'''
		__r = self._instance.TxScreen
		return None if __r is None else [None if x is None else TxscreenVariableType(x) for x in __r]

	@property
	def ualrm_msg(self) -> typing.List[str]:
		'''Value of variable $UALRM_MSG'''
		return self._instance.UalrmMsg

	@property
	def ualrm_sev(self) -> typing.List[int]:
		'''Value of variable $UALRM_SEV'''
		return self._instance.UalrmSev

	@property
	def uecfg(self) -> UecfgVariableType:
		'''Value of variable $UECFG'''
		__r = self._instance.Uecfg
		return None if __r is None else UecfgVariableType(__r)

	@property
	def uegrp(self) -> typing.List[UegrpVariableType]:
		'''Value of variable $UEGRP'''
		__r = self._instance.Uegrp
		return None if __r is None else [None if x is None else UegrpVariableType(x) for x in __r]

	@property
	def ui_bbl_note(self) -> BblNtWndVariableType:
		'''Value of variable $UI_BBL_NOTE'''
		__r = self._instance.UiBblNote
		return None if __r is None else BblNtWndVariableType(__r)

	@property
	def ui_defprog(self) -> typing.List[str]:
		'''Value of variable $UI_DEFPROG'''
		return self._instance.UiDefprog

	@property
	def ui_fkeydata(self) -> typing.List[UiFkeydatVariableType]:
		'''Value of variable $UI_FKEYDATA'''
		__r = self._instance.UiFkeydata
		return None if __r is None else [None if x is None else UiFkeydatVariableType(x) for x in __r]

	@property
	def ui_inuser(self) -> typing.List[bool]:
		'''Value of variable $UI_INUSER'''
		return self._instance.UiInuser

	@property
	def ui_menhist(self) -> typing.List[UiMenhisVariableType]:
		'''Value of variable $UI_MENHIST'''
		__r = self._instance.UiMenhist
		return None if __r is None else [None if x is None else UiMenhisVariableType(x) for x in __r]

	@property
	def ui_panedata(self) -> typing.List[UiPanedatVariableType]:
		'''Value of variable $UI_PANEDATA'''
		__r = self._instance.UiPanedata
		return None if __r is None else [None if x is None else UiPanedatVariableType(x) for x in __r]

	@property
	def ui_postype(self) -> typing.List[int]:
		'''Value of variable $UI_POSTYPE'''
		return self._instance.UiPostype

	@property
	def ui_quickmen(self) -> typing.List[bool]:
		'''Value of variable $UI_QUICKMEN'''
		return self._instance.UiQuickmen

	@property
	def ui_restore(self) -> typing.List[UiUsrviewVariableType]:
		'''Value of variable $UI_RESTORE'''
		__r = self._instance.UiRestore
		return None if __r is None else [None if x is None else UiUsrviewVariableType(x) for x in __r]

	@property
	def ui_screen(self) -> typing.List[str]:
		'''Value of variable $UI_SCREEN'''
		return self._instance.UiScreen

	@property
	def ui_state(self) -> typing.List[int]:
		'''Value of variable $UI_STATE'''
		return self._instance.UiState

	@property
	def ui_userscrn(self) -> typing.List[str]:
		'''Value of variable $UI_USERSCRN'''
		return self._instance.UiUserscrn

	@property
	def undo_cfg(self) -> UndoCfgVariableType:
		'''Value of variable $UNDO_CFG'''
		__r = self._instance.UndoCfg
		return None if __r is None else UndoCfgVariableType(__r)

	@property
	def uop_crm5(self) -> bool:
		'''Value of variable $UOP_CRM5'''
		return self._instance.UopCrm5

	@property
	def update(self) -> str:
		'''Value of variable $UPDATE'''
		return self._instance.Update

	@property
	def user_info(self) -> typing.List[UserInfoVariableType]:
		'''Value of variable $USER_INFO'''
		__r = self._instance.UserInfo
		return None if __r is None else [None if x is None else UserInfoVariableType(x) for x in __r]

	@property
	def user_offset(self) -> UserOffstVariableType:
		'''Value of variable $USER_OFFSET'''
		__r = self._instance.UserOffset
		return None if __r is None else UserOffstVariableType(__r)

	@property
	def user_work(self) -> UserWorkVariableType:
		'''Value of variable $USER_WORK'''
		__r = self._instance.UserWork
		return None if __r is None else UserWorkVariableType(__r)

	@property
	def useuframe(self) -> bool:
		'''Value of variable $USEUFRAME'''
		return self._instance.Useuframe

	@property
	def usrtol_abrt(self) -> bool:
		'''Value of variable $USRTOL_ABRT'''
		return self._instance.UsrtolAbrt

	@property
	def usrtol_enb(self) -> bool:
		'''Value of variable $USRTOL_ENB'''
		return self._instance.UsrtolEnb

	@property
	def usrtol_grp(self) -> typing.List[UsrtolGrpVariableType]:
		'''Value of variable $USRTOL_GRP'''
		__r = self._instance.UsrtolGrp
		return None if __r is None else [None if x is None else UsrtolGrpVariableType(x) for x in __r]

	@property
	def usrtol_msk(self) -> int:
		'''Value of variable $USRTOL_MSK'''
		return self._instance.UsrtolMsk

	@property
	def usrtol_name(self) -> str:
		'''Value of variable $USRTOL_NAME'''
		return self._instance.UsrtolName

	@property
	def usr_evnt(self) -> int:
		'''Value of variable $USR_EVNT'''
		return self._instance.UsrEvnt

	@property
	def usr_ev_cfg(self) -> typing.List[UsrEvCfgVariableType]:
		'''Value of variable $USR_EV_CFG'''
		__r = self._instance.UsrEvCfg
		return None if __r is None else [None if x is None else UsrEvCfgVariableType(x) for x in __r]

	@property
	def usr_ev_wrk(self) -> typing.List[UsrEvWrkVariableType]:
		'''Value of variable $USR_EV_WRK'''
		__r = self._instance.UsrEvWrk
		return None if __r is None else [None if x is None else UsrEvWrkVariableType(x) for x in __r]

	@property
	def vars_config(self) -> VarsConfigVariableType:
		'''Value of variable $VARS_CONFIG'''
		__r = self._instance.VarsConfig
		return None if __r is None else VarsConfigVariableType(__r)

	@property
	def vcmr_grp(self) -> typing.List[VcmrGrpVariableType]:
		'''Value of variable $VCMR_GRP'''
		__r = self._instance.VcmrGrp
		return None if __r is None else [None if x is None else VcmrGrpVariableType(x) for x in __r]

	@property
	def via_work(self) -> ViaWorkVariableType:
		'''Value of variable $VIA_WORK'''
		__r = self._instance.ViaWork
		return None if __r is None else ViaWorkVariableType(__r)

	@property
	def visiontmout(self) -> int:
		'''Value of variable $VISIONTMOUT'''
		return self._instance.Visiontmout

	@property
	def vision_cfg(self) -> VisionCfgVariableType:
		'''Value of variable $VISION_CFG'''
		__r = self._instance.VisionCfg
		return None if __r is None else VisionCfgVariableType(__r)

	@property
	def vision_grp(self) -> typing.List[VisionGrpVariableType]:
		'''Value of variable $VISION_GRP'''
		__r = self._instance.VisionGrp
		return None if __r is None else [None if x is None else VisionGrpVariableType(x) for x in __r]

	@property
	def vis_ge_cfg(self) -> VisGeCfgVariableType:
		'''Value of variable $VIS_GE_CFG'''
		__r = self._instance.VisGeCfg
		return None if __r is None else VisGeCfgVariableType(__r)

	@property
	def vis_logreg(self) -> VisLogregVariableType:
		'''Value of variable $VIS_LOGREG'''
		__r = self._instance.VisLogreg
		return None if __r is None else VisLogregVariableType(__r)

	@property
	def vlexe_cfg(self) -> VlexeCfgVariableType:
		'''Value of variable $VLEXE_CFG'''
		__r = self._instance.VlexeCfg
		return None if __r is None else VlexeCfgVariableType(__r)

	@property
	def vrtd_filter(self) -> typing.List[VrtdFiltVariableType]:
		'''Value of variable $VRTD_FILTER'''
		__r = self._instance.VrtdFilter
		return None if __r is None else [None if x is None else VrtdFiltVariableType(x) for x in __r]

	@property
	def vshiftmenu(self) -> typing.List[CustommenuVariableType]:
		'''Value of variable $VSHIFTMENU'''
		__r = self._instance.Vshiftmenu
		return None if __r is None else [None if x is None else CustommenuVariableType(x) for x in __r]

	@property
	def vshift_cfg(self) -> VsftCfgVariableType:
		'''Value of variable $VSHIFT_CFG'''
		__r = self._instance.VshiftCfg
		return None if __r is None else VsftCfgVariableType(__r)

	@property
	def vsmo_cfg(self) -> VsmoCfgVariableType:
		'''Value of variable $VSMO_CFG'''
		__r = self._instance.VsmoCfg
		return None if __r is None else VsmoCfgVariableType(__r)

	@property
	def vzdt_cfg(self) -> VzdtCfgVariableType:
		'''Value of variable $VZDT_CFG'''
		__r = self._instance.VzdtCfg
		return None if __r is None else VzdtCfgVariableType(__r)

	@property
	def waitrelease(self) -> bool:
		'''Value of variable $WAITRELEASE'''
		return self._instance.Waitrelease

	@property
	def waittmout(self) -> int:
		'''Value of variable $WAITTMOUT'''
		return self._instance.Waittmout

	@property
	def wait_active(self) -> bool:
		'''Value of variable $WAIT_ACTIVE'''
		return self._instance.WaitActive

	@property
	def wait_data(self) -> WaitDataVariableType:
		'''Value of variable $WAIT_DATA'''
		__r = self._instance.WaitData
		return None if __r is None else WaitDataVariableType(__r)

	@property
	def wait_rdisp(self) -> bool:
		'''Value of variable $WAIT_RDISP'''
		return self._instance.WaitRdisp

	@property
	def xvrcfg(self) -> XvrcfgVariableType:
		'''Value of variable $XVRCFG'''
		__r = self._instance.Xvrcfg
		return None if __r is None else XvrcfgVariableType(__r)

	@property
	def zabc_grp(self) -> typing.List[ZabcGrpVariableType]:
		'''Value of variable $ZABC_GRP'''
		__r = self._instance.ZabcGrp
		return None if __r is None else [None if x is None else ZabcGrpVariableType(x) for x in __r]

	@property
	def zdt_actvspt(self) -> ZdtActvsptVariableType:
		'''Value of variable $ZDT_ACTVSPT'''
		__r = self._instance.ZdtActvspt
		return None if __r is None else ZdtActvsptVariableType(__r)

	@property
	def zdt_dcschg(self) -> ZdtDcschgVariableType:
		'''Value of variable $ZDT_DCSCHG'''
		__r = self._instance.ZdtDcschg
		return None if __r is None else ZdtDcschgVariableType(__r)

	@property
	def zip_cfg(self) -> ZipCfgVariableType:
		'''Value of variable $ZIP_CFG'''
		__r = self._instance.ZipCfg
		return None if __r is None else ZipCfgVariableType(__r)

	@property
	def zmpcf_g(self) -> typing.List[ZmpcfGrpVariableType]:
		'''Value of variable $ZMPCF_G'''
		__r = self._instance.ZmpcfG
		return None if __r is None else [None if x is None else ZmpcfGrpVariableType(x) for x in __r]

	@property
	def zmp_grp(self) -> typing.List[ZmposGrpVariableType]:
		'''Value of variable $ZMP_GRP'''
		__r = self._instance.ZmpGrp
		return None if __r is None else [None if x is None else ZmposGrpVariableType(x) for x in __r]

	@property
	def zpcfg(self) -> ZpCfgVariableType:
		'''Value of variable $ZPCFG'''
		__r = self._instance.Zpcfg
		return None if __r is None else ZpCfgVariableType(__r)

	@property
	def zp_cylinder(self) -> typing.List[ZpCylinderVariableType]:
		'''Value of variable $ZP_CYLINDER'''
		__r = self._instance.ZpCylinder
		return None if __r is None else [None if x is None else ZpCylinderVariableType(x) for x in __r]

	@property
	def zp_grp(self) -> typing.List[ZpGrpVariableType]:
		'''Value of variable $ZP_GRP'''
		__r = self._instance.ZpGrp
		return None if __r is None else [None if x is None else ZpGrpVariableType(x) for x in __r]

	@property
	def zp_sphere(self) -> typing.List[ZpSphereVariableType]:
		'''Value of variable $ZP_SPHERE'''
		__r = self._instance.ZpSphere
		return None if __r is None else [None if x is None else ZpSphereVariableType(x) for x in __r]

	@property
	def zzz(self) -> int:
		'''Value of variable $ZZZ'''
		return self._instance.Zzz

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
