import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp import FtpFileSystemObjectType as ftp_file_system_object_type

class FtpFileSystemObjectType(int):
	File = ftp_file_system_object_type.File
	Directory = ftp_file_system_object_type.Directory
	Link = ftp_file_system_object_type.Link
