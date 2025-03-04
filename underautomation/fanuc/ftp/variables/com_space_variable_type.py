import typing
from underautomation.fanuc.ftp.variables.gp_status_variable_type import GpStatusVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ComSpaceVariableType as com_space_variable_type

class ComSpaceVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = com_space_variable_type()
		else:
			self._instance = _internal
	@property
	def use_mlt_ctn(self) -> bool:
		return self._instance.UseMltCtn
	@property
	def h_priority(self) -> bool:
		return self._instance.HPriority
	@property
	def in_control(self) -> bool:
		return self._instance.InControl
	@property
	def in_space_gp(self) -> int:
		return self._instance.InSpaceGp
	@property
	def wt_space_gp(self) -> int:
		return self._instance.WtSpaceGp
	@property
	def use_gp(self) -> int:
		return self._instance.UseGp
	@property
	def deadlock_gp(self) -> int:
		return self._instance.DeadlockGp
	@property
	def delay_cnt1(self) -> int:
		return self._instance.DelayCnt1
	@property
	def delay_cnt2(self) -> int:
		return self._instance.DelayCnt2
	@property
	def gp_status(self) -> typing.List[GpStatusVariableType]:
		return [GpStatusVariableType(x) for x in self._instance.GpStatus]
	@property
	def dout1_type(self) -> int:
		return self._instance.Dout1Type
	@property
	def dout1_indx(self) -> int:
		return self._instance.Dout1Indx
	@property
	def dout2_type(self) -> int:
		return self._instance.Dout2Type
	@property
	def dout2_indx(self) -> int:
		return self._instance.Dout2Indx
	@property
	def dout3_type(self) -> int:
		return self._instance.Dout3Type
	@property
	def dout3_indx(self) -> int:
		return self._instance.Dout3Indx
	@property
	def din1_type(self) -> int:
		return self._instance.Din1Type
	@property
	def din1_indx(self) -> int:
		return self._instance.Din1Indx
	@property
	def din2_type(self) -> int:
		return self._instance.Din2Type
	@property
	def din2_indx(self) -> int:
		return self._instance.Din2Indx
	@property
	def ext1(self) -> int:
		return self._instance.Ext1
	@property
	def ext2(self) -> int:
		return self._instance.Ext2
	@property
	def v1(self) -> typing.List[float]:
		return self._instance.V1
	@property
	def v2(self) -> typing.List[float]:
		return self._instance.V2
	@property
	def v3(self) -> typing.List[float]:
		return self._instance.V3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
