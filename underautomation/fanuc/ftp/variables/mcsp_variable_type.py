import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import McspVariableType as mcsp_variable_type

class McspVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mcsp_variable_type()
		else:
			self._instance = _internal
	@property
	def cldpop_enb(self) -> bool:
		return self._instance.CldpopEnb
	@property
	def trqlim_enb(self) -> bool:
		return self._instance.TrqlimEnb
	@property
	def joglim_enb(self) -> bool:
		return self._instance.JoglimEnb
	@property
	def cldpop_flg(self) -> bool:
		return self._instance.CldpopFlg
	@property
	def cldgrp_flg(self) -> int:
		return self._instance.CldgrpFlg
	@property
	def cldrel_flg(self) -> bool:
		return self._instance.CldrelFlg
	@property
	def clr_cldflg(self) -> bool:
		return self._instance.ClrCldflg
	@property
	def joglim_flg(self) -> bool:
		return self._instance.JoglimFlg
	@property
	def orgjog_ovr(self) -> int:
		return self._instance.OrgjogOvr
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def reserve1(self) -> int:
		return self._instance.Reserve1
	@property
	def reserve2(self) -> int:
		return self._instance.Reserve2
	@property
	def reserve3(self) -> int:
		return self._instance.Reserve3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
