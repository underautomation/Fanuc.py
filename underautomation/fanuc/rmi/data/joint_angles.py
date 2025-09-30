import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import JointAngles as joint_angles

class JointAngles:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_angles()
		else:
			self._instance = _internal
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
