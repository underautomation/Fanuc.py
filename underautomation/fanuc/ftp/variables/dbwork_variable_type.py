import typing
from underautomation.fanuc.ftp.variables.dbinfo_variable_type import DbinfoVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbworkVariableType as dbwork_variable_type

class DbworkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbwork_variable_type()
		else:
			self._instance = _internal
	@property
	def info(self) -> typing.List[DbinfoVariableType]:
		return [DbinfoVariableType(x) for x in self._instance.Info]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
