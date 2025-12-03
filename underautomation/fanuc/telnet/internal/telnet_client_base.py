import typing
from underautomation.fanuc.telnet.tp_coordinates import TpCoordinates
from underautomation.fanuc.telnet.program_command_result import ProgramCommandResult
from underautomation.fanuc.telnet.run_result import RunResult
from underautomation.fanuc.telnet.set_port_result import SetPortResult
from underautomation.fanuc.telnet.kcl_ports import KCLPorts
from underautomation.fanuc.telnet.set_variable_result import SetVariableResult
from underautomation.fanuc.telnet.get_current_pose_result import GetCurrentPoseResult
from underautomation.fanuc.telnet.get_variable_result import GetVariableResult
from underautomation.fanuc.telnet.simulate_result import SimulateResult
from underautomation.fanuc.telnet.unsimulate_all_result import UnsimulateAllResult
from underautomation.fanuc.telnet.unsimulate_result import UnsimulateResult
from underautomation.fanuc.telnet.custom_command_result import CustomCommandResult
from underautomation.fanuc.telnet.task_information_result import TaskInformationResult
from underautomation.fanuc.telnet.add_breakpoint_result import AddBreakpointResult
from underautomation.fanuc.telnet.remove_breakpoint_result import RemoveBreakpointResult
from underautomation.fanuc.telnet.breakpoints_result import BreakpointsResult
from underautomation.fanuc.telnet.step_on_result import StepOnResult
from underautomation.fanuc.telnet.step_off_result import StepOffResult
from underautomation.fanuc.telnet.raw_data_received_event_args import RawDataReceivedEventArgs
from underautomation.fanuc.telnet.tp_coordinates_received_event_args import TpCoordinatesReceivedEventArgs
from underautomation.fanuc.telnet.message_received_event_args import MessageReceivedEventArgs
from underautomation.fanuc.telnet.kcl_client_error_event_args import KclClientErrorEventArgs
from underautomation.fanuc.telnet.command_sent_event_args import CommandSentEventArgs
from underautomation.fanuc.telnet.kcl_command_received import KclCommandReceived
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet.Internal import TelnetClientBase as telnet_client_base

T = typing.TypeVar('T')
class TelnetClientBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = telnet_client_base()
		else:
			self._instance = _internal
	def raw_data_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.RawDataReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def tp_coordinates_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.TpCoordinatesReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def message_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.MessageReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def error_occured(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.ErrorOccured+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def command_sent(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CommandSent+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def command_received(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.CommandReceived+= lambda sender, e : handler(Wrapper(sender), Wrapper(e))
	def disconnect(self) -> None:
		self._instance.Disconnect()
	def abort(self, program: str="None", force: bool=True) -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.Abort(program, force))
	def abort_all(self, force: bool=True) -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.AbortAll(force))
	def clear_all(self) -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.ClearAll())
	def clear_program(self, program: str="None") -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.ClearProgram(program))
	def clear_vars(self, program: str="None") -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.ClearVars(program))
	def continue_(self, program: str="None") -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.Continue(program))
	def hold(self, program: str="None") -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.Hold(program))
	def pause(self, program: str="None", force: bool=False) -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.Pause(program, force))
	def reset(self) -> ProgramCommandResult:
		return ProgramCommandResult(self._instance.Reset())
	def run(self, program: str="None") -> RunResult:
		return RunResult(self._instance.Run(program))
	def set_port(self, port: KCLPorts, index: int, value: int) -> SetPortResult:
		return SetPortResult(self._instance.SetPort(port, index, value))
	def set_variable(self, name: str, value: float, program: str="None") -> SetVariableResult:
		return SetVariableResult(self._instance.SetVariable(name, value, program))
	def get_current_pose(self) -> GetCurrentPoseResult:
		return GetCurrentPoseResult(self._instance.GetCurrentPose())
	def get_variable(self, name: str, program: str="None") -> GetVariableResult:
		return GetVariableResult(self._instance.GetVariable(name, program))
	def simulate(self, port: KCLPorts, index: int, value: int) -> SimulateResult:
		return SimulateResult(self._instance.Simulate(port, index, value))
	def unsimulate_all(self) -> UnsimulateAllResult:
		return UnsimulateAllResult(self._instance.UnsimulateAll())
	def unsimulate(self, port: KCLPorts, index: int) -> UnsimulateResult:
		return UnsimulateResult(self._instance.Unsimulate(port, index))
	def send_custom_command(self, command: str) -> T:
		return self._instance.SendCustomCommand(command)
	def get_task_information(self, prog_name: str) -> TaskInformationResult:
		return TaskInformationResult(self._instance.GetTaskInformation(prog_name))
	def add_breakpoint(self, taskName: str, line: int) -> AddBreakpointResult:
		return AddBreakpointResult(self._instance.AddBreakpoint(taskName, line))
	def remove_breakpoint(self, taskName: str, line: int) -> RemoveBreakpointResult:
		return RemoveBreakpointResult(self._instance.RemoveBreakpoint(taskName, line))
	def remove_all_breakpoints(self, taskName: str) -> RemoveBreakpointResult:
		return RemoveBreakpointResult(self._instance.RemoveAllBreakpoints(taskName))
	def get_breakpoints(self, taskName: str) -> BreakpointsResult:
		return BreakpointsResult(self._instance.GetBreakpoints(taskName))
	def step_on(self, taskName: str) -> StepOnResult:
		return StepOnResult(self._instance.StepOn(taskName))
	def step_off(self) -> StepOffResult:
		return StepOffResult(self._instance.StepOff())
	@property
	def ip(self) -> str:
		return self._instance.IP
	@property
	def tp_coordinates(self) -> TpCoordinates:
		return TpCoordinates(self._instance.TpCoordinates)
	@property
	def connected(self) -> bool:
		return self._instance.Connected
