import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DnssCfgVariableType as dnss_cfg_variable_type

class DnssCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DNSS_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dnss_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def iface_num(self) -> int:
		'''Value of variable $IFACE_NUM'''
		return self._instance.IfaceNum

	@property
	def dbg_level(self) -> int:
		'''Value of variable $DBG_LEVEL'''
		return self._instance.DbgLevel

	@property
	def dom_name(self) -> str:
		'''Value of variable $DOM_NAME'''
		return self._instance.DomName

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DnssCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
