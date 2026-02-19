import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FsacLstVariableType as fsac_lst_variable_type

class FsacLstVariableType(GenericVariableType):
	'''Describes the Fanuc type FSAC_LST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fsac_lst_variable_type()
		else:
			self._instance = _internal

	@property
	def clnt_name(self) -> str:
		'''Value of variable $CLNT_NAME'''
		return self._instance.ClntName

	@property
	def ip_address(self) -> str:
		'''Value of variable $IP_ADDRESS'''
		return self._instance.IpAddress

	@property
	def access_lvl(self) -> int:
		'''Value of variable $ACCESS_LVL'''
		return self._instance.AccessLvl

	@property
	def apps(self) -> int:
		'''Value of variable $APPS'''
		return self._instance.Apps

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FsacLstVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
