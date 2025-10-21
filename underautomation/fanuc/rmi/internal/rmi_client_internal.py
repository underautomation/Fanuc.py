import typing
from underautomation.fanuc.rmi.internal.rmi_client_base import RmiClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Internal import RmiClientInternal as rmi_client_internal

class RmiClientInternal(RmiClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_client_internal()
		else:
			self._instance = _internal
