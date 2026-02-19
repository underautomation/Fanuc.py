import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PppcfgLstVariableType as pppcfg_lst_variable_type

class PppcfgLstVariableType(GenericVariableType):
	'''Describes the Fanuc type PPPCFG_LST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pppcfg_lst_variable_type()
		else:
			self._instance = _internal

	@property
	def robotip(self) -> str:
		'''Value of variable $ROBOTIP'''
		return self._instance.Robotip

	@property
	def peerip(self) -> str:
		'''Value of variable $PEERIP'''
		return self._instance.Peerip

	@property
	def netmask(self) -> str:
		'''Value of variable $NETMASK'''
		return self._instance.Netmask

	@property
	def mru(self) -> int:
		'''Value of variable $MRU'''
		return self._instance.Mru

	@property
	def comp(self) -> int:
		'''Value of variable $COMP'''
		return self._instance.Comp

	@property
	def devtype(self) -> int:
		'''Value of variable $DEVTYPE'''
		return self._instance.Devtype

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PppcfgLstVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
