from enum import IntEnum

class FtpFileSystemObjectType(IntEnum):
	'''Type of file system of object'''
	File = 0 # A file
	Directory = 1 # A directory
	Link = 2 # A symbolic link
