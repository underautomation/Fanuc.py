import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import HttpkclFile as httpkcl_file

class HttpkclFile(GenericVariableFile):
	'''Describes the Fanuc variable file httpkcl.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = httpkcl_file()
		else:
			self._instance = _internal

	@property
	def cmds(self) -> typing.List[str]:
		'''Value of variable CMDS'''
		return self._instance.Cmds

	@property
	def url(self) -> str:
		'''Value of variable URL'''
		return self._instance.Url

	@property
	def newcmd(self) -> str:
		'''Value of variable NEWCMD'''
		return self._instance.Newcmd

	@property
	def first_token(self) -> str:
		'''Value of variable FIRST_TOKEN'''
		return self._instance.FirstToken

	@property
	def status(self) -> int:
		'''Value of variable STATUS'''
		return self._instance.Status

	@property
	def found(self) -> bool:
		'''Value of variable FOUND'''
		return self._instance.Found

	@property
	def ill_flg(self) -> bool:
		'''Value of variable ILL_FLG'''
		return self._instance.IllFlg

	@property
	def i(self) -> int:
		'''Value of variable I'''
		return self._instance.I

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpkclFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
