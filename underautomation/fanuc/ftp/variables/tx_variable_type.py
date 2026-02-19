import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TxVariableType as tx_variable_type

class TxVariableType(GenericVariableType):
	'''Describes the Fanuc type TX_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tx_variable_type()
		else:
			self._instance = _internal

	@property
	def connected(self) -> bool:
		'''Value of variable $CONNECTED'''
		return self._instance.Connected

	@property
	def wdog_enable(self) -> bool:
		'''Value of variable $WDOG_ENABLE'''
		return self._instance.WdogEnable

	@property
	def wdog_erpost(self) -> bool:
		'''Value of variable $WDOG_ERPOST'''
		return self._instance.WdogErpost

	@property
	def wdog_timer(self) -> int:
		'''Value of variable $WDOG_TIMER'''
		return self._instance.WdogTimer

	@property
	def update_max(self) -> int:
		'''Value of variable $UPDATE_MAX'''
		return self._instance.UpdateMax

	@property
	def comm_mode(self) -> int:
		'''Value of variable $COMM_MODE'''
		return self._instance.CommMode

	@property
	def speed(self) -> int:
		'''Value of variable $SPEED'''
		return self._instance.Speed

	@property
	def tlnt_timer(self) -> int:
		'''Value of variable $TLNT_TIMER'''
		return self._instance.TlntTimer

	@property
	def ipaddr(self) -> int:
		'''Value of variable $IPADDR'''
		return self._instance.Ipaddr

	@property
	def input_port(self) -> int:
		'''Value of variable $INPUT_PORT'''
		return self._instance.InputPort

	@property
	def slow_timer(self) -> int:
		'''Value of variable $SLOW_TIMER'''
		return self._instance.SlowTimer

	@property
	def version(self) -> str:
		'''Value of variable $VERSION'''
		return self._instance.Version

	@property
	def coreversion(self) -> str:
		'''Value of variable $COREVERSION'''
		return self._instance.Coreversion

	@property
	def config_flag(self) -> int:
		'''Value of variable $CONFIG_FLAG'''
		return self._instance.ConfigFlag

	@property
	def touch_enb(self) -> bool:
		'''Value of variable $TOUCH_ENB'''
		return self._instance.TouchEnb

	@property
	def tp3d(self) -> bool:
		'''Value of variable $TP3D'''
		return self._instance.Tp3d

	@property
	def haptic_dev(self) -> int:
		'''Value of variable $HAPTIC_DEV'''
		return self._instance.HapticDev

	@property
	def htcg_port(self) -> int:
		'''Value of variable $HTCG_PORT'''
		return self._instance.HtcgPort

	@property
	def httc_port(self) -> int:
		'''Value of variable $HTTC_PORT'''
		return self._instance.HttcPort

	@property
	def vert_res(self) -> int:
		'''Value of variable $VERT_RES'''
		return self._instance.VertRes

	@property
	def horz_res(self) -> int:
		'''Value of variable $HORZ_RES'''
		return self._instance.HorzRes

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TxVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
