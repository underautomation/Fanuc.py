import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GpHoldVariableType as gp_hold_variable_type

class GpHoldVariableType(GenericVariableType):
	'''Describes the Fanuc type GP_HOLD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gp_hold_variable_type()
		else:
			self._instance = _internal

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def gp_msk(self) -> int:
		'''Value of variable $GP_MSK'''
		return self._instance.GpMsk

	@property
	def space_num(self) -> int:
		'''Value of variable $SPACE_NUM'''
		return self._instance.SpaceNum

	@property
	def cspace_num(self) -> int:
		'''Value of variable $CSPACE_NUM'''
		return self._instance.CspaceNum

	@property
	def req_grp(self) -> int:
		'''Value of variable $REQ_GRP'''
		return self._instance.ReqGrp

	@property
	def ps_rate(self) -> int:
		'''Value of variable $PS_RATE'''
		return self._instance.PsRate

	@property
	def rate(self) -> typing.List[float]:
		'''Value of variable $RATE'''
		return self._instance.Rate

	@property
	def int_pos(self) -> typing.List[float]:
		'''Value of variable $INT_POS'''
		return self._instance.IntPos

	@property
	def act_pos(self) -> typing.List[float]:
		'''Value of variable $ACT_POS'''
		return self._instance.ActPos

	@property
	def prd_pos(self) -> typing.List[float]:
		'''Value of variable $PRD_POS'''
		return self._instance.PrdPos

	@property
	def s1(self) -> int:
		'''Value of variable $S1'''
		return self._instance.S1

	@property
	def s2(self) -> int:
		'''Value of variable $S2'''
		return self._instance.S2

	@property
	def s3(self) -> int:
		'''Value of variable $S3'''
		return self._instance.S3

	@property
	def s4(self) -> int:
		'''Value of variable $S4'''
		return self._instance.S4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GpHoldVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
