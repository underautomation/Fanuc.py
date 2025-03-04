import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FssbCfgVariableType as fssb_cfg_variable_type

class FssbCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fssb_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def fssb_line(self) -> typing.List[int]:
		return self._instance.FssbLine
	@property
	def ex_fssbline(self) -> typing.List[int]:
		return self._instance.ExFssbline
	@property
	def fssb1_axes(self) -> int:
		return self._instance.Fssb1Axes
	@property
	def fssb3_axes(self) -> int:
		return self._instance.Fssb3Axes
	@property
	def fssb5_axes(self) -> int:
		return self._instance.Fssb5Axes
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
