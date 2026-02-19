import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UsrtolGrpVariableType as usrtol_grp_variable_type

class UsrtolGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type USRTOL_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usrtol_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def dist_tol(self) -> float:
		'''Value of variable $DIST_TOL'''
		return self._instance.DistTol

	@property
	def ornt_tol(self) -> float:
		'''Value of variable $ORNT_TOL'''
		return self._instance.OrntTol

	@property
	def raux_tol(self) -> float:
		'''Value of variable $RAUX_TOL'''
		return self._instance.RauxTol

	@property
	def taux_tol(self) -> float:
		'''Value of variable $TAUX_TOL'''
		return self._instance.TauxTol

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UsrtolGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
