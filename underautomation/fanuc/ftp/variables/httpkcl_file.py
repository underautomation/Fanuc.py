import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HttpkclFile as httpkcl_file

class HttpkclFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = httpkcl_file()
		else:
			self._instance = _internal
	@property
	def cmds(self) -> typing.List[str]:
		return self._instance.Cmds
	@property
	def url(self) -> str:
		return self._instance.Url
	@property
	def newcmd(self) -> str:
		return self._instance.Newcmd
	@property
	def first_token(self) -> str:
		return self._instance.FirstToken
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def found(self) -> bool:
		return self._instance.Found
	@property
	def ill_flg(self) -> bool:
		return self._instance.IllFlg
	@property
	def i(self) -> int:
		return self._instance.I
