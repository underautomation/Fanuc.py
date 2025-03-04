import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CoParamgpVariableType as co_paramgp_variable_type

class CoParamgpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = co_paramgp_variable_type()
		else:
			self._instance = _internal
	@property
	def opt_time(self) -> int:
		return self._instance.OptTime
	@property
	def opt_acc(self) -> bool:
		return self._instance.OptAcc
	@property
	def jacc_rratio(self) -> float:
		return self._instance.JaccRratio
	@property
	def cacc_rratio(self) -> float:
		return self._instance.CaccRratio
	@property
	def jtime_ratio(self) -> float:
		return self._instance.JtimeRatio
	@property
	def ctime_ratio(self) -> float:
		return self._instance.CtimeRatio
	@property
	def jvardmax(self) -> int:
		return self._instance.Jvardmax
	@property
	def cvardmax(self) -> int:
		return self._instance.Cvardmax
	@property
	def warnmessenb(self) -> bool:
		return self._instance.Warnmessenb
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def tba_mgn(self) -> float:
		return self._instance.TbaMgn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
