import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PmonQueVariableType as pmon_que_variable_type

class PmonQueVariableType(GenericVariableType):
	'''Describes the Fanuc type PMON_QUE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pmon_que_variable_type()
		else:
			self._instance = _internal

	@property
	def qcount(self) -> int:
		'''Value of variable $QCOUNT'''
		return self._instance.Qcount

	@property
	def qthreshold(self) -> int:
		'''Value of variable $QTHRESHOLD'''
		return self._instance.Qthreshold

	@property
	def qhysteresis(self) -> int:
		'''Value of variable $QHYSTERESIS'''
		return self._instance.Qhysteresis

	@property
	def queue_up(self) -> bool:
		'''Value of variable $QUEUE_UP'''
		return self._instance.QueueUp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PmonQueVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
