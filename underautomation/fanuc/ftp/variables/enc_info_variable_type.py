import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import EncInfoVariableType as enc_info_variable_type

class EncInfoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enc_info_variable_type()
		else:
			self._instance = _internal
	@property
	def svon_time(self) -> int:
		return self._instance.SvonTime
	@property
	def dummy1(self) -> int:
		return self._instance.Dummy1
	@property
	def dummy2(self) -> int:
		return self._instance.Dummy2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
