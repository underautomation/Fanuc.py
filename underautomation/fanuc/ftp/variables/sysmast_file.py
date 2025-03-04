import typing
from underautomation.fanuc.ftp.variables.dmr_grp_variable_type import DmrGrpVariableType
from underautomation.fanuc.ftp.variables.fms_grp_variable_type import FmsGrpVariableType
from underautomation.fanuc.ftp.variables.plcl_grp_variable_type import PlclGrpVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysmastFile as sysmast_file

class SysmastFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysmast_file()
		else:
			self._instance = _internal
	@property
	def dmr_grp(self) -> typing.List[DmrGrpVariableType]:
		return [DmrGrpVariableType(x) for x in self._instance.DmrGrp]
	@property
	def fms_grp(self) -> typing.List[FmsGrpVariableType]:
		return [FmsGrpVariableType(x) for x in self._instance.FmsGrp]
	@property
	def plcl_grp(self) -> typing.List[PlclGrpVariableType]:
		return [PlclGrpVariableType(x) for x in self._instance.PlclGrp]
