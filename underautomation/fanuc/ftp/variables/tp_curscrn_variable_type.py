import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpCurscrnVariableType as tp_curscrn_variable_type

class TpCurscrnVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_curscrn_variable_type()
		else:
			self._instance = _internal
	@property
	def nest_type(self) -> int:
		return self._instance.NestType
	@property
	def sp_id(self) -> int:
		return self._instance.SpId
	@property
	def scrn_id(self) -> int:
		return self._instance.ScrnId
	@property
	def sid(self) -> int:
		return self._instance.Sid
	@property
	def idx1(self) -> int:
		return self._instance.Idx1
	@property
	def idx2(self) -> int:
		return self._instance.Idx2
	@property
	def idx3(self) -> int:
		return self._instance.Idx3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
