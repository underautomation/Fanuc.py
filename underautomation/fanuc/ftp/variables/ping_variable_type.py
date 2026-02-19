import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PingVariableType as ping_variable_type

class PingVariableType(GenericVariableType):
	'''Describes the Fanuc type PING_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ping_variable_type()
		else:
			self._instance = _internal

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def datalen(self) -> int:
		'''Value of variable $DATALEN'''
		return self._instance.Datalen

	@property
	def npackets(self) -> int:
		'''Value of variable $NPACKETS'''
		return self._instance.Npackets

	@property
	def debug(self) -> bool:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PingVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
