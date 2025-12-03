import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxConnectParametersBase as snpx_connect_parameters_base

class SnpxConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value

SnpxConnectParametersBase.defaul_t__port = SnpxConnectParametersBase(snpx_connect_parameters_base.DEFAULT_PORT)
