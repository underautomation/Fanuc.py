import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import IDhParameters as i_dh_parameters

class IDhParameters:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_dh_parameters()
		else:
			self._instance = _internal
	@property
	def d4(self) -> float:
		return self._instance.D4
	@property
	def d5(self) -> float:
		return self._instance.D5
	@property
	def d6(self) -> float:
		return self._instance.D6
	@property
	def a1(self) -> float:
		return self._instance.A1
	@property
	def a2(self) -> float:
		return self._instance.A2
	@property
	def a3(self) -> float:
		return self._instance.A3
