import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZmposGrpVariableType as zmpos_grp_variable_type

class ZmposGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zmpos_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def m_pos_enb(self) -> int:
		return self._instance.MPosEnb
	@property
	def cmcmd_scl(self) -> int:
		return self._instance.CmcmdScl
	@property
	def cart_mcmd(self) -> typing.List[float]:
		return self._instance.CartMcmd
	@property
	def p_act(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.PAct)
	@property
	def j_act(self) -> typing.List[float]:
		return self._instance.JAct
	@property
	def p_des(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.PDes)
	@property
	def j_des(self) -> typing.List[float]:
		return self._instance.JDes
	@property
	def p_des2(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.PDes2)
	@property
	def j_des2(self) -> typing.List[float]:
		return self._instance.JDes2
	@property
	def p_act_uf(self) -> typing.List[float]:
		return self._instance.PActUf
	@property
	def p_des_uf(self) -> typing.List[float]:
		return self._instance.PDesUf
	@property
	def uxwpr_enb(self) -> int:
		return self._instance.UxwprEnb
	@property
	def uxeul_enb(self) -> int:
		return self._instance.UxeulEnb
	@property
	def uxwpr_act(self) -> typing.List[float]:
		return self._instance.UxwprAct
	@property
	def uxwpr_des(self) -> typing.List[float]:
		return self._instance.UxwprDes
	@property
	def uxeul_act(self) -> typing.List[float]:
		return self._instance.UxeulAct
	@property
	def uxeul_des(self) -> typing.List[float]:
		return self._instance.UxeulDes
	@property
	def p_aftflt(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.PAftflt)
	@property
	def j_aftflt(self) -> typing.List[float]:
		return self._instance.JAftflt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
