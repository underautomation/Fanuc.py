from __future__ import annotations
import typing
from underautomation.fanuc.common.kcl.program_command_result import ProgramCommandResult
from underautomation.fanuc.common.kcl.run_result import RunResult
from underautomation.fanuc.common.kcl.set_port_result import SetPortResult
from underautomation.fanuc.common.kcl.kcl_ports import KCLPorts
from underautomation.fanuc.common.kcl.set_variable_result import SetVariableResult
from underautomation.fanuc.common.kcl.get_current_pose_result import GetCurrentPoseResult
from underautomation.fanuc.common.kcl.get_variable_result import GetVariableResult
from underautomation.fanuc.common.kcl.simulate_result import SimulateResult
from underautomation.fanuc.common.kcl.unsimulate_all_result import UnsimulateAllResult
from underautomation.fanuc.common.kcl.unsimulate_result import UnsimulateResult
from underautomation.fanuc.common.kcl.custom_command_result import CustomCommandResult
from underautomation.fanuc.common.kcl.task_information_result import TaskInformationResult
from underautomation.fanuc.common.kcl.add_breakpoint_result import AddBreakpointResult
from underautomation.fanuc.common.kcl.remove_breakpoint_result import RemoveBreakpointResult
from underautomation.fanuc.common.kcl.breakpoints_result import BreakpointsResult
from underautomation.fanuc.common.kcl.step_on_result import StepOnResult
from underautomation.fanuc.common.kcl.step_off_result import StepOffResult
from UnderAutomation.Fanuc.Common.Kcl import KclClientBase as kcl_client_base
from UnderAutomation.Fanuc.Common.Kcl import KCLPorts as kcl_ports

T = typing.TypeVar('T')
class KclClientBase:
	'''Abstract base class for KCL (Keyboard Command Line) clients. Provides all KCL commands shared between Telnet and CGTP implementations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kcl_client_base()
		else:
			self._instance = _internal

	def abort(self, program: str=None, force: bool=True) -> ProgramCommandResult:
		'''Aborts the specified running or paused task. If program is not specified, the default program Is used. Execution of the current program statement Is completed before the task aborts except for the current motion, DELAY, WAIT, Or READ statements, which are canceled. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or TP program without extension which is a task
		:param force: Aborts all running or paused tasks
		'''
		return ProgramCommandResult(self._instance.Abort(program, force))

	def abort_all(self, force: bool=True) -> ProgramCommandResult:
		'''Aborts all running or paused tasks. Execution of the current program statement Is completed before the task aborts except for the current motion, DELAY, WAIT, Or READ statements, which are canceled. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param force: Aborts all running or paused tasks
		'''
		return ProgramCommandResult(self._instance.AbortAll(force))

	def clear_all(self) -> ProgramCommandResult:
		'''Clears all KAREL and teach pendant programs and variable data from memory. All cleared programs And variables (if they were saved with the SaveVars() command) can be reloaded into memory Using the Load() command.'''
		return ProgramCommandResult(self._instance.ClearAll())

	def clear_program(self, program: str=None) -> ProgramCommandResult:
		'''Clears the program data from memory for the specified or default program. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or teach pendant program in memory without extension
		'''
		return ProgramCommandResult(self._instance.ClearProgram(program))

	def clear_vars(self, program: str=None) -> ProgramCommandResult:
		'''Clears the variable and type data associated with the specified or default program from memory. Variables And types that are referenced by a loaded program are Not cleared. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or teach pendant program without extension
		'''
		return ProgramCommandResult(self._instance.ClearVars(program))

	def continue_(self, program: str=None) -> ProgramCommandResult:
		'''Continues program execution of the specified task (or all paused tasks if program argument is null) that has been paused by a hold, pause, or test run operation. If the program Is aborted, the program execution Is started at the first executable line. When a task Is paused, the CYCLE START button on the operator panel has the same effect as the Continue() command. Continue is a motion command; therefore, the device from which it Is issued must have motion control. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or teach pendant program without extension which is a task. If null, it continues all paused tasks
		'''
		return ProgramCommandResult(self._instance.Continue(program))

	def hold(self, program: str=None) -> ProgramCommandResult:
		'''Pauses the specified or default program that is being executed and holds motion at the current position (after a normal deceleration). Use the Continue() command Or the CYCLE START button On the Operator panel To resume program execution. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or TP program. If null, it holds all executing programs
		'''
		return ProgramCommandResult(self._instance.Hold(program))

	def pause(self, program: str=None, force: bool=False) -> ProgramCommandResult:
		'''Pauses the specified running task. If program is not specified, the default program is used. Execution of the current motion segment and the current program statement is completed before the task is paused. Condition handlers remain active. If the condition handler action is NOPAUSE and the condition is satisfied, task execution resumes. If the statement is a WAIT FOR and the wait condition is satisfied while the task is paused, the statement following the WAIT FOR is executed immediately when the task is resumed. If the statement is a DELAY, timing will continue while the task is paused. If the delay time is finished while the task is paused, the statement following the DELAY is immediately executed when the task is resumed. If the statement is a READ, it will accept input even though the task is paused. The Continue() command resumes execution of a paused task. When a task is paused, the CYCLE START button on the operator panel has the same effect as the KCL> CONTINUE command. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: the name of any KAREL or TP program without extension which is a task. If null, it pauses all running tasks.
		:param force: Pauses the task even if the NOPAUSE attribute is set
		'''
		return ProgramCommandResult(self._instance.Pause(program, force))

	def reset(self) -> ProgramCommandResult:
		'''Enables servo power after an error condition has shut off servo power, provided the cause of the error has been cleared. The command also clears the message line on the CRT/KB display. The error message remains displayed if the error condition still exists. The Reset() command has no effect on a program that is being executed. It has the same effect as the FAULT RESET button on the operator panel and the RESET function key on the teach pendant RESET screen.'''
		return ProgramCommandResult(self._instance.Reset())

	def run(self, program: str=None) -> RunResult:
		'''Executes the specified program. The program must be loaded in memory If no program is specified the default program is run. If uninitialized variables are encountered, program execution is paused. Execution begins at the first executable line. RUN is a motion command; therefore, the device from which it is issued must have motion control. If a RUN command is issued in a command file, it is executed as a NOWAIT command. Therefore, the statement following the RUN command will be executed immediately after the RUN command is issued without waiting for the program, specified by the RUN command, to end. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param program: The name of any KAREL or TP program without extension
		'''
		return RunResult(self._instance.Run(program))

	def set_port(self, port: KCLPorts, index: int, value: int) -> SetPortResult:
		'''Assigns the specified value to a specified input or output port. SET PORT can be used either physical Or simulated output ports, but only With simulated input ports.

		:param port: Port type
		:param index: Port index
		:param value: port value. For boolean ports, true is 1 and 0 is false
		'''
		return SetPortResult(self._instance.SetPort(kcl_ports(int(port)), index, value))

	def set_variable(self, name: str, value: float, program: str=None) -> SetVariableResult:
		'''Assigns the specified value to the specified variable. You can assign constant values or variable values, but the value must be of the data type that has been declared for the variable. You can assign values to system variables with KCL write access, to program variables, or to standard and user-defined variables and fields. You can assign only one ARRAY element. Use brackets ([]) after the variable name to specify an element. Certain data types like positions and vectors might have more than one value specified.

		:param name: A valid program variable
		:param value: New value for variable or a program or system variable
		:param program: The name of any KAREL or TP program.
		'''
		return SetVariableResult(self._instance.SetVariable(name, value, program))

	def get_current_pose(self) -> GetCurrentPoseResult:
		'''Returns the position of the TCP relative to the current user frame of reference with an x, y, and z location in millimeters; w, p, and r orientation in degrees; and the current configuration string. Be sure the robot is calibrated.'''
		return GetCurrentPoseResult(self._instance.GetCurrentPose())

	def get_variable(self, name: str, program: str=None) -> GetVariableResult:
		'''Get the name, type, and value of the specified variable. You can display the values of system variables that allow KCL read access or the values of program variables. Use brackets ([]) after the variable name to specify a specific ARRAY element. If you do not specify a specific element the entire variable is displayed.

		:param name: A valid program variable
		:param program: The name of any KAREL or TP program
		'''
		return GetVariableResult(self._instance.GetVariable(name, program))

	def simulate(self, port: KCLPorts, index: int, value: int) -> SimulateResult:
		'''Simulating I/O allows you to test a program that uses I/O. Simulating I/O does not actually send output signals or receive input signals. When simulating a port value, you can specify its initial simulated value or allow the initial value to be the same as the physical port value. If no value is specified, the current physical port value is used.

		:param port: I/O port type
		:param index: I/O port index
		:param value: New value for the port
		'''
		return SimulateResult(self._instance.Simulate(kcl_ports(int(port)), index, value))

	def unsimulate_all(self) -> UnsimulateAllResult:
		'''Discontinues simulation on all input or output port. When a port is unsimulated, the physical value replaces the simulated value.'''
		return UnsimulateAllResult(self._instance.UnsimulateAll())

	def unsimulate(self, port: KCLPorts, index: int) -> UnsimulateResult:
		'''Discontinues simulation of the specified input or output port. When a port is unsimulated, the physical value replaces the simulated value.

		:param port: I/O port type
		:param index: I/O port index to unsimulate
		'''
		return UnsimulateResult(self._instance.Unsimulate(kcl_ports(int(port)), index))

	def send_custom_command(self, command: str) -> T:
		'''Sends a custom KCL command to the robot and returns the raw result.

		:param command: Custom command to send
		'''
		return self._instance.SendCustomCommand(command)

	def get_task_information(self, prog_name: str) -> TaskInformationResult:
		'''Return the task control data for the specified task. If prog_name is not specified, the default program is used

		:param prog_name: the name of any KAREL or TP program which is a task
		'''
		return TaskInformationResult(self._instance.GetTaskInformation(prog_name))

	def add_breakpoint(self, taskName: str, line: int) -> AddBreakpointResult:
		'''Add a breakpoint to a specified task

		:param taskName: Name of a KAREL or TP program without extension
		:param line: Line number for breakpoint
		'''
		return AddBreakpointResult(self._instance.AddBreakpoint(taskName, line))

	def remove_breakpoint(self, taskName: str, line: int) -> RemoveBreakpointResult:
		'''Clear a breakpoint of a task at a specified line

		:param taskName: Name of a KAREL or TP program without extension
		:param line: Line number for breakpoint
		'''
		return RemoveBreakpointResult(self._instance.RemoveBreakpoint(taskName, line))

	def remove_all_breakpoints(self, taskName: str) -> RemoveBreakpointResult:
		'''Clear all breakpoints of a specified task

		:param taskName: Name of a KAREL or TP program without extension
		'''
		return RemoveBreakpointResult(self._instance.RemoveAllBreakpoints(taskName))

	def get_breakpoints(self, taskName: str) -> BreakpointsResult:
		'''Returns the breakpoints set on the specified task.

		:param taskName: Name of a KAREL or TP program without extension
		'''
		return BreakpointsResult(self._instance.GetBreakpoints(taskName))

	def step_on(self, taskName: str) -> StepOnResult:
		'''Enables step mode for the specified task. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.

		:param taskName: Name of a KAREL or TP program without extension
		'''
		return StepOnResult(self._instance.StepOn(taskName))

	def step_off(self) -> StepOffResult:
		'''Disables step mode. When used through the CGTP KCL client (Unsafe mode, from firmware 9.30), success or failure cannot be determined from the result.'''
		return StepOffResult(self._instance.StepOff())

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KclClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
