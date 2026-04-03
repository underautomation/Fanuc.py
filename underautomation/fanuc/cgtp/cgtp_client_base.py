from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.internal.cgtp_kcl_client import CgtpKclClient
from underautomation.fanuc.cgtp.internal.cgtp_http_client import CgtpHttpClient
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.cgtp.cgtp_program_sub_type import CgtpProgramSubType
from underautomation.fanuc.cgtp.cgtp_variable_value import CgtpVariableValue
from underautomation.fanuc.cgtp.cgtp_comment_type import CgtpCommentType
from underautomation.fanuc.common.numeric_register_with_comment import NumericRegisterWithComment
from underautomation.fanuc.common.string_register_with_comment import StringRegisterWithComment
from underautomation.fanuc.common.user_alarm_definition import UserAlarmDefinition
from underautomation.fanuc.common.io_comments import IOComments
from underautomation.fanuc.cgtp.cgtp_comment_io_type import CgtpCommentIoType
from underautomation.fanuc.common.position_register_with_comment import PositionRegisterWithComment
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_read_result import CgtpBatchReadResult
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_variables import CgtpBatchVariables
from underautomation.fanuc.cgtp.batch_variables.cgtp_batch_write_result import CgtpBatchWriteResult
from underautomation.fanuc.cgtp.cgtp_io_port_type import CgtpIoPortType
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition
from UnderAutomation.Fanuc.Cgtp import CgtpClientBase as cgtp_client_base
from UnderAutomation.Fanuc.Common import Languages as languages
from UnderAutomation.Fanuc.Cgtp import CgtpProgramSubType as cgtp_program_sub_type
from UnderAutomation.Fanuc.Cgtp import CgtpCommentType as cgtp_comment_type
from UnderAutomation.Fanuc.Cgtp import CgtpCommentIoType as cgtp_comment_io_type
from UnderAutomation.Fanuc.Cgtp import CgtpIoPortType as cgtp_io_port_type

class CgtpClientBase:
	'''Base implementation for the CGTP Web Server client.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnect from the CGTP Web Server. After calling this method, the client must be reconnected before it can be used again.'''
		self._instance.Disconnect()

	def abort_task(self, progName: str=None) -> None:
		'''Abort the task specified by progName. Set to null to abort all user tasks. From firmware 9.10'''
		self._instance.AbortTask(progName)

	def select_program(self, progName: str, lineNum: int=1) -> None:
		'''Open the TP program progName and move cursor to lineNum. From firmware 9.10'''
		self._instance.SelectProgram(progName, lineNum)

	def delete_program(self, progName: str) -> None:
		'''Delete the program progName from the controller. From firmware 9.10

		:param progName: Program name
		'''
		self._instance.DeleteProgram(progName)

	def get_program_comment(self, progName: str) -> str:
		'''Get the comment of program progName. From firmware 9.10'''
		return self._instance.GetProgramComment(progName)

	def set_program_comment(self, progName: str, comment: str) -> None:
		'''Set the comment of program progName. From firmware 9.10'''
		self._instance.SetProgramComment(progName, comment)

	def get_program_owner(self, progName: str) -> str:
		'''Get the owner of program progName. From firmware 9.10'''
		return self._instance.GetProgramOwner(progName)

	def set_program_owner(self, progName: str, owner: str) -> None:
		'''Set the owner of program progName. From firmware 9.10'''
		self._instance.SetProgramOwner(progName, owner)

	def get_program_stack_size(self, progName: str) -> int:
		'''Get the stack size of program progName. From firmware 9.10'''
		return self._instance.GetProgramStackSize(progName)

	def set_program_stack_size(self, progName: str, stackSize: int) -> None:
		'''Set the stack size of program progName. From firmware 9.10'''
		self._instance.SetProgramStackSize(progName, stackSize)

	def get_program_ignore_pause(self, progName: str) -> bool:
		'''Get whether program progName ignores pause requests. From firmware 9.10'''
		return self._instance.GetProgramIgnorePause(progName)

	def set_program_ignore_pause(self, progName: str, ignorePause: bool) -> None:
		'''Set whether program progName ignores pause requests. From firmware 9.10'''
		self._instance.SetProgramIgnorePause(progName, ignorePause)

	def get_program_write_protect(self, progName: str) -> bool:
		'''Get whether program progName is write-protected. From firmware 9.10'''
		return self._instance.GetProgramWriteProtect(progName)

	def set_program_write_protect(self, progName: str, writeProtect: bool) -> None:
		'''Set whether program progName is write-protected. From firmware 9.10'''
		self._instance.SetProgramWriteProtect(progName, writeProtect)

	def get_program_sub_type(self, progName: str) -> CgtpProgramSubType:
		'''Get the sub-type of program progName. From firmware 9.10'''
		return CgtpProgramSubType(int(self._instance.GetProgramSubType(progName)))

	def set_program_sub_type(self, progName: str, subType: CgtpProgramSubType) -> None:
		'''Set the sub-type of program progName. From firmware 9.10'''
		self._instance.SetProgramSubType(progName, cgtp_program_sub_type(int(subType)))

	def create_program(self, progName: str, owner: str=None, comment: str=None, defaultGroup: int=0, subType: CgtpProgramSubType=CgtpProgramSubType.None_) -> None:
		'''Create a new TP program on the controller. From firmware 9.10

		:param progName: New program name
		:param owner: Owner name (optional)
		:param comment: Comment (optional)
		:param defaultGroup: Default motion group (0 = omit)
		:param subType: Program sub-type (default: None)
		'''
		self._instance.CreateProgram(progName, owner, comment, defaultGroup, cgtp_program_sub_type(int(subType)))

	def rename_program(self, sourceName: str, newName: str) -> None:
		'''Rename program sourceName to newName. From firmware 9.10'''
		self._instance.RenameProgram(sourceName, newName)

	def run_program(self, progName: str, lineNum: int=1) -> None:
		'''Run the specified program starting at lineNum. From firmware 9.30'''
		self._instance.RunProgram(progName, lineNum)

	def change_active_program(self, progName: str) -> None:
		'''Change the active TP program to progName. From firmware 9.10'''
		self._instance.ChangeActiveProgram(progName)

	def pause_all_programs(self) -> None:
		'''Pause program execution on the controller. From firmware 9.10'''
		self._instance.PauseAllPrograms()

	def read_variable_as_string(self, varName: str, progName: str=None) -> str:
		'''Read the value of variable varName in program progName. From firmware 9.10'''
		return self._instance.ReadVariableAsString(varName, progName)

	def read_variable(self, varName: str, progName: str=None) -> CgtpVariableValue:
		'''Read the typed value of variable varName in program progName. From firmware 9.10

		:param varName: Full variable name (e.g. "$RMT_MASTER").
		:param progName: Program name, or null for system variables.
		:returns: The variable value with its data type.
		'''
		return CgtpVariableValue(self._instance.ReadVariable(varName, progName))

	def write_variable(self, varName: str, value: float, progName: str=None) -> None:
		'''Write a real (double) value to variable varName in program progName. From firmware 8.30'''
		self._instance.WriteVariable(varName, value, progName)

	def set_comment(self, type: CgtpCommentType, index: int, comment: str) -> None:
		'''Set the comment of a register or I/O port identified by type and index.

		:param type: The type of element to set the comment for.
		:param index: 1-based index of the element.
		:param comment: The comment to set.
		'''
		self._instance.SetComment(cgtp_comment_type(int(type)), index, comment)

	def write_numeric_register_as_double(self, index: int, value: float) -> None:
		'''Write a real (double) value to numeric register R[index].

		:param index: 1-based register index.
		:param value: Value to write.
		'''
		self._instance.WriteNumericRegisterAsDouble(index, value)

	def write_numeric_register_as_integer(self, index: int, value: int) -> None:
		'''Write an integer value to numeric register R[index].

		:param index: 1-based register index.
		:param value: Value to write.
		'''
		self._instance.WriteNumericRegisterAsInteger(index, value)

	def write_string_register(self, index: int, value: str) -> None:
		'''Write a string value to string register SR[index].

		:param index: 1-based register index.
		:param value: String value to write.
		'''
		self._instance.WriteStringRegister(index, value)

	def set_user_alarm_severity(self, index: int, severity: int) -> None:
		'''Set the severity of a user alarm.

		:param index: 1-based alarm index.
		:param severity: Severity value to set.
		'''
		self._instance.SetUserAlarmSeverity(index, severity)

	def read_numeric_registers_with_comment(self) -> typing.List[NumericRegisterWithComment]:
		'''Read all numeric registers (R[]) with their comments and values.

		:returns: Array where index 0 corresponds to R[1], index 1 to R[2], etc.
		'''
		return [NumericRegisterWithComment(None, None, x) for x in self._instance.ReadNumericRegistersWithComment()]

	def read_string_registers_with_comment(self) -> typing.List[StringRegisterWithComment]:
		'''Read all string registers (SR[]) with their comments and values.

		:returns: Array where index 0 corresponds to SR[1], index 1 to SR[2], etc.
		'''
		return [StringRegisterWithComment(x) for x in self._instance.ReadStringRegistersWithComment()]

	def read_user_alarms(self) -> typing.List[UserAlarmDefinition]:
		'''Read all user alarm definitions with their comments and severity.

		:returns: Array where index 0 corresponds to User Alarm[1], index 1 to User Alarm[2], etc.
		'''
		return [UserAlarmDefinition(x) for x in self._instance.ReadUserAlarms()]

	def get_io_comments(self, type: CgtpCommentIoType) -> IOComments:
		'''Read all I/O comments for the specified I/O type.

		:param type: The type of I/O pair to read comments for.
		:returns: An IOComments containing input and output comment arrays.
		'''
		return IOComments(self._instance.GetIoComments(cgtp_comment_io_type(int(type))))

	def get_comments(self, type: CgtpCommentType) -> typing.List[str]:
		'''Read all comments for the specified element type. For I/O types (RI, RO, DI, DO, GI, GO, AI, AO), returns the input or output comments accordingly.

		:param type: The type of element to read comments for.
		:returns: Array of comments where index 0 corresponds to element 1.
		'''
		return self._instance.GetComments(cgtp_comment_type(int(type)))

	def read_numeric_register_with_comment(self, index: int) -> NumericRegisterWithComment:
		'''Read the numeric register (R[]) at index. From firmware 9.10'''
		return NumericRegisterWithComment(None, None, self._instance.ReadNumericRegisterWithComment(index))

	def read_position_register_with_comment(self, index: int, groupNum: int=1) -> PositionRegisterWithComment:
		'''Read the position register (PR[]) at index for motion group groupNum. From firmware 9.10'''
		return PositionRegisterWithComment(self._instance.ReadPositionRegisterWithComment(index, groupNum))

	def read_batch_variables(self, variables: CgtpBatchVariables) -> CgtpBatchReadResult:
		'''Read multiple variables from the controller in a single batch operation. Each variable in variables will be updated with the value read from the controller.

		:param variables: Collection of variables to read. Each variable will have its value, Exists, IsUninitialized and IsReadOnly properties set after the call.
		:returns: A result object containing the controller firmware version.
		'''
		return CgtpBatchReadResult(self._instance.ReadBatchVariables(variables._instance if variables else None))

	def write_batch_variables(self, variables: CgtpBatchVariables) -> CgtpBatchWriteResult:
		'''Write multiple variables to the controller in a single batch operation.

		:param variables: Collection of variables to write. Each variable must have its value set before calling this method.
		:returns: A result object.
		'''
		return CgtpBatchWriteResult(self._instance.WriteBatchVariables(variables._instance if variables else None))

	def read_io(self, portType: CgtpIoPortType, index: int) -> int:
		'''Read the value of I/O port at index of type portType. From firmware 8.30'''
		return self._instance.ReadIo(cgtp_io_port_type(int(portType)), index)

	def write_io(self, portType: CgtpIoPortType, index: int, value: int) -> None:
		'''Set the value of I/O port at index of type portType. From firmware 8.30'''
		self._instance.WriteIo(cgtp_io_port_type(int(portType)), index, value)

	def get_io_simulation_status(self, portType: CgtpIoPortType, index: int) -> bool:
		'''Check whether I/O port at index of type portType is simulated. From firmware 8.30'''
		return self._instance.GetIoSimulationStatus(cgtp_io_port_type(int(portType)), index)

	def simulate_io(self, portType: CgtpIoPortType, index: int) -> None:
		'''Set I/O port at index of type portType to simulated. From firmware 8.30'''
		self._instance.SimulateIo(cgtp_io_port_type(int(portType)), index)

	def unsimulate_io(self, portType: CgtpIoPortType, index: int) -> None:
		'''Remove simulation from I/O port at index of type portType. From firmware 8.30'''
		self._instance.UnsimulateIo(cgtp_io_port_type(int(portType)), index)

	def read_cartesian_position(self, groupNum: int=1) -> CartesianPosition:
		'''Read the current Cartesian position of motion group groupNum. From firmware 9.10'''
		return CartesianPosition(None, None, None, None, None, None, None, self._instance.ReadCartesianPosition(groupNum))

	def read_joint_position(self, groupNum: int=1) -> JointsPosition:
		'''Read the current joint angles of motion group groupNum. From firmware 9.10'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.ReadJointPosition(groupNum))

	def invert_kinematics(self, group: int, cartesianPosition: CartesianPosition, userTool: int=-1, userFrame: int=-1) -> JointsPosition:
		'''Compute the inverse kinematics on the controller: convert a Cartesian position to joint angles.

		:param group: Motion group number to use for kinematics calculation.
		:param cartesianPosition: A Cartesian position to convert. Its StringValue is sent to the controller.
		:param userTool: Optional user tool number to use for kinematics calculation, or -1 for flange.
		:param userFrame: Optional user frame number to use for kinematics calculation, or -1 for world.
		:returns: The corresponding joint position.
		'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.InvertKinematics(group, cartesianPosition._instance if cartesianPosition else None, userTool, userFrame))

	def forward_kinematics(self, group: int, jointPosition: JointsPosition, userTool: int=-1, userFrame: int=-1) -> CartesianPosition:
		'''Compute the forward kinematics on the controller: convert joint angles to a Cartesian position.

		:param group: Motion group number to use for kinematics calculation.
		:param jointPosition: A joint position to convert. Its StringValue is sent to the controller.
		:param userTool: Optional user tool number to use for kinematics calculation, or -1 for flange.
		:param userFrame: Optional user frame number to use for kinematics calculation, or -1 for world.
		:returns: The corresponding Cartesian position.
		'''
		return CartesianPosition(None, None, None, None, None, None, None, self._instance.ForwardKinematics(group, jointPosition._instance if jointPosition else None, userTool, userFrame))

	def list_files(self, pathName: str="MD:") -> typing.List[str]:
		'''List files at the specified path on the controller. From firmware 9.40'''
		return self._instance.ListFiles(pathName)

	def get_file_as_string(self, pathName: str) -> str:
		'''Download the content of a file from the controller as a string. From firmware 9.10

		:param pathName: File path on the controller (e.g. "MD:/filename.ls").
		:returns: The file content as a string.
		'''
		return self._instance.GetFileAsString(pathName)

	@property
	def kcl(self) -> CgtpKclClient:
		'''KCL client for executing KCL commands over CGTP.'''
		return CgtpKclClient(self._instance.Kcl)

	@property
	def http(self) -> CgtpHttpClient:
		'''Provides methods to download and decode files from the controller via HTTP.'''
		return CgtpHttpClient(self._instance.Http)

	@property
	def language(self) -> Languages:
		'''Controller language (default is English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def enabled(self) -> bool:
		'''Indicates whether the client is currently connected to the CGTP Web Server.'''
		return self._instance.Enabled

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
