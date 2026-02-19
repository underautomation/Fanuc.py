import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import OnPathVariableType as on_path_variable_type

class OnPathVariableType(GenericVariableType):
	'''Describes the Fanuc type ON_PATH_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = on_path_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def status(self) -> bool:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def dist_diff(self) -> float:
		'''Value of variable $DIST_DIFF'''
		return self._instance.DistDiff

	@property
	def ornt_diff(self) -> float:
		'''Value of variable $ORNT_DIFF'''
		return self._instance.OrntDiff

	@property
	def dist_rec(self) -> float:
		'''Value of variable $DIST_REC'''
		return self._instance.DistRec

	@property
	def ornt_rec(self) -> float:
		'''Value of variable $ORNT_REC'''
		return self._instance.OrntRec

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, OnPathVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
