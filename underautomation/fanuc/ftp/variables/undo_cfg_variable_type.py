import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UndoCfgVariableType as undo_cfg_variable_type

class UndoCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = undo_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def undo_enb(self) -> bool:
		return self._instance.UndoEnb
	@property
	def warn_enb(self) -> bool:
		return self._instance.WarnEnb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
