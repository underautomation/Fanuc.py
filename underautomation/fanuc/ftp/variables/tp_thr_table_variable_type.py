import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpThrTableVariableType as tp_thr_table_variable_type

class TpThrTableVariableType(GenericVariableType):
	'''Describes the Fanuc type TP_THR_TABLE'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_thr_table_variable_type()
		else:
			self._instance = _internal

	@property
	def thr_enb(self) -> bool:
		'''Value of variable $THR_ENB'''
		return self._instance.ThrEnb

	@property
	def di_no(self) -> int:
		'''Value of variable $DI_NO'''
		return self._instance.DiNo

	@property
	def do_no(self) -> int:
		'''Value of variable $DO_NO'''
		return self._instance.DoNo

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpThrTableVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
