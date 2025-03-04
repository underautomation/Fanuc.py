import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TppMonVariableType as tpp_mon_variable_type

class TppMonVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpp_mon_variable_type()
		else:
			self._instance = _internal
	@property
	def global_mt(self) -> int:
		return self._instance.GlobalMt
	@property
	def local_mt(self) -> int:
		return self._instance.LocalMt
	@property
	def mon_num(self) -> int:
		return self._instance.MonNum
	@property
	def gmon_tid(self) -> int:
		return self._instance.GmonTid
	@property
	def sysmon_adr(self) -> int:
		return self._instance.SysmonAdr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
