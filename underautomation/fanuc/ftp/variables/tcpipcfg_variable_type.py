import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TcpipcfgVariableType as tcpipcfg_variable_type

class TcpipcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tcpipcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def arpsize(self) -> int:
		return self._instance.Arpsize
	@property
	def host_ipf(self) -> int:
		return self._instance.HostIpf
	@property
	def hw_mcfilter(self) -> int:
		return self._instance.HwMcfilter
	@property
	def def_interfa(self) -> int:
		return self._instance.DefInterfa
	@property
	def classmask(self) -> bool:
		return self._instance.Classmask
	@property
	def sho_netinfo(self) -> bool:
		return self._instance.ShoNetinfo
	@property
	def pps_int(self) -> int:
		return self._instance.PpsInt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
