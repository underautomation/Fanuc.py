import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_2 import SnpxWritableAssignableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import NumericRegisters as numeric_registers

class NumericRegisters(SnpxWritableAssignableElements2[float, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = numeric_registers()
		else:
			self._instance = _internal
