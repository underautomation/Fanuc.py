import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import ControllerStatus as controller_status

class ControllerStatus(RmiResponseBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_status()
		else:
			self._instance = _internal
	@property
	def servo_ready(self) -> int:
		return self._instance.ServoReady
	@servo_ready.setter
	def servo_ready(self, value: int):
		self._instance.ServoReady = value
	@property
	def tp_mode(self) -> int:
		return self._instance.TPMode
	@tp_mode.setter
	def tp_mode(self, value: int):
		self._instance.TPMode = value
	@property
	def rmi_motion_status(self) -> int:
		return self._instance.RMIMotionStatus
	@rmi_motion_status.setter
	def rmi_motion_status(self, value: int):
		self._instance.RMIMotionStatus = value
	@property
	def program_status(self) -> int:
		return self._instance.ProgramStatus
	@program_status.setter
	def program_status(self, value: int):
		self._instance.ProgramStatus = value
	@property
	def single_step_mode(self) -> int:
		return self._instance.SingleStepMode
	@single_step_mode.setter
	def single_step_mode(self, value: int):
		self._instance.SingleStepMode = value
	@property
	def number_u_tool(self) -> int:
		return self._instance.NumberUTool
	@number_u_tool.setter
	def number_u_tool(self, value: int):
		self._instance.NumberUTool = value
	@property
	def next_sequence_id(self) -> int:
		return self._instance.NextSequenceId
	@next_sequence_id.setter
	def next_sequence_id(self, value: int):
		self._instance.NextSequenceId = value
	@property
	def number_u_frame(self) -> int:
		return self._instance.NumberUFrame
	@number_u_frame.setter
	def number_u_frame(self, value: int):
		self._instance.NumberUFrame = value
