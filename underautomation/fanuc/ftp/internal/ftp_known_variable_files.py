import typing
from underautomation.fanuc.ftp.variables.aavmmain_file import AavmmainFile
from underautomation.fanuc.ftp.variables.bicsetup_file import BicsetupFile
from underautomation.fanuc.ftp.variables.cbparam_file import CbparamFile
from underautomation.fanuc.ftp.variables.cellio_file import CellioFile
from underautomation.fanuc.ftp.variables.comset_file import ComsetFile
from underautomation.fanuc.ftp.variables.diocfgsv_file import DiocfgsvFile
from underautomation.fanuc.ftp.variables.gemdata_file import GemdataFile
from underautomation.fanuc.ftp.variables.htcolrec_file import HtcolrecFile
from underautomation.fanuc.ftp.variables.httpkcl_file import HttpkclFile
from underautomation.fanuc.ftp.variables.irc_counter_file import IrcCounterFile
from underautomation.fanuc.ftp.variables.irc_msg_file import IrcMsgFile
from underautomation.fanuc.ftp.variables.irc_status_file import IrcStatusFile
from underautomation.fanuc.ftp.variables.irc_stlabel_file import IrcStlabelFile
from underautomation.fanuc.ftp.variables.klaction_file import KlactionFile
from underautomation.fanuc.ftp.variables.mixlogic_file import MixlogicFile
from underautomation.fanuc.ftp.variables.mtparam_file import MtparamFile
from underautomation.fanuc.ftp.variables.numreg_file import NumregFile
from underautomation.fanuc.ftp.variables.palreg_file import PalregFile
from underautomation.fanuc.ftp.variables.posreg_file import PosregFile
from underautomation.fanuc.ftp.variables.strreg_file import StrregFile
from underautomation.fanuc.ftp.variables.swiupdt_file import SwiupdtFile
from underautomation.fanuc.ftp.variables.sycldint_file import SycldintFile
from underautomation.fanuc.ftp.variables.symotn_file import SymotnFile
from underautomation.fanuc.ftp.variables.synosave_file import SynosaveFile
from underautomation.fanuc.ftp.variables.sysframe_file import SysframeFile
from underautomation.fanuc.ftp.variables.sysfsac_file import SysfsacFile
from underautomation.fanuc.ftp.variables.syshost_file import SyshostFile
from underautomation.fanuc.ftp.variables.sysmacro_file import SysmacroFile
from underautomation.fanuc.ftp.variables.sysmast_file import SysmastFile
from underautomation.fanuc.ftp.variables.syspass_file import SyspassFile
from underautomation.fanuc.ftp.variables.sysservo_file import SysservoFile
from underautomation.fanuc.ftp.variables.system_file import SystemFile
from underautomation.fanuc.ftp.variables.sysuif_file import SysuifFile
from underautomation.fanuc.ftp.variables.tpsnap_file import TpsnapFile
from underautomation.fanuc.ftp.variables.vcmrinit_file import VcmrinitFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FtpKnownVariableFiles as ftp_known_variable_files

class FtpKnownVariableFiles:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_known_variable_files()
		else:
			self._instance = _internal
	def get_aavmmain_file(self) -> AavmmainFile:
		return AavmmainFile(self._instance.GetAavmmainFile())
	def get_bicsetup_file(self) -> BicsetupFile:
		return BicsetupFile(self._instance.GetBicsetupFile())
	def get_cbparam_file(self) -> CbparamFile:
		return CbparamFile(self._instance.GetCbparamFile())
	def get_cellio_file(self) -> CellioFile:
		return CellioFile(self._instance.GetCellioFile())
	def get_comset_file(self) -> ComsetFile:
		return ComsetFile(self._instance.GetComsetFile())
	def get_diocfgsv_file(self) -> DiocfgsvFile:
		return DiocfgsvFile(self._instance.GetDiocfgsvFile())
	def get_gemdata_file(self) -> GemdataFile:
		return GemdataFile(self._instance.GetGemdataFile())
	def get_htcolrec_file(self) -> HtcolrecFile:
		return HtcolrecFile(self._instance.GetHtcolrecFile())
	def get_httpkcl_file(self) -> HttpkclFile:
		return HttpkclFile(self._instance.GetHttpkclFile())
	def get_irc_counter_file(self) -> IrcCounterFile:
		return IrcCounterFile(self._instance.GetIrcCounterFile())
	def get_irc_msg_file(self) -> IrcMsgFile:
		return IrcMsgFile(self._instance.GetIrcMsgFile())
	def get_irc_status_file(self) -> IrcStatusFile:
		return IrcStatusFile(self._instance.GetIrcStatusFile())
	def get_irc_stlabel_file(self) -> IrcStlabelFile:
		return IrcStlabelFile(self._instance.GetIrcStlabelFile())
	def get_klaction_file(self) -> KlactionFile:
		return KlactionFile(self._instance.GetKlactionFile())
	def get_mixlogic_file(self) -> MixlogicFile:
		return MixlogicFile(self._instance.GetMixlogicFile())
	def get_mtparam_file(self) -> MtparamFile:
		return MtparamFile(self._instance.GetMtparamFile())
	def get_numreg_file(self) -> NumregFile:
		return NumregFile(self._instance.GetNumregFile())
	def get_palreg_file(self) -> PalregFile:
		return PalregFile(self._instance.GetPalregFile())
	def get_posreg_file(self) -> PosregFile:
		return PosregFile(self._instance.GetPosregFile())
	def get_strreg_file(self) -> StrregFile:
		return StrregFile(self._instance.GetStrregFile())
	def get_swiupdt_file(self) -> SwiupdtFile:
		return SwiupdtFile(self._instance.GetSwiupdtFile())
	def get_sycldint_file(self) -> SycldintFile:
		return SycldintFile(self._instance.GetSycldintFile())
	def get_symotn_file(self) -> SymotnFile:
		return SymotnFile(self._instance.GetSymotnFile())
	def get_synosave_file(self) -> SynosaveFile:
		return SynosaveFile(self._instance.GetSynosaveFile())
	def get_sysframe_file(self) -> SysframeFile:
		return SysframeFile(self._instance.GetSysframeFile())
	def get_sysfsac_file(self) -> SysfsacFile:
		return SysfsacFile(self._instance.GetSysfsacFile())
	def get_syshost_file(self) -> SyshostFile:
		return SyshostFile(self._instance.GetSyshostFile())
	def get_sysmacro_file(self) -> SysmacroFile:
		return SysmacroFile(self._instance.GetSysmacroFile())
	def get_sysmast_file(self) -> SysmastFile:
		return SysmastFile(self._instance.GetSysmastFile())
	def get_syspass_file(self) -> SyspassFile:
		return SyspassFile(self._instance.GetSyspassFile())
	def get_sysservo_file(self) -> SysservoFile:
		return SysservoFile(self._instance.GetSysservoFile())
	def get_system_file(self) -> SystemFile:
		return SystemFile(self._instance.GetSystemFile())
	def get_sysuif_file(self) -> SysuifFile:
		return SysuifFile(self._instance.GetSysuifFile())
	def get_tpsnap_file(self) -> TpsnapFile:
		return TpsnapFile(self._instance.GetTpsnapFile())
	def get_vcmrinit_file(self) -> VcmrinitFile:
		return VcmrinitFile(self._instance.GetVcmrinitFile())
