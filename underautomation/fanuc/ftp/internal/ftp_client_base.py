from __future__ import annotations
import typing
from underautomation.fanuc.common.languages import Languages
from underautomation.fanuc.ftp.internal.ftp_direct_file_handling import FtpDirectFileHandling
from underautomation.fanuc.ftp.ftp_list_item import FtpListItem
from underautomation.fanuc.common.files.file_client_base import FileClientBase
from UnderAutomation.Fanuc.Ftp.Internal import FtpClientBase as ftp_client_base
from UnderAutomation.Fanuc.Common import Languages as languages

class FtpClientBase(FileClientBase):
	'''Base class for FTP features'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnects from FTP server'''
		self._instance.Disconnect()

	def enumerate_variable_files(self) -> typing.List[FtpListItem]:
		'''Get a list of all variable files on controller'''
		return [FtpListItem(x) for x in self._instance.EnumerateVariableFiles()]

	def enumerate_variable_file_names(self) -> typing.List[str]:
		return self._instance.EnumerateVariableFileNames()

	@property
	def ip(self) -> str:
		'''Connect robot IP address or host name'''
		return self._instance.IP

	@property
	def language(self) -> Languages:
		'''Controller language (default is English)'''
		return Languages(int(self._instance.Language))

	@language.setter
	def language(self, value: Languages):
		self._instance.Language = languages(int(value))

	@property
	def connected(self) -> bool:
		'''Indicates that FTP connection is active'''
		return self._instance.Connected

	@property
	def direct_file_handling(self) -> FtpDirectFileHandling:
		'''Contains methods to manipulate files and folders on the controller (upload, download, delete, ...)'''
		return FtpDirectFileHandling(self._instance.DirectFileHandling)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
