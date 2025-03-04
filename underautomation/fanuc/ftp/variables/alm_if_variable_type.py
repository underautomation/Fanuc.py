import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AlmIfVariableType as alm_if_variable_type

class AlmIfVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = alm_if_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def last_alm(self) -> str:
		return self._instance.LastAlm
	@property
	def last_ualm(self) -> str:
		return self._instance.LastUalm
	@property
	def kalm_max(self) -> int:
		return self._instance.KalmMax
	@property
	def ldebug(self) -> typing.List[int]:
		return self._instance.Ldebug
	@property
	def prog_stat(self) -> str:
		return self._instance.ProgStat
	@property
	def curr_prog(self) -> str:
		return self._instance.CurrProg
	@property
	def curr_line(self) -> int:
		return self._instance.CurrLine
	@property
	def curr_stat(self) -> str:
		return self._instance.CurrStat
	@property
	def last_cause(self) -> str:
		return self._instance.LastCause
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
