import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Internal import RmiConnectParametersBase as rmi_connect_parameters_base

class RmiConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
	@property
	def read_timeout_ms(self) -> int:
		return self._instance.ReadTimeoutMs
	@read_timeout_ms.setter
	def read_timeout_ms(self, value: int):
		self._instance.ReadTimeoutMs = value
	@property
	def write_timeout_ms(self) -> int:
		return self._instance.WriteTimeoutMs
	@write_timeout_ms.setter
	def write_timeout_ms(self, value: int):
		self._instance.WriteTimeoutMs = value
	@property
	def defaul_t__port(self) -> int:
		return self._instance.DEFAULT_PORT
	@defaul_t__port.setter
	def defaul_t__port(self, value: int):
		self._instance.DEFAULT_PORT = value
	@property
	def defaul_t__rea_d__timeou_t__ms(self) -> int:
		return self._instance.DEFAULT_READ_TIMEOUT_MS
	@defaul_t__rea_d__timeou_t__ms.setter
	def defaul_t__rea_d__timeou_t__ms(self, value: int):
		self._instance.DEFAULT_READ_TIMEOUT_MS = value
	@property
	def defaul_t__writ_e__timeou_t__ms(self) -> int:
		return self._instance.DEFAULT_WRITE_TIMEOUT_MS
	@defaul_t__writ_e__timeou_t__ms.setter
	def defaul_t__writ_e__timeou_t__ms(self, value: int):
		self._instance.DEFAULT_WRITE_TIMEOUT_MS = value
