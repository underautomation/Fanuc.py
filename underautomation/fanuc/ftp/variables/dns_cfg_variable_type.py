import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DnsCfgVariableType as dns_cfg_variable_type

class DnsCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DNS_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dns_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def primar_ip(self) -> str:
		'''Value of variable $PRIMAR_IP'''
		return self._instance.PrimarIp

	@property
	def altern_ip(self) -> str:
		'''Value of variable $ALTERN_IP'''
		return self._instance.AlternIp

	@property
	def retries(self) -> int:
		'''Value of variable $RETRIES'''
		return self._instance.Retries

	@property
	def wait_time(self) -> int:
		'''Value of variable $WAIT_TIME'''
		return self._instance.WaitTime

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DnsCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
