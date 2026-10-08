from __future__ import annotations
import typing
from underautomation.fanuc.snpx.internal.numeric_registers import NumericRegisters
from underautomation.fanuc.snpx.internal.numeric_registers_int32 import NumericRegistersInt32
from underautomation.fanuc.snpx.internal.numeric_registers_int16 import NumericRegistersInt16
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
from underautomation.fanuc.snpx.internal.current_task_status import CurrentTaskStatus
from underautomation.fanuc.snpx.internal.alarm_access import AlarmAccess
from underautomation.fanuc.snpx.internal.comments import Comments
from underautomation.fanuc.snpx.internal.simulation_status import SimulationStatus
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

	def set_variable(self, name: str, value: bool | float | int | str) -> None:
		'''Set boolean variable without assignments.
		Set double variable without assignments.
		Set integer variable without assignments.
		Set string variable without assignments.

		:param name: Variable name.
		:param value: Boolean value to set. Or: Double value to set. Or: Integer value to set. Or: String value to set.
		'''
		self._instance.SetVariable(name, value)

	def clear_assignments(self) -> None:
		'''Clear all assignments'''
		self._instance.ClearAssignments()

	def get_assignments(self) -> typing.List[Assignment]:
		'''Gets all current assignments.

		:returns: An array of all active assignments.
		'''
		__r = self._instance.GetAssignments()
		return None if __r is None else [None if x is None else Assignment(x) for x in __r]

	@property
	def ip(self) -> str:
		'''IP address of the connected robot.'''
		return self._instance.Ip

	@property
	def numeric_registers(self) -> NumericRegisters:
		'''Number registers R[] as floating point values'''
		__r = self._instance.NumericRegisters
		return None if __r is None else NumericRegisters(__r)

	@property
	def numeric_registers_int32(self) -> NumericRegistersInt32:
		'''Number registers R[] as 32-bit integer values'''
		__r = self._instance.NumericRegistersInt32
		return None if __r is None else NumericRegistersInt32(__r)

	@property
	def numeric_registers_int16(self) -> NumericRegistersInt16:
		'''Number registers R[] as 16-bit integer values'''
		__r = self._instance.NumericRegistersInt16
		return None if __r is None else NumericRegistersInt16(__r)

	@property
	def position_registers(self) -> PositionRegisters:
		'''Position registers'''
		__r = self._instance.PositionRegisters
		return None if __r is None else PositionRegisters(__r)

	@property
	def string_registers(self) -> StringRegisters:
		'''String registers'''
		__r = self._instance.StringRegisters
		return None if __r is None else StringRegisters(__r)

	@property
	def integer_system_variables(self) -> IntegerSystemVariables:
		'''Integer variables'''
		__r = self._instance.IntegerSystemVariables
		return None if __r is None else IntegerSystemVariables(__r)

	@property
	def real_system_variables(self) -> RealSystemVariables:
		'''Real variables'''
		__r = self._instance.RealSystemVariables
		return None if __r is None else RealSystemVariables(__r)

	@property
	def position_system_variables(self) -> PositionSystemVariables:
		'''Position variables'''
		__r = self._instance.PositionSystemVariables
		return None if __r is None else PositionSystemVariables(__r)

	@property
	def string_system_variables(self) -> StringSystemVariables:
		'''String variables'''
		__r = self._instance.StringSystemVariables
		return None if __r is None else StringSystemVariables(__r)

	@property
	def digital_signals(self) -> typing.List[DigitalSignals]:
		'''List of all digital signal accessors (SDI, SDO, RDI, RDO, ...)'''
		__r = self._instance.DigitalSignals
		return None if __r is None else [None if x is None else DigitalSignals(x) for x in __r]

	@property
	def sdi(self) -> DigitalSignals:
		'''Safety Digital Inputs'''
		__r = self._instance.SDI
		return None if __r is None else DigitalSignals(__r)

	@property
	def sdo(self) -> DigitalSignals:
		'''Safety Digital Outputs'''
		__r = self._instance.SDO
		return None if __r is None else DigitalSignals(__r)

	@property
	def rdi(self) -> DigitalSignals:
		'''Remote Digital Inputs'''
		__r = self._instance.RDI
		return None if __r is None else DigitalSignals(__r)

	@property
	def rdo(self) -> DigitalSignals:
		'''Remote Digital Outputs'''
		__r = self._instance.RDO
		return None if __r is None else DigitalSignals(__r)

	@property
	def ui(self) -> DigitalSignals:
		'''User Inputs'''
		__r = self._instance.UI
		return None if __r is None else DigitalSignals(__r)

	@property
	def uo(self) -> DigitalSignals:
		'''User Outputs'''
		__r = self._instance.UO
		return None if __r is None else DigitalSignals(__r)

	@property
	def si(self) -> DigitalSignals:
		'''System Inputs'''
		__r = self._instance.SI
		return None if __r is None else DigitalSignals(__r)

	@property
	def so(self) -> DigitalSignals:
		'''System Outputs'''
		__r = self._instance.SO
		return None if __r is None else DigitalSignals(__r)

	@property
	def wi(self) -> DigitalSignals:
		'''Weld Inputs'''
		__r = self._instance.WI
		return None if __r is None else DigitalSignals(__r)

	@property
	def wo(self) -> DigitalSignals:
		'''Weld Outputs'''
		__r = self._instance.WO
		return None if __r is None else DigitalSignals(__r)

	@property
	def wsi(self) -> DigitalSignals:
		'''Weld System Inputs'''
		__r = self._instance.WSI
		return None if __r is None else DigitalSignals(__r)

	@property
	def pmc_k(self) -> DigitalSignals:
		'''Programmable Machine Controller Constants'''
		__r = self._instance.PMC_K
		return None if __r is None else DigitalSignals(__r)

	@property
	def pmc_r(self) -> DigitalSignals:
		'''Programmable Machine Controller Relays'''
		__r = self._instance.PMC_R
		return None if __r is None else DigitalSignals(__r)

	@property
	def numeric_i_os(self) -> typing.List[NumericIO]:
		'''List of all Numeric IOs accessors (GI, GO, AI, AO, ...)'''
		__r = self._instance.NumericIOs
		return None if __r is None else [None if x is None else NumericIO(x) for x in __r]

	@property
	def gi(self) -> NumericIO:
		'''Group Inputs'''
		__r = self._instance.GI
		return None if __r is None else NumericIO(__r)

	@property
	def go(self) -> NumericIO:
		'''Group Outputs'''
		__r = self._instance.GO
		return None if __r is None else NumericIO(__r)

	@property
	def ai(self) -> NumericIO:
		'''Analog Inputs'''
		__r = self._instance.AI
		return None if __r is None else NumericIO(__r)

	@property
	def ao(self) -> NumericIO:
		'''Analog Outputs'''
		__r = self._instance.AO
		return None if __r is None else NumericIO(__r)

	@property
	def pmc_d(self) -> NumericIO:
		'''Programmable Machine Controller Data'''
		__r = self._instance.PMC_D
		return None if __r is None else NumericIO(__r)

	@property
	def flags(self) -> Flags:
		'''Flags'''
		__r = self._instance.Flags
		return None if __r is None else Flags(__r)

	@property
	def current_position(self) -> CurrentPosition:
		'''Current position in world or user frame'''
		__r = self._instance.CurrentPosition
		return None if __r is None else CurrentPosition(__r)

	@property
	def current_task_status(self) -> CurrentTaskStatus:
		'''Current program tasks status. Index starts from 1.'''
		__r = self._instance.CurrentTaskStatus
		return None if __r is None else CurrentTaskStatus(__r)

	@property
	def active_alarm(self) -> AlarmAccess:
		'''Current active alarms'''
		__r = self._instance.ActiveAlarm
		return None if __r is None else AlarmAccess(__r)

	@property
	def alarm_history(self) -> AlarmAccess:
		'''Alarm history'''
		__r = self._instance.AlarmHistory
		return None if __r is None else AlarmAccess(__r)

	@property
	def comments(self) -> Comments:
		'''Comments of registers, I/O signals and other data'''
		__r = self._instance.Comments
		return None if __r is None else Comments(__r)

	@property
	def simulation_status(self) -> SimulationStatus:
		'''I/O simulation status'''
		__r = self._instance.SimulationStatus
		return None if __r is None else SimulationStatus(__r)

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
