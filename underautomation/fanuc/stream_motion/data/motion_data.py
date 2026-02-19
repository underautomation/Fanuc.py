import typing
from UnderAutomation.Fanuc.StreamMotion.Data import MotionData as motion_data

class MotionData:
	'''Motion data containing 9 axis values (joint or cartesian + extended axes)'''
	def __init__(self, values: typing.List[float], _internal = 0):
		'''Constructor with initial values'''
		if(_internal == 0):
			self._instance = motion_data(values)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def values(self) -> typing.List[float]:
		'''Raw axis values (9 values: J1-J6 or X,Y,Z,W,P,R + E1,E2,E3)'''
		return self._instance.Values

	@property
	def axis1(self) -> float:
		'''First axis (J1 or X)'''
		return self._instance.Axis1

	@axis1.setter
	def axis1(self, value: float):
		self._instance.Axis1 = value

	@property
	def axis2(self) -> float:
		'''Second axis (J2 or Y)'''
		return self._instance.Axis2

	@axis2.setter
	def axis2(self, value: float):
		self._instance.Axis2 = value

	@property
	def axis3(self) -> float:
		'''Third axis (J3 or Z)'''
		return self._instance.Axis3

	@axis3.setter
	def axis3(self, value: float):
		self._instance.Axis3 = value

	@property
	def axis4(self) -> float:
		'''Fourth axis (J4 or W)'''
		return self._instance.Axis4

	@axis4.setter
	def axis4(self, value: float):
		self._instance.Axis4 = value

	@property
	def axis5(self) -> float:
		'''Fifth axis (J5 or P)'''
		return self._instance.Axis5

	@axis5.setter
	def axis5(self, value: float):
		self._instance.Axis5 = value

	@property
	def axis6(self) -> float:
		'''Sixth axis (J6 or R)'''
		return self._instance.Axis6

	@axis6.setter
	def axis6(self, value: float):
		self._instance.Axis6 = value

	@property
	def ext_axis1(self) -> float:
		'''Extended axis 1'''
		return self._instance.ExtAxis1

	@ext_axis1.setter
	def ext_axis1(self, value: float):
		self._instance.ExtAxis1 = value

	@property
	def ext_axis2(self) -> float:
		'''Extended axis 2'''
		return self._instance.ExtAxis2

	@ext_axis2.setter
	def ext_axis2(self, value: float):
		self._instance.ExtAxis2 = value

	@property
	def ext_axis3(self) -> float:
		'''Extended axis 3'''
		return self._instance.ExtAxis3

	@ext_axis3.setter
	def ext_axis3(self, value: float):
		self._instance.ExtAxis3 = value

	@property
	def j1(self) -> float:
		'''J1 (same as Axis1)'''
		return self._instance.J1

	@j1.setter
	def j1(self, value: float):
		self._instance.J1 = value

	@property
	def j2(self) -> float:
		'''J2 (same as Axis2)'''
		return self._instance.J2

	@j2.setter
	def j2(self, value: float):
		self._instance.J2 = value

	@property
	def j3(self) -> float:
		'''J3 (same as Axis3)'''
		return self._instance.J3

	@j3.setter
	def j3(self, value: float):
		self._instance.J3 = value

	@property
	def j4(self) -> float:
		'''J4 (same as Axis4)'''
		return self._instance.J4

	@j4.setter
	def j4(self, value: float):
		self._instance.J4 = value

	@property
	def j5(self) -> float:
		'''J5 (same as Axis5)'''
		return self._instance.J5

	@j5.setter
	def j5(self, value: float):
		self._instance.J5 = value

	@property
	def j6(self) -> float:
		'''J6 (same as Axis6)'''
		return self._instance.J6

	@j6.setter
	def j6(self, value: float):
		self._instance.J6 = value

	@property
	def j7(self) -> float:
		'''J7 (same as ExtAxis1)'''
		return self._instance.J7

	@j7.setter
	def j7(self, value: float):
		self._instance.J7 = value

	@property
	def j8(self) -> float:
		'''J8 (same as ExtAxis2)'''
		return self._instance.J8

	@j8.setter
	def j8(self, value: float):
		self._instance.J8 = value

	@property
	def j9(self) -> float:
		'''J9 (same as ExtAxis3)'''
		return self._instance.J9

	@j9.setter
	def j9(self, value: float):
		self._instance.J9 = value

	@property
	def x(self) -> float:
		'''X (same as Axis1) in mm'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y (same as Axis2) in mm'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z (same as Axis3) in mm'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def w(self) -> float:
		'''W (same as Axis4) in degrees'''
		return self._instance.W

	@w.setter
	def w(self, value: float):
		self._instance.W = value

	@property
	def p(self) -> float:
		'''P (same as Axis5) in degrees'''
		return self._instance.P

	@p.setter
	def p(self, value: float):
		self._instance.P = value

	@property
	def r(self) -> float:
		'''R (same as Axis6) in degrees'''
		return self._instance.R

	@r.setter
	def r(self, value: float):
		self._instance.R = value

	@property
	def e1(self) -> float:
		'''E1 (same as ExtAxis1)'''
		return self._instance.E1

	@e1.setter
	def e1(self, value: float):
		self._instance.E1 = value

	@property
	def e2(self) -> float:
		'''E2 (same as ExtAxis2)'''
		return self._instance.E2

	@e2.setter
	def e2(self, value: float):
		self._instance.E2 = value

	@property
	def e3(self) -> float:
		'''E3 (same as ExtAxis3)'''
		return self._instance.E3

	@e3.setter
	def e3(self, value: float):
		self._instance.E3 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
