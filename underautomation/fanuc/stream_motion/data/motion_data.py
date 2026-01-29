import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import MotionData as motion_data

class MotionData:
	def __init__(self, values: typing.List[float], _internal = 0):
		if(_internal == 0):
			self._instance = motion_data(values)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def values(self) -> typing.List[float]:
		return self._instance.Values
	@property
	def axis1(self) -> float:
		return self._instance.Axis1
	@axis1.setter
	def axis1(self, value: float):
		self._instance.Axis1 = value
	@property
	def axis2(self) -> float:
		return self._instance.Axis2
	@axis2.setter
	def axis2(self, value: float):
		self._instance.Axis2 = value
	@property
	def axis3(self) -> float:
		return self._instance.Axis3
	@axis3.setter
	def axis3(self, value: float):
		self._instance.Axis3 = value
	@property
	def axis4(self) -> float:
		return self._instance.Axis4
	@axis4.setter
	def axis4(self, value: float):
		self._instance.Axis4 = value
	@property
	def axis5(self) -> float:
		return self._instance.Axis5
	@axis5.setter
	def axis5(self, value: float):
		self._instance.Axis5 = value
	@property
	def axis6(self) -> float:
		return self._instance.Axis6
	@axis6.setter
	def axis6(self, value: float):
		self._instance.Axis6 = value
	@property
	def ext_axis1(self) -> float:
		return self._instance.ExtAxis1
	@ext_axis1.setter
	def ext_axis1(self, value: float):
		self._instance.ExtAxis1 = value
	@property
	def ext_axis2(self) -> float:
		return self._instance.ExtAxis2
	@ext_axis2.setter
	def ext_axis2(self, value: float):
		self._instance.ExtAxis2 = value
	@property
	def ext_axis3(self) -> float:
		return self._instance.ExtAxis3
	@ext_axis3.setter
	def ext_axis3(self, value: float):
		self._instance.ExtAxis3 = value
	@property
	def j1(self) -> float:
		return self._instance.J1
	@j1.setter
	def j1(self, value: float):
		self._instance.J1 = value
	@property
	def j2(self) -> float:
		return self._instance.J2
	@j2.setter
	def j2(self, value: float):
		self._instance.J2 = value
	@property
	def j3(self) -> float:
		return self._instance.J3
	@j3.setter
	def j3(self, value: float):
		self._instance.J3 = value
	@property
	def j4(self) -> float:
		return self._instance.J4
	@j4.setter
	def j4(self, value: float):
		self._instance.J4 = value
	@property
	def j5(self) -> float:
		return self._instance.J5
	@j5.setter
	def j5(self, value: float):
		self._instance.J5 = value
	@property
	def j6(self) -> float:
		return self._instance.J6
	@j6.setter
	def j6(self, value: float):
		self._instance.J6 = value
	@property
	def j7(self) -> float:
		return self._instance.J7
	@j7.setter
	def j7(self, value: float):
		self._instance.J7 = value
	@property
	def j8(self) -> float:
		return self._instance.J8
	@j8.setter
	def j8(self, value: float):
		self._instance.J8 = value
	@property
	def j9(self) -> float:
		return self._instance.J9
	@j9.setter
	def j9(self, value: float):
		self._instance.J9 = value
	@property
	def x(self) -> float:
		return self._instance.X
	@x.setter
	def x(self, value: float):
		self._instance.X = value
	@property
	def y(self) -> float:
		return self._instance.Y
	@y.setter
	def y(self, value: float):
		self._instance.Y = value
	@property
	def z(self) -> float:
		return self._instance.Z
	@z.setter
	def z(self, value: float):
		self._instance.Z = value
	@property
	def w(self) -> float:
		return self._instance.W
	@w.setter
	def w(self, value: float):
		self._instance.W = value
	@property
	def p(self) -> float:
		return self._instance.P
	@p.setter
	def p(self, value: float):
		self._instance.P = value
	@property
	def r(self) -> float:
		return self._instance.R
	@r.setter
	def r(self, value: float):
		self._instance.R = value
	@property
	def e1(self) -> float:
		return self._instance.E1
	@e1.setter
	def e1(self, value: float):
		self._instance.E1 = value
	@property
	def e2(self) -> float:
		return self._instance.E2
	@e2.setter
	def e2(self, value: float):
		self._instance.E2 = value
	@property
	def e3(self) -> float:
		return self._instance.E3
	@e3.setter
	def e3(self, value: float):
		self._instance.E3 = value
