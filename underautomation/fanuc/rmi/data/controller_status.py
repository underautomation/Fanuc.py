import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import ControllerStatus as controller_status

class ControllerStatus(RmiResponseBase):
	'''Status snapshot returned by FRC_GetStatus.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_status()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def servo_ready(self) -> int:
		'''Servo ready state (1 = ready).'''
		return self._instance.ServoReady

	@servo_ready.setter
	def servo_ready(self, value: int):
		self._instance.ServoReady = value

	@property
	def tp_mode(self) -> int:
		'''Teach pendant mode (0 = disabled/AUTO, 1 = enabled/TEACH).'''
		return self._instance.TPMode

	@tp_mode.setter
	def tp_mode(self, value: int):
		self._instance.TPMode = value

	@property
	def rmi_motion_status(self) -> int:
		'''RMI motion runtime state (1 = running).'''
		return self._instance.RMIMotionStatus

	@rmi_motion_status.setter
	def rmi_motion_status(self, value: int):
		self._instance.RMIMotionStatus = value

	@property
	def program_status(self) -> int:
		'''RMI_MOVE program status (1 = aborted).'''
		return self._instance.ProgramStatus

	@program_status.setter
	def program_status(self, value: int):
		self._instance.ProgramStatus = value

	@property
	def single_step_mode(self) -> int:
		'''Single step mode flag (1 = on).'''
		return self._instance.SingleStepMode

	@single_step_mode.setter
	def single_step_mode(self, value: int):
		self._instance.SingleStepMode = value

	@property
	def number_u_tool(self) -> int:
		'''Number of UTOOLs configured.'''
		return self._instance.NumberUTool

	@number_u_tool.setter
	def number_u_tool(self, value: int):
		self._instance.NumberUTool = value

	@property
	def next_sequence_id(self) -> int:
		'''Next valid SequenceID when sequence checking is enabled.'''
		return self._instance.NextSequenceId

	@next_sequence_id.setter
	def next_sequence_id(self, value: int):
		self._instance.NextSequenceId = value

	@property
	def number_u_frame(self) -> int:
		'''Number of UFRAMEs configured.'''
		return self._instance.NumberUFrame

	@number_u_frame.setter
	def number_u_frame(self, value: int):
		self._instance.NumberUFrame = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
