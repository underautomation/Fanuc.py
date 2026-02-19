import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PgDefspdVariableType as pg_defspd_variable_type

class PgDefspdVariableType(GenericVariableType):
	'''Describes the Fanuc type PG_DEFSPD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pg_defspd_variable_type()
		else:
			self._instance = _internal

	@property
	def ap_def_spd(self) -> int:
		'''Value of variable $AP_DEF_SPD'''
		return self._instance.ApDefSpd

	@property
	def ap_def_unit(self) -> int:
		'''Value of variable $AP_DEF_UNIT'''
		return self._instance.ApDefUnit

	@property
	def dummy4(self) -> int:
		'''Value of variable $DUMMY4'''
		return self._instance.Dummy4

	@property
	def apsp_prexe(self) -> bool:
		'''Value of variable $APSP_PREXE'''
		return self._instance.ApspPrexe

	@property
	def dly_lastps(self) -> int:
		'''Value of variable $DLY_LASTPS'''
		return self._instance.DlyLastps

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PgDefspdVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
