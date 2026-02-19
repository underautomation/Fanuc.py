import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DrcCfgVariableType as drc_cfg_variable_type

class DrcCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DRC_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = drc_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def host1(self) -> str:
		'''Value of variable $HOST1'''
		return self._instance.Host1

	@property
	def host2(self) -> str:
		'''Value of variable $HOST2'''
		return self._instance.Host2

	@property
	def host3(self) -> str:
		'''Value of variable $HOST3'''
		return self._instance.Host3

	@property
	def host4(self) -> str:
		'''Value of variable $HOST4'''
		return self._instance.Host4

	@property
	def host5(self) -> str:
		'''Value of variable $HOST5'''
		return self._instance.Host5

	@property
	def email_enabl(self) -> bool:
		'''Value of variable $EMAIL_ENABL'''
		return self._instance.EmailEnabl

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DrcCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
