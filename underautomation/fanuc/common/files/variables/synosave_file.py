from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.aavm_grp_variable_type import AavmGrpVariableType
from underautomation.fanuc.common.files.variables.dbwork_variable_type import DbworkVariableType
from underautomation.fanuc.common.files.variables.dhcp_int_variable_type import DhcpIntVariableType
from underautomation.fanuc.common.files.variables.fileconfig_variable_type import FileconfigVariableType
from underautomation.fanuc.common.files.variables.file_setup_variable_type import FileSetupVariableType
from underautomation.fanuc.common.files.variables.file_back_variable_type import FileBackVariableType
from underautomation.fanuc.common.files.variables.glofatt_variable_type import GlofattVariableType
from underautomation.fanuc.common.files.variables.glofset_variable_type import GlofsetVariableType
from underautomation.fanuc.common.joint_position_variable import JointPositionVariable
from underautomation.fanuc.common.files.variables.memo_memo_variable_type import MemoMemoVariableType
from underautomation.fanuc.common.files.variables.moptimiz_variable_type import MoptimizVariableType
from underautomation.fanuc.common.files.variables.optstate_variable_type import OptstateVariableType
from underautomation.fanuc.common.files.variables.pgmaxspd_variable_type import PgmaxspdVariableType
from underautomation.fanuc.common.files.variables.prgadj_sch_variable_type import PrgadjSchVariableType
from underautomation.fanuc.common.files.variables.shell_wrk_variable_type import ShellWrkVariableType
from underautomation.fanuc.common.files.variables.smh_made_variable_type import SmhMadeVariableType
from underautomation.fanuc.common.files.variables.sscbk_variable_type import SscbkVariableType
from underautomation.fanuc.common.files.variables.sys_time_variable_type import SysTimeVariableType
from underautomation.fanuc.common.files.variables.tp_curscrn_variable_type import TpCurscrnVariableType
from underautomation.fanuc.common.files.variables.tx_variable_type import TxVariableType
from underautomation.fanuc.common.files.variables.txram_variable_type import TxramVariableType
from underautomation.fanuc.common.files.variables.ui_fctnfav_variable_type import UiFctnfavVariableType
from underautomation.fanuc.common.files.variables.ui_panelnk_variable_type import UiPanelnkVariableType
from underautomation.fanuc.common.files.variables.umr_variable_type import UmrVariableType
from underautomation.fanuc.common.files.variables.vcrsm_cfg_variable_type import VcrsmCfgVariableType
from underautomation.fanuc.common.files.variables.vcwm_cfg_variable_type import VcwmCfgVariableType
from underautomation.fanuc.common.files.variables.vcwm_grp_variable_type import VcwmGrpVariableType
from underautomation.fanuc.common.files.variables.vsmo_tmp_variable_type import VsmoTmpVariableType
from underautomation.fanuc.common.files.variables.vsmo_val_variable_type import VsmoValVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SynosaveFile as synosave_file

class SynosaveFile(GenericVariableFile):
	'''Describes the Fanuc variable file synosave.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = synosave_file()
		else:
			self._instance = _internal

	@property
	def aavm_grp(self) -> typing.List[AavmGrpVariableType]:
		'''Value of variable $AAVM_GRP'''
		__r = self._instance.AavmGrp
		return None if __r is None else [None if x is None else AavmGrpVariableType(x) for x in __r]

	@property
	def aimage_back(self) -> int:
		'''Value of variable $AIMAGE_BACK'''
		return self._instance.AimageBack

	@property
	def autoupdt_st(self) -> int:
		'''Value of variable $AUTOUPDT_ST'''
		return self._instance.AutoupdtSt

	@property
	def blt(self) -> int:
		'''Value of variable $BLT'''
		return self._instance.Blt

	@property
	def daq_gfd_use(self) -> int:
		'''Value of variable $DAQ_GFD_USE'''
		return self._instance.DaqGfdUse

	@property
	def dbwork(self) -> typing.List[DbworkVariableType]:
		'''Value of variable $DBWORK'''
		__r = self._instance.Dbwork
		return None if __r is None else [None if x is None else DbworkVariableType(x) for x in __r]

	@property
	def device(self) -> str:
		'''Value of variable $DEVICE'''
		return self._instance.Device

	@property
	def dfmtn0_no(self) -> int:
		'''Value of variable $DFMTN0_NO'''
		return self._instance.Dfmtn0No

	@property
	def dhcp_int(self) -> typing.List[DhcpIntVariableType]:
		'''Value of variable $DHCP_INT'''
		__r = self._instance.DhcpInt
		return None if __r is None else [None if x is None else DhcpIntVariableType(x) for x in __r]

	@property
	def distbf_data(self) -> int:
		'''Value of variable $DISTBF_DATA'''
		return self._instance.DistbfData

	@property
	def fast_clock(self) -> int:
		'''Value of variable $FAST_CLOCK'''
		return self._instance.FastClock

	@property
	def fileconfig(self) -> FileconfigVariableType:
		'''Value of variable $FILECONFIG'''
		__r = self._instance.Fileconfig
		return None if __r is None else FileconfigVariableType(__r)

	@property
	def filesetup(self) -> FileSetupVariableType:
		'''Value of variable $FILESETUP'''
		__r = self._instance.Filesetup
		return None if __r is None else FileSetupVariableType(__r)

	@property
	def file_basept(self) -> int:
		'''Value of variable $FILE_BASEPT'''
		return self._instance.FileBasept

	@property
	def file_errbck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_ERRBCK'''
		__r = self._instance.FileErrbck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def file_maxsec(self) -> int:
		'''Value of variable $FILE_MAXSEC'''
		return self._instance.FileMaxsec

	@property
	def file_sysbck(self) -> typing.List[FileBackVariableType]:
		'''Value of variable $FILE_SYSBCK'''
		__r = self._instance.FileSysbck
		return None if __r is None else [None if x is None else FileBackVariableType(x) for x in __r]

	@property
	def glofatt(self) -> typing.List[GlofattVariableType]:
		'''Value of variable $GLOFATT'''
		__r = self._instance.Glofatt
		return None if __r is None else [None if x is None else GlofattVariableType(x) for x in __r]

	@property
	def glofset(self) -> GlofsetVariableType:
		'''Value of variable $GLOFSET'''
		__r = self._instance.Glofset
		return None if __r is None else GlofsetVariableType(__r)

	@property
	def imsave_done(self) -> bool:
		'''Value of variable $IMSAVE_DONE'''
		return self._instance.ImsaveDone

	@property
	def kcl_rpcout(self) -> str:
		'''Value of variable $KCL_RPCOUT'''
		return self._instance.KclRpcout

	@property
	def lastpauspos(self) -> typing.List[JointPositionVariable]:
		'''Value of variable $LASTPAUSPOS'''
		__r = self._instance.Lastpauspos
		return None if __r is None else [None if x is None else JointPositionVariable(None, None, x) for x in __r]

	@property
	def master_enb(self) -> int:
		'''Value of variable $MASTER_ENB'''
		return self._instance.MasterEnb

	@property
	def memo(self) -> MemoMemoVariableType:
		'''Value of variable $MEMO'''
		__r = self._instance.Memo
		return None if __r is None else MemoMemoVariableType(__r)

	@property
	def moptimiz(self) -> MoptimizVariableType:
		'''Value of variable $MOPTIMIZ'''
		__r = self._instance.Moptimiz
		return None if __r is None else MoptimizVariableType(__r)

	@property
	def null_cycle(self) -> int:
		'''Value of variable $NULL_CYCLE'''
		return self._instance.NullCycle

	@property
	def opt_state(self) -> OptstateVariableType:
		'''Value of variable $OPT_STATE'''
		__r = self._instance.OptState
		return None if __r is None else OptstateVariableType(__r)

	@property
	def padj_schnum(self) -> int:
		'''Value of variable $PADJ_SCHNUM'''
		return self._instance.PadjSchnum

	@property
	def pg_max_sped(self) -> typing.List[PgmaxspdVariableType]:
		'''Value of variable $PG_MAX_SPED'''
		__r = self._instance.PgMaxSped
		return None if __r is None else [None if x is None else PgmaxspdVariableType(x) for x in __r]

	@property
	def prgadj_sch(self) -> typing.List[PrgadjSchVariableType]:
		'''Value of variable $PRGADJ_SCH'''
		__r = self._instance.PrgadjSch
		return None if __r is None else [None if x is None else PrgadjSchVariableType(x) for x in __r]

	@property
	def shell_wrk(self) -> ShellWrkVariableType:
		'''Value of variable $SHELL_WRK'''
		__r = self._instance.ShellWrk
		return None if __r is None else ShellWrkVariableType(__r)

	@property
	def smh_made(self) -> SmhMadeVariableType:
		'''Value of variable $SMH_MADE'''
		__r = self._instance.SmhMade
		return None if __r is None else SmhMadeVariableType(__r)

	@property
	def startup_dbg(self) -> int:
		'''Value of variable $STARTUP_DBG'''
		return self._instance.StartupDbg

	@property
	def sys_config(self) -> SscbkVariableType:
		'''Value of variable $SYS_CONFIG'''
		__r = self._instance.SysConfig
		return None if __r is None else SscbkVariableType(__r)

	@property
	def sys_time(self) -> SysTimeVariableType:
		'''Value of variable $SYS_TIME'''
		__r = self._instance.SysTime
		return None if __r is None else SysTimeVariableType(__r)

	@property
	def tick_rate(self) -> int:
		'''Value of variable $TICK_RATE'''
		return self._instance.TickRate

	@property
	def tp_curscrn(self) -> typing.List[TpCurscrnVariableType]:
		'''Value of variable $TP_CURSCRN'''
		__r = self._instance.TpCurscrn
		return None if __r is None else [None if x is None else TpCurscrnVariableType(x) for x in __r]

	@property
	def tx(self) -> TxVariableType:
		'''Value of variable $TX'''
		__r = self._instance.Tx
		return None if __r is None else TxVariableType(__r)

	@property
	def txram(self) -> TxramVariableType:
		'''Value of variable $TXRAM'''
		__r = self._instance.Txram
		return None if __r is None else TxramVariableType(__r)

	@property
	def ui_curscrn(self) -> typing.List[TpCurscrnVariableType]:
		'''Value of variable $UI_CURSCRN'''
		__r = self._instance.UiCurscrn
		return None if __r is None else [None if x is None else TpCurscrnVariableType(x) for x in __r]

	@property
	def ui_fctnfav(self) -> typing.List[UiFctnfavVariableType]:
		'''Value of variable $UI_FCTNFAV'''
		__r = self._instance.UiFctnfav
		return None if __r is None else [None if x is None else UiFctnfavVariableType(x) for x in __r]

	@property
	def ui_panelink(self) -> typing.List[UiPanelnkVariableType]:
		'''Value of variable $UI_PANELINK'''
		__r = self._instance.UiPanelink
		return None if __r is None else [None if x is None else UiPanelnkVariableType(x) for x in __r]

	@property
	def umr(self) -> UmrVariableType:
		'''Value of variable $UMR'''
		__r = self._instance.Umr
		return None if __r is None else UmrVariableType(__r)

	@property
	def vcrsm_cfg(self) -> VcrsmCfgVariableType:
		'''Value of variable $VCRSM_CFG'''
		__r = self._instance.VcrsmCfg
		return None if __r is None else VcrsmCfgVariableType(__r)

	@property
	def vcwm_cfg(self) -> VcwmCfgVariableType:
		'''Value of variable $VCWM_CFG'''
		__r = self._instance.VcwmCfg
		return None if __r is None else VcwmCfgVariableType(__r)

	@property
	def vcwm_grp(self) -> typing.List[VcwmGrpVariableType]:
		'''Value of variable $VCWM_GRP'''
		__r = self._instance.VcwmGrp
		return None if __r is None else [None if x is None else VcwmGrpVariableType(x) for x in __r]

	@property
	def vdate(self) -> str:
		'''Value of variable $VDATE'''
		return self._instance.Vdate

	@property
	def version(self) -> str:
		'''Value of variable $VERSION'''
		return self._instance.Version

	@property
	def vsmo_tmp(self) -> VsmoTmpVariableType:
		'''Value of variable $VSMO_TMP'''
		__r = self._instance.VsmoTmp
		return None if __r is None else VsmoTmpVariableType(__r)

	@property
	def vsmo_val(self) -> VsmoValVariableType:
		'''Value of variable $VSMO_VAL'''
		__r = self._instance.VsmoVal
		return None if __r is None else VsmoValVariableType(__r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SynosaveFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
