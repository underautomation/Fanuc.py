import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpCurscrnVariableType as tp_curscrn_variable_type

class TpCurscrnVariableType(GenericVariableType):
	'''Describes the Fanuc type TP_CURSCRN_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tp_curscrn_variable_type()
		else:
			self._instance = _internal

	@property
	def nest_type(self) -> int:
		'''Value of variable $NEST_TYPE'''
		return self._instance.NestType

	@property
	def sp_id(self) -> int:
		'''Value of variable $SP_ID'''
		return self._instance.SpId

	@property
	def scrn_id(self) -> int:
		'''Value of variable $SCRN_ID'''
		return self._instance.ScrnId

	@property
	def sid(self) -> int:
		'''Value of variable $SID'''
		return self._instance.Sid

	@property
	def idx1(self) -> int:
		'''Value of variable $IDX1'''
		return self._instance.Idx1

	@property
	def idx2(self) -> int:
		'''Value of variable $IDX2'''
		return self._instance.Idx2

	@property
	def idx3(self) -> int:
		'''Value of variable $IDX3'''
		return self._instance.Idx3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpCurscrnVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
