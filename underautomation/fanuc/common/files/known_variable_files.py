from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.aavmmain_file import AavmmainFile
from underautomation.fanuc.common.files.variables.bicsetup_file import BicsetupFile
from underautomation.fanuc.common.files.variables.cbparam_file import CbparamFile
from underautomation.fanuc.common.files.variables.cellio_file import CellioFile
from underautomation.fanuc.common.files.variables.comset_file import ComsetFile
from underautomation.fanuc.common.files.variables.diocfgsv_file import DiocfgsvFile
from underautomation.fanuc.common.files.variables.gemdata_file import GemdataFile
from underautomation.fanuc.common.files.variables.htcolrec_file import HtcolrecFile
from underautomation.fanuc.common.files.variables.httpkcl_file import HttpkclFile
from underautomation.fanuc.common.files.variables.irc_counter_file import IrcCounterFile
from underautomation.fanuc.common.files.variables.irc_msg_file import IrcMsgFile
from underautomation.fanuc.common.files.variables.irc_status_file import IrcStatusFile
from underautomation.fanuc.common.files.variables.irc_stlabel_file import IrcStlabelFile
from underautomation.fanuc.common.files.variables.klaction_file import KlactionFile
from underautomation.fanuc.common.files.variables.mixlogic_file import MixlogicFile
from underautomation.fanuc.common.files.variables.mtparam_file import MtparamFile
from underautomation.fanuc.common.files.variables.numreg_file import NumregFile
from underautomation.fanuc.common.files.variables.palreg_file import PalregFile
from underautomation.fanuc.common.files.variables.posreg_file import PosregFile
from underautomation.fanuc.common.files.variables.strreg_file import StrregFile
from underautomation.fanuc.common.files.variables.swiupdt_file import SwiupdtFile
from underautomation.fanuc.common.files.variables.sycldint_file import SycldintFile
from underautomation.fanuc.common.files.variables.symotn_file import SymotnFile
from underautomation.fanuc.common.files.variables.synosave_file import SynosaveFile
from underautomation.fanuc.common.files.variables.sysframe_file import SysframeFile
from underautomation.fanuc.common.files.variables.sysfsac_file import SysfsacFile
from underautomation.fanuc.common.files.variables.syshost_file import SyshostFile
from underautomation.fanuc.common.files.variables.sysmacro_file import SysmacroFile
from underautomation.fanuc.common.files.variables.sysmast_file import SysmastFile
from underautomation.fanuc.common.files.variables.syspass_file import SyspassFile
from underautomation.fanuc.common.files.variables.sysservo_file import SysservoFile
from underautomation.fanuc.common.files.variables.system_file import SystemFile
from underautomation.fanuc.common.files.variables.sysuif_file import SysuifFile
from underautomation.fanuc.common.files.variables.tpsnap_file import TpsnapFile
from underautomation.fanuc.common.files.variables.vcmrinit_file import VcmrinitFile
from UnderAutomation.Fanuc.Common.Files import KnownVariableFiles as known_variable_files

class KnownVariableFiles:
	'''Wrapper class of methods to download and decode variable files'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = known_variable_files()
		else:
			self._instance = _internal

	def get_aavmmain_file(self) -> AavmmainFile:
		'''Reads and parse aavmmain.va variable file'''
		return AavmmainFile(self._instance.GetAavmmainFile())

	def get_bicsetup_file(self) -> BicsetupFile:
		'''Reads and parse bicsetup.va variable file'''
		return BicsetupFile(self._instance.GetBicsetupFile())

	def get_cbparam_file(self) -> CbparamFile:
		'''Reads and parse cbparam.va variable file'''
		return CbparamFile(self._instance.GetCbparamFile())

	def get_cellio_file(self) -> CellioFile:
		'''Reads and parse cellio.va variable file'''
		return CellioFile(self._instance.GetCellioFile())

	def get_comset_file(self) -> ComsetFile:
		'''Reads and parse comset.va variable file'''
		return ComsetFile(self._instance.GetComsetFile())

	def get_diocfgsv_file(self) -> DiocfgsvFile:
		'''Reads and parse diocfgsv.va variable file'''
		return DiocfgsvFile(self._instance.GetDiocfgsvFile())

	def get_gemdata_file(self) -> GemdataFile:
		'''Reads and parse gemdata.va variable file'''
		return GemdataFile(self._instance.GetGemdataFile())

	def get_htcolrec_file(self) -> HtcolrecFile:
		'''Reads and parse htcolrec.va variable file'''
		return HtcolrecFile(self._instance.GetHtcolrecFile())

	def get_httpkcl_file(self) -> HttpkclFile:
		'''Reads and parse httpkcl.va variable file'''
		return HttpkclFile(self._instance.GetHttpkclFile())

	def get_irc_counter_file(self) -> IrcCounterFile:
		'''Reads and parse irc_counter.va variable file'''
		return IrcCounterFile(self._instance.GetIrcCounterFile())

	def get_irc_msg_file(self) -> IrcMsgFile:
		'''Reads and parse irc_msg.va variable file'''
		return IrcMsgFile(self._instance.GetIrcMsgFile())

	def get_irc_status_file(self) -> IrcStatusFile:
		'''Reads and parse irc_status.va variable file'''
		return IrcStatusFile(self._instance.GetIrcStatusFile())

	def get_irc_stlabel_file(self) -> IrcStlabelFile:
		'''Reads and parse irc_stlabel.va variable file'''
		return IrcStlabelFile(self._instance.GetIrcStlabelFile())

	def get_klaction_file(self) -> KlactionFile:
		'''Reads and parse klaction.va variable file'''
		return KlactionFile(self._instance.GetKlactionFile())

	def get_mixlogic_file(self) -> MixlogicFile:
		'''Reads and parse mixlogic.va variable file'''
		return MixlogicFile(self._instance.GetMixlogicFile())

	def get_mtparam_file(self) -> MtparamFile:
		'''Reads and parse mtparam.va variable file'''
		return MtparamFile(self._instance.GetMtparamFile())

	def get_numreg_file(self) -> NumregFile:
		'''Reads and parse numreg.va variable file'''
		return NumregFile(self._instance.GetNumregFile())

	def get_palreg_file(self) -> PalregFile:
		'''Reads and parse palreg.va variable file'''
		return PalregFile(self._instance.GetPalregFile())

	def get_posreg_file(self) -> PosregFile:
		'''Reads and parse posreg.va variable file'''
		return PosregFile(self._instance.GetPosregFile())

	def get_strreg_file(self) -> StrregFile:
		'''Reads and parse strreg.va variable file'''
		return StrregFile(self._instance.GetStrregFile())

	def get_swiupdt_file(self) -> SwiupdtFile:
		'''Reads and parse swiupdt.va variable file'''
		return SwiupdtFile(self._instance.GetSwiupdtFile())

	def get_sycldint_file(self) -> SycldintFile:
		'''Reads and parse sycldint.va variable file'''
		return SycldintFile(self._instance.GetSycldintFile())

	def get_symotn_file(self) -> SymotnFile:
		'''Reads and parse symotn.va variable file'''
		return SymotnFile(self._instance.GetSymotnFile())

	def get_synosave_file(self) -> SynosaveFile:
		'''Reads and parse synosave.va variable file'''
		return SynosaveFile(self._instance.GetSynosaveFile())

	def get_sysframe_file(self) -> SysframeFile:
		'''Reads and parse sysframe.va variable file'''
		return SysframeFile(self._instance.GetSysframeFile())

	def get_sysfsac_file(self) -> SysfsacFile:
		'''Reads and parse sysfsac.va variable file'''
		return SysfsacFile(self._instance.GetSysfsacFile())

	def get_syshost_file(self) -> SyshostFile:
		'''Reads and parse syshost.va variable file'''
		return SyshostFile(self._instance.GetSyshostFile())

	def get_sysmacro_file(self) -> SysmacroFile:
		'''Reads and parse sysmacro.va variable file'''
		return SysmacroFile(self._instance.GetSysmacroFile())

	def get_sysmast_file(self) -> SysmastFile:
		'''Reads and parse sysmast.va variable file'''
		return SysmastFile(self._instance.GetSysmastFile())

	def get_syspass_file(self) -> SyspassFile:
		'''Reads and parse syspass.va variable file'''
		return SyspassFile(self._instance.GetSyspassFile())

	def get_sysservo_file(self) -> SysservoFile:
		'''Reads and parse sysservo.va variable file'''
		return SysservoFile(self._instance.GetSysservoFile())

	def get_system_file(self) -> SystemFile:
		'''Reads and parse system.va variable file'''
		return SystemFile(self._instance.GetSystemFile())

	def get_sysuif_file(self) -> SysuifFile:
		'''Reads and parse sysuif.va variable file'''
		return SysuifFile(self._instance.GetSysuifFile())

	def get_tpsnap_file(self) -> TpsnapFile:
		'''Reads and parse tpsnap.va variable file'''
		return TpsnapFile(self._instance.GetTpsnapFile())

	def get_vcmrinit_file(self) -> VcmrinitFile:
		'''Reads and parse vcmrinit.va variable file'''
		return VcmrinitFile(self._instance.GetVcmrinitFile())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KnownVariableFiles):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
