import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SmbClntVariableType as smb_clnt_variable_type

class SmbClntVariableType(GenericVariableType):
	'''Describes the Fanuc type SMB_CLNT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smb_clnt_variable_type()
		else:
			self._instance = _internal

	@property
	def cache(self) -> bool:
		'''Value of variable $CACHE'''
		return self._instance.Cache

	@property
	def rsptmout(self) -> int:
		'''Value of variable $RSPTMOUT'''
		return self._instance.Rsptmout

	@property
	def setpwrd(self) -> bool:
		'''Value of variable $SETPWRD'''
		return self._instance.Setpwrd

	@property
	def domain(self) -> str:
		'''Value of variable $DOMAIN'''
		return self._instance.Domain

	@property
	def spare(self) -> int:
		'''Value of variable $SPARE'''
		return self._instance.Spare

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SmbClntVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
