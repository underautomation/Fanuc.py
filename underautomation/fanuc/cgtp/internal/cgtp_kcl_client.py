from __future__ import annotations
import typing
from underautomation.fanuc.common.kcl.custom_command_result import CustomCommandResult
from underautomation.fanuc.common.kcl.kcl_client_base import KclClientBase
from UnderAutomation.Fanuc.Cgtp.Internal import CgtpKclClient as cgtp_kcl_client

class CgtpKclClient(KclClientBase):
	'''KCL client that uses the web server of the controller (CGTP) instead of Telnet. It has the same commands as the Telnet KCL client and does not need a Telnet password. Some commands (Abort, AbortAll, ClearProgram, ClearVars, Continue, Hold, Pause, Run, StepOn, StepOff, SendCustomCommandUnsafe) are sent in Unsafe mode, from firmware V9.30: the controller returns no status, the result always reports a success, and you cannot know if the command was executed. Check the state of the controller after the command, for example with GetTaskInformation() or by reading a variable. To start a program, prefer robot.Cgtp.RunProgram() (firmware V9.30 and later): it can start at a given line and throws a CgtpException when the controller refuses the command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_kcl_client()
		else:
			self._instance = _internal

	def send_custom_command_unsafe(self, command: str) -> CustomCommandResult:
		'''Sends a custom KCL command in Unsafe mode. Success or failure cannot be determined from the result.

		:param command: Custom command to send
		'''
		return CustomCommandResult(self._instance.SendCustomCommandUnsafe(command))

	@property
	def enabled(self) -> bool:
		'''Indicates whether the KCL client is currently connected.'''
		return self._instance.Enabled

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpKclClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
