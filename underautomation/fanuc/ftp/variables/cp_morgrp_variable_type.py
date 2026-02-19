import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpMorgrpVariableType as cp_morgrp_variable_type

class CpMorgrpVariableType(GenericVariableType):
	'''Describes the Fanuc type CP_MORGRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_morgrp_variable_type()
		else:
			self._instance = _internal

	@property
	def chns_empty(self) -> bool:
		'''Value of variable $CHNS_EMPTY'''
		return self._instance.ChnsEmpty

	@property
	def gtf_empty(self) -> bool:
		'''Value of variable $GTF_EMPTY'''
		return self._instance.GtfEmpty

	@property
	def chk_t1_spd(self) -> bool:
		'''Value of variable $CHK_T1_SPD'''
		return self._instance.ChkT1Spd

	@property
	def t1_fpspd(self) -> float:
		'''Value of variable $T1_FPSPD'''
		return self._instance.T1Fpspd

	@property
	def t1_tcpspd(self) -> float:
		'''Value of variable $T1_TCPSPD'''
		return self._instance.T1Tcpspd

	@property
	def speed(self) -> float:
		'''Value of variable $SPEED'''
		return self._instance.Speed

	@property
	def t1spdlim(self) -> float:
		'''Value of variable $T1SPDLIM'''
		return self._instance.T1spdlim

	@property
	def speedtol(self) -> float:
		'''Value of variable $SPEEDTOL'''
		return self._instance.Speedtol

	@property
	def jnt_vel(self) -> typing.List[float]:
		'''Value of variable $JNT_VEL'''
		return self._instance.JntVel

	@property
	def jnt_acc(self) -> typing.List[float]:
		'''Value of variable $JNT_ACC'''
		return self._instance.JntAcc

	@property
	def jnt_jrk(self) -> typing.List[float]:
		'''Value of variable $JNT_JRK'''
		return self._instance.JntJrk

	@property
	def segfraction(self) -> float:
		'''Value of variable $SEGFRACTION'''
		return self._instance.Segfraction

	@property
	def rstrt_line(self) -> int:
		'''Value of variable $RSTRT_LINE'''
		return self._instance.RstrtLine

	@property
	def rstrt_pvf(self) -> int:
		'''Value of variable $RSTRT_PVF'''
		return self._instance.RstrtPvf

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpMorgrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
