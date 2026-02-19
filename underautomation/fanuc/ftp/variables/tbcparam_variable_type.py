import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbcparamVariableType as tbcparam_variable_type

class TbcparamVariableType(GenericVariableType):
	'''Describes the Fanuc type TBCPARAM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbcparam_variable_type()
		else:
			self._instance = _internal

	@property
	def mc_max_trq(self) -> float:
		'''Value of variable $MC_MAX_TRQ'''
		return self._instance.McMaxTrq

	@property
	def max_trq_mgn(self) -> float:
		'''Value of variable $MAX_TRQ_MGN'''
		return self._instance.MaxTrqMgn

	@property
	def mc_grav_mgn(self) -> float:
		'''Value of variable $MC_GRAV_MGN'''
		return self._instance.McGravMgn

	@property
	def mc_stal_mgn(self) -> float:
		'''Value of variable $MC_STAL_MGN'''
		return self._instance.McStalMgn

	@property
	def mc_brk_mgn(self) -> float:
		'''Value of variable $MC_BRK_MGN'''
		return self._instance.McBrkMgn

	@property
	def mc_nold_mgn(self) -> float:
		'''Value of variable $MC_NOLD_MGN'''
		return self._instance.McNoldMgn

	@property
	def shortmo_lim(self) -> float:
		'''Value of variable $SHORTMO_LIM'''
		return self._instance.ShortmoLim

	@property
	def shortmo_mgn(self) -> float:
		'''Value of variable $SHORTMO_MGN'''
		return self._instance.ShortmoMgn

	@property
	def mc_nold_trq(self) -> float:
		'''Value of variable $MC_NOLD_TRQ'''
		return self._instance.McNoldTrq

	@property
	def j_lin(self) -> float:
		'''Value of variable $J_LIN'''
		return self._instance.JLin

	@property
	def spl1(self) -> float:
		'''Value of variable $SPL1'''
		return self._instance.Spl1

	@property
	def spl2(self) -> float:
		'''Value of variable $SPL2'''
		return self._instance.Spl2

	@property
	def spl3(self) -> float:
		'''Value of variable $SPL3'''
		return self._instance.Spl3

	@property
	def spl4(self) -> float:
		'''Value of variable $SPL4'''
		return self._instance.Spl4

	@property
	def spl5(self) -> float:
		'''Value of variable $SPL5'''
		return self._instance.Spl5

	@property
	def spl6(self) -> float:
		'''Value of variable $SPL6'''
		return self._instance.Spl6

	@property
	def spl7(self) -> float:
		'''Value of variable $SPL7'''
		return self._instance.Spl7

	@property
	def spl8(self) -> float:
		'''Value of variable $SPL8'''
		return self._instance.Spl8

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbcparamVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
