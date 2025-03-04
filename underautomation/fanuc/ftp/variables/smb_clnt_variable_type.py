import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SmbClntVariableType as smb_clnt_variable_type

class SmbClntVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smb_clnt_variable_type()
		else:
			self._instance = _internal
	@property
	def cache(self) -> bool:
		return self._instance.Cache
	@property
	def rsptmout(self) -> int:
		return self._instance.Rsptmout
	@property
	def setpwrd(self) -> bool:
		return self._instance.Setpwrd
	@property
	def domain(self) -> str:
		return self._instance.Domain
	@property
	def spare(self) -> int:
		return self._instance.Spare
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
