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

	def read_file(self, fileStream: typing.Any, language: Languages, fileName: str) -> GenericVariableFile:
		return GenericVariableFile(self._instance.ReadFile(fileStream, languages(int(language)), fileName))

	@staticmethod
	def read_variable_file(fileStream: typing.Any, fileName: str, language: Languages) -> GenericVariableFile:
		'''Reads and parses a variable file from a stream'''
		return GenericVariableFile(variable_reader.ReadVariableFile(fileStream, fileName, languages(int(language))))

	@staticmethod
	def parse_variable_file(stream: typing.Any, language: Languages) -> typing.List[GenericVariable]:
		'''Parses all variables from a stream'''
		return [GenericVariable(x) for x in variable_reader.ParseVariableFile(stream, languages(int(language)))]

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

VariableReader.AavmmainFile = VariableReader1[AavmmainFile](variable_reader.AavmmainFile)

VariableReader.BicsetupFile = VariableReader1[BicsetupFile](variable_reader.BicsetupFile)

VariableReader.CbparamFile = VariableReader1[CbparamFile](variable_reader.CbparamFile)

VariableReader.CellioFile = VariableReader1[CellioFile](variable_reader.CellioFile)

VariableReader.ComsetFile = VariableReader1[ComsetFile](variable_reader.ComsetFile)

VariableReader.DiocfgsvFile = VariableReader1[DiocfgsvFile](variable_reader.DiocfgsvFile)

VariableReader.GemdataFile = VariableReader1[GemdataFile](variable_reader.GemdataFile)

VariableReader.HtcolrecFile = VariableReader1[HtcolrecFile](variable_reader.HtcolrecFile)

VariableReader.HttpkclFile = VariableReader1[HttpkclFile](variable_reader.HttpkclFile)

VariableReader.IrcCounterFile = VariableReader1[IrcCounterFile](variable_reader.IrcCounterFile)

VariableReader.IrcMsgFile = VariableReader1[IrcMsgFile](variable_reader.IrcMsgFile)

VariableReader.IrcStatusFile = VariableReader1[IrcStatusFile](variable_reader.IrcStatusFile)

VariableReader.IrcStlabelFile = VariableReader1[IrcStlabelFile](variable_reader.IrcStlabelFile)

VariableReader.KlactionFile = VariableReader1[KlactionFile](variable_reader.KlactionFile)

VariableReader.MixlogicFile = VariableReader1[MixlogicFile](variable_reader.MixlogicFile)

VariableReader.MtparamFile = VariableReader1[MtparamFile](variable_reader.MtparamFile)

VariableReader.NumregFile = VariableReader1[NumregFile](variable_reader.NumregFile)

VariableReader.PalregFile = VariableReader1[PalregFile](variable_reader.PalregFile)

VariableReader.PosregFile = VariableReader1[PosregFile](variable_reader.PosregFile)

VariableReader.StrregFile = VariableReader1[StrregFile](variable_reader.StrregFile)

VariableReader.SwiupdtFile = VariableReader1[SwiupdtFile](variable_reader.SwiupdtFile)

VariableReader.SycldintFile = VariableReader1[SycldintFile](variable_reader.SycldintFile)

VariableReader.SymotnFile = VariableReader1[SymotnFile](variable_reader.SymotnFile)

VariableReader.SynosaveFile = VariableReader1[SynosaveFile](variable_reader.SynosaveFile)

VariableReader.SysframeFile = VariableReader1[SysframeFile](variable_reader.SysframeFile)

VariableReader.SysfsacFile = VariableReader1[SysfsacFile](variable_reader.SysfsacFile)

VariableReader.SyshostFile = VariableReader1[SyshostFile](variable_reader.SyshostFile)

VariableReader.SysmacroFile = VariableReader1[SysmacroFile](variable_reader.SysmacroFile)

VariableReader.SysmastFile = VariableReader1[SysmastFile](variable_reader.SysmastFile)

VariableReader.SyspassFile = VariableReader1[SyspassFile](variable_reader.SyspassFile)

VariableReader.SysservoFile = VariableReader1[SysservoFile](variable_reader.SysservoFile)

VariableReader.SystemFile = VariableReader1[SystemFile](variable_reader.SystemFile)

VariableReader.SysuifFile = VariableReader1[SysuifFile](variable_reader.SysuifFile)

VariableReader.TpsnapFile = VariableReader1[TpsnapFile](variable_reader.TpsnapFile)

VariableReader.VcmrinitFile = VariableReader1[VcmrinitFile](variable_reader.VcmrinitFile)
