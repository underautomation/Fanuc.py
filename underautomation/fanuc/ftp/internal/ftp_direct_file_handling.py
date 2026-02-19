import typing
from underautomation.fanuc.ftp.ftp_list_item import FtpListItem
from UnderAutomation.Fanuc.Ftp.Internal import FtpDirectFileHandling as ftp_direct_file_handling

class FtpDirectFileHandling:
	'''Methods to handle files on a Fanuc controller (upload, download, delete, enumerate, ...)'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ftp_direct_file_handling()
		else:
			self._instance = _internal

	def upload_file_to_controller(self, localPath: str, remotePath: str, createRemoteDir: bool=False, progress: typing.Any=None) -> bool:
		return self._instance.UploadFileToController(localPath, remotePath, createRemoteDir, progress)

	def upload_files_to_controller(self, localPaths: typing.List[str], remoteDir: str, progress: typing.Any=None) -> typing.List[str]:
		return self._instance.UploadFilesToController(localPaths, remoteDir, progress)

	def download_file_from_controller(self, localPath: str, remotePath: str, progress: typing.Any=None) -> bool:
		return self._instance.DownloadFileFromController(localPath, remotePath, progress)

	def download_files_from_controller(self, localDir: str, remotePaths: typing.List[str], progress: typing.Any=None) -> typing.List[str]:
		return self._instance.DownloadFilesFromController(localDir, remotePaths, progress)

	def file_exists(self, path: str) -> bool:
		'''Checks if a file exists on the controller.

		:param path: The full or relative path to the file
		:returns: True if the file exists
		'''
		return self._instance.FileExists(path)

	def directory_exists(self, path: str) -> bool:
		'''Tests if the specified directory exists on the controller. This method works by trying to change the working directory to the path specified. If it succeeds, the directory is changed back to the old working directory and true is returned. False is returned otherwise and since the CWD failed it is assumed the working directory is still the same.

		:param path: The path of the directory
		:returns: True if it exists, false otherwise.
		'''
		return self._instance.DirectoryExists(path)

	def create_directory(self, path: str) -> None:
		'''Creates a directory on the controller. If the preceding directories do not exist, then they are created.

		:param path: The full or relative path to the new remote directory
		'''
		self._instance.CreateDirectory(path)

	def delete_directory(self, path: str) -> None:
		'''Deletes the specified directory and all its contents.

		:param path: The full or relative path of the directory to delete
		'''
		self._instance.DeleteDirectory(path)

	def delete_file(self, path: str) -> None:
		'''Deletes a file on the controller

		:param path: The full or relative path to the file
		'''
		self._instance.DeleteFile(path)

	def get_listing(self, path: str) -> typing.List[FtpListItem]:
		'''Gets a file listing from the controller. Each FtpListItem object returned contains information about the file that was able to be retrieved.

		:param path: The path of the directory to list
		:returns: An array of FtpListItem objects
		'''
		return [FtpListItem(x) for x in self._instance.GetListing(path)]

	def get_object_info(self, path: str) -> FtpListItem:
		'''Returns information about a file system object. Returns null if the controller response can't be parsed or the controller returns a failure completion code. The error for a failure is logged with FtpTrace. No exception is thrown on error because that would negate the usefulness of this method for checking for the existence of an object.

		:param path: The path of the file or folder
		:returns: A FtpListItem object
		'''
		return FtpListItem(self._instance.GetObjectInfo(path))

	def rename(self, path: str, dest: str) -> None:
		'''Renames an object on the remote file system. Throws exceptions if the file does not exist, or if the destination file already exists.

		:param path: The full or relative path to the object
		:param dest: The new full or relative path including the new name of the object
		'''
		self._instance.Rename(path, dest)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FtpDirectFileHandling):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
