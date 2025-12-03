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

VariableReader.aavmmain_file = VariableReader(variable_reader.AavmmainFile)

VariableReader.bicsetup_file = VariableReader(variable_reader.BicsetupFile)

VariableReader.cbparam_file = VariableReader(variable_reader.CbparamFile)

VariableReader.cellio_file = VariableReader(variable_reader.CellioFile)

VariableReader.comset_file = VariableReader(variable_reader.ComsetFile)

VariableReader.diocfgsv_file = VariableReader(variable_reader.DiocfgsvFile)

VariableReader.gemdata_file = VariableReader(variable_reader.GemdataFile)

VariableReader.htcolrec_file = VariableReader(variable_reader.HtcolrecFile)

VariableReader.httpkcl_file = VariableReader(variable_reader.HttpkclFile)

VariableReader.irc_counter_file = VariableReader(variable_reader.IrcCounterFile)

VariableReader.irc_msg_file = VariableReader(variable_reader.IrcMsgFile)

VariableReader.irc_status_file = VariableReader(variable_reader.IrcStatusFile)

VariableReader.irc_stlabel_file = VariableReader(variable_reader.IrcStlabelFile)

VariableReader.klaction_file = VariableReader(variable_reader.KlactionFile)

VariableReader.mixlogic_file = VariableReader(variable_reader.MixlogicFile)

VariableReader.mtparam_file = VariableReader(variable_reader.MtparamFile)

VariableReader.numreg_file = VariableReader(variable_reader.NumregFile)

VariableReader.palreg_file = VariableReader(variable_reader.PalregFile)

VariableReader.posreg_file = VariableReader(variable_reader.PosregFile)

VariableReader.strreg_file = VariableReader(variable_reader.StrregFile)

VariableReader.swiupdt_file = VariableReader(variable_reader.SwiupdtFile)

VariableReader.sycldint_file = VariableReader(variable_reader.SycldintFile)

VariableReader.symotn_file = VariableReader(variable_reader.SymotnFile)

VariableReader.synosave_file = VariableReader(variable_reader.SynosaveFile)

VariableReader.sysframe_file = VariableReader(variable_reader.SysframeFile)

VariableReader.sysfsac_file = VariableReader(variable_reader.SysfsacFile)

VariableReader.syshost_file = VariableReader(variable_reader.SyshostFile)

VariableReader.sysmacro_file = VariableReader(variable_reader.SysmacroFile)

VariableReader.sysmast_file = VariableReader(variable_reader.SysmastFile)

VariableReader.syspass_file = VariableReader(variable_reader.SyspassFile)

VariableReader.sysservo_file = VariableReader(variable_reader.SysservoFile)

VariableReader.system_file = VariableReader(variable_reader.SystemFile)

VariableReader.sysuif_file = VariableReader(variable_reader.SysuifFile)

VariableReader.tpsnap_file = VariableReader(variable_reader.TpsnapFile)

VariableReader.vcmrinit_file = VariableReader(variable_reader.VcmrinitFile)
