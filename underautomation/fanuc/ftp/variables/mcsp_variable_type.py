import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import McspVariableType as mcsp_variable_type

class McspVariableType(GenericVariableType):
	'''Describes the Fanuc type MCSP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcsp_variable_type()
		else:
			self._instance = _internal

	@property
	def cldpop_enb(self) -> bool:
		'''Value of variable $CLDPOP_ENB'''
		return self._instance.CldpopEnb

	@property
	def trqlim_enb(self) -> bool:
		'''Value of variable $TRQLIM_ENB'''
		return self._instance.TrqlimEnb

	@property
	def joglim_enb(self) -> bool:
		'''Value of variable $JOGLIM_ENB'''
		return self._instance.JoglimEnb

	@property
	def cldpop_flg(self) -> bool:
		'''Value of variable $CLDPOP_FLG'''
		return self._instance.CldpopFlg

	@property
	def cldgrp_flg(self) -> int:
		'''Value of variable $CLDGRP_FLG'''
		return self._instance.CldgrpFlg

	@property
	def cldrel_flg(self) -> bool:
		'''Value of variable $CLDREL_FLG'''
		return self._instance.CldrelFlg

	@property
	def clr_cldflg(self) -> bool:
		'''Value of variable $CLR_CLDFLG'''
		return self._instance.ClrCldflg

	@property
	def joglim_flg(self) -> bool:
		'''Value of variable $JOGLIM_FLG'''
		return self._instance.JoglimFlg

	@property
	def orgjog_ovr(self) -> int:
		'''Value of variable $ORGJOG_OVR'''
		return self._instance.OrgjogOvr

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def reserve1(self) -> int:
		'''Value of variable $RESERVE1'''
		return self._instance.Reserve1

	@property
	def reserve2(self) -> int:
		'''Value of variable $RESERVE2'''
		return self._instance.Reserve2

	@property
	def reserve3(self) -> int:
		'''Value of variable $RESERVE3'''
		return self._instance.Reserve3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, McspVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
