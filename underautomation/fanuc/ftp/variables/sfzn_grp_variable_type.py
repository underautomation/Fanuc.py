import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SfznGrpVariableType as sfzn_grp_variable_type

class SfznGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type SFZN_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sfzn_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def min_ovrd(self) -> float:
		'''Value of variable $MIN_OVRD'''
		return self._instance.MinOvrd

	@property
	def int_ang(self) -> float:
		'''Value of variable $INT_ANG'''
		return self._instance.IntAng

	@property
	def min_ang(self) -> float:
		'''Value of variable $MIN_ANG'''
		return self._instance.MinAng

	@property
	def face_spd(self) -> float:
		'''Value of variable $FACE_SPD'''
		return self._instance.FaceSpd

	@property
	def safe_spd(self) -> float:
		'''Value of variable $SAFE_SPD'''
		return self._instance.SafeSpd

	@property
	def mixed_spd(self) -> float:
		'''Value of variable $MIXED_SPD'''
		return self._instance.MixedSpd

	@property
	def mixed_ang(self) -> float:
		'''Value of variable $MIXED_ANG'''
		return self._instance.MixedAng

	@property
	def min_dist(self) -> float:
		'''Value of variable $MIN_DIST'''
		return self._instance.MinDist

	@property
	def rob_name(self) -> str:
		'''Value of variable $ROB_NAME'''
		return self._instance.RobName

	@property
	def need_app(self) -> int:
		'''Value of variable $NEED_APP'''
		return self._instance.NeedApp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SfznGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
