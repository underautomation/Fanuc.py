import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ZmposGrpVariableType as zmpos_grp_variable_type

class ZmposGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type ZMPOS_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zmpos_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def m_pos_enb(self) -> int:
		'''Value of variable $M_POS_ENB'''
		return self._instance.MPosEnb

	@property
	def cmcmd_scl(self) -> int:
		'''Value of variable $CMCMD_SCL'''
		return self._instance.CmcmdScl

	@property
	def cart_mcmd(self) -> typing.List[float]:
		'''Value of variable $CART_MCMD'''
		return self._instance.CartMcmd

	@property
	def p_act(self) -> CartesianPositionVariable:
		'''Value of variable $P_ACT'''
		return CartesianPositionVariable(self._instance.PAct)

	@property
	def j_act(self) -> typing.List[float]:
		'''Value of variable $J_ACT'''
		return self._instance.JAct

	@property
	def p_des(self) -> CartesianPositionVariable:
		'''Value of variable $P_DES'''
		return CartesianPositionVariable(self._instance.PDes)

	@property
	def j_des(self) -> typing.List[float]:
		'''Value of variable $J_DES'''
		return self._instance.JDes

	@property
	def p_des2(self) -> CartesianPositionVariable:
		'''Value of variable $P_DES2'''
		return CartesianPositionVariable(self._instance.PDes2)

	@property
	def j_des2(self) -> typing.List[float]:
		'''Value of variable $J_DES2'''
		return self._instance.JDes2

	@property
	def p_act_uf(self) -> typing.List[float]:
		'''Value of variable $P_ACT_UF'''
		return self._instance.PActUf

	@property
	def p_des_uf(self) -> typing.List[float]:
		'''Value of variable $P_DES_UF'''
		return self._instance.PDesUf

	@property
	def uxwpr_enb(self) -> int:
		'''Value of variable $UXWPR_ENB'''
		return self._instance.UxwprEnb

	@property
	def uxeul_enb(self) -> int:
		'''Value of variable $UXEUL_ENB'''
		return self._instance.UxeulEnb

	@property
	def uxwpr_act(self) -> typing.List[float]:
		'''Value of variable $UXWPR_ACT'''
		return self._instance.UxwprAct

	@property
	def uxwpr_des(self) -> typing.List[float]:
		'''Value of variable $UXWPR_DES'''
		return self._instance.UxwprDes

	@property
	def uxeul_act(self) -> typing.List[float]:
		'''Value of variable $UXEUL_ACT'''
		return self._instance.UxeulAct

	@property
	def uxeul_des(self) -> typing.List[float]:
		'''Value of variable $UXEUL_DES'''
		return self._instance.UxeulDes

	@property
	def p_aftflt(self) -> CartesianPositionVariable:
		'''Value of variable $P_AFTFLT'''
		return CartesianPositionVariable(self._instance.PAftflt)

	@property
	def j_aftflt(self) -> typing.List[float]:
		'''Value of variable $J_AFTFLT'''
		return self._instance.JAftflt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ZmposGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
