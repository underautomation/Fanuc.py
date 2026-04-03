from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.cgtp_ascii_file_item import CgtpAsciiFileItem
from underautomation.fanuc.cgtp.cgtp_file_item import CgtpFileItem
from underautomation.fanuc.common.files.file_client_base import FileClientBase
from UnderAutomation.Fanuc.Cgtp.Internal import CgtpHttpClient as cgtp_http_client

class CgtpHttpClient(FileClientBase):
	'''Provides methods to download and list files from the controller via HTTP.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_http_client()
		else:
			self._instance = _internal

	def download_as_bytes(self, fileName: str) -> typing.List[int]:
		'''Download a file from the controller and return its raw bytes.'''
		return self._instance.DownloadAsBytes(fileName)

	def download_as_string(self, fileName: str) -> str:
		'''Download a file from the controller and return its content as a string.'''
		return self._instance.DownloadAsString(fileName)

	def download_as_stream(self, fileName: str) -> typing.Any:
		'''Download a file from the controller and return a readable stream. Otherwise the raw binary response is returned.'''
		return self._instance.DownloadAsStream(fileName)

	def list_variable_files(self) -> typing.List[CgtpAsciiFileItem]:
		'''List variable files available on the controller.'''
		return [CgtpAsciiFileItem(x) for x in self._instance.ListVariableFiles()]

	def list_tp_programs(self) -> typing.List[CgtpAsciiFileItem]:
		'''List TP program files available on the controller.'''
		return [CgtpAsciiFileItem(x) for x in self._instance.ListTpPrograms()]

	def list_diagnostic_files(self) -> typing.List[CgtpFileItem]:
		'''List diagnostic and error files available on the controller.'''
		return [CgtpFileItem(x) for x in self._instance.ListDiagnosticFiles()]

	def list_other_files(self) -> typing.List[CgtpFileItem]:
		'''List other files available on the controller.'''
		return [CgtpFileItem(x) for x in self._instance.ListOtherFiles()]

	def enumerate_variable_file_names(self) -> typing.List[str]:
		return self._instance.EnumerateVariableFileNames()

	@property
	def ip(self) -> str:
		return self._instance.IP

	@property
	def base_path(self) -> str:
		'''Base path used to build the download URL. Default is "MD".'''
		return self._instance.BasePath

	@base_path.setter
	def base_path(self, value: str):
		self._instance.BasePath = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpHttpClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
