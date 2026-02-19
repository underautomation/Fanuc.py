import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IrprogCfgVariableType as irprog_cfg_variable_type

class IrprogCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type IRPROG_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irprog_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def curr_url(self) -> str:
		'''Value of variable $CURR_URL'''
		return self._instance.CurrUrl

	@property
	def all_menus(self) -> bool:
		'''Value of variable $ALL_MENUS'''
		return self._instance.AllMenus

	@property
	def visi_prg(self) -> int:
		'''Value of variable $VISI_PRG'''
		return self._instance.VisiPrg

	@property
	def tablet_ui(self) -> int:
		'''Value of variable $TABLET_UI'''
		return self._instance.TabletUi

	@property
	def tabky_dbg(self) -> bool:
		'''Value of variable $TABKY_DBG'''
		return self._instance.TabkyDbg

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IrprogCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
