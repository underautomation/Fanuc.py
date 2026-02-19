import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpglMsetVariableType as tpgl_mset_variable_type

class TpglMsetVariableType(GenericVariableType):
	'''Describes the Fanuc type TPGL_MSET_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpgl_mset_variable_type()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def id(self) -> str:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def timeconst(self) -> int:
		'''Value of variable $TIMECONST'''
		return self._instance.Timeconst

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpglMsetVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
