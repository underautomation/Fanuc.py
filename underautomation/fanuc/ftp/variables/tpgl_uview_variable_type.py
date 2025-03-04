import typing
from underautomation.fanuc.ftp.variables.view_variable_type import ViewVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpglUviewVariableType as tpgl_uview_variable_type

class TpglUviewVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_uview_variable_type()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@property
	def gif(self) -> str:
		return self._instance.Gif
	@property
	def view(self) -> ViewVariableType:
		return ViewVariableType(self._instance.View)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
