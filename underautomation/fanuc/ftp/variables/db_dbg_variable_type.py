import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DbDbgVariableType as db_dbg_variable_type

class DbDbgVariableType(GenericVariableType):
	'''Describes the Fanuc type DB_DBG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = db_dbg_variable_type()
		else:
			self._instance = _internal

	@property
	def dbg_prm(self) -> typing.List[int]:
		'''Value of variable $DBG_PRM'''
		return self._instance.DbgPrm

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DbDbgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
