import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiUsrviewVariableType as ui_usrview_variable_type

class UiUsrviewVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_usrview_variable_type()
		else:
			self._instance = _internal
	@property
	def menu(self) -> str:
		return self._instance.Menu
	@property
	def config(self) -> str:
		return self._instance.Config
	@property
	def focus(self) -> str:
		return self._instance.Focus
	@property
	def prim(self) -> str:
		return self._instance.Prim
	@property
	def dual(self) -> str:
		return self._instance.Dual
	@property
	def triple(self) -> str:
		return self._instance.Triple
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
