import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PfPrefVariableType as pf_pref_variable_type

class PfPrefVariableType(GenericVariableType):
	'''Describes the Fanuc type PF_PREF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_pref_variable_type()
		else:
			self._instance = _internal

	@property
	def gridlines(self) -> int:
		'''Value of variable $GRIDLINES'''
		return self._instance.Gridlines

	@property
	def bars_num(self) -> int:
		'''Value of variable $BARS_NUM'''
		return self._instance.BarsNum

	@property
	def data_type(self) -> int:
		'''Value of variable $DATA_TYPE'''
		return self._instance.DataType

	@property
	def style(self) -> int:
		'''Value of variable $STYLE'''
		return self._instance.Style

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PfPrefVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
