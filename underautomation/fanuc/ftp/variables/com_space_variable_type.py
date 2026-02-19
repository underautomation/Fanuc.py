import typing
from underautomation.fanuc.ftp.variables.gp_status_variable_type import GpStatusVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ComSpaceVariableType as com_space_variable_type

class ComSpaceVariableType(GenericVariableType):
	'''Describes the Fanuc type COM_SPACE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = com_space_variable_type()
		else:
			self._instance = _internal

	@property
	def use_mlt_ctn(self) -> bool:
		'''Value of variable $USE_MLT_CTN'''
		return self._instance.UseMltCtn

	@property
	def h_priority(self) -> bool:
		'''Value of variable $H_PRIORITY'''
		return self._instance.HPriority

	@property
	def in_control(self) -> bool:
		'''Value of variable $IN_CONTROL'''
		return self._instance.InControl

	@property
	def in_space_gp(self) -> int:
		'''Value of variable $IN_SPACE_GP'''
		return self._instance.InSpaceGp

	@property
	def wt_space_gp(self) -> int:
		'''Value of variable $WT_SPACE_GP'''
		return self._instance.WtSpaceGp

	@property
	def use_gp(self) -> int:
		'''Value of variable $USE_GP'''
		return self._instance.UseGp

	@property
	def deadlock_gp(self) -> int:
		'''Value of variable $DEADLOCK_GP'''
		return self._instance.DeadlockGp

	@property
	def delay_cnt1(self) -> int:
		'''Value of variable $DELAY_CNT1'''
		return self._instance.DelayCnt1

	@property
	def delay_cnt2(self) -> int:
		'''Value of variable $DELAY_CNT2'''
		return self._instance.DelayCnt2

	@property
	def gp_status(self) -> typing.List[GpStatusVariableType]:
		'''Value of variable $GP_STATUS'''
		return [GpStatusVariableType(x) for x in self._instance.GpStatus]

	@property
	def dout1_type(self) -> int:
		'''Value of variable $DOUT1_TYPE'''
		return self._instance.Dout1Type

	@property
	def dout1_indx(self) -> int:
		'''Value of variable $DOUT1_INDX'''
		return self._instance.Dout1Indx

	@property
	def dout2_type(self) -> int:
		'''Value of variable $DOUT2_TYPE'''
		return self._instance.Dout2Type

	@property
	def dout2_indx(self) -> int:
		'''Value of variable $DOUT2_INDX'''
		return self._instance.Dout2Indx

	@property
	def dout3_type(self) -> int:
		'''Value of variable $DOUT3_TYPE'''
		return self._instance.Dout3Type

	@property
	def dout3_indx(self) -> int:
		'''Value of variable $DOUT3_INDX'''
		return self._instance.Dout3Indx

	@property
	def din1_type(self) -> int:
		'''Value of variable $DIN1_TYPE'''
		return self._instance.Din1Type

	@property
	def din1_indx(self) -> int:
		'''Value of variable $DIN1_INDX'''
		return self._instance.Din1Indx

	@property
	def din2_type(self) -> int:
		'''Value of variable $DIN2_TYPE'''
		return self._instance.Din2Type

	@property
	def din2_indx(self) -> int:
		'''Value of variable $DIN2_INDX'''
		return self._instance.Din2Indx

	@property
	def ext1(self) -> int:
		'''Value of variable $EXT1'''
		return self._instance.Ext1

	@property
	def ext2(self) -> int:
		'''Value of variable $EXT2'''
		return self._instance.Ext2

	@property
	def v1(self) -> typing.List[float]:
		'''Value of variable $V1'''
		return self._instance.V1

	@property
	def v2(self) -> typing.List[float]:
		'''Value of variable $V2'''
		return self._instance.V2

	@property
	def v3(self) -> typing.List[float]:
		'''Value of variable $V3'''
		return self._instance.V3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ComSpaceVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
