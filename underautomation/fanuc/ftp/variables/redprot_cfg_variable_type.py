import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RedprotCfgVariableType as redprot_cfg_variable_type

class RedprotCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type REDPROT_CFG_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = redprot_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def lvl2_pct(self) -> float:
		'''Value of variable $LVL2_PCT'''
		return self._instance.Lvl2Pct

	@property
	def lvl2_sev(self) -> int:
		'''Value of variable $LVL2_SEV'''
		return self._instance.Lvl2Sev

	@property
	def min_l10_cap(self) -> float:
		'''Value of variable $MIN_L10_CAP'''
		return self._instance.MinL10Cap

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RedprotCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
