import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZpCylinderVariableType as zp_cylinder_variable_type

class ZpCylinderVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zp_cylinder_variable_type()
		else:
			self._instance = _internal
	@property
	def radius(self) -> float:
		return self._instance.Radius
	@property
	def height(self) -> float:
		return self._instance.Height
	@property
	def prog_name(self) -> typing.List[str]:
		return self._instance.ProgName
	@property
	def line_num(self) -> typing.List[int]:
		return self._instance.LineNum
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
