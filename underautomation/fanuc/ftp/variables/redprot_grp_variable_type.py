import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RedprotGrpVariableType as redprot_grp_variable_type

class RedprotGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = redprot_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def pct_rem(self) -> typing.List[float]:
		return self._instance.PctRem
	@property
	def rst_date(self) -> typing.List[int]:
		return self._instance.RstDate
	@property
	def rst_rem(self) -> typing.List[float]:
		return self._instance.RstRem
	@property
	def red_reset(self) -> typing.List[bool]:
		return self._instance.RedReset
	@property
	def last_pct(self) -> typing.List[float]:
		return self._instance.LastPct
	@property
	def last_prog(self) -> str:
		return self._instance.LastProg
	@property
	def last_lvl(self) -> int:
		return self._instance.LastLvl
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
