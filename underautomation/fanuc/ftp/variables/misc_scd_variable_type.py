import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MiscScdVariableType as misc_scd_variable_type

class MiscScdVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = misc_scd_variable_type()
		else:
			self._instance = _internal
	@property
	def dstb_max_a(self) -> typing.List[float]:
		return self._instance.DstbMaxA
	@property
	def dstb_min_a(self) -> typing.List[float]:
		return self._instance.DstbMinA
	@property
	def dstb_maxenb(self) -> typing.List[bool]:
		return self._instance.DstbMaxenb
	@property
	def dstb_minenb(self) -> typing.List[bool]:
		return self._instance.DstbMinenb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
