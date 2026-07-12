from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_controller_error_text_response import RmiControllerErrorTextResponse
from underautomation.fanuc.rmi.data.rmi_u_frame_u_tool_numbers_response import RmiUFrameUToolNumbersResponse
from underautomation.fanuc.rmi.data.rmi_controller_status_response import RmiControllerStatusResponse
from underautomation.fanuc.rmi.data.rmi_extended_controller_status_response import RmiExtendedControllerStatusResponse
from underautomation.fanuc.rmi.data.rmi_indexed_frame_response import RmiIndexedFrameResponse
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.rmi.data.rmi_digital_input_value_response import RmiDigitalInputValueResponse
from underautomation.fanuc.rmi.data.rmi_on_off import RmiOnOff
from underautomation.fanuc.rmi.data.rmi_io_port_value_response import RmiIoPortValueResponse
from underautomation.fanuc.rmi.data.rmi_io_port_type import RmiIoPortType
from underautomation.fanuc.rmi.data.rmi_cartesian_position_response import RmiCartesianPositionResponse
from underautomation.fanuc.rmi.data.rmi_joint_angles_sample_response import RmiJointAnglesSampleResponse
from underautomation.fanuc.rmi.data.rmi_position_register_data_response import RmiPositionRegisterDataResponse
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.rmi.data.rmi_numeric_register_value_response import RmiNumericRegisterValueResponse
from underautomation.fanuc.rmi.data.rmi_variable_value_response import RmiVariableValueResponse
from underautomation.fanuc.rmi.data.rmi_tcp_speed_response import RmiTcpSpeedResponse
from underautomation.fanuc.rmi.data.rmi_set_payload_parameters import RmiSetPayloadParameters
from underautomation.fanuc.rmi.data.rmi_set_payload_compensation_parameters import RmiSetPayloadCompensationParameters
from underautomation.fanuc.rmi.data.rmi_instruction_response import RmiInstructionResponse
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from underautomation.fanuc.rmi.data.rmi_recorded_cartesian_position import RmiRecordedCartesianPosition
from underautomation.fanuc.rmi.data.rmi_recorded_joint_position import RmiRecordedJointPosition
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from underautomation.fanuc.rmi.data.rmi_pltz_mode import RmiPltzMode
from UnderAutomation.Fanuc.Rmi.Internal import RmiClientBase as rmi_client_base
from UnderAutomation.Fanuc.Rmi.Data import RmiOnOff as rmi_on_off
from UnderAutomation.Fanuc.Rmi.Data import RmiIoPortType as rmi_io_port_type
from UnderAutomation.Fanuc.Rmi.Data import RmiPltzMode as rmi_pltz_mode

class RmiClientBase:
	'''High-level Remote Motion Interface (RMI) client for FANUC controllers. Manages the connection lifecycle, all administrative commands, and the full set of motion instruction packets over the RMI TCP protocol.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the RMI client.'''
		if(_internal == 0):
			self._instance = rmi_client_base()
		else:
			self._instance = _internal

	def connection_terminated(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ConnectionTerminated+= lambda  : handler()

	def system_fault_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.SystemFaultReceived+= lambda obj : handler(Wrapper(obj))

	def recorded_cartesian_position_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RecordedCartesianPositionReceived+= lambda obj : handler(Wrapper(obj))

	def recorded_joint_position_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RecordedJointPositionReceived+= lambda obj : handler(Wrapper(obj))

	def unknown_packet_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.UnknownPacketReceived+= lambda obj : handler(Wrapper(obj))

	def disconnect(self) -> None:
		'''Disconnect from the controller by sending the disconnect command on the working port. Safe to call even when already disconnected.'''
		self._instance.Disconnect()

	def initialize(self, groupMask: int | None=None, rtsa: bool | None=None, pltzMode: RmiPltzMode | None=None) -> None:
		self._instance.Initialize(groupMask, rtsa, pltzMode)

	def abort(self) -> None:
		'''Abort the running motion program. Note that a Reset() will be called automatically if the controller is in the HOLD state.'''
		self._instance.Abort()

	def pause(self) -> None:
		'''Pause the running motion program.'''
		self._instance.Pause()

	def continue_(self) -> None:
		'''Resume a paused motion program.'''
		self._instance.Continue()

	def reset(self) -> None:
		'''Reset controller errors and exit the HOLD state.'''
		self._instance.Reset()

	def read_error(self, count: int | None=None) -> RmiControllerErrorTextResponse:
		return RmiControllerErrorTextResponse(self._instance.ReadError(count))

	def get_u_frame_u_tool(self, group: int | None=None) -> RmiUFrameUToolNumbersResponse:
		return RmiUFrameUToolNumbersResponse(self._instance.GetUFrameUTool(group))

	def set_u_frame_u_tool(self, uframe: int, utool: int, group: int | None=None) -> None:
		self._instance.SetUFrameUTool(uframe, utool, group)

	def get_status(self) -> RmiControllerStatusResponse:
		'''Get the current controller and RMI motion status.'''
		return RmiControllerStatusResponse(self._instance.GetStatus())

	def auto_set_next_sequence_id(self) -> RmiControllerStatusResponse:
		'''Calls internally GetStatus and set LastSequenceId only if $RMI_CFG.$Chk_seqID = FALSE. It also set CheckSequenceId to $RMI_CFG.$Chk_seqID.'''
		return RmiControllerStatusResponse(self._instance.AutoSetNextSequenceId())

	def get_extended_status(self) -> RmiExtendedControllerStatusResponse:
		'''Get extended controller status including drive power state and speed clamp.'''
		return RmiExtendedControllerStatusResponse(self._instance.GetExtendedStatus())

	def read_u_frame(self, number: int, group: int | None=None) -> RmiIndexedFrameResponse:
		return RmiIndexedFrameResponse(self._instance.ReadUFrame(number, group))

	def write_u_frame(self, number: int, position: XYZWPRPosition, group: int | None=None) -> None:
		self._instance.WriteUFrame(number, position._instance if position else None, group)

	def read_u_tool(self, number: int, group: int | None=None) -> RmiIndexedFrameResponse:
		return RmiIndexedFrameResponse(self._instance.ReadUTool(number, group))

	def write_u_tool(self, number: int, position: XYZWPRPosition, group: int | None=None) -> None:
		self._instance.WriteUTool(number, position._instance if position else None, group)

	def read_din(self, portNumber: int) -> RmiDigitalInputValueResponse:
		'''Read a digital input port value.'''
		return RmiDigitalInputValueResponse(self._instance.ReadDIN(portNumber))

	def write_dout(self, portNumber: int, value: RmiOnOff) -> None:
		'''Write a digital output port value.'''
		self._instance.WriteDOUT(portNumber, rmi_on_off(int(value)))

	def read_io_port(self, portType: RmiIoPortType, portNumber: int) -> RmiIoPortValueResponse:
		'''Read a generic IO port (DI, DO, AI, AO, GO, RO, FLAG, RI, UI, UO).

		:param portType: Type of IO port.
		:param portNumber: Port number.
		'''
		return RmiIoPortValueResponse(self._instance.ReadIOPort(rmi_io_port_type(int(portType)), portNumber))

	def write_io_port(self, portType: RmiIoPortType, portNumber: int, value: float) -> None:
		'''Write a generic IO port (AO, GO, DO, RO, FLAG).

		:param portType: Type of IO port.
		:param portNumber: Port number.
		:param value: Value to write.
		'''
		self._instance.WriteIOPort(rmi_io_port_type(int(portType)), portNumber, value)

	def read_cartesian_position(self, group: int | None=None) -> RmiCartesianPositionResponse:
		return RmiCartesianPositionResponse(self._instance.ReadCartesianPosition(group))

	def read_joint_angles(self, group: int | None=None) -> RmiJointAnglesSampleResponse:
		return RmiJointAnglesSampleResponse(self._instance.ReadJointAngles(group))

	def set_override(self, value: int) -> None:
		'''Set the program speed override (1–100 %).'''
		self._instance.SetOverride(value)

	def read_position_register(self, number: int, group: int | None=None) -> RmiPositionRegisterDataResponse:
		return RmiPositionRegisterDataResponse(self._instance.ReadPositionRegister(number, group))

	def write_position_register_cartesian(self, number: int, target: CartesianPositionWithUserFrame, group: int | None=None) -> None:
		self._instance.WritePositionRegisterCartesian(number, target._instance if target else None, group)

	def read_numeric_register(self, number: int) -> RmiNumericRegisterValueResponse:
		'''Read a numeric register

		:param number: Register number
		'''
		return RmiNumericRegisterValueResponse(self._instance.ReadNumericRegister(number))

	def write_numeric_register_as_integer(self, number: int, value: int) -> None:
		'''Write an integer value to a numeric register

		:param number: Register number
		:param value: Integer value to write.
		'''
		self._instance.WriteNumericRegisterAsInteger(number, value)

	def write_numeric_register_as_double(self, number: int, value: float) -> None:
		'''Write a float value to a numeric register

		:param number: Register number
		:param value: Float value to write.
		'''
		self._instance.WriteNumericRegisterAsDouble(number, value)

	def read_variable(self, name: str) -> RmiVariableValueResponse:
		'''Read a system variable by name (name must include the leading $ character).'''
		return RmiVariableValueResponse(self._instance.ReadVariable(name))

	def write_variable_as_integer(self, name: str, value: int) -> None:
		'''Write an integer value to a system variable (name must include the leading $).'''
		self._instance.WriteVariableAsInteger(name, value)

	def write_variable_as_double(self, name: str, value: float) -> None:
		'''Write a float value to a system variable (name must include the leading $).'''
		self._instance.WriteVariableAsDouble(name, value)

	def read_tcp_speed(self) -> RmiTcpSpeedResponse:
		'''Read the current TCP speed in mm/s.'''
		return RmiTcpSpeedResponse(self._instance.ReadTcpSpeed())

	def set_payload_schedule(self, scheduleNumber: int, group: int | None=None) -> None:
		self._instance.SetPayloadSchedule(scheduleNumber, group)

	def set_payload_value(self, scheduleNumber: int, massKg: float, cgXm: float, cgYm: float, cgZm: float, inertiaXkgm2: float | None=None, inertiaYkgm2: float | None=None, inertiaZkgm2: float | None=None, group: int | None=None) -> None:
		self._instance.SetPayloadValue(scheduleNumber, massKg, cgXm, cgYm, cgZm, inertiaXkgm2, inertiaYkgm2, inertiaZkgm2, group)

	def set_payload_compensation(self, scheduleNumber: int, massKg: float, cgXm: float, cgYm: float, cgZm: float, inertiaXkgm2: float, inertiaYkgm2: float, inertiaZkgm2: float, group: int | None=None) -> None:
		self._instance.SetPayloadCompensation(scheduleNumber, massKg, cgXm, cgYm, cgZm, inertiaXkgm2, inertiaYkgm2, inertiaZkgm2, group)

	def clear_completed_instructions(self) -> None:
		'''Removes all instructions with a terminal status (Completed or Error) from the tracked instruction list. Instructions that are still pending or in progress are not affected.'''
		self._instance.ClearCompletedInstructions()

	def clear_local_queued_instructions(self) -> None:
		'''Cancels and removes all instructions that are still in the local client buffer (LocalQueued). These instructions have not been sent to the controller yet. Each cancelled instruction is marked with an error so that any thread blocked on Int32) is unblocked. Instructions already sent to the controller are not affected.'''
		self._instance.ClearLocalQueuedInstructions()

	def send_tp_instruction(self, instruction: RmiInstructionBase) -> RmiInstructionResponse:
		'''Serializes the instruction to the RMI wire format and queues it on the controller. Returns an RmiInstructionResponse that tracks execution.

		:param instruction: Instruction to send. Must not be null.
		'''
		return RmiInstructionResponse(self._instance.SendTpInstruction(instruction._instance if instruction else None))

	def dispose(self) -> None:
		'''Disconnect from the controller and release resources.'''
		self._instance.Dispose()

	@property
	def connected(self) -> bool:
		'''Indicates that the client is currently connected to the controller working port.'''
		return self._instance.Connected

	@property
	def major_version(self) -> int:
		'''Controller protocol major version reported during the connection handshake.'''
		return self._instance.MajorVersion

	@property
	def minor_version(self) -> int:
		'''Controller protocol minor version reported during the connection handshake.'''
		return self._instance.MinorVersion

	@property
	def working_port(self) -> int:
		'''Working port returned by the controller; all commands use this port after connection.'''
		return self._instance.WorkingPort

	@property
	def last_sequence_id(self) -> int:
		'''Sequence ID used for the last instruction sent to the controller. Reset to 0 by RmiPltzMode}).. Modified by AutoSetNextSequenceId.'''
		return self._instance.LastSequenceId

	@property
	def check_sequence_id(self) -> bool:
		'''Indicates whether the controller checks for consecutive sequence IDs in motion instructions ($RMI_CFG.$Chk_seqID). Modified by AutoSetNextSequenceId.'''
		return self._instance.CheckSequenceId

	@check_sequence_id.setter
	def check_sequence_id(self, value: bool):
		self._instance.CheckSequenceId = value

	@property
	def is_in_hold_state(self) -> bool:
		'''Indicates that the controller has entered the HOLD state and will not accept new TP instructions until Reset is called. The HOLD state is entered in two situations: An invalid sequence ID was detected (error RMIT-029, error code 2556957). RMI checks that sequence IDs are consecutive. If a gap is found, RMI rejects the instruction and enters HOLD. The controller continues executing the TP instructions already queued but blocks all new ones. Use to recover the correct sequence ID, then call before resuming. An invalid motion instruction was received (error RMIT-024, error code 2556952), for example a motion option that is not loaded on the controller. RMI returns an error for that instruction, puts the controller in HOLD, and continues executing any instructions already in the TP program queue. Call once the problem is corrected, then resume sending instructions. All instructions sent while in the HOLD state are ignored by the controller and returned with an error code. This flag is cleared automatically when succeeds.'''
		return self._instance.IsInHoldState

	@property
	def read_timeout_ms(self) -> int:
		'''RMI connection parameters used during Connect().'''
		return self._instance.ReadTimeoutMs

	@property
	def instructions(self) -> typing.List[RmiInstructionResponse]:
		'''All instructions submitted since the last RmiPltzMode}) or explicit clear, in submission order. Includes instructions in all states: LocalQueued, ControllerQueued, Executing, Completed and Error. Returns a snapshot array; the array is not updated after it is returned.'''
		return [RmiInstructionResponse(x) for x in self._instance.Instructions]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._instance.Dispose()
		return False
