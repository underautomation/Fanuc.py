import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FileSetup2VariableType as file_setup2_variable_type

class FileSetup2VariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_setup2_variable_type()
		else:
			self._instance = _internal
	@property
	def file_tdc_sc(self) -> int:
		return self._instance.FileTdcSc
	@property
	def file_tv_sec(self) -> int:
		return self._instance.FileTvSec
	@property
	def file_tvc_sc(self) -> int:
		return self._instance.FileTvcSc
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
