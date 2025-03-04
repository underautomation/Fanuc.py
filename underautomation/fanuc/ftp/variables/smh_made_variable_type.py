import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SmhMadeVariableType as smh_made_variable_type

class SmhMadeVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smh_made_variable_type()
		else:
			self._instance = _internal
	@property
	def made_tasks(self) -> int:
		return self._instance.MadeTasks
	@property
	def made_grups(self) -> int:
		return self._instance.MadeGrups
	@property
	def made_mirs(self) -> int:
		return self._instance.MadeMirs
	@property
	def made_amrs(self) -> int:
		return self._instance.MadeAmrs
	@property
	def made_mode(self) -> int:
		return self._instance.MadeMode
	@property
	def made_stk(self) -> int:
		return self._instance.MadeStk
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
