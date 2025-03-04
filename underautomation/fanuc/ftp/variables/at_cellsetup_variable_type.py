import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AtCellsetupVariableType as at_cellsetup_variable_type

class AtCellsetupVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = at_cellsetup_variable_type()
		else:
			self._instance = _internal
	@property
	def home_io_prg(self) -> str:
		return self._instance.HomeIoPrg
	@property
	def home_macro(self) -> str:
		return self._instance.HomeMacro
	@property
	def repr_macro(self) -> str:
		return self._instance.ReprMacro
	@property
	def prodrun_spd(self) -> int:
		return self._instance.ProdrunSpd
	@property
	def prodrsm_spd(self) -> int:
		return self._instance.ProdrsmSpd
	@property
	def hmio_mn_enb(self) -> bool:
		return self._instance.HmioMnEnb
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
