import typing
from underautomation.fanuc.rmi.data.controller_error_text import ControllerErrorText
from underautomation.fanuc.rmi.data.controller_status import ControllerStatus
from underautomation.fanuc.rmi.data.indexed_frame import IndexedFrame
from underautomation.fanuc.rmi.data.frame import Frame
from underautomation.fanuc.rmi.data.digital_input_value import DigitalInputValue
from underautomation.fanuc.rmi.data.on_off import OnOff
from underautomation.fanuc.rmi.data.cartesian_position import CartesianPosition
from underautomation.fanuc.rmi.data.joint_angles_sample import JointAnglesSample
from underautomation.fanuc.rmi.data.u_frame_u_tool_numbers import UFrameUToolNumbers
from underautomation.fanuc.rmi.data.position_register_data import PositionRegisterData
from underautomation.fanuc.rmi.data.motion_configuration import MotionConfiguration
from underautomation.fanuc.rmi.data.tcp_speed import TcpSpeed
from underautomation.fanuc.rmi.data.rmi_sequence_response import RmiSequenceResponse
from underautomation.fanuc.rmi.data.speed_type import SpeedType
from underautomation.fanuc.rmi.data.termination_type import TerminationType
from underautomation.fanuc.rmi.data.joint_angles import JointAngles
from underautomation.fanuc.rmi.data.port_type import PortType
from UnderAutomation.Fanuc.Rmi.Internal import RmiClientBase as rmi_client_base
from UnderAutomation.Fanuc.Rmi.Data import OnOff as on_off
from UnderAutomation.Fanuc.Rmi.Data import SpeedType as speed_type
from UnderAutomation.Fanuc.Rmi.Data import TerminationType as termination_type
from UnderAutomation.Fanuc.Rmi.Data import PortType as port_type

class RmiClientBase:
	'''High level Remote Motion Interface (RMI) client for FANUC controllers. This client speaks the ASCII JSON-like protocol over TCP as described in the RMI Operator's Manual. Supports connection bootstrap on port 16001 and all documented admin commands and TP instruction packets.'''
	def __init__(self, _internal = 0):
		'''Creates a new instance of the RMI client.'''
		if(_internal == 0):
			self._instance = rmi_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnect from the controller by sending FRC_Disconnect on the working port.'''
		self._instance.Disconnect()

	def initialize(self) -> int:
		'''Send the initialize command to create and start RMI_MOVE. Must be called before sending instruction packets.'''
		return self._instance.Initialize()

	def abort(self) -> None:
		'''Abort RMI_MOVE.'''
		self._instance.Abort()

	def pause(self) -> None:
		'''Pause RMI_MOVE.'''
		self._instance.Pause()

	def continue_(self) -> None:
		'''Resume RMI_MOVE.'''
		self._instance.Continue()

	def reset(self) -> None:
		'''Reset controller errors and exit HOLD state.'''
		self._instance.Reset()

	def read_error(self) -> ControllerErrorText:
		'''Read the most recent error text.'''
		return ControllerErrorText(self._instance.ReadError())

	def set_u_frame_u_tool(self, uframe: int, utool: int) -> None:
		'''Set current UFRAME and UTOOL numbers.'''
		self._instance.SetUFrameUTool(uframe, utool)

	def get_status(self) -> ControllerStatus:
		'''Get controller status and RMI state.'''
		return ControllerStatus(self._instance.GetStatus())

	def read_u_frame(self, number: int) -> IndexedFrame:
		'''Read a UFRAME.'''
		return IndexedFrame(self._instance.ReadUFrame(number))

	def write_u_frame(self, number: int, frame: Frame) -> None:
		'''Write a UFRAME.'''
		self._instance.WriteUFrame(number, frame._instance if frame else None)

	def read_u_tool(self, number: int) -> IndexedFrame:
		'''Read a UTOOL.'''
		return IndexedFrame(self._instance.ReadUTool(number))

	def write_u_tool(self, number: int, frame: Frame) -> None:
		'''Write a UTOOL.'''
		self._instance.WriteUTool(number, frame._instance if frame else None)

	def read_din(self, portNumber: int) -> DigitalInputValue:
		'''Read a digital input port value.'''
		return DigitalInputValue(self._instance.ReadDIN(portNumber))

	def write_dout(self, portNumber: int, value: OnOff) -> None:
		'''Write a digital output port value.'''
		self._instance.WriteDOUT(portNumber, on_off(int(value)))

	def read_cartesian_position(self) -> CartesianPosition:
		'''Read current Cartesian position.'''
		return CartesianPosition(self._instance.ReadCartesianPosition())

	def read_joint_angles(self) -> JointAnglesSample:
		'''Read current joint angles.'''
		return JointAnglesSample(self._instance.ReadJointAngles())

	def set_override(self, value: int) -> None:
		'''Set program override (1-100).'''
		self._instance.SetOverride(value)

	def get_u_frame_u_tool(self) -> UFrameUToolNumbers:
		'''Get current UFRAME/UTOOL numbers.'''
		return UFrameUToolNumbers(self._instance.GetUFrameUTool())

	def read_position_register(self, number: int) -> PositionRegisterData:
		'''Read a position register.'''
		return PositionRegisterData(self._instance.ReadPositionRegister(number))

	def write_position_register(self, number: int, cfg: MotionConfiguration, frame: Frame) -> None:
		'''Write a position register.'''
		self._instance.WritePositionRegister(number, cfg._instance if cfg else None, frame._instance if frame else None)

	def read_tcp_speed(self) -> TcpSpeed:
		'''Read current TCP speed.'''
		return TcpSpeed(self._instance.ReadTcpSpeed())

	def wait_din(self, sequenceId: int, portNumber: int, value: OnOff) -> RmiSequenceResponse:
		'''Add WAIT DI[x] = ON/OFF.'''
		return RmiSequenceResponse(self._instance.WaitDin(sequenceId, portNumber, on_off(int(value))))

	def set_u_frame_instruction(self, sequenceId: int, frameNumber: int) -> RmiSequenceResponse:
		'''Add UFRAME_NUM = n.'''
		return RmiSequenceResponse(self._instance.SetUFrameInstruction(sequenceId, frameNumber))

	def set_u_tool_instruction(self, sequenceId: int, toolNumber: int) -> RmiSequenceResponse:
		'''Add UTOOL_NUM = n.'''
		return RmiSequenceResponse(self._instance.SetUToolInstruction(sequenceId, toolNumber))

	def wait_time(self, sequenceId: int, seconds: float) -> RmiSequenceResponse:
		'''Add WAIT t (sec).'''
		return RmiSequenceResponse(self._instance.WaitTime(sequenceId, seconds))

	def set_payload(self, sequenceId: int, scheduleNumber: int) -> RmiSequenceResponse:
		'''Add PAYLOAD[n].'''
		return RmiSequenceResponse(self._instance.SetPayload(sequenceId, scheduleNumber))

	def linear_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.LinearMotion(sequenceId, config._instance if config else None, position._instance if position else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def linear_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.LinearRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def joint_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointMotion(sequenceId, config._instance if config else None, position._instance if position else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def joint_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def circular_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, viaConfig: MotionConfiguration, viaPosition: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.CircularMotion(sequenceId, config._instance if config else None, position._instance if position else None, viaConfig._instance if viaConfig else None, viaPosition._instance if viaPosition else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def circular_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, viaConfig: MotionConfiguration, viaDelta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.CircularRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, viaConfig._instance if viaConfig else None, viaDelta._instance if viaDelta else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def joint_motion_j_rep(self, sequenceId: int, joints: JointAngles, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointMotionJRep(sequenceId, joints._instance if joints else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def joint_relative_j_rep(self, sequenceId: int, deltaJoints: JointAngles, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: int | None, offsetPr: int | None, visionPr: int | None, mrot: bool, lcbType: str, lcbValue: int | None, portType: PortType | None, portNumber: int | None, portValue: OnOff | None) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointRelativeJRep(sequenceId, deltaJoints._instance if deltaJoints else None, speed_type(int(speedType)), speed, termination_type(int(termType)), termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))

	def dispose(self) -> None:
		'''Dispose and disconnect'''
		self._instance.Dispose()

	@property
	def read_timeout_ms(self) -> int:
		'''Gets or sets the read timeout for TCP operations (milliseconds).'''
		return self._instance.ReadTimeoutMs

	@property
	def write_timeout_ms(self) -> int:
		'''Gets or sets the write timeout for TCP operations (milliseconds).'''
		return self._instance.WriteTimeoutMs

	@property
	def connected(self) -> bool:
		'''Indicates that the client is currently connected to the controller working port.'''
		return self._instance.Connected

	@property
	def major_version(self) -> int:
		'''Controller protocol major version reported during FRC_Connect.'''
		return self._instance.MajorVersion

	@property
	def minor_version(self) -> int:
		'''Controller protocol minor version reported during FRC_Connect.'''
		return self._instance.MinorVersion

	@property
	def working_port(self) -> int:
		'''Working port returned by the controller; all commands use this port after connection.'''
		return self._instance.WorkingPort

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
