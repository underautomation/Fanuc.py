import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import BinCfgVariableType as bin_cfg_variable_type

class BinCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bin_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def entries(self) -> int:
		return self._instance.Entries
	@property
	def q0fp(self) -> int:
		return self._instance.Q0fp
	@property
	def q0np(self) -> int:
		return self._instance.Q0np
	@property
	def q1fp(self) -> int:
		return self._instance.Q1fp
	@property
	def q1np(self) -> int:
		return self._instance.Q1np
	@property
	def q2fp(self) -> int:
		return self._instance.Q2fp
	@property
	def q2np(self) -> int:
		return self._instance.Q2np
	@property
	def pppp(self) -> int:
		return self._instance.Pppp
	@property
	def cnetp(self) -> int:
		return self._instance.Cnetp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
