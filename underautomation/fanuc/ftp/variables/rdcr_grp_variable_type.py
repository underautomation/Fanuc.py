import typing
from underautomation.fanuc.ftp.variables.j2red_variable_type import J2redVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RdcrGrpVariableType as rdcr_grp_variable_type

class RdcrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type RDCR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rdcr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def rmax_torque(self) -> typing.List[float]:
		'''Value of variable $RMAX_TORQUE'''
		return self._instance.RmaxTorque

	@property
	def rmin_torque(self) -> typing.List[float]:
		'''Value of variable $RMIN_TORQUE'''
		return self._instance.RminTorque

	@property
	def thres_torq(self) -> typing.List[float]:
		'''Value of variable $THRES_TORQ'''
		return self._instance.ThresTorq

	@property
	def rgear_ratio(self) -> typing.List[float]:
		'''Value of variable $RGEAR_RATIO'''
		return self._instance.RgearRatio

	@property
	def comp_sw(self) -> int:
		'''Value of variable $COMP_SW'''
		return self._instance.CompSw

	@property
	def reserve(self) -> typing.List[float]:
		'''Value of variable $RESERVE'''
		return self._instance.Reserve

	@property
	def spc_itp(self) -> int:
		'''Value of variable $SPC_ITP'''
		return self._instance.SpcItp

	@property
	def num_exd(self) -> int:
		'''Value of variable $NUM_EXD'''
		return self._instance.NumExd

	@property
	def j2th2nd(self) -> float:
		'''Value of variable $J2TH2ND'''
		return self._instance.J2th2nd

	@property
	def j2red(self) -> typing.List[J2redVariableType]:
		'''Value of variable $J2RED'''
		return [J2redVariableType(x) for x in self._instance.J2red]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RdcrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
