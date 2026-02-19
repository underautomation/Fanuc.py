import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VarsConfigVariableType as vars_config_variable_type

class VarsConfigVariableType(GenericVariableType):
	'''Describes the Fanuc type VARS_CONFIG_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vars_config_variable_type()
		else:
			self._instance = _internal

	@property
	def shadowrecs(self) -> int:
		'''Value of variable $SHADOWRECS'''
		return self._instance.Shadowrecs

	@property
	def shad_unscan(self) -> int:
		'''Value of variable $SHAD_UNSCAN'''
		return self._instance.ShadUnscan

	@property
	def shadowtime(self) -> int:
		'''Value of variable $SHADOWTIME'''
		return self._instance.Shadowtime

	@property
	def shaddgdet(self) -> int:
		'''Value of variable $SHADDGDET'''
		return self._instance.Shaddgdet

	@property
	def legacy(self) -> bool:
		'''Value of variable $LEGACY'''
		return self._instance.Legacy

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VarsConfigVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
