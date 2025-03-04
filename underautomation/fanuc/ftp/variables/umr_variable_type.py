import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UmrVariableType as umr_variable_type

class UmrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = umr_variable_type()
		else:
			self._instance = _internal
	@property
	def gupr_p(self) -> int:
		return self._instance.GuprP
	@property
	def gmrr_p(self) -> int:
		return self._instance.GmrrP
	@property
	def gujr_p(self) -> int:
		return self._instance.GujrP
	@property
	def gmrr2_p(self) -> int:
		return self._instance.Gmrr2P
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
