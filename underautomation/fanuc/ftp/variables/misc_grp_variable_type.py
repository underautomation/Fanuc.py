import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MiscGrpVariableType as misc_grp_variable_type

class MiscGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = misc_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def hpd_trq(self) -> typing.List[float]:
		return self._instance.HpdTrq
	@property
	def dstb_max(self) -> typing.List[int]:
		return self._instance.DstbMax
	@property
	def dstb_min(self) -> typing.List[int]:
		return self._instance.DstbMin
	@property
	def dstb_maxenb(self) -> typing.List[bool]:
		return self._instance.DstbMaxenb
	@property
	def dstb_minenb(self) -> typing.List[bool]:
		return self._instance.DstbMinenb
	@property
	def dstb_excess(self) -> bool:
		return self._instance.DstbExcess
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
