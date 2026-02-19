import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TppMonVariableType as tpp_mon_variable_type

class TppMonVariableType(GenericVariableType):
	'''Describes the Fanuc type TPP_MON_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpp_mon_variable_type()
		else:
			self._instance = _internal

	@property
	def global_mt(self) -> int:
		'''Value of variable $GLOBAL_MT'''
		return self._instance.GlobalMt

	@property
	def local_mt(self) -> int:
		'''Value of variable $LOCAL_MT'''
		return self._instance.LocalMt

	@property
	def mon_num(self) -> int:
		'''Value of variable $MON_NUM'''
		return self._instance.MonNum

	@property
	def gmon_tid(self) -> int:
		'''Value of variable $GMON_TID'''
		return self._instance.GmonTid

	@property
	def sysmon_adr(self) -> int:
		'''Value of variable $SYSMON_ADR'''
		return self._instance.SysmonAdr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TppMonVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
