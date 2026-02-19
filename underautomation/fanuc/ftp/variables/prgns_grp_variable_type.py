import typing
from underautomation.fanuc.ftp.variables.prgns_elem_variable_type import PrgnsElemVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsGrpVariableType as prgns_grp_variable_type

class PrgnsGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PRGNS_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def elem(self) -> typing.List[PrgnsElemVariableType]:
		'''Value of variable $ELEM'''
		return [PrgnsElemVariableType(x) for x in self._instance.Elem]

	@property
	def min_ang(self) -> typing.List[float]:
		'''Value of variable $MIN_ANG'''
		return self._instance.MinAng

	@property
	def max_ang(self) -> typing.List[float]:
		'''Value of variable $MAX_ANG'''
		return self._instance.MaxAng

	@property
	def base_ang(self) -> typing.List[float]:
		'''Value of variable $BASE_ANG'''
		return self._instance.BaseAng

	@property
	def last_mod(self) -> typing.List[int]:
		'''Value of variable $LAST_MOD'''
		return self._instance.LastMod

	@property
	def base_mod(self) -> typing.List[int]:
		'''Value of variable $BASE_MOD'''
		return self._instance.BaseMod

	@property
	def payload(self) -> int:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def warn_dout(self) -> int:
		'''Value of variable $WARN_DOUT'''
		return self._instance.WarnDout

	@property
	def warn_din(self) -> int:
		'''Value of variable $WARN_DIN'''
		return self._instance.WarnDin

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrgnsGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
