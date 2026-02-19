import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AtCellsetupVariableType as at_cellsetup_variable_type

class AtCellsetupVariableType(GenericVariableType):
	'''Describes the Fanuc type AT_CELLSETUP'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = at_cellsetup_variable_type()
		else:
			self._instance = _internal

	@property
	def home_io_prg(self) -> str:
		'''Value of variable $HOME_IO_PRG'''
		return self._instance.HomeIoPrg

	@property
	def home_macro(self) -> str:
		'''Value of variable $HOME_MACRO'''
		return self._instance.HomeMacro

	@property
	def repr_macro(self) -> str:
		'''Value of variable $REPR_MACRO'''
		return self._instance.ReprMacro

	@property
	def prodrun_spd(self) -> int:
		'''Value of variable $PRODRUN_SPD'''
		return self._instance.ProdrunSpd

	@property
	def prodrsm_spd(self) -> int:
		'''Value of variable $PRODRSM_SPD'''
		return self._instance.ProdrsmSpd

	@property
	def hmio_mn_enb(self) -> bool:
		'''Value of variable $HMIO_MN_ENB'''
		return self._instance.HmioMnEnb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AtCellsetupVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
