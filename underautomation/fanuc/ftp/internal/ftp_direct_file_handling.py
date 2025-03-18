import typing
from underautomation.fanuc.ftp.ftp_list_item import FtpListItem
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Internal import FtpDirectFileHandling as ftp_direct_file_handling

class FtpDirectFileHandling:
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
		return self._instance.FileExists(path)
	def directory_exists(self, path: str) -> bool:
		return self._instance.DirectoryExists(path)
	def create_directory(self, path: str) -> None:
		self._instance.CreateDirectory(path)
	def delete_directory(self, path: str) -> None:
		self._instance.DeleteDirectory(path)
	def delete_file(self, path: str) -> None:
		self._instance.DeleteFile(path)
	def get_listing(self, path: str) -> typing.List[FtpListItem]:
		return [FtpListItem(x) for x in self._instance.GetListing(path)]
	def get_object_info(self, path: str) -> FtpListItem:
		return FtpListItem(self._instance.GetObjectInfo(path))
	def rename(self, path: str, dest: str) -> None:
		self._instance.Rename(path, dest)
