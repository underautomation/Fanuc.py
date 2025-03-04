import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Rs232CfgVariableType as rs232_cfg_variable_type

class Rs232CfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rs232_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def deviceuse(self) -> int:
		return self._instance.Deviceuse
	@property
	def speed(self) -> int:
		return self._instance.Speed
	@property
	def parity(self) -> int:
		return self._instance.Parity
	@property
	def stopbits(self) -> int:
		return self._instance.Stopbits
	@property
	def flowcontrol(self) -> int:
		return self._instance.Flowcontrol
	@property
	def timeout(self) -> int:
		return self._instance.Timeout
	@property
	def custom(self) -> int:
		return self._instance.Custom
	@property
	def auxtask(self) -> int:
		return self._instance.Auxtask
	@property
	def interface(self) -> int:
		return self._instance.Interface
	@property
	def status(self) -> str:
		return self._instance.Status
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
