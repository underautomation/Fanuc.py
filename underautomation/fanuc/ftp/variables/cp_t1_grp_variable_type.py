import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpT1GrpVariableType as cp_t1_grp_variable_type

class CpT1GrpVariableType(GenericVariableType):
	'''Describes the Fanuc type CP_T1_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_t1_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def pred_sf_acc(self) -> float:
		'''Value of variable $PRED_SF_ACC'''
		return self._instance.PredSfAcc

	@property
	def pred_sf_jrk(self) -> float:
		'''Value of variable $PRED_SF_JRK'''
		return self._instance.PredSfJrk

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpT1GrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
