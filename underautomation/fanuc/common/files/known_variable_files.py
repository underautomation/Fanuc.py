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
		__r = self._instance.GetAavmmainFile()
		return None if __r is None else AavmmainFile(__r)

	def get_bicsetup_file(self) -> BicsetupFile:
		'''Reads and parse bicsetup.va variable file'''
		__r = self._instance.GetBicsetupFile()
		return None if __r is None else BicsetupFile(__r)

	def get_cbparam_file(self) -> CbparamFile:
		'''Reads and parse cbparam.va variable file'''
		__r = self._instance.GetCbparamFile()
		return None if __r is None else CbparamFile(__r)

	def get_cellio_file(self) -> CellioFile:
		'''Reads and parse cellio.va variable file'''
		__r = self._instance.GetCellioFile()
		return None if __r is None else CellioFile(__r)

	def get_comset_file(self) -> ComsetFile:
		'''Reads and parse comset.va variable file'''
		__r = self._instance.GetComsetFile()
		return None if __r is None else ComsetFile(__r)

	def get_diocfgsv_file(self) -> DiocfgsvFile:
		'''Reads and parse diocfgsv.va variable file'''
		__r = self._instance.GetDiocfgsvFile()
		return None if __r is None else DiocfgsvFile(__r)

	def get_gemdata_file(self) -> GemdataFile:
		'''Reads and parse gemdata.va variable file'''
		__r = self._instance.GetGemdataFile()
		return None if __r is None else GemdataFile(__r)

	def get_htcolrec_file(self) -> HtcolrecFile:
		'''Reads and parse htcolrec.va variable file'''
		__r = self._instance.GetHtcolrecFile()
		return None if __r is None else HtcolrecFile(__r)

	def get_httpkcl_file(self) -> HttpkclFile:
		'''Reads and parse httpkcl.va variable file'''
		__r = self._instance.GetHttpkclFile()
		return None if __r is None else HttpkclFile(__r)

	def get_irc_counter_file(self) -> IrcCounterFile:
		'''Reads and parse irc_counter.va variable file'''
		__r = self._instance.GetIrcCounterFile()
		return None if __r is None else IrcCounterFile(__r)

	def get_irc_msg_file(self) -> IrcMsgFile:
		'''Reads and parse irc_msg.va variable file'''
		__r = self._instance.GetIrcMsgFile()
		return None if __r is None else IrcMsgFile(__r)

	def get_irc_status_file(self) -> IrcStatusFile:
		'''Reads and parse irc_status.va variable file'''
		__r = self._instance.GetIrcStatusFile()
		return None if __r is None else IrcStatusFile(__r)

	def get_irc_stlabel_file(self) -> IrcStlabelFile:
		'''Reads and parse irc_stlabel.va variable file'''
		__r = self._instance.GetIrcStlabelFile()
		return None if __r is None else IrcStlabelFile(__r)

	def get_klaction_file(self) -> KlactionFile:
		'''Reads and parse klaction.va variable file'''
		__r = self._instance.GetKlactionFile()
		return None if __r is None else KlactionFile(__r)

	def get_mixlogic_file(self) -> MixlogicFile:
		'''Reads and parse mixlogic.va variable file'''
		__r = self._instance.GetMixlogicFile()
		return None if __r is None else MixlogicFile(__r)

	def get_mtparam_file(self) -> MtparamFile:
		'''Reads and parse mtparam.va variable file'''
		__r = self._instance.GetMtparamFile()
		return None if __r is None else MtparamFile(__r)

	def get_numreg_file(self) -> NumregFile:
		'''Reads and parse numreg.va variable file'''
		__r = self._instance.GetNumregFile()
		return None if __r is None else NumregFile(__r)

	def get_palreg_file(self) -> PalregFile:
		'''Reads and parse palreg.va variable file'''
		__r = self._instance.GetPalregFile()
		return None if __r is None else PalregFile(__r)

	def get_posreg_file(self) -> PosregFile:
		'''Reads and parse posreg.va variable file'''
		__r = self._instance.GetPosregFile()
		return None if __r is None else PosregFile(__r)

	def get_strreg_file(self) -> StrregFile:
		'''Reads and parse strreg.va variable file'''
		__r = self._instance.GetStrregFile()
		return None if __r is None else StrregFile(__r)

	def get_swiupdt_file(self) -> SwiupdtFile:
		'''Reads and parse swiupdt.va variable file'''
		__r = self._instance.GetSwiupdtFile()
		return None if __r is None else SwiupdtFile(__r)

	def get_sycldint_file(self) -> SycldintFile:
		'''Reads and parse sycldint.va variable file'''
		__r = self._instance.GetSycldintFile()
		return None if __r is None else SycldintFile(__r)

	def get_symotn_file(self) -> SymotnFile:
		'''Reads and parse symotn.va variable file'''
		__r = self._instance.GetSymotnFile()
		return None if __r is None else SymotnFile(__r)

	def get_synosave_file(self) -> SynosaveFile:
		'''Reads and parse synosave.va variable file'''
		__r = self._instance.GetSynosaveFile()
		return None if __r is None else SynosaveFile(__r)

	def get_sysframe_file(self) -> SysframeFile:
		'''Reads and parse sysframe.va variable file'''
		__r = self._instance.GetSysframeFile()
		return None if __r is None else SysframeFile(__r)

	def get_sysfsac_file(self) -> SysfsacFile:
		'''Reads and parse sysfsac.va variable file'''
		__r = self._instance.GetSysfsacFile()
		return None if __r is None else SysfsacFile(__r)

	def get_syshost_file(self) -> SyshostFile:
		'''Reads and parse syshost.va variable file'''
		__r = self._instance.GetSyshostFile()
		return None if __r is None else SyshostFile(__r)

	def get_sysmacro_file(self) -> SysmacroFile:
		'''Reads and parse sysmacro.va variable file'''
		__r = self._instance.GetSysmacroFile()
		return None if __r is None else SysmacroFile(__r)

	def get_sysmast_file(self) -> SysmastFile:
		'''Reads and parse sysmast.va variable file'''
		__r = self._instance.GetSysmastFile()
		return None if __r is None else SysmastFile(__r)

	def get_syspass_file(self) -> SyspassFile:
		'''Reads and parse syspass.va variable file'''
		__r = self._instance.GetSyspassFile()
		return None if __r is None else SyspassFile(__r)

	def get_sysservo_file(self) -> SysservoFile:
		'''Reads and parse sysservo.va variable file'''
		__r = self._instance.GetSysservoFile()
		return None if __r is None else SysservoFile(__r)

	def get_system_file(self) -> SystemFile:
		'''Reads and parse system.va variable file'''
		__r = self._instance.GetSystemFile()
		return None if __r is None else SystemFile(__r)

	def get_sysuif_file(self) -> SysuifFile:
		'''Reads and parse sysuif.va variable file'''
		__r = self._instance.GetSysuifFile()
		return None if __r is None else SysuifFile(__r)

	def get_tpsnap_file(self) -> TpsnapFile:
		'''Reads and parse tpsnap.va variable file'''
		__r = self._instance.GetTpsnapFile()
		return None if __r is None else TpsnapFile(__r)

	def get_vcmrinit_file(self) -> VcmrinitFile:
		'''Reads and parse vcmrinit.va variable file'''
		__r = self._instance.GetVcmrinitFile()
		return None if __r is None else VcmrinitFile(__r)

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
