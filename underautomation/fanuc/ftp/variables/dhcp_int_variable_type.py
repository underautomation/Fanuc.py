import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DhcpIntVariableType as dhcp_int_variable_type

class DhcpIntVariableType(GenericVariableType):
	'''Describes the Fanuc type DHCP_INT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dhcp_int_variable_type()
		else:
			self._instance = _internal

	@property
	def leasestrtim(self) -> int:
		'''Value of variable $LEASESTRTIM'''
		return self._instance.Leasestrtim

	@property
	def leasestart(self) -> str:
		'''Value of variable $LEASESTART'''
		return self._instance.Leasestart

	@property
	def leaseendtim(self) -> int:
		'''Value of variable $LEASEENDTIM'''
		return self._instance.Leaseendtim

	@property
	def leaseend(self) -> str:
		'''Value of variable $LEASEEND'''
		return self._instance.Leaseend

	@property
	def ipadd(self) -> str:
		'''Value of variable $IPADD'''
		return self._instance.Ipadd

	@property
	def routerip(self) -> str:
		'''Value of variable $ROUTERIP'''
		return self._instance.Routerip

	@property
	def snmask(self) -> str:
		'''Value of variable $SNMASK'''
		return self._instance.Snmask

	@property
	def status(self) -> str:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def statnum(self) -> int:
		'''Value of variable $STATNUM'''
		return self._instance.Statnum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DhcpIntVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
