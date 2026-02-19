import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import BlalOutVariableType as blal_out_variable_type

class BlalOutVariableType(GenericVariableType):
	'''Describes the Fanuc type BLAL_OUT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = blal_out_variable_type()
		else:
			self._instance = _internal

	@property
	def do_index(self) -> int:
		'''Value of variable $DO_INDEX'''
		return self._instance.DoIndex

	@property
	def ps_batalm_o(self) -> int:
		'''Value of variable $PS_BATALM_O'''
		return self._instance.PsBatalmO

	@property
	def batalm_or(self) -> bool:
		'''Value of variable $BATALM_OR'''
		return self._instance.BatalmOr

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BlalOutVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
