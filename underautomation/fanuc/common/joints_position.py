import typing
from UnderAutomation.Fanuc.Common import JointsPosition as joints_position

class JointsPosition:
	'''Joints position in degrees'''
	def __init__(self, j1Deg: float, j2Deg: float, j3Deg: float, j4Deg: float, j5Deg: float, j6Deg: float, j7Deg: float, j8Deg: float, j9Deg: float, _internal = 0):
		'''Constructor with 9 joint values in degrees'''
		if(_internal == 0):
			self._instance = joints_position(j1Deg, j2Deg, j3Deg, j4Deg, j5Deg, j6Deg, j7Deg, j8Deg, j9Deg)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@staticmethod
	def is_near(j1: 'JointsPosition', j2: 'JointsPosition', degreesTolerance: float) -> bool:
		'''Check if joints position is near to expected joints position with a tolerance value'''
		return joints_position.IsNear(j1._instance if j1 else None, j2._instance if j2 else None, degreesTolerance)

	@property
	def item(self) -> float:
		return self._instance.Item

	@item.setter
	def item(self, value: float):
		self._instance.Item = value

	@property
	def values(self) -> typing.List[float]:
		'''Numeric values for each joints'''
		return self._instance.Values

	@property
	def j1(self) -> float:
		'''Joint 1 in degrees'''
		return self._instance.J1

	@j1.setter
	def j1(self, value: float):
		self._instance.J1 = value

	@property
	def j2(self) -> float:
		'''Joint 2 in degrees'''
		return self._instance.J2

	@j2.setter
	def j2(self, value: float):
		self._instance.J2 = value

	@property
	def j3(self) -> float:
		'''Joint 3 in degrees'''
		return self._instance.J3

	@j3.setter
	def j3(self, value: float):
		self._instance.J3 = value

	@property
	def j4(self) -> float:
		'''Joint 4 in degrees'''
		return self._instance.J4

	@j4.setter
	def j4(self, value: float):
		self._instance.J4 = value

	@property
	def j5(self) -> float:
		'''Joint 5 in degrees'''
		return self._instance.J5

	@j5.setter
	def j5(self, value: float):
		self._instance.J5 = value

	@property
	def j6(self) -> float:
		'''Joint 6 in degrees'''
		return self._instance.J6

	@j6.setter
	def j6(self, value: float):
		self._instance.J6 = value

	@property
	def j7(self) -> float:
		'''Joint 7 in degrees'''
		return self._instance.J7

	@j7.setter
	def j7(self, value: float):
		self._instance.J7 = value

	@property
	def j8(self) -> float:
		'''Joint 8 in degrees'''
		return self._instance.J8

	@j8.setter
	def j8(self, value: float):
		self._instance.J8 = value

	@property
	def j9(self) -> float:
		'''Joint 9 in degrees'''
		return self._instance.J9

	@j9.setter
	def j9(self, value: float):
		self._instance.J9 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointsPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
