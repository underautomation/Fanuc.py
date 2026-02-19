import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import Rs232CfgVariableType as rs232_cfg_variable_type

class Rs232CfgVariableType(GenericVariableType):
	'''Describes the Fanuc type RS232_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rs232_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def deviceuse(self) -> int:
		'''Value of variable $DEVICEUSE'''
		return self._instance.Deviceuse

	@property
	def speed(self) -> int:
		'''Value of variable $SPEED'''
		return self._instance.Speed

	@property
	def parity(self) -> int:
		'''Value of variable $PARITY'''
		return self._instance.Parity

	@property
	def stopbits(self) -> int:
		'''Value of variable $STOPBITS'''
		return self._instance.Stopbits

	@property
	def flowcontrol(self) -> int:
		'''Value of variable $FLOWCONTROL'''
		return self._instance.Flowcontrol

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def custom(self) -> int:
		'''Value of variable $CUSTOM'''
		return self._instance.Custom

	@property
	def auxtask(self) -> int:
		'''Value of variable $AUXTASK'''
		return self._instance.Auxtask

	@property
	def interface(self) -> int:
		'''Value of variable $INTERFACE'''
		return self._instance.Interface

	@property
	def status(self) -> str:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Rs232CfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
