from __future__ import annotations
import typing
from underautomation.fanuc.common.task_status import TaskStatus
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiControllerStatusResponse as rmi_controller_status_response
from UnderAutomation.Fanuc.Common import TaskStatus as task_status

class RmiControllerStatusResponse(RmiResponseBase):
	'''Status snapshot returned by FRC_GetStatus.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_controller_status_response()
		else:
			self._instance = _internal

	@property
	def servo_ready(self) -> bool:
		'''The robot controller is ready for motion'''
		return self._instance.ServoReady

	@servo_ready.setter
	def servo_ready(self, value: bool):
		self._instance.ServoReady = value

	@property
	def tp_enabled(self) -> bool:
		'''Teach Pendant Enabled (Switch on position ON) The Remote Motion interface only works when the teach pendant is disabled'''
		return self._instance.TPEnabled

	@tp_enabled.setter
	def tp_enabled(self, value: bool):
		self._instance.TPEnabled = value

	@property
	def rmi_motion_status(self) -> bool:
		'''The Remote Motion Interface is running'''
		return self._instance.RmiMotionStatus

	@rmi_motion_status.setter
	def rmi_motion_status(self, value: bool):
		self._instance.RmiMotionStatus = value

	@property
	def program_status(self) -> TaskStatus:
		'''RMI_MOVE program status'''
		return TaskStatus(int(self._instance.ProgramStatus))

	@program_status.setter
	def program_status(self, value: TaskStatus):
		self._instance.ProgramStatus = task_status(int(value))

	@property
	def single_step_mode(self) -> bool:
		'''Single step mode'''
		return self._instance.SingleStepMode

	@single_step_mode.setter
	def single_step_mode(self, value: bool):
		self._instance.SingleStepMode = value

	@property
	def number_u_tool(self) -> int:
		'''Number of user tools available in the robot controller'''
		return self._instance.NumberUTool

	@number_u_tool.setter
	def number_u_tool(self, value: int):
		self._instance.NumberUTool = value

	@property
	def next_sequence_id(self) -> int | None:
		'''The next valid sequence ID. This key is only valid if the system variable $RMI_CFG.$Chk_seqID = TRUE'''
		return self._instance.NextSequenceId

	@next_sequence_id.setter
	def next_sequence_id(self, value: int | None):
		self._instance.NextSequenceId = value

	@property
	def number_u_frame(self) -> int:
		'''Number of user frames available in the robot controller'''
		return self._instance.NumberUFrame

	@number_u_frame.setter
	def number_u_frame(self, value: int):
		self._instance.NumberUFrame = value

	@property
	def speed_override(self) -> int:
		'''The current speed override setting (1–100).'''
		return self._instance.SpeedOverride

	@speed_override.setter
	def speed_override(self, value: int):
		self._instance.SpeedOverride = value

	@property
	def check_sequence_id(self) -> bool:
		'''Indicates the value of $RMI_CFG.$Chk_seqID, which is the configuration value that determines whether the controller checks valid incremented sequence IDs on incoming instructions.'''
		return self._instance.CheckSequenceId

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiControllerStatusResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
