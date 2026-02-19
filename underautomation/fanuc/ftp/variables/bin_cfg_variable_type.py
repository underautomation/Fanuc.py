import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import BinCfgVariableType as bin_cfg_variable_type

class BinCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type BIN_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bin_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def entries(self) -> int:
		'''Value of variable $ENTRIES'''
		return self._instance.Entries

	@property
	def q0fp(self) -> int:
		'''Value of variable $Q0FP'''
		return self._instance.Q0fp

	@property
	def q0np(self) -> int:
		'''Value of variable $Q0NP'''
		return self._instance.Q0np

	@property
	def q1fp(self) -> int:
		'''Value of variable $Q1FP'''
		return self._instance.Q1fp

	@property
	def q1np(self) -> int:
		'''Value of variable $Q1NP'''
		return self._instance.Q1np

	@property
	def q2fp(self) -> int:
		'''Value of variable $Q2FP'''
		return self._instance.Q2fp

	@property
	def q2np(self) -> int:
		'''Value of variable $Q2NP'''
		return self._instance.Q2np

	@property
	def pppp(self) -> int:
		'''Value of variable $PPPP'''
		return self._instance.Pppp

	@property
	def cnetp(self) -> int:
		'''Value of variable $CNETP'''
		return self._instance.Cnetp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BinCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
