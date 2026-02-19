import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PrgadjVariableType as prgadj_variable_type

class PrgadjVariableType(GenericVariableType):
	'''Describes the Fanuc type PRGADJ_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgadj_variable_type()
		else:
			self._instance = _internal

	@property
	def x_limit(self) -> float:
		'''Value of variable $X_LIMIT'''
		return self._instance.XLimit

	@property
	def y_limit(self) -> float:
		'''Value of variable $Y_LIMIT'''
		return self._instance.YLimit

	@property
	def z_limit(self) -> float:
		'''Value of variable $Z_LIMIT'''
		return self._instance.ZLimit

	@property
	def w_limit(self) -> float:
		'''Value of variable $W_LIMIT'''
		return self._instance.WLimit

	@property
	def p_limit(self) -> float:
		'''Value of variable $P_LIMIT'''
		return self._instance.PLimit

	@property
	def r_limit(self) -> float:
		'''Value of variable $R_LIMIT'''
		return self._instance.RLimit

	@property
	def speed_adj(self) -> int:
		'''Value of variable $SPEED_ADJ'''
		return self._instance.SpeedAdj

	@property
	def next_cycle(self) -> bool:
		'''Value of variable $NEXT_CYCLE'''
		return self._instance.NextCycle

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrgadjVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
