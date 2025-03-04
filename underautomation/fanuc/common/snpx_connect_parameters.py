import typing
from underautomation.fanuc.snpx.internal.snpx_connect_parameters_base import SnpxConnectParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import SnpxConnectParameters as snpx_connect_parameters

class SnpxConnectParameters(SnpxConnectParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
