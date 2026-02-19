import typing
from UnderAutomation.Fanuc.Rmi.Data import JointAngles as joint_angles

class JointAngles:
	'''Joint angle set. Unused joints default to 0 if the robot has fewer than 9 axes.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_angles()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def j1(self) -> float:
		'''Joint 1 angle.'''
		return self._instance.J1

	@j1.setter
	def j1(self, value: float):
		self._instance.J1 = value

	@property
	def j2(self) -> float:
		'''Joint 2 angle.'''
		return self._instance.J2

	@j2.setter
	def j2(self, value: float):
		self._instance.J2 = value

	@property
	def j3(self) -> float:
		'''Joint 3 angle.'''
		return self._instance.J3

	@j3.setter
	def j3(self, value: float):
		self._instance.J3 = value

	@property
	def j4(self) -> float:
		'''Joint 4 angle.'''
		return self._instance.J4

	@j4.setter
	def j4(self, value: float):
		self._instance.J4 = value

	@property
	def j5(self) -> float:
		'''Joint 5 angle.'''
		return self._instance.J5

	@j5.setter
	def j5(self, value: float):
		self._instance.J5 = value

	@property
	def j6(self) -> float:
		'''Joint 6 angle.'''
		return self._instance.J6

	@j6.setter
	def j6(self, value: float):
		self._instance.J6 = value

	@property
	def j7(self) -> float:
		'''Joint 7 angle (optional extended axis).'''
		return self._instance.J7

	@j7.setter
	def j7(self, value: float):
		self._instance.J7 = value

	@property
	def j8(self) -> float:
		'''Joint 8 angle (optional extended axis).'''
		return self._instance.J8

	@j8.setter
	def j8(self, value: float):
		self._instance.J8 = value

	@property
	def j9(self) -> float:
		'''Joint 9 angle (optional extended axis).'''
		return self._instance.J9

	@j9.setter
	def j9(self, value: float):
		self._instance.J9 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointAngles):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
