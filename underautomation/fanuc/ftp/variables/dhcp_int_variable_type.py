import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DhcpIntVariableType as dhcp_int_variable_type

class DhcpIntVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dhcp_int_variable_type()
		else:
			self._instance = _internal
	@property
	def leasestrtim(self) -> int:
		return self._instance.Leasestrtim
	@property
	def leasestart(self) -> str:
		return self._instance.Leasestart
	@property
	def leaseendtim(self) -> int:
		return self._instance.Leaseendtim
	@property
	def leaseend(self) -> str:
		return self._instance.Leaseend
	@property
	def ipadd(self) -> str:
		return self._instance.Ipadd
	@property
	def routerip(self) -> str:
		return self._instance.Routerip
	@property
	def snmask(self) -> str:
		return self._instance.Snmask
	@property
	def status(self) -> str:
		return self._instance.Status
	@property
	def statnum(self) -> int:
		return self._instance.Statnum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
