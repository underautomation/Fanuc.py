import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import EoatcfgVariableType as eoatcfg_variable_type

class EoatcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type EOATCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = eoatcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def curr_cnt(self) -> int:
		'''Value of variable $CURR_CNT'''
		return self._instance.CurrCnt

	@property
	def rqst_cnt(self) -> int:
		'''Value of variable $RQST_CNT'''
		return self._instance.RqstCnt

	@property
	def enb_msg(self) -> bool:
		'''Value of variable $ENB_MSG'''
		return self._instance.EnbMsg

	@property
	def throttle(self) -> int:
		'''Value of variable $THROTTLE'''
		return self._instance.Throttle

	@property
	def thro_num(self) -> float:
		'''Value of variable $THRO_NUM'''
		return self._instance.ThroNum

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EoatcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
