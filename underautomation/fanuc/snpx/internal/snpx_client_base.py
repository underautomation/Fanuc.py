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
from underautomation.fanuc.snpx.internal.flags import Flags
from underautomation.fanuc.snpx.internal.current_position import CurrentPosition
from underautomation.fanuc.snpx.internal.alarm_access import AlarmAccess
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.snpx.internal.assignment import Assignment
from UnderAutomation.Fanuc.Snpx.Internal import SnpxClientBase as snpx_client_base
from UnderAutomation.Fanuc.Common import Languages as languages

class SnpxClientBase:
	'''Base class for Snpx internal and public client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_client_base()
		else:
			self._instance = _internal

	def poll_and_get_updated_connected_state(self) -> bool:
		'''Checks the actual connection status via an active socket polling

		:returns: True if the connection is still open after checking via polling
		'''
		return self._instance.PollAndGetUpdatedConnectedState()

	def disconnect(self) -> None:
		'''Disconnect from the robot'''
		self._instance.Disconnect()

	def clear_alarms(self) -> None:
		'''Clear all active alarms'''
		self._instance.ClearAlarms()

	def set_variable(self, name: str, value: str) -> None:
		'''Set string variable without assignments.

		:param name: Variable name.
		:param value: String value to set.
		'''
		self._instance.SetVariable(name, value)

	def clear_assignments(self) -> None:
		'''Clear all assignments'''
		self._instance.ClearAssignments()

	def get_assignments(self) -> typing.List[Assignment]:
		'''Gets all current assignments.

		:returns: An array of all active assignments.
		'''
		return [Assignment(x) for x in self._instance.GetAssignments()]

	@property
	def ip(self) -> str:
		'''IP address of the connected robot.'''
		return self._instance.Ip

	@property
	def numeric_registers(self) -> NumericRegisters:
		'''Number registers'''
		return NumericRegisters(self._instance.NumericRegisters)

	@property
	def position_registers(self) -> PositionRegisters:
		'''Position registers'''
		return PositionRegisters(self._instance.PositionRegisters)

	@property
	def string_registers(self) -> StringRegisters:
		'''String registers'''
		return StringRegisters(self._instance.StringRegisters)

	@property
	def integer_system_variables(self) -> IntegerSystemVariables:
		'''Integer variables'''
		return IntegerSystemVariables(self._instance.IntegerSystemVariables)

	@property
	def real_system_variables(self) -> RealSystemVariables:
		'''Real variables'''
		return RealSystemVariables(self._instance.RealSystemVariables)

	@property
	def position_system_variables(self) -> PositionSystemVariables:
		'''Position variables'''
		return PositionSystemVariables(self._instance.PositionSystemVariables)

	@property
	def string_system_variables(self) -> StringSystemVariables:
		'''String variables'''
		return StringSystemVariables(self._instance.StringSystemVariables)

	@property
	def digital_signals(self) -> typing.List[DigitalSignals]:
		'''List of all digital signal accessors (SDI, SDO, RDI, RDO, ...)'''
		return [DigitalSignals(x) for x in self._instance.DigitalSignals]

	@property
	def sdi(self) -> DigitalSignals:
		'''Safety Digital Inputs'''
		return DigitalSignals(self._instance.SDI)

	@property
	def sdo(self) -> DigitalSignals:
		'''Safety Digital Outputs'''
		return DigitalSignals(self._instance.SDO)

	@property
	def rdi(self) -> DigitalSignals:
		'''Remote Digital Inputs'''
		return DigitalSignals(self._instance.RDI)

	@property
	def rdo(self) -> DigitalSignals:
		'''Remote Digital Outputs'''
		return DigitalSignals(self._instance.RDO)

	@property
	def ui(self) -> DigitalSignals:
		'''User Inputs'''
		return DigitalSignals(self._instance.UI)

	@property
	def uo(self) -> DigitalSignals:
		'''User Outputs'''
		return DigitalSignals(self._instance.UO)

	@property
	def si(self) -> DigitalSignals:
		'''System Inputs'''
		return DigitalSignals(self._instance.SI)

	@property
	def so(self) -> DigitalSignals:
		'''System Outputs'''
		return DigitalSignals(self._instance.SO)

	@property
	def wi(self) -> DigitalSignals:
		'''Weld Inputs'''
		return DigitalSignals(self._instance.WI)

	@property
	def wo(self) -> DigitalSignals:
		'''Weld Outputs'''
		return DigitalSignals(self._instance.WO)

	@property
	def wsi(self) -> DigitalSignals:
		'''Weld System Inputs'''
		return DigitalSignals(self._instance.WSI)

	@property
	def pm_c__k(self) -> DigitalSignals:
		'''Programmable Machine Controller Constants'''
		return DigitalSignals(self._instance.PMC_K)

	@property
	def pm_c__r(self) -> DigitalSignals:
		'''Programmable Machine Controller Relays'''
		return DigitalSignals(self._instance.PMC_R)

	@property
	def numeric_i_os(self) -> typing.List[NumericIO]:
		'''List of all Numeric IOs accessors (GI, GO, AI, AO, ...)'''
		return [NumericIO(x) for x in self._instance.NumericIOs]

	@property
	def gi(self) -> NumericIO:
		'''Group Inputs'''
		return NumericIO(self._instance.GI)

	@property
	def go(self) -> NumericIO:
		'''Group Outputs'''
		return NumericIO(self._instance.GO)

	@property
	def ai(self) -> NumericIO:
		'''Analog Inputs'''
		return NumericIO(self._instance.AI)

	@property
	def ao(self) -> NumericIO:
		'''Analog Outputs'''
		return NumericIO(self._instance.AO)

	@property
	def pm_c__d(self) -> NumericIO:
		'''Programmable Machine Controller Data'''
		return NumericIO(self._instance.PMC_D)

	@property
	def flags(self) -> Flags:
		'''Flags'''
		return Flags(self._instance.Flags)

	@property
	def current_position(self) -> CurrentPosition:
		'''Current position in world or user frame'''
		return CurrentPosition(self._instance.CurrentPosition)

	@property
	def active_alarm(self) -> AlarmAccess:
		'''Current active alarms'''
		return AlarmAccess(self._instance.ActiveAlarm)

	@property
	def alarm_history(self) -> AlarmAccess:
		'''Alarm history'''
		return AlarmAccess(self._instance.AlarmHistory)

	@property
	def language(self) -> Languages:
		'''Controller language (default is English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def connected(self) -> bool:
		'''Indicates if the SNPX underlying TCP client is connected to the robot'''
		return self._instance.Connected

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SnpxClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
