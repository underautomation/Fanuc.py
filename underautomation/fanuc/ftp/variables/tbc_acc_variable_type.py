import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbcAccVariableType as tbc_acc_variable_type

class TbcAccVariableType(GenericVariableType):
	'''Describes the Fanuc type TBC_ACC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbc_acc_variable_type()
		else:
			self._instance = _internal

	@property
	def acc_len1(self) -> int:
		'''Value of variable $ACC_LEN1'''
		return self._instance.AccLen1

	@property
	def acc_len2(self) -> int:
		'''Value of variable $ACC_LEN2'''
		return self._instance.AccLen2

	@property
	def accel_ratio(self) -> float:
		'''Value of variable $ACCEL_RATIO'''
		return self._instance.AccelRatio

	@property
	def slow_axis(self) -> int:
		'''Value of variable $SLOW_AXIS'''
		return self._instance.SlowAxis

	@property
	def f1acc_i(self) -> int:
		'''Value of variable $F1ACC_I'''
		return self._instance.F1accI

	@property
	def f2acc_i(self) -> int:
		'''Value of variable $F2ACC_I'''
		return self._instance.F2accI

	@property
	def move_time(self) -> float:
		'''Value of variable $MOVE_TIME'''
		return self._instance.MoveTime

	@property
	def s_inertia(self) -> typing.List[float]:
		'''Value of variable $S_INERTIA'''
		return self._instance.SInertia

	@property
	def d_inertia(self) -> typing.List[float]:
		'''Value of variable $D_INERTIA'''
		return self._instance.DInertia

	@property
	def torque_acc(self) -> typing.List[float]:
		'''Value of variable $TORQUE_ACC'''
		return self._instance.TorqueAcc

	@property
	def torque_dec(self) -> typing.List[float]:
		'''Value of variable $TORQUE_DEC'''
		return self._instance.TorqueDec

	@property
	def displacemnt(self) -> typing.List[float]:
		'''Value of variable $DISPLACEMNT'''
		return self._instance.Displacemnt

	@property
	def acctime(self) -> typing.List[float]:
		'''Value of variable $ACCTIME'''
		return self._instance.Acctime

	@property
	def vel_max_acc(self) -> typing.List[float]:
		'''Value of variable $VEL_MAX_ACC'''
		return self._instance.VelMaxAcc

	@property
	def vel_max_dec(self) -> typing.List[float]:
		'''Value of variable $VEL_MAX_DEC'''
		return self._instance.VelMaxDec

	@property
	def vel_tcv_acc(self) -> typing.List[float]:
		'''Value of variable $VEL_TCV_ACC'''
		return self._instance.VelTcvAcc

	@property
	def vel_tcv_dec(self) -> typing.List[float]:
		'''Value of variable $VEL_TCV_DEC'''
		return self._instance.VelTcvDec

	@property
	def trq_tcv_acc(self) -> typing.List[float]:
		'''Value of variable $TRQ_TCV_ACC'''
		return self._instance.TrqTcvAcc

	@property
	def trq_tcv_dec(self) -> typing.List[float]:
		'''Value of variable $TRQ_TCV_DEC'''
		return self._instance.TrqTcvDec

	@property
	def trqstat_acc(self) -> typing.List[int]:
		'''Value of variable $TRQSTAT_ACC'''
		return self._instance.TrqstatAcc

	@property
	def trqstat_dec(self) -> typing.List[int]:
		'''Value of variable $TRQSTAT_DEC'''
		return self._instance.TrqstatDec

	@property
	def j_stat(self) -> typing.List[int]:
		'''Value of variable $J_STAT'''
		return self._instance.JStat

	@property
	def m_stat(self) -> int:
		'''Value of variable $M_STAT'''
		return self._instance.MStat

	@property
	def j_mode(self) -> int:
		'''Value of variable $J_MODE'''
		return self._instance.JMode

	@property
	def dt_acc(self) -> typing.List[float]:
		'''Value of variable $DT_ACC'''
		return self._instance.DtAcc

	@property
	def dt_dec(self) -> typing.List[float]:
		'''Value of variable $DT_DEC'''
		return self._instance.DtDec

	@property
	def acc2_stp(self) -> typing.List[int]:
		'''Value of variable $ACC2_STP'''
		return self._instance.Acc2Stp

	@property
	def ac_acc(self) -> float:
		'''Value of variable $AC_ACC'''
		return self._instance.AcAcc

	@property
	def jk_acc(self) -> float:
		'''Value of variable $JK_ACC'''
		return self._instance.JkAcc

	@property
	def vk1(self) -> float:
		'''Value of variable $VK1'''
		return self._instance.Vk1

	@property
	def vk2(self) -> float:
		'''Value of variable $VK2'''
		return self._instance.Vk2

	@property
	def vk3(self) -> float:
		'''Value of variable $VK3'''
		return self._instance.Vk3

	@property
	def jj0(self) -> float:
		'''Value of variable $JJ0'''
		return self._instance.Jj0

	@property
	def jj1(self) -> float:
		'''Value of variable $JJ1'''
		return self._instance.Jj1

	@property
	def jj2(self) -> float:
		'''Value of variable $JJ2'''
		return self._instance.Jj2

	@property
	def jj3(self) -> float:
		'''Value of variable $JJ3'''
		return self._instance.Jj3

	@property
	def aal1(self) -> float:
		'''Value of variable $AAL1'''
		return self._instance.Aal1

	@property
	def aal2(self) -> float:
		'''Value of variable $AAL2'''
		return self._instance.Aal2

	@property
	def aal3(self) -> float:
		'''Value of variable $AAL3'''
		return self._instance.Aal3

	@property
	def aal4(self) -> float:
		'''Value of variable $AAL4'''
		return self._instance.Aal4

	@property
	def aal5(self) -> float:
		'''Value of variable $AAL5'''
		return self._instance.Aal5

	@property
	def trq_n1_acc(self) -> typing.List[float]:
		'''Value of variable $TRQ_N1_ACC'''
		return self._instance.TrqN1Acc

	@property
	def trq_n1_dec(self) -> typing.List[float]:
		'''Value of variable $TRQ_N1_DEC'''
		return self._instance.TrqN1Dec

	@property
	def vel_max(self) -> typing.List[float]:
		'''Value of variable $VEL_MAX'''
		return self._instance.VelMax

	@property
	def line_num(self) -> int:
		'''Value of variable $LINE_NUM'''
		return self._instance.LineNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbcAccVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
