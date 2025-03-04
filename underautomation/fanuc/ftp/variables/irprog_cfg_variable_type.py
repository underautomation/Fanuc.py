import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import IrprogCfgVariableType as irprog_cfg_variable_type

class IrprogCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irprog_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def curr_url(self) -> str:
		return self._instance.CurrUrl
	@property
	def all_menus(self) -> bool:
		return self._instance.AllMenus
	@property
	def visi_prg(self) -> int:
		return self._instance.VisiPrg
	@property
	def tablet_ui(self) -> int:
		return self._instance.TabletUi
	@property
	def tabky_dbg(self) -> bool:
		return self._instance.TabkyDbg
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
