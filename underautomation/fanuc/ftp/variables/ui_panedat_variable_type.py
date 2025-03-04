import typing
from underautomation.fanuc.ftp.variables.mouse_variable_type import MouseVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiPanedatVariableType as ui_panedat_variable_type

class UiPanedatVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_panedat_variable_type()
		else:
			self._instance = _internal
	@property
	def pageurl(self) -> str:
		return self._instance.Pageurl
	@property
	def frame(self) -> str:
		return self._instance.Frame
	@property
	def helpurl(self) -> str:
		return self._instance.Helpurl
	@property
	def parameter1(self) -> str:
		return self._instance.Parameter1
	@property
	def parameter2(self) -> str:
		return self._instance.Parameter2
	@property
	def parameter3(self) -> str:
		return self._instance.Parameter3
	@property
	def parameter4(self) -> str:
		return self._instance.Parameter4
	@property
	def parameter5(self) -> str:
		return self._instance.Parameter5
	@property
	def parameter6(self) -> str:
		return self._instance.Parameter6
	@property
	def parameter7(self) -> str:
		return self._instance.Parameter7
	@property
	def parameter8(self) -> str:
		return self._instance.Parameter8
	@property
	def interval(self) -> int:
		return self._instance.Interval
	@property
	def panestate(self) -> int:
		return self._instance.Panestate
	@property
	def dummy14(self) -> int:
		return self._instance.Dummy14
	@property
	def mouse(self) -> MouseVariableType:
		return MouseVariableType(self._instance.Mouse)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
