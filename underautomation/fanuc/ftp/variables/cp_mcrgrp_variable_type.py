import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpMcrgrpVariableType as cp_mcrgrp_variable_type

class CpMcrgrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_mcrgrp_variable_type()
		else:
			self._instance = _internal
	@property
	def rsm_jbf_pct(self) -> int:
		return self._instance.RsmJbfPct
	@property
	def rsm_dec_pct(self) -> int:
		return self._instance.RsmDecPct
	@property
	def rsm_ofs_pct(self) -> int:
		return self._instance.RsmOfsPct
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
