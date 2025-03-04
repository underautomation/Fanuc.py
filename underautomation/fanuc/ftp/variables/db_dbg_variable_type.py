import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbDbgVariableType as db_dbg_variable_type

class DbDbgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = db_dbg_variable_type()
		else:
			self._instance = _internal
	@property
	def dbg_prm(self) -> typing.List[int]:
		return self._instance.DbgPrm
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
