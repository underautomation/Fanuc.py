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
from UnderAutomation.Fanuc.Ftp.Internal import FtpKnownVariableFiles as ftp_known_variable_files

class FtpKnownVariableFiles:
	'''Wrapper class of methods to download and decode variable files'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_known_variable_files()
		else:
			self._instance = _internal

	def get_aavmmain_file(self) -> AavmmainFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return AavmmainFile(self._instance.GetAavmmainFile())

	def get_bicsetup_file(self) -> BicsetupFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return BicsetupFile(self._instance.GetBicsetupFile())

	def get_cbparam_file(self) -> CbparamFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return CbparamFile(self._instance.GetCbparamFile())

	def get_cellio_file(self) -> CellioFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return CellioFile(self._instance.GetCellioFile())

	def get_comset_file(self) -> ComsetFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return ComsetFile(self._instance.GetComsetFile())

	def get_diocfgsv_file(self) -> DiocfgsvFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return DiocfgsvFile(self._instance.GetDiocfgsvFile())

	def get_gemdata_file(self) -> GemdataFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return GemdataFile(self._instance.GetGemdataFile())

	def get_htcolrec_file(self) -> HtcolrecFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return HtcolrecFile(self._instance.GetHtcolrecFile())

	def get_httpkcl_file(self) -> HttpkclFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return HttpkclFile(self._instance.GetHttpkclFile())

	def get_irc_counter_file(self) -> IrcCounterFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return IrcCounterFile(self._instance.GetIrcCounterFile())

	def get_irc_msg_file(self) -> IrcMsgFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return IrcMsgFile(self._instance.GetIrcMsgFile())

	def get_irc_status_file(self) -> IrcStatusFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return IrcStatusFile(self._instance.GetIrcStatusFile())

	def get_irc_stlabel_file(self) -> IrcStlabelFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return IrcStlabelFile(self._instance.GetIrcStlabelFile())

	def get_klaction_file(self) -> KlactionFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return KlactionFile(self._instance.GetKlactionFile())

	def get_mixlogic_file(self) -> MixlogicFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return MixlogicFile(self._instance.GetMixlogicFile())

	def get_mtparam_file(self) -> MtparamFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return MtparamFile(self._instance.GetMtparamFile())

	def get_numreg_file(self) -> NumregFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return NumregFile(self._instance.GetNumregFile())

	def get_palreg_file(self) -> PalregFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return PalregFile(self._instance.GetPalregFile())

	def get_posreg_file(self) -> PosregFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return PosregFile(self._instance.GetPosregFile())

	def get_strreg_file(self) -> StrregFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return StrregFile(self._instance.GetStrregFile())

	def get_swiupdt_file(self) -> SwiupdtFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SwiupdtFile(self._instance.GetSwiupdtFile())

	def get_sycldint_file(self) -> SycldintFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SycldintFile(self._instance.GetSycldintFile())

	def get_symotn_file(self) -> SymotnFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SymotnFile(self._instance.GetSymotnFile())

	def get_synosave_file(self) -> SynosaveFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SynosaveFile(self._instance.GetSynosaveFile())

	def get_sysframe_file(self) -> SysframeFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysframeFile(self._instance.GetSysframeFile())

	def get_sysfsac_file(self) -> SysfsacFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysfsacFile(self._instance.GetSysfsacFile())

	def get_syshost_file(self) -> SyshostFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SyshostFile(self._instance.GetSyshostFile())

	def get_sysmacro_file(self) -> SysmacroFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysmacroFile(self._instance.GetSysmacroFile())

	def get_sysmast_file(self) -> SysmastFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysmastFile(self._instance.GetSysmastFile())

	def get_syspass_file(self) -> SyspassFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SyspassFile(self._instance.GetSyspassFile())

	def get_sysservo_file(self) -> SysservoFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysservoFile(self._instance.GetSysservoFile())

	def get_system_file(self) -> SystemFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SystemFile(self._instance.GetSystemFile())

	def get_sysuif_file(self) -> SysuifFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return SysuifFile(self._instance.GetSysuifFile())

	def get_tpsnap_file(self) -> TpsnapFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return TpsnapFile(self._instance.GetTpsnapFile())

	def get_vcmrinit_file(self) -> VcmrinitFile:
		'''Reads and parse aavmmain.va variable file via FTP'''
		return VcmrinitFile(self._instance.GetVcmrinitFile())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpKnownVariableFiles):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
