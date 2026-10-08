from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.common.files.variables.generic_variable import GenericVariable
from underautomation.fanuc.common.files.variables.variable_reader_1 import VariableReader1
from underautomation.fanuc.common.files.file_reader_1 import FileReader1
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
from UnderAutomation.Fanuc.Common.Files.Variables import VariableReader as variable_reader
from UnderAutomation.Fanuc.Common import Languages as languages

class VariableReader(FileReader1[GenericVariableFile]):
	'''Reader for Fanuc variable files (*.va)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_reader()
		else:
			self._instance = _internal

	@staticmethod
	def read_variable_file(fileName: str, language: Languages) -> GenericVariableFile:
		'''Reads and parses a variable file from a file path'''
		__r = variable_reader.ReadVariableFile(fileName, languages(int(language)))
		return None if __r is None else GenericVariableFile(__r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VariableReader):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

VariableReader.AavmmainFile = None if variable_reader.AavmmainFile is None else VariableReader1[AavmmainFile](variable_reader.AavmmainFile)

VariableReader.BicsetupFile = None if variable_reader.BicsetupFile is None else VariableReader1[BicsetupFile](variable_reader.BicsetupFile)

VariableReader.CbparamFile = None if variable_reader.CbparamFile is None else VariableReader1[CbparamFile](variable_reader.CbparamFile)

VariableReader.CellioFile = None if variable_reader.CellioFile is None else VariableReader1[CellioFile](variable_reader.CellioFile)

VariableReader.ComsetFile = None if variable_reader.ComsetFile is None else VariableReader1[ComsetFile](variable_reader.ComsetFile)

VariableReader.DiocfgsvFile = None if variable_reader.DiocfgsvFile is None else VariableReader1[DiocfgsvFile](variable_reader.DiocfgsvFile)

VariableReader.GemdataFile = None if variable_reader.GemdataFile is None else VariableReader1[GemdataFile](variable_reader.GemdataFile)

VariableReader.HtcolrecFile = None if variable_reader.HtcolrecFile is None else VariableReader1[HtcolrecFile](variable_reader.HtcolrecFile)

VariableReader.HttpkclFile = None if variable_reader.HttpkclFile is None else VariableReader1[HttpkclFile](variable_reader.HttpkclFile)

VariableReader.IrcCounterFile = None if variable_reader.IrcCounterFile is None else VariableReader1[IrcCounterFile](variable_reader.IrcCounterFile)

VariableReader.IrcMsgFile = None if variable_reader.IrcMsgFile is None else VariableReader1[IrcMsgFile](variable_reader.IrcMsgFile)

VariableReader.IrcStatusFile = None if variable_reader.IrcStatusFile is None else VariableReader1[IrcStatusFile](variable_reader.IrcStatusFile)

VariableReader.IrcStlabelFile = None if variable_reader.IrcStlabelFile is None else VariableReader1[IrcStlabelFile](variable_reader.IrcStlabelFile)

VariableReader.KlactionFile = None if variable_reader.KlactionFile is None else VariableReader1[KlactionFile](variable_reader.KlactionFile)

VariableReader.MixlogicFile = None if variable_reader.MixlogicFile is None else VariableReader1[MixlogicFile](variable_reader.MixlogicFile)

VariableReader.MtparamFile = None if variable_reader.MtparamFile is None else VariableReader1[MtparamFile](variable_reader.MtparamFile)

VariableReader.NumregFile = None if variable_reader.NumregFile is None else VariableReader1[NumregFile](variable_reader.NumregFile)

VariableReader.PalregFile = None if variable_reader.PalregFile is None else VariableReader1[PalregFile](variable_reader.PalregFile)

VariableReader.PosregFile = None if variable_reader.PosregFile is None else VariableReader1[PosregFile](variable_reader.PosregFile)

VariableReader.StrregFile = None if variable_reader.StrregFile is None else VariableReader1[StrregFile](variable_reader.StrregFile)

VariableReader.SwiupdtFile = None if variable_reader.SwiupdtFile is None else VariableReader1[SwiupdtFile](variable_reader.SwiupdtFile)

VariableReader.SycldintFile = None if variable_reader.SycldintFile is None else VariableReader1[SycldintFile](variable_reader.SycldintFile)

VariableReader.SymotnFile = None if variable_reader.SymotnFile is None else VariableReader1[SymotnFile](variable_reader.SymotnFile)

VariableReader.SynosaveFile = None if variable_reader.SynosaveFile is None else VariableReader1[SynosaveFile](variable_reader.SynosaveFile)

VariableReader.SysframeFile = None if variable_reader.SysframeFile is None else VariableReader1[SysframeFile](variable_reader.SysframeFile)

VariableReader.SysfsacFile = None if variable_reader.SysfsacFile is None else VariableReader1[SysfsacFile](variable_reader.SysfsacFile)

VariableReader.SyshostFile = None if variable_reader.SyshostFile is None else VariableReader1[SyshostFile](variable_reader.SyshostFile)

VariableReader.SysmacroFile = None if variable_reader.SysmacroFile is None else VariableReader1[SysmacroFile](variable_reader.SysmacroFile)

VariableReader.SysmastFile = None if variable_reader.SysmastFile is None else VariableReader1[SysmastFile](variable_reader.SysmastFile)

VariableReader.SyspassFile = None if variable_reader.SyspassFile is None else VariableReader1[SyspassFile](variable_reader.SyspassFile)

VariableReader.SysservoFile = None if variable_reader.SysservoFile is None else VariableReader1[SysservoFile](variable_reader.SysservoFile)

VariableReader.SystemFile = None if variable_reader.SystemFile is None else VariableReader1[SystemFile](variable_reader.SystemFile)

VariableReader.SysuifFile = None if variable_reader.SysuifFile is None else VariableReader1[SysuifFile](variable_reader.SysuifFile)

VariableReader.TpsnapFile = None if variable_reader.TpsnapFile is None else VariableReader1[TpsnapFile](variable_reader.TpsnapFile)

VariableReader.VcmrinitFile = None if variable_reader.VcmrinitFile is None else VariableReader1[VcmrinitFile](variable_reader.VcmrinitFile)
