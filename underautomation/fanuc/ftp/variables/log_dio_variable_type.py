import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import LogDioVariableType as log_dio_variable_type

class LogDioVariableType(GenericVariableType):
	'''Describes the Fanuc type LOG_DIO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_dio_variable_type()
		else:
			self._instance = _internal

	@property
	def rack(self) -> int:
		'''Value of variable $RACK'''
		return self._instance.Rack

	@property
	def slot(self) -> int:
		'''Value of variable $SLOT'''
		return self._instance.Slot

	@property
	def mod_type(self) -> int:
		'''Value of variable $MOD_TYPE'''
		return self._instance.ModType

	@property
	def port_type(self) -> int:
		'''Value of variable $PORT_TYPE'''
		return self._instance.PortType

	@property
	def start_port(self) -> int:
		'''Value of variable $START_PORT'''
		return self._instance.StartPort

	@property
	def end_port(self) -> int:
		'''Value of variable $END_PORT'''
		return self._instance.EndPort

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogDioVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
