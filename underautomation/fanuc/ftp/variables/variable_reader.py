import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.variables.generic_variable import GenericVariable
from underautomation.fanuc.ftp.variables.variable_reader_1 import VariableReader1
from underautomation.fanuc.ftp.internal.file_reader_1 import FileReader1
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
from UnderAutomation.Fanuc.Ftp.Variables import VariableReader as variable_reader
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
