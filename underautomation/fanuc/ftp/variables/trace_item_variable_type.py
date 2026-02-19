import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TraceItemVariableType as trace_item_variable_type

class TraceItemVariableType(GenericVariableType):
	'''Describes the Fanuc type TRACE_ITEM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trace_item_variable_type()
		else:
			self._instance = _internal

	@property
	def prg_name(self) -> str:
		'''Value of variable $PRG_NAME'''
		return self._instance.PrgName

	@property
	def var_name(self) -> str:
		'''Value of variable $VAR_NAME'''
		return self._instance.VarName

	@property
	def desc(self) -> str:
		'''Value of variable $DESC'''
		return self._instance.Desc

	@property
	def units(self) -> str:
		'''Value of variable $UNITS'''
		return self._instance.Units

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def io_type(self) -> int:
		'''Value of variable $IO_TYPE'''
		return self._instance.IoType

	@property
	def port_num(self) -> int:
		'''Value of variable $PORT_NUM'''
		return self._instance.PortNum

	@property
	def square(self) -> float:
		'''Value of variable $SQUARE'''
		return self._instance.Square

	@property
	def slope(self) -> float:
		'''Value of variable $SLOPE'''
		return self._instance.Slope

	@property
	def intercept(self) -> float:
		'''Value of variable $INTERCEPT'''
		return self._instance.Intercept

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TraceItemVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
