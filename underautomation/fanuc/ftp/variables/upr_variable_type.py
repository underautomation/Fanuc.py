import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UprVariableType as upr_variable_type

class UprVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = upr_variable_type()
		else:
			self._instance = _internal
	@property
	def motype(self) -> int:
		return self._instance.Motype
	@property
	def termtype(self) -> int:
		return self._instance.Termtype
	@property
	def segtermtype(self) -> int:
		return self._instance.Segtermtype
	@property
	def deceltol(self) -> float:
		return self._instance.Deceltol
	@property
	def use_config(self) -> bool:
		return self._instance.UseConfig
	@property
	def use_turns(self) -> bool:
		return self._instance.UseTurns
	@property
	def orient_type(self) -> int:
		return self._instance.OrientType
	@property
	def uframe(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Uframe)
	@property
	def utool(self) -> CartesianPositionVariable:
		return CartesianPositionVariable(self._instance.Utool)
	@property
	def speed(self) -> float:
		return self._instance.Speed
	@property
	def rotspeed(self) -> float:
		return self._instance.Rotspeed
	@property
	def contaxisvel(self) -> float:
		return self._instance.Contaxisvel
	@property
	def cnstnt_path(self) -> bool:
		return self._instance.CnstntPath
	@property
	def cnstntpthjt(self) -> bool:
		return self._instance.Cnstntpthjt
	@property
	def seg_time(self) -> int:
		return self._instance.SegTime
	@property
	def use_cartacc(self) -> bool:
		return self._instance.UseCartacc
	@property
	def usemaxaccel(self) -> bool:
		return self._instance.Usemaxaccel
	@property
	def userelaccel(self) -> bool:
		return self._instance.Userelaccel
	@property
	def usetimeshft(self) -> bool:
		return self._instance.Usetimeshft
	@property
	def use_pathacc(self) -> bool:
		return self._instance.UsePathacc
	@property
	def use_shortmo(self) -> bool:
		return self._instance.UseShortmo
	@property
	def sm_profile(self) -> int:
		return self._instance.SmProfile
	@property
	def ta_profile(self) -> int:
		return self._instance.TaProfile
	@property
	def accel_ovrd(self) -> int:
		return self._instance.AccelOvrd
	@property
	def time_shift(self) -> int:
		return self._instance.TimeShift
	@property
	def accu_num(self) -> int:
		return self._instance.AccuNum
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def dyn_i_comp(self) -> bool:
		return self._instance.DynIComp
	@property
	def pathres_enb(self) -> bool:
		return self._instance.PathresEnb
	@property
	def reserve1(self) -> int:
		return self._instance.Reserve1
	@property
	def cnt_shortmo(self) -> bool:
		return self._instance.CntShortmo
	@property
	def ext_speed(self) -> float:
		return self._instance.ExtSpeed
	@property
	def cnt_accel1(self) -> int:
		return self._instance.CntAccel1
	@property
	def cnt_accel2(self) -> int:
		return self._instance.CntAccel2
	@property
	def crccompenb(self) -> bool:
		return self._instance.Crccompenb
	@property
	def asymfltrenb(self) -> bool:
		return self._instance.Asymfltrenb
	@property
	def use_wjturns(self) -> bool:
		return self._instance.UseWjturns
	@property
	def ext_indep(self) -> bool:
		return self._instance.ExtIndep
	@property
	def cartfltrenb(self) -> bool:
		return self._instance.Cartfltrenb
	@property
	def cnt_speedup(self) -> bool:
		return self._instance.CntSpeedup
	@property
	def cnt_dyn_acc(self) -> bool:
		return self._instance.CntDynAcc
	@property
	def max_speed(self) -> bool:
		return self._instance.MaxSpeed
	@property
	def userelpspd(self) -> bool:
		return self._instance.Userelpspd
	@property
	def pspd_ovrd(self) -> int:
		return self._instance.PspdOvrd
	@property
	def ornt_mrot(self) -> bool:
		return self._instance.OrntMrot
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
