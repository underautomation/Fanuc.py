import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SystemTimerVariableType as system_timer_variable_type

class SystemTimerVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = system_timer_variable_type()
		else:
			self._instance = _internal
	@property
	def pwr_tot(self) -> int:
		return self._instance.PwrTot
	@property
	def pwr_lap(self) -> int:
		return self._instance.PwrLap
	@property
	def srv_tot(self) -> int:
		return self._instance.SrvTot
	@property
	def srv_lap(self) -> int:
		return self._instance.SrvLap
	@property
	def run_flg(self) -> int:
		return self._instance.RunFlg
	@property
	def run_tot(self) -> int:
		return self._instance.RunTot
	@property
	def run_lap(self) -> int:
		return self._instance.RunLap
	@property
	def wit_flg(self) -> int:
		return self._instance.WitFlg
	@property
	def wit_tot(self) -> int:
		return self._instance.WitTot
	@property
	def wit_lap(self) -> int:
		return self._instance.WitLap
	@property
	def shm_tot(self) -> int:
		return self._instance.ShmTot
	@property
	def shm_lap(self) -> int:
		return self._instance.ShmLap
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
