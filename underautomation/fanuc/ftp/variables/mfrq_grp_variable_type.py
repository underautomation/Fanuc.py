import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MfrqGrpVariableType as mfrq_grp_variable_type

class MfrqGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MFRQ_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mfrq_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def act_axis(self) -> int:
		'''Value of variable $ACT_AXIS'''
		return self._instance.ActAxis

	@property
	def upd_date(self) -> typing.List[str]:
		'''Value of variable $UPD_DATE'''
		return self._instance.UpdDate

	@property
	def ave_psd(self) -> typing.List[float]:
		'''Value of variable $AVE_PSD'''
		return self._instance.AvePsd

	@property
	def freq_cnt(self) -> typing.List[int]:
		'''Value of variable $FREQ_CNT'''
		return self._instance.FreqCnt

	@property
	def last_date(self) -> typing.List[int]:
		'''Value of variable $LAST_DATE'''
		return self._instance.LastDate

	@property
	def run_task(self) -> typing.List[str]:
		'''Value of variable $RUN_TASK'''
		return self._instance.RunTask

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MfrqGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
