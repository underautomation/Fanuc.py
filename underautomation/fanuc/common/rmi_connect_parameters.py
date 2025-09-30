import typing
from underautomation.fanuc.rmi.internal.rmi_connect_parameters_base import RmiConnectParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import RmiConnectParameters as rmi_connect_parameters

class RmiConnectParameters(RmiConnectParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
