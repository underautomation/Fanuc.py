import typing
from datetime import datetime, timedelta
from underautomation.fanuc.ftp.ftp_file_system_object_type import FtpFileSystemObjectType
from UnderAutomation.Fanuc.Ftp import FtpListItem as ftp_list_item
from UnderAutomation.Fanuc.Ftp import FtpFileSystemObjectType as ftp_file_system_object_type

class FtpListItem:
	'''Represents a file system object on the controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_list_item()
		else:
			self._instance = _internal

	@property
	def size(self) -> int:
		'''Gets the size of the object. Only a few files (like *.tp or *.df) have a size that can be retrieved, for most files this is 0 even if they are not empty. For directories this is always 0.'''
		return self._instance.Size

	@property
	def chmod(self) -> int:
		'''Gets the file permissions in the CHMOD format.'''
		return self._instance.Chmod

	@property
	def created(self) -> datetime:
		'''Gets the created date of the object.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Created.Ticks // 10)

	@property
	def full_name(self) -> str:
		'''Gets the full path name to the object.'''
		return self._instance.FullName

	@property
	def name(self) -> str:
		'''Gets name to the object.'''
		return self._instance.Name

	@property
	def modified(self) -> datetime:
		'''Gets the last write time of the object.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Modified.Ticks // 10)

	@property
	def type(self) -> FtpFileSystemObjectType:
		'''Gets the type of file system object.'''
		return FtpFileSystemObjectType(int(self._instance.Type))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpListItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
