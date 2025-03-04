import typing
from underautomation.fanuc.ftp.variables.cpidebug_variable_type import CpidebugVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpdbgVariableType as cpdbg_variable_type

class CpdbgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpdbg_variable_type()
		else:
			self._instance = _internal
	@property
	def output(self) -> bool:
		return self._instance.Output
	@property
	def cpidebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Cpidebug)
	@property
	def cppdebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Cppdebug)
	@property
	def midebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Midebug)
	@property
	def mpdebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Mpdebug)
	@property
	def mgdebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Mgdebug)
	@property
	def mfdebug(self) -> CpidebugVariableType:
		return CpidebugVariableType(self._instance.Mfdebug)
	@property
	def simqstop(self) -> bool:
		return self._instance.Simqstop
	@property
	def keep(self) -> bool:
		return self._instance.Keep
	@property
	def path(self) -> str:
		return self._instance.Path
	@property
	def extra1(self) -> int:
		return self._instance.Extra1
	@property
	def extra2(self) -> int:
		return self._instance.Extra2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
