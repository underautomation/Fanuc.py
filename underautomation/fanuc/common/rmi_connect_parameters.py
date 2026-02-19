import typing
from underautomation.fanuc.rmi.internal.rmi_connect_parameters_base import RmiConnectParametersBase
from UnderAutomation.Fanuc.Common import RmiConnectParameters as rmi_connect_parameters

class RmiConnectParameters(RmiConnectParametersBase):
	'''RMI parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should enable RMI for this connection (default: false)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
