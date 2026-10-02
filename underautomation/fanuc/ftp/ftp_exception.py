from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Ftp import FtpException as ftp_exception

class FtpException:
	'''Exception thrown when the controller refuses an FTP operation, or when the FTP communication fails. The message gives the reply of the controller and, when it is known, what to do.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_exception()
		else:
			self._instance = _internal

	@property
	def remote_path(self) -> str:
		'''Path of the file or folder on the controller concerned by the operation. Null when the operation has no path.'''
		return self._instance.RemotePath

	@property
	def reply_code(self) -> int:
		'''FTP reply code returned by the controller (for example 550). 0 when the controller did not reply.'''
		return self._instance.ReplyCode

	@property
	def reply_message(self) -> str:
		'''Reply text returned by the controller (for example "Specified program is in use"). Null when the controller did not reply.'''
		return self._instance.ReplyMessage

	@property
	def program_in_use(self) -> bool:
		'''True when the controller refused the operation because the program is in use: it is selected on the teach pendant or it runs. Select another program before you upload or delete it.'''
		return self._instance.ProgramInUse

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
