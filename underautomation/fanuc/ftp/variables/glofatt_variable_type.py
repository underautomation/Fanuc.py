import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GlofattVariableType as glofatt_variable_type

class GlofattVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = glofatt_variable_type()
		else:
			self._instance = _internal
	@property
	def device(self) -> str:
		return self._instance.Device
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def ext(self) -> str:
		return self._instance.Ext
	@property
	def taskid(self) -> int:
		return self._instance.Taskid
	@property
	def mode(self) -> int:
		return self._instance.Mode
	@property
	def tskfnum(self) -> int:
		return self._instance.Tskfnum
	@property
	def fileptr(self) -> int:
		return self._instance.Fileptr
	@property
	def kfile(self) -> int:
		return self._instance.Kfile
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
