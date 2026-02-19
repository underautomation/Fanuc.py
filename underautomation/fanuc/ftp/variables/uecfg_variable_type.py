import typing
from underautomation.fanuc.ftp.variables.req_data_variable_type import ReqDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UecfgVariableType as uecfg_variable_type

class UecfgVariableType(GenericVariableType):
	'''Describes the Fanuc type UECFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = uecfg_variable_type()
		else:
			self._instance = _internal

	@property
	def chk_version(self) -> int:
		'''Value of variable $CHK_VERSION'''
		return self._instance.ChkVersion

	@property
	def rsm_chk_enb(self) -> bool:
		'''Value of variable $RSM_CHK_ENB'''
		return self._instance.RsmChkEnb

	@property
	def unexcep_enb(self) -> bool:
		'''Value of variable $UNEXCEP_ENB'''
		return self._instance.UnexcepEnb

	@property
	def rsm_thrs_r(self) -> float:
		'''Value of variable $RSM_THRS_R'''
		return self._instance.RsmThrsR

	@property
	def rsm_thrs_l(self) -> float:
		'''Value of variable $RSM_THRS_L'''
		return self._instance.RsmThrsL

	@property
	def unex_thrs_r(self) -> float:
		'''Value of variable $UNEX_THRS_R'''
		return self._instance.UnexThrsR

	@property
	def unex_thrs_l(self) -> float:
		'''Value of variable $UNEX_THRS_L'''
		return self._instance.UnexThrsL

	@property
	def req_count(self) -> int:
		'''Value of variable $REQ_COUNT'''
		return self._instance.ReqCount

	@property
	def req_data(self) -> typing.List[ReqDataVariableType]:
		'''Value of variable $REQ_DATA'''
		return [ReqDataVariableType(x) for x in self._instance.ReqData]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UecfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
