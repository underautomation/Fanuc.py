import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CoParamgpVariableType as co_paramgp_variable_type

class CoParamgpVariableType(GenericVariableType):
	'''Describes the Fanuc type CO_PARAMGP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = co_paramgp_variable_type()
		else:
			self._instance = _internal

	@property
	def opt_time(self) -> int:
		'''Value of variable $OPT_TIME'''
		return self._instance.OptTime

	@property
	def opt_acc(self) -> bool:
		'''Value of variable $OPT_ACC'''
		return self._instance.OptAcc

	@property
	def jacc_rratio(self) -> float:
		'''Value of variable $JACC_RRATIO'''
		return self._instance.JaccRratio

	@property
	def cacc_rratio(self) -> float:
		'''Value of variable $CACC_RRATIO'''
		return self._instance.CaccRratio

	@property
	def jtime_ratio(self) -> float:
		'''Value of variable $JTIME_RATIO'''
		return self._instance.JtimeRatio

	@property
	def ctime_ratio(self) -> float:
		'''Value of variable $CTIME_RATIO'''
		return self._instance.CtimeRatio

	@property
	def jvardmax(self) -> int:
		'''Value of variable $JVARDMAX'''
		return self._instance.Jvardmax

	@property
	def cvardmax(self) -> int:
		'''Value of variable $CVARDMAX'''
		return self._instance.Cvardmax

	@property
	def warnmessenb(self) -> bool:
		'''Value of variable $WARNMESSENB'''
		return self._instance.Warnmessenb

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def tba_mgn(self) -> float:
		'''Value of variable $TBA_MGN'''
		return self._instance.TbaMgn

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CoParamgpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
