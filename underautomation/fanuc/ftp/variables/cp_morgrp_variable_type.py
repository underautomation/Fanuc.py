import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpMorgrpVariableType as cp_morgrp_variable_type

class CpMorgrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cp_morgrp_variable_type()
		else:
			self._instance = _internal
	@property
	def chns_empty(self) -> bool:
		return self._instance.ChnsEmpty
	@property
	def gtf_empty(self) -> bool:
		return self._instance.GtfEmpty
	@property
	def chk_t1_spd(self) -> bool:
		return self._instance.ChkT1Spd
	@property
	def t1_fpspd(self) -> float:
		return self._instance.T1Fpspd
	@property
	def t1_tcpspd(self) -> float:
		return self._instance.T1Tcpspd
	@property
	def speed(self) -> float:
		return self._instance.Speed
	@property
	def t1spdlim(self) -> float:
		return self._instance.T1spdlim
	@property
	def speedtol(self) -> float:
		return self._instance.Speedtol
	@property
	def jnt_vel(self) -> typing.List[float]:
		return self._instance.JntVel
	@property
	def jnt_acc(self) -> typing.List[float]:
		return self._instance.JntAcc
	@property
	def jnt_jrk(self) -> typing.List[float]:
		return self._instance.JntJrk
	@property
	def segfraction(self) -> float:
		return self._instance.Segfraction
	@property
	def rstrt_line(self) -> int:
		return self._instance.RstrtLine
	@property
	def rstrt_pvf(self) -> int:
		return self._instance.RstrtPvf
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
