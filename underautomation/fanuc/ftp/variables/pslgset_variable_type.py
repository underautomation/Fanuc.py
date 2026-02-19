import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PslgsetVariableType as pslgset_variable_type

class PslgsetVariableType(GenericVariableType):
	'''Describes the Fanuc type PSLGSET_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pslgset_variable_type()
		else:
			self._instance = _internal

	@property
	def ps_size(self) -> int:
		'''Value of variable $PS_SIZE'''
		return self._instance.PsSize

	@property
	def ps_mode(self) -> int:
		'''Value of variable $PS_MODE'''
		return self._instance.PsMode

	@property
	def timesent(self) -> int:
		'''Value of variable $TIMESENT'''
		return self._instance.Timesent

	@property
	def lastdev(self) -> str:
		'''Value of variable $LASTDEV'''
		return self._instance.Lastdev

	@property
	def ps_debug(self) -> int:
		'''Value of variable $PS_DEBUG'''
		return self._instance.PsDebug

	@property
	def timesent2(self) -> int:
		'''Value of variable $TIMESENT2'''
		return self._instance.Timesent2

	@property
	def lastdev2(self) -> str:
		'''Value of variable $LASTDEV2'''
		return self._instance.Lastdev2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PslgsetVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
