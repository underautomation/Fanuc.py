from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.dmr_grp_variable_type import DmrGrpVariableType
from underautomation.fanuc.common.files.variables.fms_grp_variable_type import FmsGrpVariableType
from underautomation.fanuc.common.files.variables.plcl_grp_variable_type import PlclGrpVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SysmastFile as sysmast_file

class SysmastFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysmast.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysmast_file()
		else:
			self._instance = _internal

	@property
	def dmr_grp(self) -> typing.List[DmrGrpVariableType]:
		'''Value of variable $DMR_GRP'''
		__r = self._instance.DmrGrp
		return None if __r is None else [None if x is None else DmrGrpVariableType(x) for x in __r]

	@property
	def fms_grp(self) -> typing.List[FmsGrpVariableType]:
		'''Value of variable $FMS_GRP'''
		__r = self._instance.FmsGrp
		return None if __r is None else [None if x is None else FmsGrpVariableType(x) for x in __r]

	@property
	def plcl_grp(self) -> typing.List[PlclGrpVariableType]:
		'''Value of variable $PLCL_GRP'''
		__r = self._instance.PlclGrp
		return None if __r is None else [None if x is None else PlclGrpVariableType(x) for x in __r]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysmastFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
