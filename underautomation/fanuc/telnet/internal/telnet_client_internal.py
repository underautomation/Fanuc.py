import typing
from underautomation.fanuc.telnet.internal.telnet_client_base import TelnetClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet.Internal import TelnetClientInternal as telnet_client_internal

class TelnetClientInternal(TelnetClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_client_internal()
		else:
			self._instance = _internal
