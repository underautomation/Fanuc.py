import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UprVariableType as upr_variable_type

class UprVariableType(GenericVariableType):
	'''Describes the Fanuc type UPR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = upr_variable_type()
		else:
			self._instance = _internal

	@property
	def motype(self) -> int:
		'''Value of variable $MOTYPE'''
		return self._instance.Motype

	@property
	def termtype(self) -> int:
		'''Value of variable $TERMTYPE'''
		return self._instance.Termtype

	@property
	def segtermtype(self) -> int:
		'''Value of variable $SEGTERMTYPE'''
		return self._instance.Segtermtype

	@property
	def deceltol(self) -> float:
		'''Value of variable $DECELTOL'''
		return self._instance.Deceltol

	@property
	def use_config(self) -> bool:
		'''Value of variable $USE_CONFIG'''
		return self._instance.UseConfig

	@property
	def use_turns(self) -> bool:
		'''Value of variable $USE_TURNS'''
		return self._instance.UseTurns

	@property
	def orient_type(self) -> int:
		'''Value of variable $ORIENT_TYPE'''
		return self._instance.OrientType

	@property
	def uframe(self) -> CartesianPositionVariable:
		'''Value of variable $UFRAME'''
		return CartesianPositionVariable(self._instance.Uframe)

	@property
	def utool(self) -> CartesianPositionVariable:
		'''Value of variable $UTOOL'''
		return CartesianPositionVariable(self._instance.Utool)

	@property
	def speed(self) -> float:
		'''Value of variable $SPEED'''
		return self._instance.Speed

	@property
	def rotspeed(self) -> float:
		'''Value of variable $ROTSPEED'''
		return self._instance.Rotspeed

	@property
	def contaxisvel(self) -> float:
		'''Value of variable $CONTAXISVEL'''
		return self._instance.Contaxisvel

	@property
	def cnstnt_path(self) -> bool:
		'''Value of variable $CNSTNT_PATH'''
		return self._instance.CnstntPath

	@property
	def cnstntpthjt(self) -> bool:
		'''Value of variable $CNSTNTPTHJT'''
		return self._instance.Cnstntpthjt

	@property
	def seg_time(self) -> int:
		'''Value of variable $SEG_TIME'''
		return self._instance.SegTime

	@property
	def use_cartacc(self) -> bool:
		'''Value of variable $USE_CARTACC'''
		return self._instance.UseCartacc

	@property
	def usemaxaccel(self) -> bool:
		'''Value of variable $USEMAXACCEL'''
		return self._instance.Usemaxaccel

	@property
	def userelaccel(self) -> bool:
		'''Value of variable $USERELACCEL'''
		return self._instance.Userelaccel

	@property
	def usetimeshft(self) -> bool:
		'''Value of variable $USETIMESHFT'''
		return self._instance.Usetimeshft

	@property
	def use_pathacc(self) -> bool:
		'''Value of variable $USE_PATHACC'''
		return self._instance.UsePathacc

	@property
	def use_shortmo(self) -> bool:
		'''Value of variable $USE_SHORTMO'''
		return self._instance.UseShortmo

	@property
	def sm_profile(self) -> int:
		'''Value of variable $SM_PROFILE'''
		return self._instance.SmProfile

	@property
	def ta_profile(self) -> int:
		'''Value of variable $TA_PROFILE'''
		return self._instance.TaProfile

	@property
	def accel_ovrd(self) -> int:
		'''Value of variable $ACCEL_OVRD'''
		return self._instance.AccelOvrd

	@property
	def time_shift(self) -> int:
		'''Value of variable $TIME_SHIFT'''
		return self._instance.TimeShift

	@property
	def accu_num(self) -> int:
		'''Value of variable $ACCU_NUM'''
		return self._instance.AccuNum

	@property
	def payload(self) -> float:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def dyn_i_comp(self) -> bool:
		'''Value of variable $DYN_I_COMP'''
		return self._instance.DynIComp

	@property
	def pathres_enb(self) -> bool:
		'''Value of variable $PATHRES_ENB'''
		return self._instance.PathresEnb

	@property
	def reserve1(self) -> int:
		'''Value of variable $RESERVE1'''
		return self._instance.Reserve1

	@property
	def cnt_shortmo(self) -> bool:
		'''Value of variable $CNT_SHORTMO'''
		return self._instance.CntShortmo

	@property
	def ext_speed(self) -> float:
		'''Value of variable $EXT_SPEED'''
		return self._instance.ExtSpeed

	@property
	def cnt_accel1(self) -> int:
		'''Value of variable $CNT_ACCEL1'''
		return self._instance.CntAccel1

	@property
	def cnt_accel2(self) -> int:
		'''Value of variable $CNT_ACCEL2'''
		return self._instance.CntAccel2

	@property
	def crccompenb(self) -> bool:
		'''Value of variable $CRCCOMPENB'''
		return self._instance.Crccompenb

	@property
	def asymfltrenb(self) -> bool:
		'''Value of variable $ASYMFLTRENB'''
		return self._instance.Asymfltrenb

	@property
	def use_wjturns(self) -> bool:
		'''Value of variable $USE_WJTURNS'''
		return self._instance.UseWjturns

	@property
	def ext_indep(self) -> bool:
		'''Value of variable $EXT_INDEP'''
		return self._instance.ExtIndep

	@property
	def cartfltrenb(self) -> bool:
		'''Value of variable $CARTFLTRENB'''
		return self._instance.Cartfltrenb

	@property
	def cnt_speedup(self) -> bool:
		'''Value of variable $CNT_SPEEDUP'''
		return self._instance.CntSpeedup

	@property
	def cnt_dyn_acc(self) -> bool:
		'''Value of variable $CNT_DYN_ACC'''
		return self._instance.CntDynAcc

	@property
	def max_speed(self) -> bool:
		'''Value of variable $MAX_SPEED'''
		return self._instance.MaxSpeed

	@property
	def userelpspd(self) -> bool:
		'''Value of variable $USERELPSPD'''
		return self._instance.Userelpspd

	@property
	def pspd_ovrd(self) -> int:
		'''Value of variable $PSPD_OVRD'''
		return self._instance.PspdOvrd

	@property
	def ornt_mrot(self) -> bool:
		'''Value of variable $ORNT_MROT'''
		return self._instance.OrntMrot

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UprVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
