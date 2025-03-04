import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PgDefspdVariableType as pg_defspd_variable_type

class PgDefspdVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pg_defspd_variable_type()
		else:
			self._instance = _internal
	@property
	def ap_def_spd(self) -> int:
		return self._instance.ApDefSpd
	@property
	def ap_def_unit(self) -> int:
		return self._instance.ApDefUnit
	@property
	def dummy4(self) -> int:
		return self._instance.Dummy4
	@property
	def apsp_prexe(self) -> bool:
		return self._instance.ApspPrexe
	@property
	def dly_lastps(self) -> int:
		return self._instance.DlyLastps
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
