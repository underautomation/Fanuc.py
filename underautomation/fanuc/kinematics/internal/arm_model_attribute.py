import typing
from underautomation.fanuc.kinematics.i_dh_parameters import IDhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics.Internal import ArmModelAttribute as arm_model_attribute

class ArmModelAttribute(IDhParameters):
	def __init__(self, description: str, d4: float, d5: float, d6: float, a1: float, a2: float, a3: float, _internal = 0):
		if(_internal == 0):
			self._instance = arm_model_attribute(description, d4, d5, d6, a1, a2, a3)
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
