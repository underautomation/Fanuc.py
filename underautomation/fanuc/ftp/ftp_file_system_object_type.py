import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp import FtpFileSystemObjectType as ftp_file_system_object_type

class FtpFileSystemObjectType(int):
	File = int(ftp_file_system_object_type.File)
	Directory = int(ftp_file_system_object_type.Directory)
	Link = int(ftp_file_system_object_type.Link)

	def __repr__(self):
		for name, value in vars(FtpFileSystemObjectType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
