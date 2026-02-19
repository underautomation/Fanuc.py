import typing
from underautomation.fanuc.kinematics.i_dh_parameters import IDhParameters
from UnderAutomation.Fanuc.Kinematics.Internal import ArmModelAttribute as arm_model_attribute

class ArmModelAttribute(IDhParameters):
	'''Attribute that associates DH parameters with an arm kinematic model enum value.'''
	def __init__(self, description: str, d4: float, d5: float, d6: float, a1: float, a2: float, a3: float, _internal = 0):
		'''Initializes a new instance of ArmModelAttribute with the specified description and DH parameters.

		:param description: The human-readable model name.
		:param d4: DH parameter D4 (mm).
		:param d5: DH parameter D5 (mm).
		:param d6: DH parameter D6 (mm).
		:param a1: DH parameter A1 (mm).
		:param a2: DH parameter A2 (mm).
		:param a3: DH parameter A3 (mm).
		'''
		if(_internal == 0):
			self._instance = arm_model_attribute(description, d4, d5, d6, a1, a2, a3)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def d4(self) -> float:
		'''DH parameter D4 (mm).'''
		return self._instance.D4

	@property
	def d5(self) -> float:
		'''DH parameter D5 (mm).'''
		return self._instance.D5

	@property
	def d6(self) -> float:
		'''DH parameter D6 (mm).'''
		return self._instance.D6

	@property
	def a1(self) -> float:
		'''DH parameter A1 (mm).'''
		return self._instance.A1

	@property
	def a2(self) -> float:
		'''DH parameter A2 (mm).'''
		return self._instance.A2

	@property
	def a3(self) -> float:
		'''DH parameter A3 (mm).'''
		return self._instance.A3

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ArmModelAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
