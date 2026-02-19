import typing
from underautomation.fanuc.ftp.variables.adj_rtrq_variable_type import AdjRtrqVariableType
from underautomation.fanuc.ftp.variables.ctrl_cab_variable_type import CtrlCabVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DiagGrpVariableType as diag_grp_variable_type

class DiagGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type DIAG_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = diag_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def val_set(self) -> int:
		'''Value of variable $VAL_SET'''
		return self._instance.ValSet

	@property
	def tacc(self) -> typing.List[float]:
		'''Value of variable $TACC'''
		return self._instance.Tacc

	@property
	def tacc_lim1(self) -> typing.List[float]:
		'''Value of variable $TACC_LIM1'''
		return self._instance.TaccLim1

	@property
	def tacc_lim2(self) -> typing.List[float]:
		'''Value of variable $TACC_LIM2'''
		return self._instance.TaccLim2

	@property
	def rrate_load(self) -> typing.List[float]:
		'''Value of variable $RRATE_LOAD'''
		return self._instance.RrateLoad

	@property
	def ver(self) -> str:
		'''Value of variable $VER'''
		return self._instance.Ver

	@property
	def answer(self) -> int:
		'''Value of variable $ANSWER'''
		return self._instance.Answer

	@property
	def rcc_ans(self) -> int:
		'''Value of variable $RCC_ANS'''
		return self._instance.RccAns

	@property
	def adj_rtrq(self) -> typing.List[AdjRtrqVariableType]:
		'''Value of variable $ADJ_RTRQ'''
		return [AdjRtrqVariableType(x) for x in self._instance.AdjRtrq]

	@property
	def adj_ohtrq(self) -> typing.List[float]:
		'''Value of variable $ADJ_OHTRQ'''
		return self._instance.AdjOhtrq

	@property
	def copper(self) -> typing.List[float]:
		'''Value of variable $COPPER'''
		return self._instance.Copper

	@property
	def iron(self) -> typing.List[float]:
		'''Value of variable $IRON'''
		return self._instance.Iron

	@property
	def brk_pwr(self) -> typing.List[float]:
		'''Value of variable $BRK_PWR'''
		return self._instance.BrkPwr

	@property
	def cable_act(self) -> typing.List[float]:
		'''Value of variable $CABLE_ACT'''
		return self._instance.CableAct

	@property
	def cable_base(self) -> typing.List[float]:
		'''Value of variable $CABLE_BASE'''
		return self._instance.CableBase

	@property
	def cable_leng(self) -> typing.List[float]:
		'''Value of variable $CABLE_LENG'''
		return self._instance.CableLeng

	@property
	def cab_num(self) -> int:
		'''Value of variable $CAB_NUM'''
		return self._instance.CabNum

	@property
	def ctrl_cab(self) -> typing.List[CtrlCabVariableType]:
		'''Value of variable $CTRL_CAB'''
		return [CtrlCabVariableType(x) for x in self._instance.CtrlCab]

	@property
	def trqcns(self) -> typing.List[float]:
		'''Value of variable $TRQCNS'''
		return self._instance.Trqcns

	@property
	def trqdwn(self) -> typing.List[float]:
		'''Value of variable $TRQDWN'''
		return self._instance.Trqdwn

	@property
	def msbas(self) -> typing.List[float]:
		'''Value of variable $MSBAS'''
		return self._instance.Msbas

	@property
	def maxtrq(self) -> typing.List[float]:
		'''Value of variable $MAXTRQ'''
		return self._instance.Maxtrq

	@property
	def rrate(self) -> typing.List[float]:
		'''Value of variable $RRATE'''
		return self._instance.Rrate

	@property
	def lifecalc(self) -> typing.List[int]:
		'''Value of variable $LIFECALC'''
		return self._instance.Lifecalc

	@property
	def l10(self) -> typing.List[int]:
		'''Value of variable $L10'''
		return self._instance.L10

	@property
	def n0(self) -> typing.List[float]:
		'''Value of variable $N0'''
		return self._instance.N0

	@property
	def t0(self) -> typing.List[float]:
		'''Value of variable $T0'''
		return self._instance.T0

	@property
	def cur_l10(self) -> typing.List[float]:
		'''Value of variable $CUR_L10'''
		return self._instance.CurL10

	@property
	def tcp_type(self) -> int:
		'''Value of variable $TCP_TYPE'''
		return self._instance.TcpType

	@property
	def cur_tcp(self) -> CartesianPositionVariable:
		'''Value of variable $CUR_TCP'''
		return CartesianPositionVariable(self._instance.CurTcp)

	@property
	def motn_style(self) -> int:
		'''Value of variable $MOTN_STYLE'''
		return self._instance.MotnStyle

	@property
	def flag(self) -> int:
		'''Value of variable $FLAG'''
		return self._instance.Flag

	@property
	def cur_ovc(self) -> typing.List[float]:
		'''Value of variable $CUR_OVC'''
		return self._instance.CurOvc

	@property
	def cur_heat(self) -> typing.List[float]:
		'''Value of variable $CUR_HEAT'''
		return self._instance.CurHeat

	@property
	def support_typ(self) -> typing.List[int]:
		'''Value of variable $SUPPORT_TYP'''
		return self._instance.SupportTyp

	@property
	def all_support(self) -> int:
		'''Value of variable $ALL_SUPPORT'''
		return self._instance.AllSupport

	@property
	def cur_tcp_x(self) -> float:
		'''Value of variable $CUR_TCP_X'''
		return self._instance.CurTcpX

	@property
	def cur_tcp_y(self) -> float:
		'''Value of variable $CUR_TCP_Y'''
		return self._instance.CurTcpY

	@property
	def cur_tcp_z(self) -> float:
		'''Value of variable $CUR_TCP_Z'''
		return self._instance.CurTcpZ

	@property
	def cur_tcp_w(self) -> float:
		'''Value of variable $CUR_TCP_W'''
		return self._instance.CurTcpW

	@property
	def cur_tcp_p(self) -> float:
		'''Value of variable $CUR_TCP_P'''
		return self._instance.CurTcpP

	@property
	def cur_tcp_r(self) -> float:
		'''Value of variable $CUR_TCP_R'''
		return self._instance.CurTcpR

	@property
	def cur_speed(self) -> float:
		'''Value of variable $CUR_SPEED'''
		return self._instance.CurSpeed

	@property
	def xz_arm(self) -> typing.List[float]:
		'''Value of variable $XZ_ARM'''
		return self._instance.XzArm

	@property
	def y2_arm(self) -> typing.List[float]:
		'''Value of variable $Y2_ARM'''
		return self._instance.Y2Arm

	@property
	def cos_tpress(self) -> typing.List[float]:
		'''Value of variable $COS_TPRESS'''
		return self._instance.CosTpress

	@property
	def tan_inc(self) -> typing.List[float]:
		'''Value of variable $TAN_INC'''
		return self._instance.TanInc

	@property
	def cur_jspd(self) -> typing.List[float]:
		'''Value of variable $CUR_JSPD'''
		return self._instance.CurJspd

	@property
	def iron_h(self) -> typing.List[float]:
		'''Value of variable $IRON_H'''
		return self._instance.IronH

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DiagGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
