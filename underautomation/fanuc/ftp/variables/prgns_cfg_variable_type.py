import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsCfgVariableType as prgns_cfg_variable_type

class PrgnsCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PRGNS_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def algo_ver(self) -> float:
		'''Value of variable $ALGO_VER'''
		return self._instance.AlgoVer

	@property
	def nyq_freq(self) -> float:
		'''Value of variable $NYQ_FREQ'''
		return self._instance.NyqFreq

	@property
	def win_type(self) -> int:
		'''Value of variable $WIN_TYPE'''
		return self._instance.WinType

	@property
	def win_size(self) -> int:
		'''Value of variable $WIN_SIZE'''
		return self._instance.WinSize

	@property
	def overlap(self) -> int:
		'''Value of variable $OVERLAP'''
		return self._instance.Overlap

	@property
	def freq_lim(self) -> float:
		'''Value of variable $FREQ_LIM'''
		return self._instance.FreqLim

	@property
	def min_num(self) -> int:
		'''Value of variable $MIN_NUM'''
		return self._instance.MinNum

	@property
	def created(self) -> int:
		'''Value of variable $CREATED'''
		return self._instance.Created

	@property
	def verify(self) -> int:
		'''Value of variable $VERIFY'''
		return self._instance.Verify

	@property
	def progname(self) -> str:
		'''Value of variable $PROGNAME'''
		return self._instance.Progname

	@property
	def create_gp(self) -> int:
		'''Value of variable $CREATE_GP'''
		return self._instance.CreateGp

	@property
	def status_gp(self) -> int:
		'''Value of variable $STATUS_GP'''
		return self._instance.StatusGp

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def mailtime(self) -> int:
		'''Value of variable $MAILTIME'''
		return self._instance.Mailtime

	@property
	def mailevent(self) -> int:
		'''Value of variable $MAILEVENT'''
		return self._instance.Mailevent

	@property
	def lastmail(self) -> int:
		'''Value of variable $LASTMAIL'''
		return self._instance.Lastmail

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrgnsCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
