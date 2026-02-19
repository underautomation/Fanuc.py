import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IrcGnrcVariableType as irc_gnrc_variable_type

class IrcGnrcVariableType(GenericVariableType):
	'''Describes the Fanuc type IRC_GNRC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = irc_gnrc_variable_type()
		else:
			self._instance = _internal

	@property
	def dostime(self) -> int:
		'''Value of variable DOSTIME'''
		return self._instance.Dostime

	@property
	def msgtype(self) -> int:
		'''Value of variable MSGTYPE'''
		return self._instance.Msgtype

	@property
	def int1(self) -> int:
		'''Value of variable INT1'''
		return self._instance.Int1

	@property
	def int2(self) -> int:
		'''Value of variable INT2'''
		return self._instance.Int2

	@property
	def str1(self) -> str:
		'''Value of variable STR1'''
		return self._instance.Str1

	@property
	def str2(self) -> str:
		'''Value of variable STR2'''
		return self._instance.Str2

	@property
	def str3(self) -> str:
		'''Value of variable STR3'''
		return self._instance.Str3

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IrcGnrcVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
