import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbcparamVariableType as tbcparam_variable_type

class TbcparamVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbcparam_variable_type()
		else:
			self._instance = _internal
	@property
	def mc_max_trq(self) -> float:
		return self._instance.McMaxTrq
	@property
	def max_trq_mgn(self) -> float:
		return self._instance.MaxTrqMgn
	@property
	def mc_grav_mgn(self) -> float:
		return self._instance.McGravMgn
	@property
	def mc_stal_mgn(self) -> float:
		return self._instance.McStalMgn
	@property
	def mc_brk_mgn(self) -> float:
		return self._instance.McBrkMgn
	@property
	def mc_nold_mgn(self) -> float:
		return self._instance.McNoldMgn
	@property
	def shortmo_lim(self) -> float:
		return self._instance.ShortmoLim
	@property
	def shortmo_mgn(self) -> float:
		return self._instance.ShortmoMgn
	@property
	def mc_nold_trq(self) -> float:
		return self._instance.McNoldTrq
	@property
	def j_lin(self) -> float:
		return self._instance.JLin
	@property
	def spl1(self) -> float:
		return self._instance.Spl1
	@property
	def spl2(self) -> float:
		return self._instance.Spl2
	@property
	def spl3(self) -> float:
		return self._instance.Spl3
	@property
	def spl4(self) -> float:
		return self._instance.Spl4
	@property
	def spl5(self) -> float:
		return self._instance.Spl5
	@property
	def spl6(self) -> float:
		return self._instance.Spl6
	@property
	def spl7(self) -> float:
		return self._instance.Spl7
	@property
	def spl8(self) -> float:
		return self._instance.Spl8
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
