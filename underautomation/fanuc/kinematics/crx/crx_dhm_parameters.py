import typing
from underautomation.fanuc.kinematics.crx.i_crx_dhm_parameters import ICrxDhmParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Kinematics.Crx import CrxDhmParameters as crx_dhm_parameters

class CrxDhmParameters(ICrxDhmParameters):
	def __init__(self, a1: float, r4: float, r5: float, r6: float, _internal = 0):
		if(_internal == 0):
			self._instance = crx_dhm_parameters(a1, r4, r5, r6)
		else:
			self._instance = _internal
	@property
	def a2(self) -> float:
		return self._instance.A2
	@a2.setter
	def a2(self, value: float):
		self._instance.A2 = value
	@property
	def d4(self) -> float:
		return self._instance.D4
	@d4.setter
	def d4(self, value: float):
		self._instance.D4 = value
	@property
	def d5(self) -> float:
		return self._instance.D5
	@d5.setter
	def d5(self, value: float):
		self._instance.D5 = value
	@property
	def d6(self) -> float:
		return self._instance.D6
	@d6.setter
	def d6(self, value: float):
		self._instance.D6 = value
