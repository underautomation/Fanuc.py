import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpMcrgrpVariableType as cp_mcrgrp_variable_type

class CpMcrgrpVariableType(GenericVariableType):
	'''Describes the Fanuc type CP_MCRGRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_mcrgrp_variable_type()
		else:
			self._instance = _internal

	@property
	def rsm_jbf_pct(self) -> int:
		'''Value of variable $RSM_JBF_PCT'''
		return self._instance.RsmJbfPct

	@property
	def rsm_dec_pct(self) -> int:
		'''Value of variable $RSM_DEC_PCT'''
		return self._instance.RsmDecPct

	@property
	def rsm_ofs_pct(self) -> int:
		'''Value of variable $RSM_OFS_PCT'''
		return self._instance.RsmOfsPct

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpMcrgrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
