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
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Internal import RmiClientBase as rmi_client_base

class RmiClientBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_client_base()
		else:
			self._instance = _internal
	def disconnect(self) -> None:
		self._instance.Disconnect()
	def initialize(self) -> int:
		return self._instance.Initialize()
	def abort(self) -> None:
		self._instance.Abort()
	def pause(self) -> None:
		self._instance.Pause()
	def continue_(self) -> None:
		self._instance.Continue()
	def reset(self) -> None:
		self._instance.Reset()
	def read_error(self) -> ControllerErrorText:
		return ControllerErrorText(self._instance.ReadError())
	def set_u_frame_u_tool(self, uframe: int, utool: int) -> None:
		self._instance.SetUFrameUTool(uframe, utool)
	def get_status(self) -> ControllerStatus:
		return ControllerStatus(self._instance.GetStatus())
	def read_u_frame(self, number: int) -> IndexedFrame:
		return IndexedFrame(self._instance.ReadUFrame(number))
	def write_u_frame(self, number: int, frame: Frame) -> None:
		self._instance.WriteUFrame(number, frame._instance if frame else None)
	def read_u_tool(self, number: int) -> IndexedFrame:
		return IndexedFrame(self._instance.ReadUTool(number))
	def write_u_tool(self, number: int, frame: Frame) -> None:
		self._instance.WriteUTool(number, frame._instance if frame else None)
	def read_din(self, portNumber: int) -> DigitalInputValue:
		return DigitalInputValue(self._instance.ReadDIN(portNumber))
	def write_dout(self, portNumber: int, value: OnOff) -> None:
		self._instance.WriteDOUT(portNumber, value)
	def read_cartesian_position(self) -> CartesianPosition:
		return CartesianPosition(self._instance.ReadCartesianPosition())
	def read_joint_angles(self) -> JointAnglesSample:
		return JointAnglesSample(self._instance.ReadJointAngles())
	def set_override(self, value: int) -> None:
		self._instance.SetOverride(value)
	def get_u_frame_u_tool(self) -> UFrameUToolNumbers:
		return UFrameUToolNumbers(self._instance.GetUFrameUTool())
	def read_position_register(self, number: int) -> PositionRegisterData:
		return PositionRegisterData(self._instance.ReadPositionRegister(number))
	def write_position_register(self, number: int, cfg: MotionConfiguration, frame: Frame) -> None:
		self._instance.WritePositionRegister(number, cfg._instance if cfg else None, frame._instance if frame else None)
	def read_tcp_speed(self) -> TcpSpeed:
		return TcpSpeed(self._instance.ReadTcpSpeed())
	def wait_din(self, sequenceId: int, portNumber: int, value: OnOff) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.WaitDin(sequenceId, portNumber, value))
	def set_u_frame_instruction(self, sequenceId: int, frameNumber: int) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.SetUFrameInstruction(sequenceId, frameNumber))
	def set_u_tool_instruction(self, sequenceId: int, toolNumber: int) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.SetUToolInstruction(sequenceId, toolNumber))
	def wait_time(self, sequenceId: int, seconds: float) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.WaitTime(sequenceId, seconds))
	def set_payload(self, sequenceId: int, scheduleNumber: int) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.SetPayload(sequenceId, scheduleNumber))
	def linear_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.LinearMotion(sequenceId, config._instance if config else None, position._instance if position else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def linear_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.LinearRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def joint_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointMotion(sequenceId, config._instance if config else None, position._instance if position else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def joint_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def circular_motion(self, sequenceId: int, config: MotionConfiguration, position: Frame, viaConfig: MotionConfiguration, viaPosition: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.CircularMotion(sequenceId, config._instance if config else None, position._instance if position else None, viaConfig._instance if viaConfig else None, viaPosition._instance if viaPosition else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def circular_relative(self, sequenceId: int, config: MotionConfiguration, delta: Frame, viaConfig: MotionConfiguration, viaDelta: Frame, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, wristJoint: bool, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.CircularRelative(sequenceId, config._instance if config else None, delta._instance if delta else None, viaConfig._instance if viaConfig else None, viaDelta._instance if viaDelta else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, wristJoint, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def joint_motion_j_rep(self, sequenceId: int, joints: JointAngles, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointMotionJRep(sequenceId, joints._instance if joints else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def joint_relative_j_rep(self, sequenceId: int, deltaJoints: JointAngles, speedType: SpeedType, speed: int, termType: TerminationType, termValue: int, acc: typing.Any, offsetPr: typing.Any, visionPr: typing.Any, mrot: bool, lcbType: str, lcbValue: typing.Any, portType: typing.Any, portNumber: typing.Any, portValue: typing.Any) -> RmiSequenceResponse:
		return RmiSequenceResponse(self._instance.JointRelativeJRep(sequenceId, deltaJoints._instance if deltaJoints else None, speedType, speed, termType, termValue, acc, offsetPr, visionPr, mrot, lcbType, lcbValue, portType, portNumber, portValue))
	def dispose(self) -> None:
		self._instance.Dispose()
	@property
	def read_timeout_ms(self) -> int:
		return self._instance.ReadTimeoutMs
	@property
	def write_timeout_ms(self) -> int:
		return self._instance.WriteTimeoutMs
	@property
	def connected(self) -> bool:
		return self._instance.Connected
	@property
	def major_version(self) -> int:
		return self._instance.MajorVersion
	@property
	def minor_version(self) -> int:
		return self._instance.MinorVersion
	@property
	def working_port(self) -> int:
		return self._instance.WorkingPort
