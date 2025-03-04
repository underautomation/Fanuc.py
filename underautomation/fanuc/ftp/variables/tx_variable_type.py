import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TxVariableType as tx_variable_type

class TxVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tx_variable_type()
		else:
			self._instance = _internal
	@property
	def connected(self) -> bool:
		return self._instance.Connected
	@property
	def wdog_enable(self) -> bool:
		return self._instance.WdogEnable
	@property
	def wdog_erpost(self) -> bool:
		return self._instance.WdogErpost
	@property
	def wdog_timer(self) -> int:
		return self._instance.WdogTimer
	@property
	def update_max(self) -> int:
		return self._instance.UpdateMax
	@property
	def comm_mode(self) -> int:
		return self._instance.CommMode
	@property
	def speed(self) -> int:
		return self._instance.Speed
	@property
	def tlnt_timer(self) -> int:
		return self._instance.TlntTimer
	@property
	def ipaddr(self) -> int:
		return self._instance.Ipaddr
	@property
	def input_port(self) -> int:
		return self._instance.InputPort
	@property
	def slow_timer(self) -> int:
		return self._instance.SlowTimer
	@property
	def version(self) -> str:
		return self._instance.Version
	@property
	def coreversion(self) -> str:
		return self._instance.Coreversion
	@property
	def config_flag(self) -> int:
		return self._instance.ConfigFlag
	@property
	def touch_enb(self) -> bool:
		return self._instance.TouchEnb
	@property
	def tp3d(self) -> bool:
		return self._instance.Tp3d
	@property
	def haptic_dev(self) -> int:
		return self._instance.HapticDev
	@property
	def htcg_port(self) -> int:
		return self._instance.HtcgPort
	@property
	def httc_port(self) -> int:
		return self._instance.HttcPort
	@property
	def vert_res(self) -> int:
		return self._instance.VertRes
	@property
	def horz_res(self) -> int:
		return self._instance.HorzRes
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
