import typing
from __future__ import annotation
from underautomation.fanuc.cgtp.internal.cgtp_connect_parameters_base import CgtpConnectParametersBase
from UnderAutomation.Fanuc.Common import CgtpConnectParameters as cgtp_connect_parameters

class CgtpConnectParameters(CgtpConnectParametersBase):
	'''CGTP Web Server connection parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should enable CGTP Web Server for this connection (default: true)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
