import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbjopGrpVariableType as tbjop_grp_variable_type

class TbjopGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbjop_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def f2mgn(self) -> float:
		return self._instance.F2mgn
	@property
	def minf2(self) -> float:
		return self._instance.Minf2
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
