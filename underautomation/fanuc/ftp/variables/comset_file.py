import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ComsetFile as comset_file

class ComsetFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = comset_file()
		else:
			self._instance = _internal
	@property
	def searchcase(self) -> bool:
		return self._instance.Searchcase
	@property
	def ifc(self) -> int:
		return self._instance.Ifc
	@property
	def url(self) -> str:
		return self._instance.Url
	@property
	def respfile(self) -> str:
		return self._instance.Respfile
	@property
	def scomment(self) -> str:
		return self._instance.Scomment
	@property
	def sindx(self) -> str:
		return self._instance.Sindx
	@property
	def srealflag(self) -> str:
		return self._instance.Srealflag
	@property
	def sfc(self) -> str:
		return self._instance.Sfc
	@property
	def svalue(self) -> str:
		return self._instance.Svalue
	@property
	def scopystr(self) -> str:
		return self._instance.Scopystr
	@property
	def n_status(self) -> int:
		return self._instance.NStatus
	@property
	def icomment_len(self) -> int:
		return self._instance.IcommentLen
	@property
	def iretsize(self) -> int:
		return self._instance.Iretsize
	@property
	def frvrc(self) -> bool:
		return self._instance.Frvrc
	@property
	def searchfile(self) -> str:
		return self._instance.Searchfile
	@property
	def searchcancel(self) -> bool:
		return self._instance.Searchcancel
	@property
	def reg_almfc(self) -> int:
		return self._instance.RegAlmfc
	@property
	def preg_almfc(self) -> int:
		return self._instance.PregAlmfc
	@property
	def di_almfc(self) -> int:
		return self._instance.DiAlmfc
	@property
	def do_almfc(self) -> int:
		return self._instance.DoAlmfc
	@property
	def flag_almfc(self) -> int:
		return self._instance.FlagAlmfc
