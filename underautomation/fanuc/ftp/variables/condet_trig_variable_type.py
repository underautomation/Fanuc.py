import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CondetTrigVariableType as condet_trig_variable_type

class CondetTrigVariableType(GenericVariableType):
	'''Describes the Fanuc type CONDET_TRIG_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_trig_variable_type()
		else:
			self._instance = _internal

	@property
	def io_type(self) -> int:
		'''Value of variable $IO_TYPE'''
		return self._instance.IoType

	@property
	def io_port(self) -> int:
		'''Value of variable $IO_PORT'''
		return self._instance.IoPort

	@property
	def io_style(self) -> int:
		'''Value of variable $IO_STYLE'''
		return self._instance.IoStyle

	@property
	def delay(self) -> int:
		'''Value of variable $DELAY'''
		return self._instance.Delay

	@property
	def style_type(self) -> int:
		'''Value of variable $STYLE_TYPE'''
		return self._instance.StyleType

	@property
	def style_port(self) -> int:
		'''Value of variable $STYLE_PORT'''
		return self._instance.StylePort

	@property
	def flag(self) -> int:
		'''Value of variable $FLAG'''
		return self._instance.Flag

	@property
	def debug(self) -> int:
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
		if not isinstance(other, CondetTrigVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
