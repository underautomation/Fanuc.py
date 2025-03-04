import typing
from underautomation.fanuc.ftp.variables.det_io_variable_type import DetIoVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CondetIoVariableType as condet_io_variable_type

class CondetIoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_io_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def req_mask(self) -> int:
		return self._instance.ReqMask
	@property
	def used_msk(self) -> int:
		return self._instance.UsedMsk
	@property
	def io_data(self) -> typing.List[DetIoVariableType]:
		return [DetIoVariableType(x) for x in self._instance.IoData]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
