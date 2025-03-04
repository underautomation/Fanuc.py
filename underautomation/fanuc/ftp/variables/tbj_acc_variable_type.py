import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbjAccVariableType as tbj_acc_variable_type

class TbjAccVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbj_acc_variable_type()
		else:
			self._instance = _internal
	@property
	def acc_len1(self) -> int:
		return self._instance.AccLen1
	@property
	def acc_len2(self) -> int:
		return self._instance.AccLen2
	@property
	def dec_len1(self) -> int:
		return self._instance.DecLen1
	@property
	def dec_len2(self) -> int:
		return self._instance.DecLen2
	@property
	def accel_ratio(self) -> float:
		return self._instance.AccelRatio
	@property
	def decel_ratio(self) -> float:
		return self._instance.DecelRatio
	@property
	def slow_axis(self) -> int:
		return self._instance.SlowAxis
	@property
	def f1acc_i(self) -> int:
		return self._instance.F1accI
	@property
	def f2acc_i(self) -> int:
		return self._instance.F2accI
	@property
	def f1dec_i(self) -> int:
		return self._instance.F1decI
	@property
	def f2dec_i(self) -> int:
		return self._instance.F2decI
	@property
	def move_time(self) -> float:
		return self._instance.MoveTime
	@property
	def s_inertia(self) -> typing.List[float]:
		return self._instance.SInertia
	@property
	def d_inertia(self) -> typing.List[float]:
		return self._instance.DInertia
	@property
	def torque_acc(self) -> typing.List[float]:
		return self._instance.TorqueAcc
	@property
	def torque_dec(self) -> typing.List[float]:
		return self._instance.TorqueDec
	@property
	def displacemnt(self) -> typing.List[float]:
		return self._instance.Displacemnt
	@property
	def acctime(self) -> typing.List[float]:
		return self._instance.Acctime
	@property
	def dectime(self) -> typing.List[float]:
		return self._instance.Dectime
	@property
	def vel_max_acc(self) -> typing.List[float]:
		return self._instance.VelMaxAcc
	@property
	def vel_max_dec(self) -> typing.List[float]:
		return self._instance.VelMaxDec
	@property
	def vel_tcv_acc(self) -> typing.List[float]:
		return self._instance.VelTcvAcc
	@property
	def vel_tcv_dec(self) -> typing.List[float]:
		return self._instance.VelTcvDec
	@property
	def trq_tcv_acc(self) -> typing.List[float]:
		return self._instance.TrqTcvAcc
	@property
	def trq_tcv_dec(self) -> typing.List[float]:
		return self._instance.TrqTcvDec
	@property
	def trqstat_acc(self) -> typing.List[int]:
		return self._instance.TrqstatAcc
	@property
	def trqstat_dec(self) -> typing.List[int]:
		return self._instance.TrqstatDec
	@property
	def j_stat_acc(self) -> typing.List[int]:
		return self._instance.JStatAcc
	@property
	def j_stat_dec(self) -> typing.List[int]:
		return self._instance.JStatDec
	@property
	def m_stat_acc(self) -> int:
		return self._instance.MStatAcc
	@property
	def m_stat_dec(self) -> int:
		return self._instance.MStatDec
	@property
	def j_mode(self) -> int:
		return self._instance.JMode
	@property
	def dt_acc(self) -> typing.List[float]:
		return self._instance.DtAcc
	@property
	def dt_dec(self) -> typing.List[float]:
		return self._instance.DtDec
	@property
	def acc2_stp(self) -> typing.List[int]:
		return self._instance.Acc2Stp
	@property
	def dec2_stp(self) -> typing.List[int]:
		return self._instance.Dec2Stp
	@property
	def at_mode(self) -> int:
		return self._instance.AtMode
	@property
	def at_axs(self) -> typing.List[int]:
		return self._instance.AtAxs
	@property
	def ac_acc(self) -> typing.List[float]:
		return self._instance.AcAcc
	@property
	def ac_dec(self) -> typing.List[float]:
		return self._instance.AcDec
	@property
	def jk_acc(self) -> typing.List[float]:
		return self._instance.JkAcc
	@property
	def jk_dec(self) -> typing.List[float]:
		return self._instance.JkDec
	@property
	def vk1(self) -> float:
		return self._instance.Vk1
	@property
	def vk2(self) -> float:
		return self._instance.Vk2
	@property
	def vk3(self) -> float:
		return self._instance.Vk3
	@property
	def jj0(self) -> float:
		return self._instance.Jj0
	@property
	def jj1(self) -> float:
		return self._instance.Jj1
	@property
	def jj2(self) -> float:
		return self._instance.Jj2
	@property
	def jj3(self) -> float:
		return self._instance.Jj3
	@property
	def aa1(self) -> float:
		return self._instance.Aa1
	@property
	def aa2(self) -> float:
		return self._instance.Aa2
	@property
	def aa3(self) -> float:
		return self._instance.Aa3
	@property
	def aa4(self) -> float:
		return self._instance.Aa4
	@property
	def aa5(self) -> float:
		return self._instance.Aa5
	@property
	def trq_n1_acc(self) -> typing.List[float]:
		return self._instance.TrqN1Acc
	@property
	def trq_n1_dec(self) -> typing.List[float]:
		return self._instance.TrqN1Dec
	@property
	def vel_max(self) -> typing.List[float]:
		return self._instance.VelMax
	@property
	def line_num(self) -> int:
		return self._instance.LineNum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
