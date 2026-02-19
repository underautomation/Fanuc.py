import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MiscScdVariableType as misc_scd_variable_type

class MiscScdVariableType(GenericVariableType):
	'''Describes the Fanuc type MISC_SCD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = misc_scd_variable_type()
		else:
			self._instance = _internal

	@property
	def dstb_max_a(self) -> typing.List[float]:
		'''Value of variable $DSTB_MAX_A'''
		return self._instance.DstbMaxA

	@property
	def dstb_min_a(self) -> typing.List[float]:
		'''Value of variable $DSTB_MIN_A'''
		return self._instance.DstbMinA

	@property
	def dstb_maxenb(self) -> typing.List[bool]:
		'''Value of variable $DSTB_MAXENB'''
		return self._instance.DstbMaxenb

	@property
	def dstb_minenb(self) -> typing.List[bool]:
		'''Value of variable $DSTB_MINENB'''
		return self._instance.DstbMinenb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MiscScdVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
