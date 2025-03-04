import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EoatcfgVariableType as eoatcfg_variable_type

class EoatcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = eoatcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def curr_cnt(self) -> int:
		return self._instance.CurrCnt
	@property
	def rqst_cnt(self) -> int:
		return self._instance.RqstCnt
	@property
	def enb_msg(self) -> bool:
		return self._instance.EnbMsg
	@property
	def throttle(self) -> int:
		return self._instance.Throttle
	@property
	def thro_num(self) -> float:
		return self._instance.ThroNum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
