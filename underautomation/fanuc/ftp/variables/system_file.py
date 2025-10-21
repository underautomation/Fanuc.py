import typing
from underautomation.fanuc.ftp.variables.aavm_wrk_variable_type import AavmWrkVariableType
from underautomation.fanuc.ftp.variables.abspos_grp_variable_type import AbsposGrpVariableType
from underautomation.fanuc.ftp.variables.aio_cnv_variable_type import AioCnvVariableType
from underautomation.fanuc.ftp.variables.almdg_variable_type import AlmdgVariableType
from underautomation.fanuc.ftp.variables.alm_if_variable_type import AlmIfVariableType
from underautomation.fanuc.ftp.variables.appinfo_variable_type import AppinfoVariableType
from underautomation.fanuc.ftp.variables.apcoupled_variable_type import ApcoupledVariableType
from underautomation.fanuc.ftp.variables.apcureq_variable_type import ApcureqVariableType
from underautomation.fanuc.ftp.variables.arg_str_variable_type import ArgStrVariableType
from underautomation.fanuc.ftp.variables.asbn_cfg_variable_type import AsbnCfgVariableType
from underautomation.fanuc.ftp.variables.at_cellsetup_variable_type import AtCellsetupVariableType
from underautomation.fanuc.ftp.variables.autobackup_variable_type import AutobackupVariableType
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.axscrdcfg_variable_type import AxscrdcfgVariableType
from underautomation.fanuc.ftp.variables.back_edit_variable_type import BackEditVariableType
from underautomation.fanuc.ftp.variables.bigallow_variable_type import BigallowVariableType
from underautomation.fanuc.ftp.variables.blal_out_variable_type import BlalOutVariableType
from underautomation.fanuc.ftp.variables.cfcfg_variable_type import CfcfgVariableType
from underautomation.fanuc.ftp.variables.chg_pri_variable_type import ChgPriVariableType
from underautomation.fanuc.ftp.variables.chkpos_variable_type import ChkposVariableType
from underautomation.fanuc.ftp.variables.cmd_info_variable_type import CmdInfoVariableType
from underautomation.fanuc.ftp.variables.cocfg_variable_type import CocfgVariableType
from underautomation.fanuc.ftp.variables.collect_variable_type import CollectVariableType
from underautomation.fanuc.ftp.variables.condet_cfg_variable_type import CondetCfgVariableType
from underautomation.fanuc.ftp.variables.condet_grp_variable_type import CondetGrpVariableType
from underautomation.fanuc.ftp.variables.condet_io_variable_type import CondetIoVariableType
from underautomation.fanuc.ftp.variables.condet_trgp_variable_type import CondetTrgpVariableType
from underautomation.fanuc.ftp.variables.condet_trig_variable_type import CondetTrigVariableType
from underautomation.fanuc.ftp.variables.co_morgrp_variable_type import CoMorgrpVariableType
from underautomation.fanuc.ftp.variables.co_paramgp_variable_type import CoParamgpVariableType
from underautomation.fanuc.ftp.variables.cpcfg_variable_type import CpcfgVariableType
from underautomation.fanuc.ftp.variables.cpdbg_variable_type import CpdbgVariableType
from underautomation.fanuc.ftp.variables.cp_mcrgrp_variable_type import CpMcrgrpVariableType
from underautomation.fanuc.ftp.variables.cp_morgrp_variable_type import CpMorgrpVariableType
from underautomation.fanuc.ftp.variables.cp_paramgp_variable_type import CpParamgpVariableType
from underautomation.fanuc.ftp.variables.cp_t1_grp_variable_type import CpT1GrpVariableType
from underautomation.fanuc.ftp.variables.cp_t1_mode_variable_type import CpT1ModeVariableType
from underautomation.fanuc.ftp.variables.custommenu_variable_type import CustommenuVariableType
from underautomation.fanuc.ftp.variables.dbg_errlog_variable_type import DbgErrlogVariableType
from underautomation.fanuc.ftp.variables.dbpxwork_variable_type import DbpxworkVariableType
from underautomation.fanuc.ftp.variables.dbtb_ctrl_variable_type import DbtbCtrlVariableType
from underautomation.fanuc.ftp.variables.db_dbg_variable_type import DbDbgVariableType
from underautomation.fanuc.ftp.variables.db_record_variable_type import DbRecordVariableType
from underautomation.fanuc.ftp.variables.dcss_cnstcy_variable_type import DcssCnstcyVariableType
from underautomation.fanuc.ftp.variables.dcss_device_variable_type import DcssDeviceVariableType
from underautomation.fanuc.ftp.variables.dcss_hndgd_variable_type import DcssHndgdVariableType
from underautomation.fanuc.ftp.variables.dcss_ls_variable_type import DcssLsVariableType
from underautomation.fanuc.ftp.variables.dcss_param_variable_type import DcssParamVariableType
from underautomation.fanuc.ftp.variables.dcss_slave_variable_type import DcssSlaveVariableType
from underautomation.fanuc.ftp.variables.dcs_cfg_variable_type import DcsCfgVariableType
from underautomation.fanuc.ftp.variables.dcs_crc_out_variable_type import DcsCrcOutVariableType
from underautomation.fanuc.ftp.variables.dcs_nocode_variable_type import DcsNocodeVariableType
from underautomation.fanuc.ftp.variables.dcs_sgn_variable_type import DcsSgnVariableType
from underautomation.fanuc.ftp.variables.deflogic_variable_type import DeflogicVariableType
from underautomation.fanuc.ftp.variables.demo_init_variable_type import DemoInitVariableType
from underautomation.fanuc.ftp.variables.diag_grp_variable_type import DiagGrpVariableType
from underautomation.fanuc.ftp.variables.dict_cfg_variable_type import DictCfgVariableType
from underautomation.fanuc.ftp.variables.dmsw_cfg_variable_type import DmswCfgVariableType
from underautomation.fanuc.ftp.variables.docviewer_variable_type import DocviewerVariableType
from underautomation.fanuc.ftp.variables.drc_cfg_variable_type import DrcCfgVariableType
from underautomation.fanuc.ftp.variables.dsbl_fault_variable_type import DsblFaultVariableType
from underautomation.fanuc.ftp.variables.dtrec_variable_type import DtrecVariableType
from underautomation.fanuc.ftp.variables.dyn_brk_variable_type import DynBrkVariableType
from underautomation.fanuc.ftp.variables.edt_recent_variable_type import EdtRecentVariableType
from underautomation.fanuc.ftp.variables.enc_info_variable_type import EncInfoVariableType
from underautomation.fanuc.ftp.variables.enetmode_variable_type import EnetmodeVariableType
from underautomation.fanuc.ftp.variables.eoatcfg_variable_type import EoatcfgVariableType
from underautomation.fanuc.ftp.variables.eoatdata_variable_type import EoatdataVariableType
from underautomation.fanuc.ftp.variables.erpost_log_variable_type import ErpostLogVariableType
from underautomation.fanuc.ftp.variables.er_noauto_variable_type import ErNoautoVariableType
from underautomation.fanuc.ftp.variables.er_noalm_variable_type import ErNoalmVariableType
from underautomation.fanuc.ftp.variables.ext_set_variable_type import ExtSetVariableType
from underautomation.fanuc.ftp.variables.fdr_grp_variable_type import FdrGrpVariableType
from underautomation.fanuc.ftp.variables.feature_variable_type import FeatureVariableType
from underautomation.fanuc.ftp.variables.filecomp_variable_type import FilecompVariableType
from underautomation.fanuc.ftp.variables.file_setup2_variable_type import FileSetup2VariableType
from underautomation.fanuc.ftp.variables.file_back_variable_type import FileBackVariableType
from underautomation.fanuc.ftp.variables.flui_cfg_variable_type import FluiCfgVariableType
from underautomation.fanuc.ftp.variables.flui_data_variable_type import FluiDataVariableType
from underautomation.fanuc.ftp.variables.flui_res_variable_type import FluiResVariableType
from underautomation.fanuc.ftp.variables.fmr_cfg_variable_type import FmrCfgVariableType
from underautomation.fanuc.ftp.variables.fssb_cfg_variable_type import FssbCfgVariableType
from underautomation.fanuc.ftp.variables.gravc_grp_variable_type import GravcGrpVariableType
from underautomation.fanuc.ftp.variables.grsmt_grp_variable_type import GrsmtGrpVariableType
from underautomation.fanuc.ftp.variables.host_cfg_variable_type import HostCfgVariableType
from underautomation.fanuc.ftp.variables.hostent_variable_type import HostentVariableType
from underautomation.fanuc.ftp.variables.err_mask_variable_type import ErrMaskVariableType
from underautomation.fanuc.ftp.variables.hscd_mng_variable_type import HscdMngVariableType
from underautomation.fanuc.ftp.variables.http_auth_variable_type import HttpAuthVariableType
from underautomation.fanuc.ftp.variables.http_variable_type import HttpVariableType
from underautomation.fanuc.ftp.variables.hwr_config_variable_type import HwrConfigVariableType
from underautomation.fanuc.ftp.variables.iolnk_variable_type import IolnkVariableType
from underautomation.fanuc.ftp.variables.ioslave_variable_type import IoslaveVariableType
from underautomation.fanuc.ftp.variables.io_def_asg_variable_type import IoDefAsgVariableType
from underautomation.fanuc.ftp.variables.io_uop_cfg_variable_type import IoUopCfgVariableType
from underautomation.fanuc.ftp.variables.item_acc_variable_type import ItemAccVariableType
from underautomation.fanuc.ftp.variables.item_buff_el_variable_type import ItemBuffElVariableType
from underautomation.fanuc.ftp.variables.irca_cnf_variable_type import IrcaCnfVariableType
from underautomation.fanuc.ftp.variables.hist_day_variable_type import HistDayVariableType
from underautomation.fanuc.ftp.variables.item_name_variable_type import ItemNameVariableType
from underautomation.fanuc.ftp.variables.irprog_cfg_variable_type import IrprogCfgVariableType
from underautomation.fanuc.ftp.variables.jinc_variable_type import JincVariableType
from underautomation.fanuc.ftp.variables.karelmon_variable_type import KarelmonVariableType
from underautomation.fanuc.ftp.variables.karel_cfg_variable_type import KarelCfgVariableType
from underautomation.fanuc.ftp.variables.lgcfg_variable_type import LgcfgVariableType
from underautomation.fanuc.ftp.variables.ln_disp_variable_type import LnDispVariableType
from underautomation.fanuc.ftp.variables.logbook_variable_type import LogbookVariableType
from underautomation.fanuc.ftp.variables.log_buff_variable_type import LogBuffVariableType
from underautomation.fanuc.ftp.variables.log_dcs_variable_type import LogDcsVariableType
from underautomation.fanuc.ftp.variables.log_dio_variable_type import LogDioVariableType
from underautomation.fanuc.ftp.variables.log_scrn_fl_variable_type import LogScrnFlVariableType
from underautomation.fanuc.ftp.variables.mcsp_variable_type import McspVariableType
from underautomation.fanuc.ftp.variables.mcsp_grp_variable_type import McspGrpVariableType
from underautomation.fanuc.ftp.variables.mfrq_cfg_variable_type import MfrqCfgVariableType
from underautomation.fanuc.ftp.variables.mfrq_grp_variable_type import MfrqGrpVariableType
from underautomation.fanuc.ftp.variables.misc_mstr_variable_type import MiscMstrVariableType
from underautomation.fanuc.ftp.variables.misc_scd_variable_type import MiscScdVariableType
from underautomation.fanuc.ftp.variables.mkcfg_variable_type import MkcfgVariableType
from underautomation.fanuc.ftp.variables.mltarm_cfg_variable_type import MltarmCfgVariableType
from underautomation.fanuc.ftp.variables.mndsp_mst_variable_type import MndspMstVariableType
from underautomation.fanuc.ftp.variables.mndsppstl_variable_type import MndsppstlVariableType
from underautomation.fanuc.ftp.variables.modaq_cfg_variable_type import ModaqCfgVariableType
from underautomation.fanuc.ftp.variables.fx_trigger_variable_type import FxTriggerVariableType
from underautomation.fanuc.ftp.variables.modem_inf_variable_type import ModemInfVariableType
from underautomation.fanuc.ftp.variables.mor_grp_sv_variable_type import MorGrpSvVariableType
from underautomation.fanuc.ftp.variables.motion_dbg_variable_type import MotionDbgVariableType
from underautomation.fanuc.ftp.variables.mr_hist_variable_type import MrHistVariableType
from underautomation.fanuc.ftp.variables.msk_ce_grp_variable_type import MskCeGrpVariableType
from underautomation.fanuc.ftp.variables.mtcom_cfg_variable_type import MtcomCfgVariableType
from underautomation.fanuc.ftp.variables.opwork_variable_type import OpworkVariableType
from underautomation.fanuc.ftp.variables.ovrdslct_variable_type import OvrdslctVariableType
from underautomation.fanuc.ftp.variables.ovrd_setup_variable_type import OvrdSetupVariableType
from underautomation.fanuc.ftp.variables.plcfg_variable_type import PlcfgVariableType
from underautomation.fanuc.ftp.variables.tracectl_variable_type import TracectlVariableType
from underautomation.fanuc.ftp.variables.tracedt_variable_type import TracedtVariableType
from underautomation.fanuc.ftp.variables.traceup_variable_type import TraceupVariableType
from underautomation.fanuc.ftp.variables.pg_cfg_variable_type import PgCfgVariableType
from underautomation.fanuc.ftp.variables.pg_defspd_variable_type import PgDefspdVariableType
from underautomation.fanuc.ftp.variables.ping_variable_type import PingVariableType
from underautomation.fanuc.ftp.variables.pipe_cfg_variable_type import PipeCfgVariableType
from underautomation.fanuc.ftp.variables.plid_cfg_variable_type import PlidCfgVariableType
from underautomation.fanuc.ftp.variables.plid_cllb_variable_type import PlidCllbVariableType
from underautomation.fanuc.ftp.variables.plim_grp_variable_type import PlimGrpVariableType
from underautomation.fanuc.ftp.variables.plmr_grp_variable_type import PlmrGrpVariableType
from underautomation.fanuc.ftp.variables.plst_grp_variable_type import PlstGrpVariableType
from underautomation.fanuc.ftp.variables.pl_res_g_variable_type import PlResGVariableType
from underautomation.fanuc.ftp.variables.pmon_que_variable_type import PmonQueVariableType
from underautomation.fanuc.ftp.variables.pocfg_variable_type import PocfgVariableType
from underautomation.fanuc.ftp.variables.pos_edit_variable_type import PosEditVariableType
from underautomation.fanuc.ftp.variables.prgadj_variable_type import PrgadjVariableType
from underautomation.fanuc.ftp.variables.prgns_cfg_variable_type import PrgnsCfgVariableType
from underautomation.fanuc.ftp.variables.prgns_grp_variable_type import PrgnsGrpVariableType
from underautomation.fanuc.ftp.variables.prgns_pref_variable_type import PrgnsPrefVariableType
from underautomation.fanuc.ftp.variables.protoent_variable_type import ProtoentVariableType
from underautomation.fanuc.ftp.variables.proxy_cfg_variable_type import ProxyCfgVariableType
from underautomation.fanuc.ftp.variables.pf_cfg_variable_type import PfCfgVariableType
from underautomation.fanuc.ftp.variables.pf_enhance_variable_type import PfEnhanceVariableType
from underautomation.fanuc.ftp.variables.pf_pref_variable_type import PfPrefVariableType
from underautomation.fanuc.ftp.variables.pslgset_variable_type import PslgsetVariableType
from underautomation.fanuc.ftp.variables.pslgtemp_variable_type import PslgtempVariableType
from underautomation.fanuc.ftp.variables.pssave_variable_type import PssaveVariableType
from underautomation.fanuc.ftp.variables.pwrup_dly_variable_type import PwrupDlyVariableType
from underautomation.fanuc.ftp.variables.qskip_grp_variable_type import QskipGrpVariableType
from underautomation.fanuc.ftp.variables.rdcr_grp_variable_type import RdcrGrpVariableType
from underautomation.fanuc.ftp.variables.redprot_cfg_variable_type import RedprotCfgVariableType
from underautomation.fanuc.ftp.variables.redprot_grp_variable_type import RedprotGrpVariableType
from underautomation.fanuc.ftp.variables.refpos11_variable_type import Refpos11VariableType
from underautomation.fanuc.ftp.variables.refpos21_variable_type import Refpos21VariableType
from underautomation.fanuc.ftp.variables.refpos31_variable_type import Refpos31VariableType
from underautomation.fanuc.ftp.variables.refpos41_variable_type import Refpos41VariableType
from underautomation.fanuc.ftp.variables.refpos51_variable_type import Refpos51VariableType
from underautomation.fanuc.ftp.variables.refpos61_variable_type import Refpos61VariableType
from underautomation.fanuc.ftp.variables.refpos71_variable_type import Refpos71VariableType
from underautomation.fanuc.ftp.variables.refpos81_variable_type import Refpos81VariableType
from underautomation.fanuc.ftp.variables.refpsmsk_variable_type import RefpsmskVariableType
from underautomation.fanuc.ftp.variables.remote_cfg_variable_type import RemoteCfgVariableType
from underautomation.fanuc.ftp.variables.repower_variable_type import RepowerVariableType
from underautomation.fanuc.ftp.variables.restart_variable_type import RestartVariableType
from underautomation.fanuc.ftp.variables.rs232_cfg_variable_type import Rs232CfgVariableType
from underautomation.fanuc.ftp.variables.rsch_variable_type import RschVariableType
from underautomation.fanuc.ftp.variables.rspace_variable_type import RspaceVariableType
from underautomation.fanuc.ftp.variables.rspaceg_variable_type import RspacegVariableType
from underautomation.fanuc.ftp.variables.rspacesr_variable_type import RspacesrVariableType
from underautomation.fanuc.ftp.variables.servent_variable_type import ServentVariableType
from underautomation.fanuc.ftp.variables.sfzn_cfg_variable_type import SfznCfgVariableType
from underautomation.fanuc.ftp.variables.sfzn_grp_variable_type import SfznGrpVariableType
from underautomation.fanuc.ftp.variables.shell_cfg_variable_type import ShellCfgVariableType
from underautomation.fanuc.ftp.variables.shell_chk_variable_type import ShellChkVariableType
from underautomation.fanuc.ftp.variables.shell_comm_variable_type import ShellCommVariableType
from underautomation.fanuc.ftp.variables.simiofwdlm_variable_type import SimiofwdlmVariableType
from underautomation.fanuc.ftp.variables.snpx_asg_variable_type import SnpxAsgVariableType
from underautomation.fanuc.ftp.variables.snpx_param_variable_type import SnpxParamVariableType
from underautomation.fanuc.ftp.variables.ssr_variable_type import SsrVariableType
from underautomation.fanuc.ftp.variables.svdt_grp_variable_type import SvdtGrpVariableType
from underautomation.fanuc.ftp.variables.svprm_upd_variable_type import SvprmUpdVariableType
from underautomation.fanuc.ftp.variables.sv_info_variable_type import SvInfoVariableType
from underautomation.fanuc.ftp.variables.syslog_variable_type import SyslogVariableType
from underautomation.fanuc.ftp.variables.syslog_sav_variable_type import SyslogSavVariableType
from underautomation.fanuc.ftp.variables.system_timer_variable_type import SystemTimerVariableType
from underautomation.fanuc.ftp.variables.t2mode_lim_variable_type import T2modeLimVariableType
from underautomation.fanuc.ftp.variables.t2spdlim_variable_type import T2spdlimVariableType
from underautomation.fanuc.ftp.variables.tbc2_grp_variable_type import Tbc2GrpVariableType
from underautomation.fanuc.ftp.variables.tbcsg_grp_variable_type import TbcsgGrpVariableType
from underautomation.fanuc.ftp.variables.tbj2_grp_variable_type import Tbj2GrpVariableType
from underautomation.fanuc.ftp.variables.tbjop_grp_variable_type import TbjopGrpVariableType
from underautomation.fanuc.ftp.variables.tp_thr_table_variable_type import TpThrTableVariableType
from underautomation.fanuc.ftp.variables.thr_cfg_variable_type import ThrCfgVariableType
from underautomation.fanuc.ftp.variables.timer_variable_type import TimerVariableType
from underautomation.fanuc.ftp.variables.tpgl_conf_variable_type import TpglConfVariableType
from underautomation.fanuc.ftp.variables.tpgl_out_variable_type import TpglOutVariableType
from underautomation.fanuc.ftp.variables.tpp_mon_variable_type import TppMonVariableType
from underautomation.fanuc.ftp.variables.tpstrtchk_variable_type import TpstrtchkVariableType
from underautomation.fanuc.ftp.variables.tpvwvar_variable_type import TpvwvarVariableType
from underautomation.fanuc.ftp.variables.trace_cfg_variable_type import TraceCfgVariableType
from underautomation.fanuc.ftp.variables.trace_chnl_variable_type import TraceChnlVariableType
from underautomation.fanuc.ftp.variables.trace_item_variable_type import TraceItemVariableType
from underautomation.fanuc.ftp.variables.tscfg_variable_type import TscfgVariableType
from underautomation.fanuc.ftp.variables.tsscb_variable_type import TsscbVariableType
from underautomation.fanuc.ftp.variables.tutorial_variable_type import TutorialVariableType
from underautomation.fanuc.ftp.variables.tv_config_variable_type import TvConfigVariableType
from underautomation.fanuc.ftp.variables.tv_output_variable_type import TvOutputVariableType
from underautomation.fanuc.ftp.variables.txscreen_variable_type import TxscreenVariableType
from underautomation.fanuc.ftp.variables.uecfg_variable_type import UecfgVariableType
from underautomation.fanuc.ftp.variables.uegrp_variable_type import UegrpVariableType
from underautomation.fanuc.ftp.variables.bbl_nt_wnd_variable_type import BblNtWndVariableType
from underautomation.fanuc.ftp.variables.ui_fkeydat_variable_type import UiFkeydatVariableType
from underautomation.fanuc.ftp.variables.ui_menhis_variable_type import UiMenhisVariableType
from underautomation.fanuc.ftp.variables.ui_panedat_variable_type import UiPanedatVariableType
from underautomation.fanuc.ftp.variables.ui_usrview_variable_type import UiUsrviewVariableType
from underautomation.fanuc.ftp.variables.undo_cfg_variable_type import UndoCfgVariableType
from underautomation.fanuc.ftp.variables.user_info_variable_type import UserInfoVariableType
from underautomation.fanuc.ftp.variables.user_offst_variable_type import UserOffstVariableType
from underautomation.fanuc.ftp.variables.user_work_variable_type import UserWorkVariableType
from underautomation.fanuc.ftp.variables.usrtol_grp_variable_type import UsrtolGrpVariableType
from underautomation.fanuc.ftp.variables.usr_ev_cfg_variable_type import UsrEvCfgVariableType
from underautomation.fanuc.ftp.variables.usr_ev_wrk_variable_type import UsrEvWrkVariableType
from underautomation.fanuc.ftp.variables.vars_config_variable_type import VarsConfigVariableType
from underautomation.fanuc.ftp.variables.vcmr_grp_variable_type import VcmrGrpVariableType
from underautomation.fanuc.ftp.variables.via_work_variable_type import ViaWorkVariableType
from underautomation.fanuc.ftp.variables.vision_cfg_variable_type import VisionCfgVariableType
from underautomation.fanuc.ftp.variables.vision_grp_variable_type import VisionGrpVariableType
from underautomation.fanuc.ftp.variables.vis_ge_cfg_variable_type import VisGeCfgVariableType
from underautomation.fanuc.ftp.variables.vis_logreg_variable_type import VisLogregVariableType
from underautomation.fanuc.ftp.variables.vlexe_cfg_variable_type import VlexeCfgVariableType
from underautomation.fanuc.ftp.variables.vrtd_filt_variable_type import VrtdFiltVariableType
from underautomation.fanuc.ftp.variables.vsft_cfg_variable_type import VsftCfgVariableType
from underautomation.fanuc.ftp.variables.vsmo_cfg_variable_type import VsmoCfgVariableType
from underautomation.fanuc.ftp.variables.vzdt_cfg_variable_type import VzdtCfgVariableType
from underautomation.fanuc.ftp.variables.wait_data_variable_type import WaitDataVariableType
from underautomation.fanuc.ftp.variables.xvrcfg_variable_type import XvrcfgVariableType
from underautomation.fanuc.ftp.variables.zabc_grp_variable_type import ZabcGrpVariableType
from underautomation.fanuc.ftp.variables.zdt_actvspt_variable_type import ZdtActvsptVariableType
from underautomation.fanuc.ftp.variables.zdt_dcschg_variable_type import ZdtDcschgVariableType
from underautomation.fanuc.ftp.variables.zip_cfg_variable_type import ZipCfgVariableType
from underautomation.fanuc.ftp.variables.zmpcf_grp_variable_type import ZmpcfGrpVariableType
from underautomation.fanuc.ftp.variables.zmpos_grp_variable_type import ZmposGrpVariableType
from underautomation.fanuc.ftp.variables.zp_cfg_variable_type import ZpCfgVariableType
from underautomation.fanuc.ftp.variables.zp_cylinder_variable_type import ZpCylinderVariableType
from underautomation.fanuc.ftp.variables.zp_grp_variable_type import ZpGrpVariableType
from underautomation.fanuc.ftp.variables.zp_sphere_variable_type import ZpSphereVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SystemFile as system_file

class SystemFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = system_file()
		else:
			self._instance = _internal
	@property
	def aavm_wrk(self) -> typing.List[AavmWrkVariableType]:
		return [AavmWrkVariableType(x) for x in self._instance.AavmWrk]
	@property
	def abspos_grp(self) -> typing.List[AbsposGrpVariableType]:
		return [AbsposGrpVariableType(x) for x in self._instance.AbsposGrp]
	@property
	def acc_maxlmt(self) -> int:
		return self._instance.AccMaxlmt
	@property
	def acc_minlmt(self) -> int:
		return self._instance.AccMinlmt
	@property
	def acc_pre_exe(self) -> int:
		return self._instance.AccPreExe
	@property
	def ac_update(self) -> int:
		return self._instance.AcUpdate
	@property
	def aiocnv_num(self) -> int:
		return self._instance.AiocnvNum
	@property
	def aiocnv_use(self) -> int:
		return self._instance.AiocnvUse
	@property
	def aio_cnv(self) -> typing.List[AioCnvVariableType]:
		return [AioCnvVariableType(x) for x in self._instance.AioCnv]
	@property
	def almdg(self) -> AlmdgVariableType:
		return AlmdgVariableType(self._instance.Almdg)
	@property
	def alm_if(self) -> AlmIfVariableType:
		return AlmIfVariableType(self._instance.AlmIf)
	@property
	def angtol(self) -> typing.List[float]:
		return self._instance.Angtol
	@property
	def appinfo(self) -> AppinfoVariableType:
		return AppinfoVariableType(self._instance.Appinfo)
	@property
	def application(self) -> typing.List[str]:
		return self._instance.Application
	@property
	def ap_active(self) -> int:
		return self._instance.ApActive
	@property
	def ap_automode(self) -> bool:
		return self._instance.ApAutomode
	@property
	def ap_chgaponl(self) -> bool:
		return self._instance.ApChgaponl
	@property
	def ap_coupled(self) -> typing.List[ApcoupledVariableType]:
		return [ApcoupledVariableType(x) for x in self._instance.ApCoupled]
	@property
	def ap_cureq(self) -> typing.List[ApcureqVariableType]:
		return [ApcureqVariableType(x) for x in self._instance.ApCureq]
	@property
	def ap_curtool(self) -> int:
		return self._instance.ApCurtool
	@property
	def ap_do_clean(self) -> bool:
		return self._instance.ApDoClean
	@property
	def ap_do_clenm(self) -> typing.List[bool]:
		return self._instance.ApDoClenm
	@property
	def ap_dspdryrn(self) -> bool:
		return self._instance.ApDspdryrn
	@property
	def ap_hide(self) -> typing.List[bool]:
		return self._instance.ApHide
	@property
	def ap_maxapp(self) -> int:
		return self._instance.ApMaxapp
	@property
	def ap_maxax(self) -> int:
		return self._instance.ApMaxax
	@property
	def ap_plugged(self) -> int:
		return self._instance.ApPlugged
	@property
	def ap_prc_dsbm(self) -> typing.List[int]:
		return self._instance.ApPrcDsbm
	@property
	def ap_proc_dsb(self) -> bool:
		return self._instance.ApProcDsb
	@property
	def ap_segf_chk(self) -> bool:
		return self._instance.ApSegfChk
	@property
	def ap_seg_chkm(self) -> typing.List[bool]:
		return self._instance.ApSegChkm
	@property
	def ap_selap(self) -> typing.List[bool]:
		return self._instance.ApSelap
	@property
	def ap_totalax(self) -> int:
		return self._instance.ApTotalax
	@property
	def ap_usenum(self) -> typing.List[int]:
		return self._instance.ApUsenum
	@property
	def argdispmmck(self) -> float:
		return self._instance.Argdispmmck
	@property
	def argdispmode(self) -> int:
		return self._instance.Argdispmode
	@property
	def arg_string(self) -> typing.List[ArgStrVariableType]:
		return [ArgStrVariableType(x) for x in self._instance.ArgString]
	@property
	def arg_word(self) -> typing.List[str]:
		return self._instance.ArgWord
	@property
	def asbn_config(self) -> AsbnCfgVariableType:
		return AsbnCfgVariableType(self._instance.AsbnConfig)
	@property
	def atcellsetup(self) -> AtCellsetupVariableType:
		return AtCellsetupVariableType(self._instance.Atcellsetup)
	@property
	def autobackup(self) -> AutobackupVariableType:
		return AutobackupVariableType(self._instance.Autobackup)
	@property
	def autoinit(self) -> int:
		return self._instance.Autoinit
	@property
	def automessage(self) -> int:
		return self._instance.Automessage
	@property
	def automode_do(self) -> bool:
		return self._instance.AutomodeDo
	@property
	def automode_ov(self) -> bool:
		return self._instance.AutomodeOv
	@property
	def autopauspos(self) -> typing.List[JointPositionVariable]:
		return [JointPositionVariable(x) for x in self._instance.Autopauspos]
	@property
	def autoppostsk(self) -> typing.List[int]:
		return self._instance.Autoppostsk
	@property
	def autoupdtmod(self) -> int:
		return self._instance.Autoupdtmod
	@property
	def auxwzd_enb(self) -> int:
		return self._instance.AuxwzdEnb
	@property
	def auxwzd_stat(self) -> int:
		return self._instance.AuxwzdStat
	@property
	def axscrdcfg(self) -> typing.List[AxscrdcfgVariableType]:
		return [AxscrdcfgVariableType(x) for x in self._instance.Axscrdcfg]
	@property
	def background(self) -> bool:
		return self._instance.Background
	@property
	def backup_name(self) -> str:
		return self._instance.BackupName
	@property
	def back_edit(self) -> typing.List[BackEditVariableType]:
		return [BackEditVariableType(x) for x in self._instance.BackEdit]
	@property
	def bck_no_del(self) -> bool:
		return self._instance.BckNoDel
	@property
	def bge_unusend(self) -> bool:
		return self._instance.BgeUnusend
	@property
	def bigallow(self) -> typing.List[BigallowVariableType]:
		return [BigallowVariableType(x) for x in self._instance.Bigallow]
	@property
	def blal_out(self) -> BlalOutVariableType:
		return BlalOutVariableType(self._instance.BlalOut)
	@property
	def bwd_abort(self) -> bool:
		return self._instance.BwdAbort
	@property
	def bwd_itr_rtn(self) -> int:
		return self._instance.BwdItrRtn
	@property
	def bwd_nonstop(self) -> int:
		return self._instance.BwdNonstop
	@property
	def ce_option(self) -> int:
		return self._instance.CeOption
	@property
	def ce_ria_id(self) -> int:
		return self._instance.CeRiaId
	@property
	def cfcfg(self) -> CfcfgVariableType:
		return CfcfgVariableType(self._instance.Cfcfg)
	@property
	def checkconfig(self) -> bool:
		return self._instance.Checkconfig
	@property
	def chg_pri(self) -> typing.List[ChgPriVariableType]:
		return [ChgPriVariableType(x) for x in self._instance.ChgPri]
	@property
	def chkpauspos(self) -> typing.List[ChkposVariableType]:
		return [ChkposVariableType(x) for x in self._instance.Chkpauspos]
	@property
	def cmd_info(self) -> typing.List[CmdInfoVariableType]:
		return [CmdInfoVariableType(x) for x in self._instance.CmdInfo]
	@property
	def cocfg(self) -> CocfgVariableType:
		return CocfgVariableType(self._instance.Cocfg)
	@property
	def collect_cfg(self) -> CollectVariableType:
		return CollectVariableType(self._instance.CollectCfg)
	@property
	def collect_enb(self) -> int:
		return self._instance.CollectEnb
	@property
	def condet_cfg(self) -> CondetCfgVariableType:
		return CondetCfgVariableType(self._instance.CondetCfg)
	@property
	def condet_grp(self) -> typing.List[CondetGrpVariableType]:
		return [CondetGrpVariableType(x) for x in self._instance.CondetGrp]
	@property
	def condet_io(self) -> CondetIoVariableType:
		return CondetIoVariableType(self._instance.CondetIo)
	@property
	def condet_trgp(self) -> typing.List[CondetTrgpVariableType]:
		return [CondetTrgpVariableType(x) for x in self._instance.CondetTrgp]
	@property
	def condet_trig(self) -> CondetTrigVariableType:
		return CondetTrigVariableType(self._instance.CondetTrig)
	@property
	def co_morgrp(self) -> typing.List[CoMorgrpVariableType]:
		return [CoMorgrpVariableType(x) for x in self._instance.CoMorgrp]
	@property
	def co_paramgrp(self) -> typing.List[CoParamgpVariableType]:
		return [CoParamgpVariableType(x) for x in self._instance.CoParamgrp]
	@property
	def cpcfg(self) -> CpcfgVariableType:
		return CpcfgVariableType(self._instance.Cpcfg)
	@property
	def cpdbg(self) -> CpdbgVariableType:
		return CpdbgVariableType(self._instance.Cpdbg)
	@property
	def cp_mcrgrp(self) -> typing.List[CpMcrgrpVariableType]:
		return [CpMcrgrpVariableType(x) for x in self._instance.CpMcrgrp]
	@property
	def cp_morgrp(self) -> typing.List[CpMorgrpVariableType]:
		return [CpMorgrpVariableType(x) for x in self._instance.CpMorgrp]
	@property
	def cp_paramgrp(self) -> typing.List[CpParamgpVariableType]:
		return [CpParamgpVariableType(x) for x in self._instance.CpParamgrp]
	@property
	def cp_t1_grp(self) -> typing.List[CpT1GrpVariableType]:
		return [CpT1GrpVariableType(x) for x in self._instance.CpT1Grp]
	@property
	def cp_t1_mode(self) -> CpT1ModeVariableType:
		return CpT1ModeVariableType(self._instance.CpT1Mode)
	@property
	def crt_defprog(self) -> str:
		return self._instance.CrtDefprog
	@property
	def crt_inuser(self) -> bool:
		return self._instance.CrtInuser
	@property
	def crt_key_tbl(self) -> typing.List[int]:
		return self._instance.CrtKeyTbl
	@property
	def crt_lckuser(self) -> bool:
		return self._instance.CrtLckuser
	@property
	def crt_usestat(self) -> bool:
		return self._instance.CrtUsestat
	@property
	def cr_auto_do(self) -> int:
		return self._instance.CrAutoDo
	@property
	def cr_indt_enb(self) -> bool:
		return self._instance.CrIndtEnb
	@property
	def cr_t1_do(self) -> int:
		return self._instance.CrT1Do
	@property
	def cr_t2_do(self) -> int:
		return self._instance.CrT2Do
	@property
	def cstop(self) -> bool:
		return self._instance.Cstop
	@property
	def ctrl_delete(self) -> int:
		return self._instance.CtrlDelete
	@property
	def ct_screen(self) -> str:
		return self._instance.CtScreen
	@property
	def custommenu(self) -> typing.List[CustommenuVariableType]:
		return [CustommenuVariableType(x) for x in self._instance.Custommenu]
	@property
	def cust_manual(self) -> bool:
		return self._instance.CustManual
	@property
	def dbcondtrig(self) -> int:
		return self._instance.Dbcondtrig
	@property
	def dbg_errlog(self) -> DbgErrlogVariableType:
		return DbgErrlogVariableType(self._instance.DbgErrlog)
	@property
	def dbnumlim(self) -> int:
		return self._instance.Dbnumlim
	@property
	def dbpxwork(self) -> typing.List[DbpxworkVariableType]:
		return [DbpxworkVariableType(x) for x in self._instance.Dbpxwork]
	@property
	def dbtb_ctrl(self) -> DbtbCtrlVariableType:
		return DbtbCtrlVariableType(self._instance.DbtbCtrl)
	@property
	def db_awaytrig(self) -> float:
		return self._instance.DbAwaytrig
	@property
	def db_away_alm(self) -> bool:
		return self._instance.DbAwayAlm
	@property
	def db_condtyp(self) -> int:
		return self._instance.DbCondtyp
	@property
	def db_dbg(self) -> typing.List[DbDbgVariableType]:
		return [DbDbgVariableType(x) for x in self._instance.DbDbg]
	@property
	def db_mindist(self) -> float:
		return self._instance.DbMindist
	@property
	def db_montime(self) -> int:
		return self._instance.DbMontime
	@property
	def db_montyp(self) -> int:
		return self._instance.DbMontyp
	@property
	def db_motnend(self) -> bool:
		return self._instance.DbMotnend
	@property
	def db_record(self) -> typing.List[DbRecordVariableType]:
		return [DbRecordVariableType(x) for x in self._instance.DbRecord]
	@property
	def db_tolerenc(self) -> float:
		return self._instance.DbTolerenc
	@property
	def dcss_cnstcy(self) -> typing.List[DcssCnstcyVariableType]:
		return [DcssCnstcyVariableType(x) for x in self._instance.DcssCnstcy]
	@property
	def dcss_device(self) -> typing.List[DcssDeviceVariableType]:
		return [DcssDeviceVariableType(x) for x in self._instance.DcssDevice]
	@property
	def dcss_hndgd(self) -> DcssHndgdVariableType:
		return DcssHndgdVariableType(self._instance.DcssHndgd)
	@property
	def dcss_ls(self) -> typing.List[DcssLsVariableType]:
		return [DcssLsVariableType(x) for x in self._instance.DcssLs]
	@property
	def dcss_param(self) -> DcssParamVariableType:
		return DcssParamVariableType(self._instance.DcssParam)
	@property
	def dcss_slave(self) -> DcssSlaveVariableType:
		return DcssSlaveVariableType(self._instance.DcssSlave)
	@property
	def dcs_cfg(self) -> DcsCfgVariableType:
		return DcsCfgVariableType(self._instance.DcsCfg)
	@property
	def dcs_crc_out(self) -> DcsCrcOutVariableType:
		return DcsCrcOutVariableType(self._instance.DcsCrcOut)
	@property
	def dcs_nocode(self) -> DcsNocodeVariableType:
		return DcsNocodeVariableType(self._instance.DcsNocode)
	@property
	def dcs_sgn(self) -> DcsSgnVariableType:
		return DcsSgnVariableType(self._instance.DcsSgn)
	@property
	def dcs_version(self) -> str:
		return self._instance.DcsVersion
	@property
	def deflogic(self) -> typing.List[DeflogicVariableType]:
		return [DeflogicVariableType(x) for x in self._instance.Deflogic]
	@property
	def defprog_enb(self) -> bool:
		return self._instance.DefprogEnb
	@property
	def defpulse(self) -> int:
		return self._instance.Defpulse
	@property
	def def_acclim(self) -> int:
		return self._instance.DefAcclim
	@property
	def def_wrstjnt(self) -> int:
		return self._instance.DefWrstjnt
	@property
	def demo_init(self) -> DemoInitVariableType:
		return DemoInitVariableType(self._instance.DemoInit)
	@property
	def dev_index(self) -> int:
		return self._instance.DevIndex
	@property
	def dev_path(self) -> str:
		return self._instance.DevPath
	@property
	def dhcp_clntid(self) -> typing.List[str]:
		return self._instance.DhcpClntid
	@property
	def diag_grp(self) -> typing.List[DiagGrpVariableType]:
		return [DiagGrpVariableType(x) for x in self._instance.DiagGrp]
	@property
	def dict_config(self) -> DictCfgVariableType:
		return DictCfgVariableType(self._instance.DictConfig)
	@property
	def distbf_tts(self) -> int:
		return self._instance.DistbfTts
	@property
	def distbf_ver(self) -> int:
		return self._instance.DistbfVer
	@property
	def dmaurst(self) -> bool:
		return self._instance.Dmaurst
	@property
	def dmsw_cfg(self) -> DmswCfgVariableType:
		return DmswCfgVariableType(self._instance.DmswCfg)
	@property
	def docviewer(self) -> DocviewerVariableType:
		return DocviewerVariableType(self._instance.Docviewer)
	@property
	def drc_cfg(self) -> DrcCfgVariableType:
		return DrcCfgVariableType(self._instance.DrcCfg)
	@property
	def dsbl_fault(self) -> DsblFaultVariableType:
		return DsblFaultVariableType(self._instance.DsblFault)
	@property
	def dsbl_gpmsk(self) -> int:
		return self._instance.DsblGpmsk
	@property
	def dtdiag(self) -> DtrecVariableType:
		return DtrecVariableType(self._instance.Dtdiag)
	@property
	def dtrecp(self) -> DtrecVariableType:
		return DtrecVariableType(self._instance.Dtrecp)
	@property
	def dump_option(self) -> int:
		return self._instance.DumpOption
	@property
	def dutr_cfg(self) -> int:
		return self._instance.DutrCfg
	@property
	def dutr_cpmes(self) -> int:
		return self._instance.DutrCpmes
	@property
	def duty_temp(self) -> float:
		return self._instance.DutyTemp
	@property
	def duty_unit(self) -> int:
		return self._instance.DutyUnit
	@property
	def dyn_brk(self) -> DynBrkVariableType:
		return DynBrkVariableType(self._instance.DynBrk)
	@property
	def editor_optn(self) -> int:
		return self._instance.EditorOptn
	@property
	def edit_recent(self) -> typing.List[EdtRecentVariableType]:
		return [EdtRecentVariableType(x) for x in self._instance.EditRecent]
	@property
	def emgdi_stat(self) -> int:
		return self._instance.EmgdiStat
	@property
	def enc_info(self) -> typing.List[EncInfoVariableType]:
		return [EncInfoVariableType(x) for x in self._instance.EncInfo]
	@property
	def enetmode(self) -> typing.List[EnetmodeVariableType]:
		return [EnetmodeVariableType(x) for x in self._instance.Enetmode]
	@property
	def eoatcfg(self) -> EoatcfgVariableType:
		return EoatcfgVariableType(self._instance.Eoatcfg)
	@property
	def eoatdata(self) -> typing.List[EoatdataVariableType]:
		return [EoatdataVariableType(x) for x in self._instance.Eoatdata]
	@property
	def erpost_log(self) -> ErpostLogVariableType:
		return ErpostLogVariableType(self._instance.ErpostLog)
	@property
	def error_prog(self) -> str:
		return self._instance.ErrorProg
	@property
	def error_table(self) -> typing.List[int]:
		return self._instance.ErrorTable
	@property
	def errsev_num(self) -> int:
		return self._instance.ErrsevNum
	@property
	def er_auto_enb(self) -> bool:
		return self._instance.ErAutoEnb
	@property
	def er_noauto(self) -> ErNoautoVariableType:
		return ErNoautoVariableType(self._instance.ErNoauto)
	@property
	def er_nofltr(self) -> bool:
		return self._instance.ErNofltr
	@property
	def er_nohis(self) -> int:
		return self._instance.ErNohis
	@property
	def er_no_alm(self) -> typing.List[ErNoalmVariableType]:
		return [ErNoalmVariableType(x) for x in self._instance.ErNoAlm]
	@property
	def er_sev_noau(self) -> typing.List[bool]:
		return self._instance.ErSevNoau
	@property
	def etcp_ver(self) -> str:
		return self._instance.EtcpVer
	@property
	def extlog_req(self) -> int:
		return self._instance.ExtlogReq
	@property
	def extlog_siz(self) -> int:
		return self._instance.ExtlogSiz
	@property
	def extstksiz(self) -> int:
		return self._instance.Extstksiz
	@property
	def exttol(self) -> float:
		return self._instance.Exttol
	@property
	def ext_bwd_sel(self) -> bool:
		return self._instance.ExtBwdSel
	@property
	def ext_di_bwd(self) -> ExtSetVariableType:
		return ExtSetVariableType(self._instance.ExtDiBwd)
	@property
	def ext_di_step(self) -> ExtSetVariableType:
		return ExtSetVariableType(self._instance.ExtDiStep)
	@property
	def e_stop_do(self) -> int:
		return self._instance.EStopDo
	@property
	def factory_tun(self) -> int:
		return self._instance.FactoryTun
	@property
	def fdr_grp(self) -> typing.List[FdrGrpVariableType]:
		return [FdrGrpVariableType(x) for x in self._instance.FdrGrp]
	@property
	def feature(self) -> FeatureVariableType:
		return FeatureVariableType(self._instance.Feature)
	@property
	def feat_add(self) -> typing.List[str]:
		return self._instance.FeatAdd
	@property
	def feat_demo(self) -> FeatureVariableType:
		return FeatureVariableType(self._instance.FeatDemo)
	@property
	def feat_demoin(self) -> int:
		return self._instance.FeatDemoin
	@property
	def feat_index(self) -> int:
		return self._instance.FeatIndex
	@property
	def filecomp(self) -> FilecompVariableType:
		return FilecompVariableType(self._instance.Filecomp)
	@property
	def filesetup2(self) -> FileSetup2VariableType:
		return FileSetup2VariableType(self._instance.Filesetup2)
	@property
	def file_ap2bck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileAp2bck]
	@property
	def file_appbck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileAppbck]
	@property
	def file_dgbck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileDgbck]
	@property
	def file_frsprt(self) -> bool:
		return self._instance.FileFrsprt
	@property
	def file_visbck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileVisbck]
	@property
	def flui_config(self) -> FluiCfgVariableType:
		return FluiCfgVariableType(self._instance.FluiConfig)
	@property
	def flui_data(self) -> FluiDataVariableType:
		return FluiDataVariableType(self._instance.FluiData)
	@property
	def flui_result(self) -> typing.List[FluiResVariableType]:
		return [FluiResVariableType(x) for x in self._instance.FluiResult]
	@property
	def fmr_cfg(self) -> FmrCfgVariableType:
		return FmrCfgVariableType(self._instance.FmrCfg)
	@property
	def fno(self) -> str:
		return self._instance.Fno
	@property
	def frm_chktyp(self) -> int:
		return self._instance.FrmChktyp
	@property
	def fromchk_min(self) -> int:
		return self._instance.FromchkMin
	@property
	def fssb_cfg(self) -> FssbCfgVariableType:
		return FssbCfgVariableType(self._instance.FssbCfg)
	@property
	def ftp_def_ow(self) -> bool:
		return self._instance.FtpDefOw
	@property
	def ftp_dircomp(self) -> bool:
		return self._instance.FtpDircomp
	@property
	def genov_enb(self) -> bool:
		return self._instance.GenovEnb
	@property
	def gravc_grp(self) -> typing.List[GravcGrpVariableType]:
		return [GravcGrpVariableType(x) for x in self._instance.GravcGrp]
	@property
	def grsmt_grp(self) -> typing.List[GrsmtGrpVariableType]:
		return [GrsmtGrpVariableType(x) for x in self._instance.GrsmtGrp]
	@property
	def hostc_cfg(self) -> typing.List[HostCfgVariableType]:
		return [HostCfgVariableType(x) for x in self._instance.HostcCfg]
	@property
	def hostent(self) -> typing.List[HostentVariableType]:
		return [HostentVariableType(x) for x in self._instance.Hostent]
	@property
	def hostname(self) -> str:
		return self._instance.Hostname
	@property
	def hosts_cfg(self) -> typing.List[HostCfgVariableType]:
		return [HostCfgVariableType(x) for x in self._instance.HostsCfg]
	@property
	def host_err(self) -> ErrMaskVariableType:
		return ErrMaskVariableType(self._instance.HostErr)
	@property
	def host_pdusiz(self) -> int:
		return self._instance.HostPdusiz
	@property
	def hscdmngrp(self) -> typing.List[HscdMngVariableType]:
		return [HscdMngVariableType(x) for x in self._instance.Hscdmngrp]
	@property
	def hscd_qupd(self) -> bool:
		return self._instance.HscdQupd
	@property
	def hscd_updtyp(self) -> int:
		return self._instance.HscdUpdtyp
	@property
	def http_auth(self) -> typing.List[HttpAuthVariableType]:
		return [HttpAuthVariableType(x) for x in self._instance.HttpAuth]
	@property
	def http_ctrl(self) -> HttpVariableType:
		return HttpVariableType(self._instance.HttpCtrl)
	@property
	def hwr_config(self) -> HwrConfigVariableType:
		return HwrConfigVariableType(self._instance.HwrConfig)
	@property
	def idl_cpu_pct(self) -> float:
		return self._instance.IdlCpuPct
	@property
	def idl_min_pct(self) -> float:
		return self._instance.IdlMinPct
	@property
	def ignr_ioerr(self) -> int:
		return self._instance.IgnrIoerr
	@property
	def inpt_sim_do(self) -> int:
		return self._instance.InptSimDo
	@property
	def instal_scrn(self) -> int:
		return self._instance.InstalScrn
	@property
	def intpmodntol(self) -> int:
		return self._instance.Intpmodntol
	@property
	def intp_prty(self) -> int:
		return self._instance.IntpPrty
	@property
	def invistp_enb(self) -> int:
		return self._instance.InvistpEnb
	@property
	def iolnk(self) -> typing.List[IolnkVariableType]:
		return [IolnkVariableType(x) for x in self._instance.Iolnk]
	@property
	def iomaster(self) -> bool:
		return self._instance.Iomaster
	@property
	def ioslave(self) -> IoslaveVariableType:
		return IoslaveVariableType(self._instance.Ioslave)
	@property
	def iosramcache(self) -> bool:
		return self._instance.Iosramcache
	@property
	def io_auto_cfg(self) -> bool:
		return self._instance.IoAutoCfg
	@property
	def io_auto_uop(self) -> bool:
		return self._instance.IoAutoUop
	@property
	def io_cmt_opt(self) -> int:
		return self._instance.IoCmtOpt
	@property
	def io_cycle(self) -> bool:
		return self._instance.IoCycle
	@property
	def io_def_asg(self) -> typing.List[IoDefAsgVariableType]:
		return [IoDefAsgVariableType(x) for x in self._instance.IoDefAsg]
	@property
	def io_def_num(self) -> int:
		return self._instance.IoDefNum
	@property
	def io_ipche(self) -> bool:
		return self._instance.IoIpche
	@property
	def io_rtry_cnt(self) -> int:
		return self._instance.IoRtryCnt
	@property
	def io_scrn_upd(self) -> int:
		return self._instance.IoScrnUpd
	@property
	def io_uop_cfg(self) -> IoUopCfgVariableType:
		return IoUopCfgVariableType(self._instance.IoUopCfg)
	@property
	def irca_acc(self) -> typing.List[ItemAccVariableType]:
		return [ItemAccVariableType(x) for x in self._instance.IrcaAcc]
	@property
	def irca_buf001(self) -> typing.List[ItemBuffElVariableType]:
		return [ItemBuffElVariableType(x) for x in self._instance.IrcaBuf001]
	@property
	def irca_buf002(self) -> typing.List[ItemBuffElVariableType]:
		return [ItemBuffElVariableType(x) for x in self._instance.IrcaBuf002]
	@property
	def irca_buf003(self) -> typing.List[ItemBuffElVariableType]:
		return [ItemBuffElVariableType(x) for x in self._instance.IrcaBuf003]
	@property
	def irca_cfg(self) -> typing.List[IrcaCnfVariableType]:
		return [IrcaCnfVariableType(x) for x in self._instance.IrcaCfg]
	@property
	def irca_his001(self) -> typing.List[HistDayVariableType]:
		return [HistDayVariableType(x) for x in self._instance.IrcaHis001]
	@property
	def irca_his002(self) -> typing.List[HistDayVariableType]:
		return [HistDayVariableType(x) for x in self._instance.IrcaHis002]
	@property
	def irca_his003(self) -> typing.List[HistDayVariableType]:
		return [HistDayVariableType(x) for x in self._instance.IrcaHis003]
	@property
	def irca_i_cfg(self) -> typing.List[ItemNameVariableType]:
		return [ItemNameVariableType(x) for x in self._instance.IrcaICfg]
	@property
	def irprog_cfg(self) -> IrprogCfgVariableType:
		return IrprogCfgVariableType(self._instance.IrprogCfg)
	@property
	def isdt_isolc(self) -> typing.List[int]:
		return self._instance.IsdtIsolc
	@property
	def j23_dsp_enb(self) -> bool:
		return self._instance.J23DspEnb
	@property
	def jinc(self) -> JincVariableType:
		return JincVariableType(self._instance.Jinc)
	@property
	def jobproc_enb(self) -> int:
		return self._instance.JobprocEnb
	@property
	def jog_in_auto(self) -> int:
		return self._instance.JogInAuto
	@property
	def jposrec_enb(self) -> int:
		return self._instance.JposrecEnb
	@property
	def kanji_mask(self) -> int:
		return self._instance.KanjiMask
	@property
	def karelmon(self) -> KarelmonVariableType:
		return KarelmonVariableType(self._instance.Karelmon)
	@property
	def karel_cfg(self) -> KarelCfgVariableType:
		return KarelCfgVariableType(self._instance.KarelCfg)
	@property
	def karel_enb(self) -> int:
		return self._instance.KarelEnb
	@property
	def kcl_lin_num(self) -> bool:
		return self._instance.KclLinNum
	@property
	def keylogging(self) -> int:
		return self._instance.Keylogging
	@property
	def language(self) -> str:
		return self._instance.Language
	@property
	def lgcfg(self) -> LgcfgVariableType:
		return LgcfgVariableType(self._instance.Lgcfg)
	@property
	def ln_disp(self) -> LnDispVariableType:
		return LnDispVariableType(self._instance.LnDisp)
	@property
	def loctol(self) -> float:
		return self._instance.Loctol
	@property
	def logbook(self) -> LogbookVariableType:
		return LogbookVariableType(self._instance.Logbook)
	@property
	def log_buff(self) -> typing.List[LogBuffVariableType]:
		return [LogBuffVariableType(x) for x in self._instance.LogBuff]
	@property
	def log_dcs(self) -> LogDcsVariableType:
		return LogDcsVariableType(self._instance.LogDcs)
	@property
	def log_dio(self) -> typing.List[LogDioVariableType]:
		return [LogDioVariableType(x) for x in self._instance.LogDio]
	@property
	def log_er_itm(self) -> typing.List[int]:
		return self._instance.LogErItm
	@property
	def log_er_sev(self) -> int:
		return self._instance.LogErSev
	@property
	def log_er_typ(self) -> typing.List[int]:
		return self._instance.LogErTyp
	@property
	def log_rec_rst(self) -> bool:
		return self._instance.LogRecRst
	@property
	def log_scrn_fl(self) -> typing.List[LogScrnFlVariableType]:
		return [LogScrnFlVariableType(x) for x in self._instance.LogScrnFl]
	@property
	def log_tpkey(self) -> typing.List[int]:
		return self._instance.LogTpkey
	@property
	def longnam_enb(self) -> bool:
		return self._instance.LongnamEnb
	@property
	def lups_digit(self) -> int:
		return self._instance.LupsDigit
	@property
	def lu_loadprog(self) -> str:
		return self._instance.LuLoadprog
	@property
	def maxualrmnum(self) -> int:
		return self._instance.Maxualrmnum
	@property
	def max_dig_prt(self) -> int:
		return self._instance.MaxDigPrt
	@property
	def mcsp(self) -> McspVariableType:
		return McspVariableType(self._instance.Mcsp)
	@property
	def mcsp_grp(self) -> typing.List[McspGrpVariableType]:
		return [McspGrpVariableType(x) for x in self._instance.McspGrp]
	@property
	def md_ldxdisab(self) -> int:
		return self._instance.MdLdxdisab
	@property
	def memo_apname(self) -> typing.List[str]:
		return self._instance.MemoApname
	@property
	def mfrq_cfg(self) -> MfrqCfgVariableType:
		return MfrqCfgVariableType(self._instance.MfrqCfg)
	@property
	def mfrq_grp(self) -> typing.List[MfrqGrpVariableType]:
		return [MfrqGrpVariableType(x) for x in self._instance.MfrqGrp]
	@property
	def misc_mstr(self) -> MiscMstrVariableType:
		return MiscMstrVariableType(self._instance.MiscMstr)
	@property
	def misc_scd(self) -> typing.List[MiscScdVariableType]:
		return [MiscScdVariableType(x) for x in self._instance.MiscScd]
	@property
	def mkcfg(self) -> MkcfgVariableType:
		return MkcfgVariableType(self._instance.Mkcfg)
	@property
	def mltarm_cfg(self) -> MltarmCfgVariableType:
		return MltarmCfgVariableType(self._instance.MltarmCfg)
	@property
	def mmetpu(self) -> int:
		return self._instance.Mmetpu
	@property
	def mndsp_adcol(self) -> int:
		return self._instance.MndspAdcol
	@property
	def mndsp_cmnt(self) -> int:
		return self._instance.MndspCmnt
	@property
	def mndsp_fncmn(self) -> int:
		return self._instance.MndspFncmn
	@property
	def mndsp_fstli(self) -> int:
		return self._instance.MndspFstli
	@property
	def mndsp_mst(self) -> MndspMstVariableType:
		return MndspMstVariableType(self._instance.MndspMst)
	@property
	def mndsp_poscf(self) -> int:
		return self._instance.MndspPoscf
	@property
	def mndsp_prpmt(self) -> int:
		return self._instance.MndspPrpmt
	@property
	def mndsp_pstol(self) -> typing.List[MndsppstlVariableType]:
		return [MndsppstlVariableType(x) for x in self._instance.MndspPstol]
	@property
	def mnsing_chk(self) -> bool:
		return self._instance.MnsingChk
	@property
	def modaq_cfg(self) -> ModaqCfgVariableType:
		return ModaqCfgVariableType(self._instance.ModaqCfg)
	@property
	def modaq_dev(self) -> str:
		return self._instance.ModaqDev
	@property
	def modaq_hsize(self) -> int:
		return self._instance.ModaqHsize
	@property
	def modaq_task(self) -> str:
		return self._instance.ModaqTask
	@property
	def modaq_trig(self) -> typing.List[FxTriggerVariableType]:
		return [FxTriggerVariableType(x) for x in self._instance.ModaqTrig]
	@property
	def modaq_type(self) -> int:
		return self._instance.ModaqType
	@property
	def modem_inf(self) -> typing.List[ModemInfVariableType]:
		return [ModemInfVariableType(x) for x in self._instance.ModemInf]
	@property
	def monitor_msg(self) -> typing.List[str]:
		return self._instance.MonitorMsg
	@property
	def mor_grp_sv(self) -> typing.List[MorGrpSvVariableType]:
		return [MorGrpSvVariableType(x) for x in self._instance.MorGrpSv]
	@property
	def motion_dbg(self) -> MotionDbgVariableType:
		return MotionDbgVariableType(self._instance.MotionDbg)
	@property
	def mpl_name(self) -> str:
		return self._instance.MplName
	@property
	def mr_hist(self) -> typing.List[MrHistVariableType]:
		return [MrHistVariableType(x) for x in self._instance.MrHist]
	@property
	def mskcfmap(self) -> typing.List[int]:
		return self._instance.Mskcfmap
	@property
	def mskconrel(self) -> int:
		return self._instance.Mskconrel
	@property
	def mskexcfenb(self) -> int:
		return self._instance.Mskexcfenb
	@property
	def mskexcffnc(self) -> int:
		return self._instance.Mskexcffnc
	@property
	def mskjogovlim(self) -> int:
		return self._instance.Mskjogovlim
	@property
	def mskkey(self) -> int:
		return self._instance.Mskkey
	@property
	def mskkey_panl(self) -> int:
		return self._instance.MskkeyPanl
	@property
	def mskrunovlim(self) -> int:
		return self._instance.Mskrunovlim
	@property
	def msksfspdtyp(self) -> int:
		return self._instance.Msksfspdtyp
	@property
	def msksign(self) -> int:
		return self._instance.Msksign
	@property
	def mskt1motlim(self) -> int:
		return self._instance.Mskt1motlim
	@property
	def msk_ce_grp(self) -> typing.List[MskCeGrpVariableType]:
		return [MskCeGrpVariableType(x) for x in self._instance.MskCeGrp]
	@property
	def msqz_edit(self) -> int:
		return self._instance.MsqzEdit
	@property
	def mtcom_cfg(self) -> typing.List[MtcomCfgVariableType]:
		return [MtcomCfgVariableType(x) for x in self._instance.MtcomCfg]
	@property
	def mt_arc_enb(self) -> bool:
		return self._instance.MtArcEnb
	@property
	def mt_mn_mode(self) -> int:
		return self._instance.MtMnMode
	@property
	def mt_spl_enb(self) -> bool:
		return self._instance.MtSplEnb
	@property
	def muap_cplenb(self) -> bool:
		return self._instance.MuapCplenb
	@property
	def nocheck(self) -> typing.List[str]:
		return self._instance.Nocheck
	@property
	def no_wait_ln(self) -> int:
		return self._instance.NoWaitLn
	@property
	def num_rspace(self) -> typing.List[int]:
		return self._instance.NumRspace
	@property
	def odrdsp_enb(self) -> int:
		return self._instance.OdrdspEnb
	@property
	def offset_cart(self) -> bool:
		return self._instance.OffsetCart
	@property
	def offset_dis(self) -> bool:
		return self._instance.OffsetDis
	@property
	def ofs_at_mark(self) -> int:
		return self._instance.OfsAtMark
	@property
	def open_files(self) -> int:
		return self._instance.OpenFiles
	@property
	def option_io(self) -> int:
		return self._instance.OptionIo
	@property
	def optm_prg(self) -> str:
		return self._instance.OptmPrg
	@property
	def opwork(self) -> OpworkVariableType:
		return OpworkVariableType(self._instance.Opwork)
	@property
	def org_dsbl(self) -> typing.List[int]:
		return self._instance.OrgDsbl
	@property
	def orienttol(self) -> float:
		return self._instance.Orienttol
	@property
	def out_sim_do(self) -> int:
		return self._instance.OutSimDo
	@property
	def ovrdslct(self) -> OvrdslctVariableType:
		return OvrdslctVariableType(self._instance.Ovrdslct)
	@property
	def ovrd_pexe(self) -> bool:
		return self._instance.OvrdPexe
	@property
	def ovrd_rate(self) -> int:
		return self._instance.OvrdRate
	@property
	def ovrd_setup(self) -> OvrdSetupVariableType:
		return OvrdSetupVariableType(self._instance.OvrdSetup)
	@property
	def palcfg(self) -> PlcfgVariableType:
		return PlcfgVariableType(self._instance.Palcfg)
	@property
	def pal_pos_chk(self) -> bool:
		return self._instance.PalPosChk
	@property
	def param_menu(self) -> typing.List[str]:
		return self._instance.ParamMenu
	@property
	def pause_prog(self) -> str:
		return self._instance.PauseProg
	@property
	def pccrt(self) -> int:
		return self._instance.Pccrt
	@property
	def pccrt_host(self) -> str:
		return self._instance.PccrtHost
	@property
	def pctp(self) -> int:
		return self._instance.Pctp
	@property
	def pctp_host(self) -> str:
		return self._instance.PctpHost
	@property
	def pc_timeout(self) -> int:
		return self._instance.PcTimeout
	@property
	def pgdebug(self) -> int:
		return self._instance.Pgdebug
	@property
	def pginp_flmsk(self) -> int:
		return self._instance.PginpFlmsk
	@property
	def pginp_fltr(self) -> int:
		return self._instance.PginpFltr
	@property
	def pginp_pgatr(self) -> typing.List[int]:
		return self._instance.PginpPgatr
	@property
	def pginp_pgchk(self) -> int:
		return self._instance.PginpPgchk
	@property
	def pginp_type(self) -> typing.List[str]:
		return self._instance.PginpType
	@property
	def pginp_word(self) -> typing.List[str]:
		return self._instance.PginpWord
	@property
	def pglog(self) -> int:
		return self._instance.Pglog
	@property
	def pgtracectl(self) -> typing.List[TracectlVariableType]:
		return [TracectlVariableType(x) for x in self._instance.Pgtracectl]
	@property
	def pgtracedt(self) -> typing.List[TracedtVariableType]:
		return [TracedtVariableType(x) for x in self._instance.Pgtracedt]
	@property
	def pgtracelen(self) -> int:
		return self._instance.Pgtracelen
	@property
	def pgtrace_up(self) -> TraceupVariableType:
		return TraceupVariableType(self._instance.PgtraceUp)
	@property
	def pg_cfg(self) -> PgCfgVariableType:
		return PgCfgVariableType(self._instance.PgCfg)
	@property
	def pg_defspd(self) -> PgDefspdVariableType:
		return PgDefspdVariableType(self._instance.PgDefspd)
	@property
	def ping_ctrl(self) -> PingVariableType:
		return PingVariableType(self._instance.PingCtrl)
	@property
	def pipe_config(self) -> PipeCfgVariableType:
		return PipeCfgVariableType(self._instance.PipeConfig)
	@property
	def plid_cfg(self) -> PlidCfgVariableType:
		return PlidCfgVariableType(self._instance.PlidCfg)
	@property
	def plid_cllb(self) -> typing.List[PlidCllbVariableType]:
		return [PlidCllbVariableType(x) for x in self._instance.PlidCllb]
	@property
	def plid_know_m(self) -> bool:
		return self._instance.PlidKnowM
	@property
	def plim_grp(self) -> typing.List[PlimGrpVariableType]:
		return [PlimGrpVariableType(x) for x in self._instance.PlimGrp]
	@property
	def plmr_grp(self) -> typing.List[PlmrGrpVariableType]:
		return [PlmrGrpVariableType(x) for x in self._instance.PlmrGrp]
	@property
	def ploadbanfwd(self) -> bool:
		return self._instance.Ploadbanfwd
	@property
	def plst_grp6(self) -> typing.List[PlstGrpVariableType]:
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp6]
	@property
	def plst_grp7(self) -> typing.List[PlstGrpVariableType]:
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp7]
	@property
	def plst_grp8(self) -> typing.List[PlstGrpVariableType]:
		return [PlstGrpVariableType(x) for x in self._instance.PlstGrp8]
	@property
	def plst_ovld(self) -> typing.List[bool]:
		return self._instance.PlstOvld
	@property
	def pls_cmp_lim(self) -> int:
		return self._instance.PlsCmpLim
	@property
	def pls_er_chk(self) -> int:
		return self._instance.PlsErChk
	@property
	def pls_er_lim(self) -> int:
		return self._instance.PlsErLim
	@property
	def pls_er_rst(self) -> bool:
		return self._instance.PlsErRst
	@property
	def pl_mod(self) -> bool:
		return self._instance.PlMod
	@property
	def pl_mod_st(self) -> bool:
		return self._instance.PlModSt
	@property
	def pl_res_g1(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG1]
	@property
	def pl_res_g2(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG2]
	@property
	def pl_res_g3(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG3]
	@property
	def pl_res_g4(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG4]
	@property
	def pl_res_g5(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG5]
	@property
	def pl_res_g6(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG6]
	@property
	def pl_res_g7(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG7]
	@property
	def pl_res_g8(self) -> typing.List[PlResGVariableType]:
		return [PlResGVariableType(x) for x in self._instance.PlResG8]
	@property
	def pl_thr_inrt(self) -> int:
		return self._instance.PlThrInrt
	@property
	def pl_thr_mass(self) -> int:
		return self._instance.PlThrMass
	@property
	def pl_thr_mmnt(self) -> int:
		return self._instance.PlThrMmnt
	@property
	def pmon_queue(self) -> PmonQueVariableType:
		return PmonQueVariableType(self._instance.PmonQueue)
	@property
	def pns_cur_lin(self) -> int:
		return self._instance.PnsCurLin
	@property
	def pns_end_cur(self) -> bool:
		return self._instance.PnsEndCur
	@property
	def pns_end_exe(self) -> bool:
		return self._instance.PnsEndExe
	@property
	def pns_number(self) -> int:
		return self._instance.PnsNumber
	@property
	def pns_option(self) -> int:
		return self._instance.PnsOption
	@property
	def pns_program(self) -> str:
		return self._instance.PnsProgram
	@property
	def pns_task_id(self) -> int:
		return self._instance.PnsTaskId
	@property
	def pocfg(self) -> PocfgVariableType:
		return PocfgVariableType(self._instance.Pocfg)
	@property
	def pos_edit(self) -> PosEditVariableType:
		return PosEditVariableType(self._instance.PosEdit)
	@property
	def prgadj(self) -> PrgadjVariableType:
		return PrgadjVariableType(self._instance.Prgadj)
	@property
	def prgns_cfg(self) -> PrgnsCfgVariableType:
		return PrgnsCfgVariableType(self._instance.PrgnsCfg)
	@property
	def prgns_grp(self) -> typing.List[PrgnsGrpVariableType]:
		return [PrgnsGrpVariableType(x) for x in self._instance.PrgnsGrp]
	@property
	def prgns_pref(self) -> PrgnsPrefVariableType:
		return PrgnsPrefVariableType(self._instance.PrgnsPref)
	@property
	def priority(self) -> int:
		return self._instance.Priority
	@property
	def product_id(self) -> str:
		return self._instance.ProductId
	@property
	def proggrp_tgl(self) -> int:
		return self._instance.ProggrpTgl
	@property
	def prohibit_do(self) -> bool:
		return self._instance.ProhibitDo
	@property
	def protoent(self) -> typing.List[ProtoentVariableType]:
		return [ProtoentVariableType(x) for x in self._instance.Protoent]
	@property
	def proxy_cfg(self) -> ProxyCfgVariableType:
		return ProxyCfgVariableType(self._instance.ProxyCfg)
	@property
	def pro_cfg(self) -> PfCfgVariableType:
		return PfCfgVariableType(self._instance.ProCfg)
	@property
	def pro_enhance(self) -> PfEnhanceVariableType:
		return PfEnhanceVariableType(self._instance.ProEnhance)
	@property
	def pro_pref(self) -> PfPrefVariableType:
		return PfPrefVariableType(self._instance.ProPref)
	@property
	def prport_num(self) -> int:
		return self._instance.PrportNum
	@property
	def pr_cartrep(self) -> bool:
		return self._instance.PrCartrep
	@property
	def pskstat(self) -> int:
		return self._instance.Pskstat
	@property
	def pslgset(self) -> PslgsetVariableType:
		return PslgsetVariableType(self._instance.Pslgset)
	@property
	def pslgtemp(self) -> PslgtempVariableType:
		return PslgtempVariableType(self._instance.Pslgtemp)
	@property
	def pslgversion(self) -> str:
		return self._instance.Pslgversion
	@property
	def pssave(self) -> PssaveVariableType:
		return PssaveVariableType(self._instance.Pssave)
	@property
	def purge_enbl(self) -> bool:
		return self._instance.PurgeEnbl
	@property
	def pwf_io(self) -> int:
		return self._instance.PwfIo
	@property
	def pwrup_delay(self) -> PwrupDlyVariableType:
		return PwrupDlyVariableType(self._instance.PwrupDelay)
	@property
	def pwr_normal(self) -> str:
		return self._instance.PwrNormal
	@property
	def pwr_semi(self) -> str:
		return self._instance.PwrSemi
	@property
	def qskip_grp(self) -> typing.List[QskipGrpVariableType]:
		return [QskipGrpVariableType(x) for x in self._instance.QskipGrp]
	@property
	def rbtif(self) -> int:
		return self._instance.Rbtif
	@property
	def rcvtmout(self) -> int:
		return self._instance.Rcvtmout
	@property
	def rdcr_grp(self) -> typing.List[RdcrGrpVariableType]:
		return [RdcrGrpVariableType(x) for x in self._instance.RdcrGrp]
	@property
	def rdio_type(self) -> typing.List[int]:
		return self._instance.RdioType
	@property
	def redprot_cfg(self) -> RedprotCfgVariableType:
		return RedprotCfgVariableType(self._instance.RedprotCfg)
	@property
	def redprot_grp(self) -> typing.List[RedprotGrpVariableType]:
		return [RedprotGrpVariableType(x) for x in self._instance.RedprotGrp]
	@property
	def refpos1(self) -> typing.List[Refpos11VariableType]:
		return [Refpos11VariableType(x) for x in self._instance.Refpos1]
	@property
	def refpos2(self) -> typing.List[Refpos21VariableType]:
		return [Refpos21VariableType(x) for x in self._instance.Refpos2]
	@property
	def refpos3(self) -> typing.List[Refpos31VariableType]:
		return [Refpos31VariableType(x) for x in self._instance.Refpos3]
	@property
	def refpos4(self) -> typing.List[Refpos41VariableType]:
		return [Refpos41VariableType(x) for x in self._instance.Refpos4]
	@property
	def refpos5(self) -> typing.List[Refpos51VariableType]:
		return [Refpos51VariableType(x) for x in self._instance.Refpos5]
	@property
	def refpos6(self) -> typing.List[Refpos61VariableType]:
		return [Refpos61VariableType(x) for x in self._instance.Refpos6]
	@property
	def refpos7(self) -> typing.List[Refpos71VariableType]:
		return [Refpos71VariableType(x) for x in self._instance.Refpos7]
	@property
	def refpos8(self) -> typing.List[Refpos81VariableType]:
		return [Refpos81VariableType(x) for x in self._instance.Refpos8]
	@property
	def refposmask(self) -> typing.List[RefpsmskVariableType]:
		return [RefpsmskVariableType(x) for x in self._instance.Refposmask]
	@property
	def refposmaxno(self) -> typing.List[int]:
		return self._instance.Refposmaxno
	@property
	def remote(self) -> int:
		return self._instance.Remote
	@property
	def remote_cfg(self) -> RemoteCfgVariableType:
		return RemoteCfgVariableType(self._instance.RemoteCfg)
	@property
	def repl_range(self) -> int:
		return self._instance.ReplRange
	@property
	def repower(self) -> RepowerVariableType:
		return RepowerVariableType(self._instance.Repower)
	@property
	def resm_dryprg(self) -> str:
		return self._instance.ResmDryprg
	@property
	def restart(self) -> RestartVariableType:
		return RestartVariableType(self._instance.Restart)
	@property
	def resume_prog(self) -> str:
		return self._instance.ResumeProg
	@property
	def re_exec_enb(self) -> bool:
		return self._instance.ReExecEnb
	@property
	def rgspd_prexe(self) -> bool:
		return self._instance.RgspdPrexe
	@property
	def rgtdb_prexe(self) -> bool:
		return self._instance.RgtdbPrexe
	@property
	def rgtrm_prexe(self) -> bool:
		return self._instance.RgtrmPrexe
	@property
	def ri_airpurge(self) -> typing.List[bool]:
		return self._instance.RiAirpurge
	@property
	def rmt_master(self) -> int:
		return self._instance.RmtMaster
	@property
	def robot_isolc(self) -> typing.List[int]:
		return self._instance.RobotIsolc
	@property
	def robot_name(self) -> str:
		return self._instance.RobotName
	@property
	def rob_categ(self) -> typing.List[int]:
		return self._instance.RobCateg
	@property
	def rob_ord_num(self) -> typing.List[str]:
		return self._instance.RobOrdNum
	@property
	def rpc_timeout(self) -> int:
		return self._instance.RpcTimeout
	@property
	def rs232_cfg(self) -> typing.List[Rs232CfgVariableType]:
		return [Rs232CfgVariableType(x) for x in self._instance.Rs232Cfg]
	@property
	def rs232_nport(self) -> int:
		return self._instance.Rs232Nport
	@property
	def rsch_log(self) -> RschVariableType:
		return RschVariableType(self._instance.RschLog)
	@property
	def rsmavailnum(self) -> int:
		return self._instance.Rsmavailnum
	@property
	def rspace1(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace1]
	@property
	def rspace2(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace2]
	@property
	def rspace3(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace3]
	@property
	def rspace4(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace4]
	@property
	def rspace5(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace5]
	@property
	def rspace6(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace6]
	@property
	def rspace7(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace7]
	@property
	def rspace8(self) -> typing.List[RspaceVariableType]:
		return [RspaceVariableType(x) for x in self._instance.Rspace8]
	@property
	def rspaceg(self) -> RspacegVariableType:
		return RspacegVariableType(self._instance.Rspaceg)
	@property
	def rspace_mode(self) -> int:
		return self._instance.RspaceMode
	@property
	def rspace_s(self) -> RspacesrVariableType:
		return RspacesrVariableType(self._instance.RspaceS)
	@property
	def rspcwork_ad(self) -> int:
		return self._instance.RspcworkAd
	@property
	def rsr(self) -> typing.List[int]:
		return self._instance.Rsr
	@property
	def rsr_intval(self) -> int:
		return self._instance.RsrIntval
	@property
	def rsr_option(self) -> int:
		return self._instance.RsrOption
	@property
	def saf_do_puls(self) -> int:
		return self._instance.SafDoPuls
	@property
	def scan_time(self) -> int:
		return self._instance.ScanTime
	@property
	def sel_default(self) -> int:
		return self._instance.SelDefault
	@property
	def sel_hotstrt(self) -> int:
		return self._instance.SelHotstrt
	@property
	def semipowerfl(self) -> bool:
		return self._instance.Semipowerfl
	@property
	def semipwfdo(self) -> int:
		return self._instance.Semipwfdo
	@property
	def servent(self) -> typing.List[ServentVariableType]:
		return [ServentVariableType(x) for x in self._instance.Servent]
	@property
	def service_kl(self) -> typing.List[str]:
		return self._instance.ServiceKl
	@property
	def service_prg(self) -> typing.List[str]:
		return self._instance.ServicePrg
	@property
	def serv_dev(self) -> str:
		return self._instance.ServDev
	@property
	def serv_mail(self) -> int:
		return self._instance.ServMail
	@property
	def serv_output(self) -> int:
		return self._instance.ServOutput
	@property
	def serv_save(self) -> int:
		return self._instance.ServSave
	@property
	def serv_type(self) -> int:
		return self._instance.ServType
	@property
	def sfzn_cfg(self) -> SfznCfgVariableType:
		return SfznCfgVariableType(self._instance.SfznCfg)
	@property
	def sfzn_grp(self) -> typing.List[SfznGrpVariableType]:
		return [SfznGrpVariableType(x) for x in self._instance.SfznGrp]
	@property
	def shell_cfg(self) -> ShellCfgVariableType:
		return ShellCfgVariableType(self._instance.ShellCfg)
	@property
	def shell_chk(self) -> typing.List[ShellChkVariableType]:
		return [ShellChkVariableType(x) for x in self._instance.ShellChk]
	@property
	def shell_comm(self) -> ShellCommVariableType:
		return ShellCommVariableType(self._instance.ShellComm)
	@property
	def shftov_enb(self) -> int:
		return self._instance.ShftovEnb
	@property
	def show_reg_ui(self) -> int:
		return self._instance.ShowRegUi
	@property
	def simiofwdlm(self) -> SimiofwdlmVariableType:
		return SimiofwdlmVariableType(self._instance.Simiofwdlm)
	@property
	def si_unit_enb(self) -> bool:
		return self._instance.SiUnitEnb
	@property
	def slc_retry(self) -> int:
		return self._instance.SlcRetry
	@property
	def smon_alias(self) -> typing.List[str]:
		return self._instance.SmonAlias
	@property
	def smon_defprog(self) -> str:
		return self._instance.SmonDefprog
	@property
	def smon_recall(self) -> typing.List[str]:
		return self._instance.SmonRecall
	@property
	def snpx_asg(self) -> typing.List[SnpxAsgVariableType]:
		return [SnpxAsgVariableType(x) for x in self._instance.SnpxAsg]
	@property
	def snpx_param(self) -> SnpxParamVariableType:
		return SnpxParamVariableType(self._instance.SnpxParam)
	@property
	def soft_kb_cfg(self) -> int:
		return self._instance.SoftKbCfg
	@property
	def sopin_sim(self) -> typing.List[int]:
		return self._instance.SopinSim
	@property
	def srvnordy_do(self) -> bool:
		return self._instance.SrvnordyDo
	@property
	def srvqstp_dsb(self) -> typing.List[int]:
		return self._instance.SrvqstpDsb
	@property
	def ssr(self) -> SsrVariableType:
		return SsrVariableType(self._instance.Ssr)
	@property
	def stop_on_err(self) -> bool:
		return self._instance.StopOnErr
	@property
	def stop_ptn(self) -> str:
		return self._instance.StopPtn
	@property
	def string_prm(self) -> bool:
		return self._instance.StringPrm
	@property
	def svdt_grp(self) -> typing.List[SvdtGrpVariableType]:
		return [SvdtGrpVariableType(x) for x in self._instance.SvdtGrp]
	@property
	def svprg_count(self) -> int:
		return self._instance.SvprgCount
	@property
	def svprg_enb(self) -> bool:
		return self._instance.SvprgEnb
	@property
	def svprm_enb(self) -> int:
		return self._instance.SvprmEnb
	@property
	def svprm_upd(self) -> typing.List[SvprmUpdVariableType]:
		return [SvprmUpdVariableType(x) for x in self._instance.SvprmUpd]
	@property
	def sv_info(self) -> typing.List[SvInfoVariableType]:
		return [SvInfoVariableType(x) for x in self._instance.SvInfo]
	@property
	def sysdebug(self) -> int:
		return self._instance.Sysdebug
	@property
	def sysdsp_pass(self) -> int:
		return self._instance.SysdspPass
	@property
	def syslog(self) -> SyslogVariableType:
		return SyslogVariableType(self._instance.Syslog)
	@property
	def syslog_mpc(self) -> SyslogVariableType:
		return SyslogVariableType(self._instance.SyslogMpc)
	@property
	def syslog_sav(self) -> SyslogSavVariableType:
		return SyslogSavVariableType(self._instance.SyslogSav)
	@property
	def system_time(self) -> typing.List[SystemTimerVariableType]:
		return [SystemTimerVariableType(x) for x in self._instance.SystemTime]
	@property
	def systskmem(self) -> typing.List[int]:
		return self._instance.Systskmem
	@property
	def t1svgunspd(self) -> int:
		return self._instance.T1svgunspd
	@property
	def t2mode_lim(self) -> T2modeLimVariableType:
		return T2modeLimVariableType(self._instance.T2modeLim)
	@property
	def t2spdlim(self) -> T2spdlimVariableType:
		return T2spdlimVariableType(self._instance.T2spdlim)
	@property
	def ta_disp_enb(self) -> bool:
		return self._instance.TaDispEnb
	@property
	def tbc2_grp(self) -> typing.List[Tbc2GrpVariableType]:
		return [Tbc2GrpVariableType(x) for x in self._instance.Tbc2Grp]
	@property
	def tbcsg_grp(self) -> typing.List[TbcsgGrpVariableType]:
		return [TbcsgGrpVariableType(x) for x in self._instance.TbcsgGrp]
	@property
	def tbj2_grp(self) -> typing.List[Tbj2GrpVariableType]:
		return [Tbj2GrpVariableType(x) for x in self._instance.Tbj2Grp]
	@property
	def tbjop_grp(self) -> typing.List[TbjopGrpVariableType]:
		return [TbjopGrpVariableType(x) for x in self._instance.TbjopGrp]
	@property
	def threstable(self) -> typing.List[TpThrTableVariableType]:
		return [TpThrTableVariableType(x) for x in self._instance.Threstable]
	@property
	def thrrditable(self) -> typing.List[TpThrTableVariableType]:
		return [TpThrTableVariableType(x) for x in self._instance.Thrrditable]
	@property
	def thrrdotable(self) -> typing.List[TpThrTableVariableType]:
		return [TpThrTableVariableType(x) for x in self._instance.Thrrdotable]
	@property
	def thrsditable(self) -> typing.List[TpThrTableVariableType]:
		return [TpThrTableVariableType(x) for x in self._instance.Thrsditable]
	@property
	def thrsitable(self) -> typing.List[TpThrTableVariableType]:
		return [TpThrTableVariableType(x) for x in self._instance.Thrsitable]
	@property
	def thrtablenum(self) -> typing.List[int]:
		return self._instance.Thrtablenum
	@property
	def thr_cfg(self) -> ThrCfgVariableType:
		return ThrCfgVariableType(self._instance.ThrCfg)
	@property
	def timebf_tts(self) -> int:
		return self._instance.TimebfTts
	@property
	def timebf_ver(self) -> int:
		return self._instance.TimebfVer
	@property
	def timer(self) -> typing.List[TimerVariableType]:
		return [TimerVariableType(x) for x in self._instance.Timer]
	@property
	def timer_num(self) -> int:
		return self._instance.TimerNum
	@property
	def tmi_chan(self) -> int:
		return self._instance.TmiChan
	@property
	def tmi_dbglvl(self) -> int:
		return self._instance.TmiDbglvl
	@property
	def tmi_etherad(self) -> typing.List[str]:
		return self._instance.TmiEtherad
	@property
	def tmi_router(self) -> str:
		return self._instance.TmiRouter
	@property
	def tmi_snmask(self) -> typing.List[str]:
		return self._instance.TmiSnmask
	@property
	def toolofs_dis(self) -> bool:
		return self._instance.ToolofsDis
	@property
	def tpe_detail(self) -> int:
		return self._instance.TpeDetail
	@property
	def tpgl_config(self) -> TpglConfVariableType:
		return TpglConfVariableType(self._instance.TpglConfig)
	@property
	def tpgl_output(self) -> TpglOutVariableType:
		return TpglOutVariableType(self._instance.TpglOutput)
	@property
	def tpoff_lim(self) -> int:
		return self._instance.TpoffLim
	@property
	def tpon_svoff(self) -> bool:
		return self._instance.TponSvoff
	@property
	def tpp_mon(self) -> TppMonVariableType:
		return TppMonVariableType(self._instance.TppMon)
	@property
	def tpstrtchk(self) -> TpstrtchkVariableType:
		return TpstrtchkVariableType(self._instance.Tpstrtchk)
	@property
	def tpvtcompat(self) -> bool:
		return self._instance.Tpvtcompat
	@property
	def tpvwvar(self) -> TpvwvarVariableType:
		return TpvwvarVariableType(self._instance.Tpvwvar)
	@property
	def tp_defprog(self) -> str:
		return self._instance.TpDefprog
	@property
	def tp_display(self) -> int:
		return self._instance.TpDisplay
	@property
	def tp_inst_msk(self) -> typing.List[int]:
		return self._instance.TpInstMsk
	@property
	def tp_inuser(self) -> bool:
		return self._instance.TpInuser
	@property
	def tp_lckuser(self) -> bool:
		return self._instance.TpLckuser
	@property
	def tp_quickmen(self) -> bool:
		return self._instance.TpQuickmen
	@property
	def tp_screen(self) -> str:
		return self._instance.TpScreen
	@property
	def tp_userscrn(self) -> str:
		return self._instance.TpUserscrn
	@property
	def tp_usestat(self) -> bool:
		return self._instance.TpUsestat
	@property
	def trace_cfg(self) -> TraceCfgVariableType:
		return TraceCfgVariableType(self._instance.TraceCfg)
	@property
	def trace_chnl(self) -> typing.List[TraceChnlVariableType]:
		return [TraceChnlVariableType(x) for x in self._instance.TraceChnl]
	@property
	def trace_item(self) -> typing.List[TraceItemVariableType]:
		return [TraceItemVariableType(x) for x in self._instance.TraceItem]
	@property
	def tscfg(self) -> TscfgVariableType:
		return TscfgVariableType(self._instance.Tscfg)
	@property
	def tsscb(self) -> typing.List[TsscbVariableType]:
		return [TsscbVariableType(x) for x in self._instance.Tsscb]
	@property
	def tutorial(self) -> TutorialVariableType:
		return TutorialVariableType(self._instance.Tutorial)
	@property
	def tv_config(self) -> TvConfigVariableType:
		return TvConfigVariableType(self._instance.TvConfig)
	@property
	def tv_output(self) -> TvOutputVariableType:
		return TvOutputVariableType(self._instance.TvOutput)
	@property
	def tx_screen(self) -> typing.List[TxscreenVariableType]:
		return [TxscreenVariableType(x) for x in self._instance.TxScreen]
	@property
	def ualrm_msg(self) -> typing.List[str]:
		return self._instance.UalrmMsg
	@property
	def ualrm_sev(self) -> typing.List[int]:
		return self._instance.UalrmSev
	@property
	def uecfg(self) -> UecfgVariableType:
		return UecfgVariableType(self._instance.Uecfg)
	@property
	def uegrp(self) -> typing.List[UegrpVariableType]:
		return [UegrpVariableType(x) for x in self._instance.Uegrp]
	@property
	def ui_bbl_note(self) -> BblNtWndVariableType:
		return BblNtWndVariableType(self._instance.UiBblNote)
	@property
	def ui_defprog(self) -> typing.List[str]:
		return self._instance.UiDefprog
	@property
	def ui_fkeydata(self) -> typing.List[UiFkeydatVariableType]:
		return [UiFkeydatVariableType(x) for x in self._instance.UiFkeydata]
	@property
	def ui_inuser(self) -> typing.List[bool]:
		return self._instance.UiInuser
	@property
	def ui_menhist(self) -> typing.List[UiMenhisVariableType]:
		return [UiMenhisVariableType(x) for x in self._instance.UiMenhist]
	@property
	def ui_panedata(self) -> typing.List[UiPanedatVariableType]:
		return [UiPanedatVariableType(x) for x in self._instance.UiPanedata]
	@property
	def ui_postype(self) -> typing.List[int]:
		return self._instance.UiPostype
	@property
	def ui_quickmen(self) -> typing.List[bool]:
		return self._instance.UiQuickmen
	@property
	def ui_restore(self) -> typing.List[UiUsrviewVariableType]:
		return [UiUsrviewVariableType(x) for x in self._instance.UiRestore]
	@property
	def ui_screen(self) -> typing.List[str]:
		return self._instance.UiScreen
	@property
	def ui_state(self) -> typing.List[int]:
		return self._instance.UiState
	@property
	def ui_userscrn(self) -> typing.List[str]:
		return self._instance.UiUserscrn
	@property
	def undo_cfg(self) -> UndoCfgVariableType:
		return UndoCfgVariableType(self._instance.UndoCfg)
	@property
	def uop_crm5(self) -> bool:
		return self._instance.UopCrm5
	@property
	def update(self) -> str:
		return self._instance.Update
	@property
	def user_info(self) -> typing.List[UserInfoVariableType]:
		return [UserInfoVariableType(x) for x in self._instance.UserInfo]
	@property
	def user_offset(self) -> UserOffstVariableType:
		return UserOffstVariableType(self._instance.UserOffset)
	@property
	def user_work(self) -> UserWorkVariableType:
		return UserWorkVariableType(self._instance.UserWork)
	@property
	def useuframe(self) -> bool:
		return self._instance.Useuframe
	@property
	def usrtol_abrt(self) -> bool:
		return self._instance.UsrtolAbrt
	@property
	def usrtol_enb(self) -> bool:
		return self._instance.UsrtolEnb
	@property
	def usrtol_grp(self) -> typing.List[UsrtolGrpVariableType]:
		return [UsrtolGrpVariableType(x) for x in self._instance.UsrtolGrp]
	@property
	def usrtol_msk(self) -> int:
		return self._instance.UsrtolMsk
	@property
	def usrtol_name(self) -> str:
		return self._instance.UsrtolName
	@property
	def usr_evnt(self) -> int:
		return self._instance.UsrEvnt
	@property
	def usr_ev_cfg(self) -> typing.List[UsrEvCfgVariableType]:
		return [UsrEvCfgVariableType(x) for x in self._instance.UsrEvCfg]
	@property
	def usr_ev_wrk(self) -> typing.List[UsrEvWrkVariableType]:
		return [UsrEvWrkVariableType(x) for x in self._instance.UsrEvWrk]
	@property
	def vars_config(self) -> VarsConfigVariableType:
		return VarsConfigVariableType(self._instance.VarsConfig)
	@property
	def vcmr_grp(self) -> typing.List[VcmrGrpVariableType]:
		return [VcmrGrpVariableType(x) for x in self._instance.VcmrGrp]
	@property
	def via_work(self) -> ViaWorkVariableType:
		return ViaWorkVariableType(self._instance.ViaWork)
	@property
	def visiontmout(self) -> int:
		return self._instance.Visiontmout
	@property
	def vision_cfg(self) -> VisionCfgVariableType:
		return VisionCfgVariableType(self._instance.VisionCfg)
	@property
	def vision_grp(self) -> typing.List[VisionGrpVariableType]:
		return [VisionGrpVariableType(x) for x in self._instance.VisionGrp]
	@property
	def vis_ge_cfg(self) -> VisGeCfgVariableType:
		return VisGeCfgVariableType(self._instance.VisGeCfg)
	@property
	def vis_logreg(self) -> VisLogregVariableType:
		return VisLogregVariableType(self._instance.VisLogreg)
	@property
	def vlexe_cfg(self) -> VlexeCfgVariableType:
		return VlexeCfgVariableType(self._instance.VlexeCfg)
	@property
	def vrtd_filter(self) -> typing.List[VrtdFiltVariableType]:
		return [VrtdFiltVariableType(x) for x in self._instance.VrtdFilter]
	@property
	def vshiftmenu(self) -> typing.List[CustommenuVariableType]:
		return [CustommenuVariableType(x) for x in self._instance.Vshiftmenu]
	@property
	def vshift_cfg(self) -> VsftCfgVariableType:
		return VsftCfgVariableType(self._instance.VshiftCfg)
	@property
	def vsmo_cfg(self) -> VsmoCfgVariableType:
		return VsmoCfgVariableType(self._instance.VsmoCfg)
	@property
	def vzdt_cfg(self) -> VzdtCfgVariableType:
		return VzdtCfgVariableType(self._instance.VzdtCfg)
	@property
	def waitrelease(self) -> bool:
		return self._instance.Waitrelease
	@property
	def waittmout(self) -> int:
		return self._instance.Waittmout
	@property
	def wait_active(self) -> bool:
		return self._instance.WaitActive
	@property
	def wait_data(self) -> WaitDataVariableType:
		return WaitDataVariableType(self._instance.WaitData)
	@property
	def wait_rdisp(self) -> bool:
		return self._instance.WaitRdisp
	@property
	def xvrcfg(self) -> XvrcfgVariableType:
		return XvrcfgVariableType(self._instance.Xvrcfg)
	@property
	def zabc_grp(self) -> typing.List[ZabcGrpVariableType]:
		return [ZabcGrpVariableType(x) for x in self._instance.ZabcGrp]
	@property
	def zdt_actvspt(self) -> ZdtActvsptVariableType:
		return ZdtActvsptVariableType(self._instance.ZdtActvspt)
	@property
	def zdt_dcschg(self) -> ZdtDcschgVariableType:
		return ZdtDcschgVariableType(self._instance.ZdtDcschg)
	@property
	def zip_cfg(self) -> ZipCfgVariableType:
		return ZipCfgVariableType(self._instance.ZipCfg)
	@property
	def zmpcf_g(self) -> typing.List[ZmpcfGrpVariableType]:
		return [ZmpcfGrpVariableType(x) for x in self._instance.ZmpcfG]
	@property
	def zmp_grp(self) -> typing.List[ZmposGrpVariableType]:
		return [ZmposGrpVariableType(x) for x in self._instance.ZmpGrp]
	@property
	def zpcfg(self) -> ZpCfgVariableType:
		return ZpCfgVariableType(self._instance.Zpcfg)
	@property
	def zp_cylinder(self) -> typing.List[ZpCylinderVariableType]:
		return [ZpCylinderVariableType(x) for x in self._instance.ZpCylinder]
	@property
	def zp_grp(self) -> typing.List[ZpGrpVariableType]:
		return [ZpGrpVariableType(x) for x in self._instance.ZpGrp]
	@property
	def zp_sphere(self) -> typing.List[ZpSphereVariableType]:
		return [ZpSphereVariableType(x) for x in self._instance.ZpSphere]
	@property
	def zzz(self) -> int:
		return self._instance.Zzz
