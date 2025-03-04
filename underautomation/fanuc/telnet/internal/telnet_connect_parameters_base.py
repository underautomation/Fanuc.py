import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet.Internal import TelnetConnectParametersBase as telnet_connect_parameters_base

class TelnetConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def telnet_kcl_password(self) -> str:
		return self._instance.TelnetKclPassword
	@telnet_kcl_password.setter
	def telnet_kcl_password(self, value: str):
		self._instance.TelnetKclPassword = value
