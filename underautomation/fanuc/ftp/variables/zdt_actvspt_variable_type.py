import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ZdtActvsptVariableType as zdt_actvspt_variable_type

class ZdtActvsptVariableType(GenericVariableType):
	'''Describes the Fanuc type ZDT_ACTVSPT_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zdt_actvspt_variable_type()
		else:
			self._instance = _internal

	@property
	def actvspt_enb(self) -> bool:
		'''Value of variable $ACTVSPT_ENB'''
		return self._instance.ActvsptEnb

	@property
	def activate(self) -> int:
		'''Value of variable $ACTIVATE'''
		return self._instance.Activate

	@property
	def iotype(self) -> int:
		'''Value of variable $IOTYPE'''
		return self._instance.Iotype

	@property
	def ioport(self) -> int:
		'''Value of variable $IOPORT'''
		return self._instance.Ioport

	@property
	def timeitvl(self) -> int:
		'''Value of variable $TIMEITVL'''
		return self._instance.Timeitvl

	@property
	def trgtdvc(self) -> str:
		'''Value of variable $TRGTDVC'''
		return self._instance.Trgtdvc

	@property
	def trgcfg(self) -> str:
		'''Value of variable $TRGCFG'''
		return self._instance.Trgcfg

	@property
	def tmpdir(self) -> str:
		'''Value of variable $TMPDIR'''
		return self._instance.Tmpdir

	@property
	def ps_numfile(self) -> int:
		'''Value of variable $PS_NUMFILE'''
		return self._instance.PsNumfile

	@property
	def numfile(self) -> int:
		'''Value of variable $NUMFILE'''
		return self._instance.Numfile

	@property
	def numcfg(self) -> int:
		'''Value of variable $NUMCFG'''
		return self._instance.Numcfg

	@property
	def lsttime(self) -> int:
		'''Value of variable $LSTTIME'''
		return self._instance.Lsttime

	@property
	def extra(self) -> int:
		'''Value of variable $EXTRA'''
		return self._instance.Extra

	@property
	def extra_str(self) -> str:
		'''Value of variable $EXTRA_STR'''
		return self._instance.ExtraStr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ZdtActvsptVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
