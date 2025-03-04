import typing
from underautomation.fanuc.snpx.internal.snpx_writable_assignable_elements_2 import SnpxWritableAssignableElements2
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import StringRegisters as string_registers

class StringRegisters(SnpxWritableAssignableElements2[str, int]):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_registers()
		else:
			self._instance = _internal
