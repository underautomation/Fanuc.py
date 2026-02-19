import typing
from UnderAutomation.Fanuc.Kinematics import IDhParameters as i_dh_parameters

class IDhParameters:
	'''Interface defining the Denavit-Hartenberg parameters for a 6-axis robot arm.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_dh_parameters()
		else:
			self._instance = _internal

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
		if not isinstance(other, IDhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
