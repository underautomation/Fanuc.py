import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RspaceVariableType as rspace_variable_type

class RspaceVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspace_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def usage(self) -> int:
		return self._instance.Usage
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def in_exterior(self) -> bool:
		return self._instance.InExterior
	@property
	def entry(self) -> bool:
		return self._instance.Entry
	@property
	def ent_sign_on(self) -> bool:
		return self._instance.EntSignOn
	@property
	def priority(self) -> bool:
		return self._instance.Priority
	@property
	def priorwrk(self) -> bool:
		return self._instance.Priorwrk
	@property
	def dout_type(self) -> int:
		return self._instance.DoutType
	@property
	def dout_indx(self) -> int:
		return self._instance.DoutIndx
	@property
	def din_type(self) -> int:
		return self._instance.DinType
	@property
	def din_indx(self) -> int:
		return self._instance.DinIndx
	@property
	def friend_grp(self) -> int:
		return self._instance.FriendGrp
	@property
	def ufram_num(self) -> int:
		return self._instance.UframNum
	@property
	def utool_num(self) -> int:
		return self._instance.UtoolNum
	@property
	def myhold(self) -> int:
		return self._instance.Myhold
	@property
	def length_vtex(self) -> int:
		return self._instance.LengthVtex
	@property
	def first_vtex(self) -> typing.List[float]:
		return self._instance.FirstVtex
	@property
	def secnd_vtex(self) -> typing.List[float]:
		return self._instance.SecndVtex
	@property
	def ufinv_post(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.UfinvPost)
	@property
	def margin(self) -> float:
		return self._instance.Margin
	@property
	def waiting(self) -> int:
		return self._instance.Waiting
	@property
	def first_vtx2(self) -> typing.List[float]:
		return self._instance.FirstVtx2
	@property
	def secnd_vtx2(self) -> typing.List[float]:
		return self._instance.SecndVtx2
	@property
	def g2entry(self) -> bool:
		return self._instance.G2entry
	@property
	def g1ent_intr(self) -> bool:
		return self._instance.G1entIntr
	@property
	def g2ent_intr(self) -> bool:
		return self._instance.G2entIntr
	@property
	def pre_ufram(self) -> int:
		return self._instance.PreUfram
	@property
	def no_use_di(self) -> bool:
		return self._instance.NoUseDi
	@property
	def hold_req(self) -> bool:
		return self._instance.HoldReq
	@property
	def cspace_num(self) -> int:
		return self._instance.CspaceNum
	@property
	def cur_tcp(self) -> typing.List[float]:
		return self._instance.CurTcp
	@property
	def pre_tcp(self) -> typing.List[float]:
		return self._instance.PreTcp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
