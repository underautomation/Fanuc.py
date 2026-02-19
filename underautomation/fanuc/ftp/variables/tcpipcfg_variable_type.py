import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TcpipcfgVariableType as tcpipcfg_variable_type

class TcpipcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type TCPIPCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tcpipcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def arpsize(self) -> int:
		'''Value of variable $ARPSIZE'''
		return self._instance.Arpsize

	@property
	def host_ipf(self) -> int:
		'''Value of variable $HOST_IPF'''
		return self._instance.HostIpf

	@property
	def hw_mcfilter(self) -> int:
		'''Value of variable $HW_MCFILTER'''
		return self._instance.HwMcfilter

	@property
	def def_interfa(self) -> int:
		'''Value of variable $DEF_INTERFA'''
		return self._instance.DefInterfa

	@property
	def classmask(self) -> bool:
		'''Value of variable $CLASSMASK'''
		return self._instance.Classmask

	@property
	def sho_netinfo(self) -> bool:
		'''Value of variable $SHO_NETINFO'''
		return self._instance.ShoNetinfo

	@property
	def pps_int(self) -> int:
		'''Value of variable $PPS_INT'''
		return self._instance.PpsInt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TcpipcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
