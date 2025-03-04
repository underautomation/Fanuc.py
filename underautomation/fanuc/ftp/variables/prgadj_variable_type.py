import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PrgadjVariableType as prgadj_variable_type

class PrgadjVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgadj_variable_type()
		else:
			self._instance = _internal
	@property
	def x_limit(self) -> float:
		return self._instance.XLimit
	@property
	def y_limit(self) -> float:
		return self._instance.YLimit
	@property
	def z_limit(self) -> float:
		return self._instance.ZLimit
	@property
	def w_limit(self) -> float:
		return self._instance.WLimit
	@property
	def p_limit(self) -> float:
		return self._instance.PLimit
	@property
	def r_limit(self) -> float:
		return self._instance.RLimit
	@property
	def speed_adj(self) -> int:
		return self._instance.SpeedAdj
	@property
	def next_cycle(self) -> bool:
		return self._instance.NextCycle
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
