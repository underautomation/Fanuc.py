import typing
from underautomation.fanuc.snpx.internal.numeric_registers import NumericRegisters
from underautomation.fanuc.snpx.internal.position_registers import PositionRegisters
from underautomation.fanuc.snpx.internal.string_registers import StringRegisters
from underautomation.fanuc.snpx.internal.integer_system_variables import IntegerSystemVariables
from underautomation.fanuc.snpx.internal.real_system_variables import RealSystemVariables
from underautomation.fanuc.snpx.internal.position_system_variables import PositionSystemVariables
from underautomation.fanuc.snpx.internal.string_system_variables import StringSystemVariables
from underautomation.fanuc.snpx.internal.digital_signals import DigitalSignals
from underautomation.fanuc.snpx.internal.numeric_io import NumericIO
from underautomation.fanuc.snpx.internal.current_position import CurrentPosition
from underautomation.fanuc.snpx.internal.alarm_access import AlarmAccess
from underautomation.fanuc.snpx.internal.assignment import Assignment
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SnpxClientBase as snpx_client_base

class SnpxClientBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_client_base()
		else:
			self._instance = _internal
	def disconnect(self) -> None:
		self._instance.Disconnect()
	def clear_alarms(self) -> None:
		self._instance.ClearAlarms()
	def set_variable(self, name: str, value: float) -> None:
		self._instance.SetVariable(name, value)
	def clear_assignments(self) -> None:
		self._instance.ClearAssignments()
	def get_assignments(self) -> typing.List[Assignment]:
		return [Assignment(x) for x in self._instance.GetAssignments()]
	@property
	def ip(self) -> str:
		return self._instance.Ip
	@property
	def numeric_registers(self) -> NumericRegisters:
		return NumericRegisters(self._instance.NumericRegisters)
	@property
	def position_registers(self) -> PositionRegisters:
		return PositionRegisters(self._instance.PositionRegisters)
	@property
	def string_registers(self) -> StringRegisters:
		return StringRegisters(self._instance.StringRegisters)
	@property
	def integer_system_variables(self) -> IntegerSystemVariables:
		return IntegerSystemVariables(self._instance.IntegerSystemVariables)
	@property
	def real_system_variables(self) -> RealSystemVariables:
		return RealSystemVariables(self._instance.RealSystemVariables)
	@property
	def position_system_variables(self) -> PositionSystemVariables:
		return PositionSystemVariables(self._instance.PositionSystemVariables)
	@property
	def string_system_variables(self) -> StringSystemVariables:
		return StringSystemVariables(self._instance.StringSystemVariables)
	@property
	def digital_signals(self) -> typing.List[DigitalSignals]:
		return [DigitalSignals(x) for x in self._instance.DigitalSignals]
	@property
	def sdi(self) -> DigitalSignals:
		return DigitalSignals(self._instance.SDI)
	@property
	def sdo(self) -> DigitalSignals:
		return DigitalSignals(self._instance.SDO)
	@property
	def rdi(self) -> DigitalSignals:
		return DigitalSignals(self._instance.RDI)
	@property
	def rdo(self) -> DigitalSignals:
		return DigitalSignals(self._instance.RDO)
	@property
	def ui(self) -> DigitalSignals:
		return DigitalSignals(self._instance.UI)
	@property
	def uo(self) -> DigitalSignals:
		return DigitalSignals(self._instance.UO)
	@property
	def si(self) -> DigitalSignals:
		return DigitalSignals(self._instance.SI)
	@property
	def so(self) -> DigitalSignals:
		return DigitalSignals(self._instance.SO)
	@property
	def wi(self) -> DigitalSignals:
		return DigitalSignals(self._instance.WI)
	@property
	def wo(self) -> DigitalSignals:
		return DigitalSignals(self._instance.WO)
	@property
	def wsi(self) -> DigitalSignals:
		return DigitalSignals(self._instance.WSI)
	@property
	def pm_c__k(self) -> DigitalSignals:
		return DigitalSignals(self._instance.PMC_K)
	@property
	def pm_c__r(self) -> DigitalSignals:
		return DigitalSignals(self._instance.PMC_R)
	@property
	def numeric_i_os(self) -> typing.List[NumericIO]:
		return [NumericIO(x) for x in self._instance.NumericIOs]
	@property
	def gi(self) -> NumericIO:
		return NumericIO(self._instance.GI)
	@property
	def go(self) -> NumericIO:
		return NumericIO(self._instance.GO)
	@property
	def ai(self) -> NumericIO:
		return NumericIO(self._instance.AI)
	@property
	def ao(self) -> NumericIO:
		return NumericIO(self._instance.AO)
	@property
	def pm_c__d(self) -> NumericIO:
		return NumericIO(self._instance.PMC_D)
	@property
	def current_position(self) -> CurrentPosition:
		return CurrentPosition(self._instance.CurrentPosition)
	@property
	def active_alarm(self) -> AlarmAccess:
		return AlarmAccess(self._instance.ActiveAlarm)
	@property
	def alarm_history(self) -> AlarmAccess:
		return AlarmAccess(self._instance.AlarmHistory)
	@property
	def connected(self) -> bool:
		return self._instance.Connected
