import typing
from underautomation.fanuc.kinematics.i_dh_parameters import IDhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics import Crx10iaLDhmParameters as crx10ia_l_dhm_parameters

class Crx10iaLDhmParameters(IDhParameters):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = crx10ia_l_dhm_parameters()
		else:
			self._instance = _internal
	@property
	def a1(self) -> float:
		return self._instance.A1
	@property
	def a2(self) -> float:
		return self._instance.A2
	@property
	def a3(self) -> float:
		return self._instance.A3
	@property
	def d4(self) -> float:
		return self._instance.D4
	@property
	def d5(self) -> float:
		return self._instance.D5
	@property
	def d6(self) -> float:
		return self._instance.D6
