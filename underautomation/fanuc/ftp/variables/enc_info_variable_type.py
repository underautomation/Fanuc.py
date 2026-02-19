import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import EncInfoVariableType as enc_info_variable_type

class EncInfoVariableType(GenericVariableType):
	'''Describes the Fanuc type ENC_INFO_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = enc_info_variable_type()
		else:
			self._instance = _internal

	@property
	def svon_time(self) -> int:
		'''Value of variable $SVON_TIME'''
		return self._instance.SvonTime

	@property
	def dummy1(self) -> int:
		'''Value of variable $DUMMY1'''
		return self._instance.Dummy1

	@property
	def dummy2(self) -> int:
		'''Value of variable $DUMMY2'''
		return self._instance.Dummy2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, EncInfoVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
