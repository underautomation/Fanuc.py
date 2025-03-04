import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CfParamgpVariableType as cf_paramgp_variable_type

class CfParamgpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cf_paramgp_variable_type()
		else:
			self._instance = _internal
	@property
	def warnmessenb(self) -> bool:
		return self._instance.Warnmessenb
	@property
	def chkjntlim(self) -> bool:
		return self._instance.Chkjntlim
	@property
	def cnstnt_corn(self) -> bool:
		return self._instance.CnstntCorn
	@property
	def timefltrenb(self) -> bool:
		return self._instance.Timefltrenb
	@property
	def tratio_tb(self) -> typing.List[float]:
		return self._instance.TratioTb
	@property
	def acctime_tb1(self) -> typing.List[float]:
		return self._instance.AcctimeTb1
	@property
	def acctime_tb2(self) -> typing.List[float]:
		return self._instance.AcctimeTb2
	@property
	def orient_type(self) -> int:
		return self._instance.OrientType
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def rtspd_sf(self) -> float:
		return self._instance.RtspdSf
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
