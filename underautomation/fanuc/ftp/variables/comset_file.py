import typing
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import ComsetFile as comset_file

class ComsetFile(GenericVariableFile):
	'''Describes the Fanuc variable file comset.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = comset_file()
		else:
			self._instance = _internal

	@property
	def searchcase(self) -> bool:
		'''Value of variable SEARCHCASE'''
		return self._instance.Searchcase

	@property
	def ifc(self) -> int:
		'''Value of variable IFC'''
		return self._instance.Ifc

	@property
	def url(self) -> str:
		'''Value of variable URL'''
		return self._instance.Url

	@property
	def respfile(self) -> str:
		'''Value of variable RESPFILE'''
		return self._instance.Respfile

	@property
	def scomment(self) -> str:
		'''Value of variable SCOMMENT'''
		return self._instance.Scomment

	@property
	def sindx(self) -> str:
		'''Value of variable SINDX'''
		return self._instance.Sindx

	@property
	def srealflag(self) -> str:
		'''Value of variable SREALFLAG'''
		return self._instance.Srealflag

	@property
	def sfc(self) -> str:
		'''Value of variable SFC'''
		return self._instance.Sfc

	@property
	def svalue(self) -> str:
		'''Value of variable SVALUE'''
		return self._instance.Svalue

	@property
	def scopystr(self) -> str:
		'''Value of variable SCOPYSTR'''
		return self._instance.Scopystr

	@property
	def n_status(self) -> int:
		'''Value of variable N_STATUS'''
		return self._instance.NStatus

	@property
	def icomment_len(self) -> int:
		'''Value of variable ICOMMENT_LEN'''
		return self._instance.IcommentLen

	@property
	def iretsize(self) -> int:
		'''Value of variable IRETSIZE'''
		return self._instance.Iretsize

	@property
	def frvrc(self) -> bool:
		'''Value of variable FRVRC'''
		return self._instance.Frvrc

	@property
	def searchfile(self) -> str:
		'''Value of variable SEARCHFILE'''
		return self._instance.Searchfile

	@property
	def searchcancel(self) -> bool:
		'''Value of variable SEARCHCANCEL'''
		return self._instance.Searchcancel

	@property
	def reg_almfc(self) -> int:
		'''Value of variable REG_ALMFC'''
		return self._instance.RegAlmfc

	@property
	def preg_almfc(self) -> int:
		'''Value of variable PREG_ALMFC'''
		return self._instance.PregAlmfc

	@property
	def di_almfc(self) -> int:
		'''Value of variable DI_ALMFC'''
		return self._instance.DiAlmfc

	@property
	def do_almfc(self) -> int:
		'''Value of variable DO_ALMFC'''
		return self._instance.DoAlmfc

	@property
	def flag_almfc(self) -> int:
		'''Value of variable FLAG_ALMFC'''
		return self._instance.FlagAlmfc

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ComsetFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
