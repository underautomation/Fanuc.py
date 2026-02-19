import typing
from underautomation.fanuc.ftp.variables.com_space_variable_type import ComSpaceVariableType
from underautomation.fanuc.ftp.variables.gp_hold_variable_type import GpHoldVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RspacegVariableType as rspaceg_variable_type

class RspacegVariableType(GenericVariableType):
	'''Describes the Fanuc type RSPACEG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspaceg_variable_type()
		else:
			self._instance = _internal

	@property
	def com_space(self) -> typing.List[ComSpaceVariableType]:
		'''Value of variable $COM_SPACE'''
		return [ComSpaceVariableType(x) for x in self._instance.ComSpace]

	@property
	def gp_hold(self) -> typing.List[GpHoldVariableType]:
		'''Value of variable $GP_HOLD'''
		return [GpHoldVariableType(x) for x in self._instance.GpHold]

	@property
	def spare_int(self) -> typing.List[int]:
		'''Value of variable $SPARE_INT'''
		return self._instance.SpareInt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RspacegVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
