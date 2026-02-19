import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RedprotGrpVariableType as redprot_grp_variable_type

class RedprotGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type REDPROT_GRP_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = redprot_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def pct_rem(self) -> typing.List[float]:
		'''Value of variable $PCT_REM'''
		return self._instance.PctRem

	@property
	def rst_date(self) -> typing.List[int]:
		'''Value of variable $RST_DATE'''
		return self._instance.RstDate

	@property
	def rst_rem(self) -> typing.List[float]:
		'''Value of variable $RST_REM'''
		return self._instance.RstRem

	@property
	def red_reset(self) -> typing.List[bool]:
		'''Value of variable $RED_RESET'''
		return self._instance.RedReset

	@property
	def last_pct(self) -> typing.List[float]:
		'''Value of variable $LAST_PCT'''
		return self._instance.LastPct

	@property
	def last_prog(self) -> str:
		'''Value of variable $LAST_PROG'''
		return self._instance.LastProg

	@property
	def last_lvl(self) -> int:
		'''Value of variable $LAST_LVL'''
		return self._instance.LastLvl

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RedprotGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
