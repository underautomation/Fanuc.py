import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GpStatusVariableType as gp_status_variable_type

class GpStatusVariableType(GenericVariableType):
	'''Describes the Fanuc type GP_STATUS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gp_status_variable_type()
		else:
			self._instance = _internal

	@property
	def in_use(self) -> bool:
		'''Value of variable $IN_USE'''
		return self._instance.InUse

	@property
	def space_num(self) -> int:
		'''Value of variable $SPACE_NUM'''
		return self._instance.SpaceNum

	@property
	def priority(self) -> int:
		'''Value of variable $PRIORITY'''
		return self._instance.Priority

	@property
	def status1(self) -> int:
		'''Value of variable $STATUS1'''
		return self._instance.Status1

	@property
	def status2(self) -> int:
		'''Value of variable $STATUS2'''
		return self._instance.Status2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GpStatusVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
