import typing
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.cgtp.program_sub_type import ProgramSubType
from UnderAutomation.Fanuc.Cgtp import CgtpClientBase as cgtp_client_base
from UnderAutomation.Fanuc.Common import Languages as languages
from UnderAutomation.Fanuc.Cgtp import ProgramSubType as program_sub_type

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

	def abort_task(self, progName: str="None") -> None:
		'''Abort the task specified by progName. Set to null to abort all user tasks.'''
		self._instance.AbortTask(progName)

	def select_program(self, progName: str, lineNum: int=1) -> None:
		'''Open the TP program progName and move cursor to lineNum.'''
		self._instance.SelectProgram(progName, lineNum)

	def delete_program(self, progName: str) -> None:
		'''Delete the program progName from the controller.

		:param progName: Program name
		'''
		self._instance.DeleteProgram(progName)

	def get_program_comment(self, progName: str) -> str:
		'''Get the comment of program progName.'''
		return self._instance.GetProgramComment(progName)

	def set_program_comment(self, progName: str, comment: str) -> None:
		'''Set the comment of program progName.'''
		self._instance.SetProgramComment(progName, comment)

	def get_program_owner(self, progName: str) -> str:
		'''Get the owner of program progName.'''
		return self._instance.GetProgramOwner(progName)

	def set_program_owner(self, progName: str, owner: str) -> None:
		'''Set the owner of program progName.'''
		self._instance.SetProgramOwner(progName, owner)

	def get_program_stack_size(self, progName: str) -> int:
		'''Get the stack size of program progName.'''
		return self._instance.GetProgramStackSize(progName)

	def set_program_stack_size(self, progName: str, stackSize: int) -> None:
		'''Set the stack size of program progName.'''
		self._instance.SetProgramStackSize(progName, stackSize)

	def get_program_ignore_pause(self, progName: str) -> bool:
		'''Get whether program progName ignores pause requests.'''
		return self._instance.GetProgramIgnorePause(progName)

	def set_program_ignore_pause(self, progName: str, ignorePause: bool) -> None:
		'''Set whether program progName ignores pause requests.'''
		self._instance.SetProgramIgnorePause(progName, ignorePause)

	def get_program_write_protect(self, progName: str) -> bool:
		'''Get whether program progName is write-protected.'''
		return self._instance.GetProgramWriteProtect(progName)

	def set_program_write_protect(self, progName: str, writeProtect: bool) -> None:
		'''Set whether program progName is write-protected.'''
		self._instance.SetProgramWriteProtect(progName, writeProtect)

	def get_program_sub_type(self, progName: str) -> ProgramSubType:
		'''Get the sub-type of program progName.'''
		return ProgramSubType(int(self._instance.GetProgramSubType(progName)))

	def set_program_sub_type(self, progName: str, subType: ProgramSubType) -> None:
		'''Set the sub-type of program progName.'''
		self._instance.SetProgramSubType(progName, program_sub_type(int(subType)))

	def create_program(self, progName: str, owner: str="None", comment: str="None", defaultGroup: int=0, subType: ProgramSubType=ProgramSubType.None) -> None:
		'''Create a new TP program on the controller.

		:param progName: New program name
		:param owner: Owner name (optional)
		:param comment: Comment (optional)
		:param defaultGroup: Default motion group (0 = omit)
		:param subType: Program sub-type (default: None)
		'''
		self._instance.CreateProgram(progName, owner, comment, defaultGroup, program_sub_type(int(subType)))

	def rename_program(self, sourceName: str, newName: str) -> None:
		'''Rename program sourceName to newName.'''
		self._instance.RenameProgram(sourceName, newName)

	def run_program(self, progName: str, lineNum: int=1) -> None:
		'''Run the specified program starting at lineNum.'''
		self._instance.RunProgram(progName, lineNum)

	def change_active_program(self, progName: str) -> None:
		'''Change the active TP program to progName.'''
		self._instance.ChangeActiveProgram(progName)

	def pause_all_programs(self) -> None:
		'''Pause program execution on the controller.'''
		self._instance.PauseAllPrograms()

	def read_variable_as_string(self, varName: str, progName: str="None") -> str:
		'''Read the value of variable varName in program progName.'''
		return self._instance.ReadVariableAsString(varName, progName)

	def write_variable(self, varName: str, value: str, progName: str="None") -> None:
		'''Write value to variable varName in program progName.'''
		self._instance.WriteVariable(varName, value, progName)

	def list_files(self, pathName: str="MD:") -> typing.List[str]:
		'''List files at the specified path on the controller.'''
		return self._instance.ListFiles(pathName)

	def get_file_as_string(self, pathName: str) -> str:
		return self._instance.GetFileAsString(pathName)

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
