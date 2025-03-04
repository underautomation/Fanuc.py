import typing
from underautomation.fanuc.ftp.variables.adj_rtrq_variable_type import AdjRtrqVariableType
from underautomation.fanuc.ftp.variables.ctrl_cab_variable_type import CtrlCabVariableType
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DiagGrpVariableType as diag_grp_variable_type

class DiagGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = diag_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def val_set(self) -> int:
		return self._instance.ValSet
	@property
	def tacc(self) -> typing.List[float]:
		return self._instance.Tacc
	@property
	def tacc_lim1(self) -> typing.List[float]:
		return self._instance.TaccLim1
	@property
	def tacc_lim2(self) -> typing.List[float]:
		return self._instance.TaccLim2
	@property
	def rrate_load(self) -> typing.List[float]:
		return self._instance.RrateLoad
	@property
	def ver(self) -> str:
		return self._instance.Ver
	@property
	def answer(self) -> int:
		return self._instance.Answer
	@property
	def rcc_ans(self) -> int:
		return self._instance.RccAns
	@property
	def adj_rtrq(self) -> typing.List[AdjRtrqVariableType]:
		return [AdjRtrqVariableType(x) for x in self._instance.AdjRtrq]
	@property
	def adj_ohtrq(self) -> typing.List[float]:
		return self._instance.AdjOhtrq
	@property
	def copper(self) -> typing.List[float]:
		return self._instance.Copper
	@property
	def iron(self) -> typing.List[float]:
		return self._instance.Iron
	@property
	def brk_pwr(self) -> typing.List[float]:
		return self._instance.BrkPwr
	@property
	def cable_act(self) -> typing.List[float]:
		return self._instance.CableAct
	@property
	def cable_base(self) -> typing.List[float]:
		return self._instance.CableBase
	@property
	def cable_leng(self) -> typing.List[float]:
		return self._instance.CableLeng
	@property
	def cab_num(self) -> int:
		return self._instance.CabNum
	@property
	def ctrl_cab(self) -> typing.List[CtrlCabVariableType]:
		return [CtrlCabVariableType(x) for x in self._instance.CtrlCab]
	@property
	def trqcns(self) -> typing.List[float]:
		return self._instance.Trqcns
	@property
	def trqdwn(self) -> typing.List[float]:
		return self._instance.Trqdwn
	@property
	def msbas(self) -> typing.List[float]:
		return self._instance.Msbas
	@property
	def maxtrq(self) -> typing.List[float]:
		return self._instance.Maxtrq
	@property
	def rrate(self) -> typing.List[float]:
		return self._instance.Rrate
	@property
	def lifecalc(self) -> typing.List[int]:
		return self._instance.Lifecalc
	@property
	def l10(self) -> typing.List[int]:
		return self._instance.L10
	@property
	def n0(self) -> typing.List[float]:
		return self._instance.N0
	@property
	def t0(self) -> typing.List[float]:
		return self._instance.T0
	@property
	def cur_l10(self) -> typing.List[float]:
		return self._instance.CurL10
	@property
	def tcp_type(self) -> int:
		return self._instance.TcpType
	@property
	def cur_tcp(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.CurTcp)
	@property
	def motn_style(self) -> int:
		return self._instance.MotnStyle
	@property
	def flag(self) -> int:
		return self._instance.Flag
	@property
	def cur_ovc(self) -> typing.List[float]:
		return self._instance.CurOvc
	@property
	def cur_heat(self) -> typing.List[float]:
		return self._instance.CurHeat
	@property
	def support_typ(self) -> typing.List[int]:
		return self._instance.SupportTyp
	@property
	def all_support(self) -> int:
		return self._instance.AllSupport
	@property
	def cur_tcp_x(self) -> float:
		return self._instance.CurTcpX
	@property
	def cur_tcp_y(self) -> float:
		return self._instance.CurTcpY
	@property
	def cur_tcp_z(self) -> float:
		return self._instance.CurTcpZ
	@property
	def cur_tcp_w(self) -> float:
		return self._instance.CurTcpW
	@property
	def cur_tcp_p(self) -> float:
		return self._instance.CurTcpP
	@property
	def cur_tcp_r(self) -> float:
		return self._instance.CurTcpR
	@property
	def cur_speed(self) -> float:
		return self._instance.CurSpeed
	@property
	def xz_arm(self) -> typing.List[float]:
		return self._instance.XzArm
	@property
	def y2_arm(self) -> typing.List[float]:
		return self._instance.Y2Arm
	@property
	def cos_tpress(self) -> typing.List[float]:
		return self._instance.CosTpress
	@property
	def tan_inc(self) -> typing.List[float]:
		return self._instance.TanInc
	@property
	def cur_jspd(self) -> typing.List[float]:
		return self._instance.CurJspd
	@property
	def iron_h(self) -> typing.List[float]:
		return self._instance.IronH
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
