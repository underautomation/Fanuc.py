import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RspaceVariableType as rspace_variable_type

class RspaceVariableType(GenericVariableType):
	'''Describes the Fanuc type RSPACE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspace_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def usage(self) -> int:
		'''Value of variable $USAGE'''
		return self._instance.Usage

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def in_exterior(self) -> bool:
		'''Value of variable $IN_EXTERIOR'''
		return self._instance.InExterior

	@property
	def entry(self) -> bool:
		'''Value of variable $ENTRY'''
		return self._instance.Entry

	@property
	def ent_sign_on(self) -> bool:
		'''Value of variable $ENT_SIGN_ON'''
		return self._instance.EntSignOn

	@property
	def priority(self) -> bool:
		'''Value of variable $PRIORITY'''
		return self._instance.Priority

	@property
	def priorwrk(self) -> bool:
		'''Value of variable $PRIORWRK'''
		return self._instance.Priorwrk

	@property
	def dout_type(self) -> int:
		'''Value of variable $DOUT_TYPE'''
		return self._instance.DoutType

	@property
	def dout_indx(self) -> int:
		'''Value of variable $DOUT_INDX'''
		return self._instance.DoutIndx

	@property
	def din_type(self) -> int:
		'''Value of variable $DIN_TYPE'''
		return self._instance.DinType

	@property
	def din_indx(self) -> int:
		'''Value of variable $DIN_INDX'''
		return self._instance.DinIndx

	@property
	def friend_grp(self) -> int:
		'''Value of variable $FRIEND_GRP'''
		return self._instance.FriendGrp

	@property
	def ufram_num(self) -> int:
		'''Value of variable $UFRAM_NUM'''
		return self._instance.UframNum

	@property
	def utool_num(self) -> int:
		'''Value of variable $UTOOL_NUM'''
		return self._instance.UtoolNum

	@property
	def myhold(self) -> int:
		'''Value of variable $MYHOLD'''
		return self._instance.Myhold

	@property
	def length_vtex(self) -> int:
		'''Value of variable $LENGTH_VTEX'''
		return self._instance.LengthVtex

	@property
	def first_vtex(self) -> typing.List[float]:
		'''Value of variable $FIRST_VTEX'''
		return self._instance.FirstVtex

	@property
	def secnd_vtex(self) -> typing.List[float]:
		'''Value of variable $SECND_VTEX'''
		return self._instance.SecndVtex

	@property
	def ufinv_post(self) -> CartesianPositionVariable:
		'''Value of variable $UFINV_POST'''
		return CartesianPositionVariable(self._instance.UfinvPost)

	@property
	def margin(self) -> float:
		'''Value of variable $MARGIN'''
		return self._instance.Margin

	@property
	def waiting(self) -> int:
		'''Value of variable $WAITING'''
		return self._instance.Waiting

	@property
	def first_vtx2(self) -> typing.List[float]:
		'''Value of variable $FIRST_VTX2'''
		return self._instance.FirstVtx2

	@property
	def secnd_vtx2(self) -> typing.List[float]:
		'''Value of variable $SECND_VTX2'''
		return self._instance.SecndVtx2

	@property
	def g2entry(self) -> bool:
		'''Value of variable $G2ENTRY'''
		return self._instance.G2entry

	@property
	def g1ent_intr(self) -> bool:
		'''Value of variable $G1ENT_INTR'''
		return self._instance.G1entIntr

	@property
	def g2ent_intr(self) -> bool:
		'''Value of variable $G2ENT_INTR'''
		return self._instance.G2entIntr

	@property
	def pre_ufram(self) -> int:
		'''Value of variable $PRE_UFRAM'''
		return self._instance.PreUfram

	@property
	def no_use_di(self) -> bool:
		'''Value of variable $NO_USE_DI'''
		return self._instance.NoUseDi

	@property
	def hold_req(self) -> bool:
		'''Value of variable $HOLD_REQ'''
		return self._instance.HoldReq

	@property
	def cspace_num(self) -> int:
		'''Value of variable $CSPACE_NUM'''
		return self._instance.CspaceNum

	@property
	def cur_tcp(self) -> typing.List[float]:
		'''Value of variable $CUR_TCP'''
		return self._instance.CurTcp

	@property
	def pre_tcp(self) -> typing.List[float]:
		'''Value of variable $PRE_TCP'''
		return self._instance.PreTcp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RspaceVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
