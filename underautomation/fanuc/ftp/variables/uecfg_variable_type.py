import typing
from underautomation.fanuc.ftp.variables.req_data_variable_type import ReqDataVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UecfgVariableType as uecfg_variable_type

class UecfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = uecfg_variable_type()
		else:
			self._instance = _internal
	@property
	def chk_version(self) -> int:
		return self._instance.ChkVersion
	@property
	def rsm_chk_enb(self) -> bool:
		return self._instance.RsmChkEnb
	@property
	def unexcep_enb(self) -> bool:
		return self._instance.UnexcepEnb
	@property
	def rsm_thrs_r(self) -> float:
		return self._instance.RsmThrsR
	@property
	def rsm_thrs_l(self) -> float:
		return self._instance.RsmThrsL
	@property
	def unex_thrs_r(self) -> float:
		return self._instance.UnexThrsR
	@property
	def unex_thrs_l(self) -> float:
		return self._instance.UnexThrsL
	@property
	def req_count(self) -> int:
		return self._instance.ReqCount
	@property
	def req_data(self) -> typing.List[ReqDataVariableType]:
		return [ReqDataVariableType(x) for x in self._instance.ReqData]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
