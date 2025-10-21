import typing
from underautomation.fanuc.ftp.variables.aavm_grp_variable_type import AavmGrpVariableType
from underautomation.fanuc.ftp.variables.dbwork_variable_type import DbworkVariableType
from underautomation.fanuc.ftp.variables.dhcp_int_variable_type import DhcpIntVariableType
from underautomation.fanuc.ftp.variables.fileconfig_variable_type import FileconfigVariableType
from underautomation.fanuc.ftp.variables.file_setup_variable_type import FileSetupVariableType
from underautomation.fanuc.ftp.variables.file_back_variable_type import FileBackVariableType
from underautomation.fanuc.ftp.variables.glofatt_variable_type import GlofattVariableType
from underautomation.fanuc.ftp.variables.glofset_variable_type import GlofsetVariableType
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.memo_memo_variable_type import MemoMemoVariableType
from underautomation.fanuc.ftp.variables.moptimiz_variable_type import MoptimizVariableType
from underautomation.fanuc.ftp.variables.optstate_variable_type import OptstateVariableType
from underautomation.fanuc.ftp.variables.pgmaxspd_variable_type import PgmaxspdVariableType
from underautomation.fanuc.ftp.variables.prgadj_sch_variable_type import PrgadjSchVariableType
from underautomation.fanuc.ftp.variables.shell_wrk_variable_type import ShellWrkVariableType
from underautomation.fanuc.ftp.variables.smh_made_variable_type import SmhMadeVariableType
from underautomation.fanuc.ftp.variables.sscbk_variable_type import SscbkVariableType
from underautomation.fanuc.ftp.variables.sys_time_variable_type import SysTimeVariableType
from underautomation.fanuc.ftp.variables.tp_curscrn_variable_type import TpCurscrnVariableType
from underautomation.fanuc.ftp.variables.tx_variable_type import TxVariableType
from underautomation.fanuc.ftp.variables.txram_variable_type import TxramVariableType
from underautomation.fanuc.ftp.variables.ui_fctnfav_variable_type import UiFctnfavVariableType
from underautomation.fanuc.ftp.variables.ui_panelnk_variable_type import UiPanelnkVariableType
from underautomation.fanuc.ftp.variables.umr_variable_type import UmrVariableType
from underautomation.fanuc.ftp.variables.vcrsm_cfg_variable_type import VcrsmCfgVariableType
from underautomation.fanuc.ftp.variables.vcwm_cfg_variable_type import VcwmCfgVariableType
from underautomation.fanuc.ftp.variables.vcwm_grp_variable_type import VcwmGrpVariableType
from underautomation.fanuc.ftp.variables.vsmo_tmp_variable_type import VsmoTmpVariableType
from underautomation.fanuc.ftp.variables.vsmo_val_variable_type import VsmoValVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SynosaveFile as synosave_file

class SynosaveFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = synosave_file()
		else:
			self._instance = _internal
	@property
	def aavm_grp(self) -> typing.List[AavmGrpVariableType]:
		return [AavmGrpVariableType(x) for x in self._instance.AavmGrp]
	@property
	def aimage_back(self) -> int:
		return self._instance.AimageBack
	@property
	def autoupdt_st(self) -> int:
		return self._instance.AutoupdtSt
	@property
	def blt(self) -> int:
		return self._instance.Blt
	@property
	def daq_gfd_use(self) -> int:
		return self._instance.DaqGfdUse
	@property
	def dbwork(self) -> typing.List[DbworkVariableType]:
		return [DbworkVariableType(x) for x in self._instance.Dbwork]
	@property
	def device(self) -> str:
		return self._instance.Device
	@property
	def dfmtn0_no(self) -> int:
		return self._instance.Dfmtn0No
	@property
	def dhcp_int(self) -> typing.List[DhcpIntVariableType]:
		return [DhcpIntVariableType(x) for x in self._instance.DhcpInt]
	@property
	def distbf_data(self) -> int:
		return self._instance.DistbfData
	@property
	def fast_clock(self) -> int:
		return self._instance.FastClock
	@property
	def fileconfig(self) -> FileconfigVariableType:
		return FileconfigVariableType(self._instance.Fileconfig)
	@property
	def filesetup(self) -> FileSetupVariableType:
		return FileSetupVariableType(self._instance.Filesetup)
	@property
	def file_basept(self) -> int:
		return self._instance.FileBasept
	@property
	def file_errbck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileErrbck]
	@property
	def file_maxsec(self) -> int:
		return self._instance.FileMaxsec
	@property
	def file_sysbck(self) -> typing.List[FileBackVariableType]:
		return [FileBackVariableType(x) for x in self._instance.FileSysbck]
	@property
	def glofatt(self) -> typing.List[GlofattVariableType]:
		return [GlofattVariableType(x) for x in self._instance.Glofatt]
	@property
	def glofset(self) -> GlofsetVariableType:
		return GlofsetVariableType(self._instance.Glofset)
	@property
	def imsave_done(self) -> bool:
		return self._instance.ImsaveDone
	@property
	def kcl_rpcout(self) -> str:
		return self._instance.KclRpcout
	@property
	def lastpauspos(self) -> typing.List[JointPositionVariable]:
		return [JointPositionVariable(x) for x in self._instance.Lastpauspos]
	@property
	def master_enb(self) -> int:
		return self._instance.MasterEnb
	@property
	def memo(self) -> MemoMemoVariableType:
		return MemoMemoVariableType(self._instance.Memo)
	@property
	def moptimiz(self) -> MoptimizVariableType:
		return MoptimizVariableType(self._instance.Moptimiz)
	@property
	def null_cycle(self) -> int:
		return self._instance.NullCycle
	@property
	def opt_state(self) -> OptstateVariableType:
		return OptstateVariableType(self._instance.OptState)
	@property
	def padj_schnum(self) -> int:
		return self._instance.PadjSchnum
	@property
	def pg_max_sped(self) -> typing.List[PgmaxspdVariableType]:
		return [PgmaxspdVariableType(x) for x in self._instance.PgMaxSped]
	@property
	def prgadj_sch(self) -> typing.List[PrgadjSchVariableType]:
		return [PrgadjSchVariableType(x) for x in self._instance.PrgadjSch]
	@property
	def shell_wrk(self) -> ShellWrkVariableType:
		return ShellWrkVariableType(self._instance.ShellWrk)
	@property
	def smh_made(self) -> SmhMadeVariableType:
		return SmhMadeVariableType(self._instance.SmhMade)
	@property
	def startup_dbg(self) -> int:
		return self._instance.StartupDbg
	@property
	def sys_config(self) -> SscbkVariableType:
		return SscbkVariableType(self._instance.SysConfig)
	@property
	def sys_time(self) -> SysTimeVariableType:
		return SysTimeVariableType(self._instance.SysTime)
	@property
	def tick_rate(self) -> int:
		return self._instance.TickRate
	@property
	def tp_curscrn(self) -> typing.List[TpCurscrnVariableType]:
		return [TpCurscrnVariableType(x) for x in self._instance.TpCurscrn]
	@property
	def tx(self) -> TxVariableType:
		return TxVariableType(self._instance.Tx)
	@property
	def txram(self) -> TxramVariableType:
		return TxramVariableType(self._instance.Txram)
	@property
	def ui_curscrn(self) -> typing.List[TpCurscrnVariableType]:
		return [TpCurscrnVariableType(x) for x in self._instance.UiCurscrn]
	@property
	def ui_fctnfav(self) -> typing.List[UiFctnfavVariableType]:
		return [UiFctnfavVariableType(x) for x in self._instance.UiFctnfav]
	@property
	def ui_panelink(self) -> typing.List[UiPanelnkVariableType]:
		return [UiPanelnkVariableType(x) for x in self._instance.UiPanelink]
	@property
	def umr(self) -> UmrVariableType:
		return UmrVariableType(self._instance.Umr)
	@property
	def vcrsm_cfg(self) -> VcrsmCfgVariableType:
		return VcrsmCfgVariableType(self._instance.VcrsmCfg)
	@property
	def vcwm_cfg(self) -> VcwmCfgVariableType:
		return VcwmCfgVariableType(self._instance.VcwmCfg)
	@property
	def vcwm_grp(self) -> typing.List[VcwmGrpVariableType]:
		return [VcwmGrpVariableType(x) for x in self._instance.VcwmGrp]
	@property
	def vdate(self) -> str:
		return self._instance.Vdate
	@property
	def version(self) -> str:
		return self._instance.Version
	@property
	def vsmo_tmp(self) -> VsmoTmpVariableType:
		return VsmoTmpVariableType(self._instance.VsmoTmp)
	@property
	def vsmo_val(self) -> VsmoValVariableType:
		return VsmoValVariableType(self._instance.VsmoVal)
