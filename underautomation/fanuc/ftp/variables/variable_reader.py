import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
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
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VariableReader as variable_reader

T = typing.TypeVar('T')
class VariableReader(FileReader1[GenericVariableFile]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = variable_reader()
		else:
			self._instance = _internal
	def read_file(self, fileStream: typing.Any, fileName: str) -> GenericVariableFile:
		return GenericVariableFile(self._instance.ReadFile(fileStream, fileName))
	@staticmethod
	def read_variable_file(fileStream: typing.Any, fileName: str) -> GenericVariableFile:
		return GenericVariableFile(variable_reader.ReadVariableFile(fileStream, fileName))
	@staticmethod
	def parse_variable_file(stream: typing.Any) -> typing.List[GenericVariable]:
		return [GenericVariable(x) for x in variable_reader.ParseVariableFile(stream)]
	@property
	def aavmmain_file(self) -> VariableReader1[AavmmainFile]:
		return VariableReader1[AavmmainFile](self._instance.AavmmainFile)
	@property
	def bicsetup_file(self) -> VariableReader1[BicsetupFile]:
		return VariableReader1[BicsetupFile](self._instance.BicsetupFile)
	@property
	def cbparam_file(self) -> VariableReader1[CbparamFile]:
		return VariableReader1[CbparamFile](self._instance.CbparamFile)
	@property
	def cellio_file(self) -> VariableReader1[CellioFile]:
		return VariableReader1[CellioFile](self._instance.CellioFile)
	@property
	def comset_file(self) -> VariableReader1[ComsetFile]:
		return VariableReader1[ComsetFile](self._instance.ComsetFile)
	@property
	def diocfgsv_file(self) -> VariableReader1[DiocfgsvFile]:
		return VariableReader1[DiocfgsvFile](self._instance.DiocfgsvFile)
	@property
	def gemdata_file(self) -> VariableReader1[GemdataFile]:
		return VariableReader1[GemdataFile](self._instance.GemdataFile)
	@property
	def htcolrec_file(self) -> VariableReader1[HtcolrecFile]:
		return VariableReader1[HtcolrecFile](self._instance.HtcolrecFile)
	@property
	def httpkcl_file(self) -> VariableReader1[HttpkclFile]:
		return VariableReader1[HttpkclFile](self._instance.HttpkclFile)
	@property
	def irc_counter_file(self) -> VariableReader1[IrcCounterFile]:
		return VariableReader1[IrcCounterFile](self._instance.IrcCounterFile)
	@property
	def irc_msg_file(self) -> VariableReader1[IrcMsgFile]:
		return VariableReader1[IrcMsgFile](self._instance.IrcMsgFile)
	@property
	def irc_status_file(self) -> VariableReader1[IrcStatusFile]:
		return VariableReader1[IrcStatusFile](self._instance.IrcStatusFile)
	@property
	def irc_stlabel_file(self) -> VariableReader1[IrcStlabelFile]:
		return VariableReader1[IrcStlabelFile](self._instance.IrcStlabelFile)
	@property
	def klaction_file(self) -> VariableReader1[KlactionFile]:
		return VariableReader1[KlactionFile](self._instance.KlactionFile)
	@property
	def mixlogic_file(self) -> VariableReader1[MixlogicFile]:
		return VariableReader1[MixlogicFile](self._instance.MixlogicFile)
	@property
	def mtparam_file(self) -> VariableReader1[MtparamFile]:
		return VariableReader1[MtparamFile](self._instance.MtparamFile)
	@property
	def numreg_file(self) -> VariableReader1[NumregFile]:
		return VariableReader1[NumregFile](self._instance.NumregFile)
	@property
	def palreg_file(self) -> VariableReader1[PalregFile]:
		return VariableReader1[PalregFile](self._instance.PalregFile)
	@property
	def posreg_file(self) -> VariableReader1[PosregFile]:
		return VariableReader1[PosregFile](self._instance.PosregFile)
	@property
	def strreg_file(self) -> VariableReader1[StrregFile]:
		return VariableReader1[StrregFile](self._instance.StrregFile)
	@property
	def swiupdt_file(self) -> VariableReader1[SwiupdtFile]:
		return VariableReader1[SwiupdtFile](self._instance.SwiupdtFile)
	@property
	def sycldint_file(self) -> VariableReader1[SycldintFile]:
		return VariableReader1[SycldintFile](self._instance.SycldintFile)
	@property
	def symotn_file(self) -> VariableReader1[SymotnFile]:
		return VariableReader1[SymotnFile](self._instance.SymotnFile)
	@property
	def synosave_file(self) -> VariableReader1[SynosaveFile]:
		return VariableReader1[SynosaveFile](self._instance.SynosaveFile)
	@property
	def sysframe_file(self) -> VariableReader1[SysframeFile]:
		return VariableReader1[SysframeFile](self._instance.SysframeFile)
	@property
	def sysfsac_file(self) -> VariableReader1[SysfsacFile]:
		return VariableReader1[SysfsacFile](self._instance.SysfsacFile)
	@property
	def syshost_file(self) -> VariableReader1[SyshostFile]:
		return VariableReader1[SyshostFile](self._instance.SyshostFile)
	@property
	def sysmacro_file(self) -> VariableReader1[SysmacroFile]:
		return VariableReader1[SysmacroFile](self._instance.SysmacroFile)
	@property
	def sysmast_file(self) -> VariableReader1[SysmastFile]:
		return VariableReader1[SysmastFile](self._instance.SysmastFile)
	@property
	def syspass_file(self) -> VariableReader1[SyspassFile]:
		return VariableReader1[SyspassFile](self._instance.SyspassFile)
	@property
	def sysservo_file(self) -> VariableReader1[SysservoFile]:
		return VariableReader1[SysservoFile](self._instance.SysservoFile)
	@property
	def system_file(self) -> VariableReader1[SystemFile]:
		return VariableReader1[SystemFile](self._instance.SystemFile)
	@property
	def sysuif_file(self) -> VariableReader1[SysuifFile]:
		return VariableReader1[SysuifFile](self._instance.SysuifFile)
	@property
	def tpsnap_file(self) -> VariableReader1[TpsnapFile]:
		return VariableReader1[TpsnapFile](self._instance.TpsnapFile)
	@property
	def vcmrinit_file(self) -> VariableReader1[VcmrinitFile]:
		return VariableReader1[VcmrinitFile](self._instance.VcmrinitFile)
