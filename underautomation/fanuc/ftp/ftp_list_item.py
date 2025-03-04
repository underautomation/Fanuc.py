import typing
from underautomation.fanuc.ftp.ftp_file_system_object_type import FtpFileSystemObjectType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp import FtpListItem as ftp_list_item

class FtpListItem:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_list_item()
		else:
			self._instance = _internal
	@property
	def size(self) -> int:
		return self._instance.Size
	@property
	def chmod(self) -> int:
		return self._instance.Chmod
	@property
	def created(self) -> typing.Any:
		return self._instance.Created
	@property
	def full_name(self) -> str:
		return self._instance.FullName
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def modified(self) -> typing.Any:
		return self._instance.Modified
	@property
	def type(self) -> FtpFileSystemObjectType:
		return FtpFileSystemObjectType(self._instance.Type)
