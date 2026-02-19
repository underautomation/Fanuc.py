import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlimGrpVariableType as plim_grp_variable_type

class PlimGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PLIM_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plim_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def max_pyld(self) -> float:
		'''Value of variable $MAX_PYLD'''
		return self._instance.MaxPyld

	@property
	def axisinertia(self) -> typing.List[int]:
		'''Value of variable $AXISINERTIA'''
		return self._instance.Axisinertia

	@property
	def axisinertil(self) -> typing.List[int]:
		'''Value of variable $AXISINERTIL'''
		return self._instance.Axisinertil

	@property
	def axismoment(self) -> typing.List[int]:
		'''Value of variable $AXISMOMENT'''
		return self._instance.Axismoment

	@property
	def axis_im_scl(self) -> int:
		'''Value of variable $AXIS_IM_SCL'''
		return self._instance.AxisImScl

	@property
	def lim_wt_scl(self) -> float:
		'''Value of variable $LIM_WT_SCL'''
		return self._instance.LimWtScl

	@property
	def lim_inr_scl(self) -> typing.List[float]:
		'''Value of variable $LIM_INR_SCL'''
		return self._instance.LimInrScl

	@property
	def lim_mnt_scl(self) -> typing.List[float]:
		'''Value of variable $LIM_MNT_SCL'''
		return self._instance.LimMntScl

	@property
	def lim_cl_scl(self) -> typing.List[float]:
		'''Value of variable $LIM_CL_SCL'''
		return self._instance.LimClScl

	@property
	def pld_mode(self) -> int:
		'''Value of variable $PLD_MODE'''
		return self._instance.PldMode

	@property
	def dummy11(self) -> int:
		'''Value of variable $DUMMY11'''
		return self._instance.Dummy11

	@property
	def dummy12(self) -> int:
		'''Value of variable $DUMMY12'''
		return self._instance.Dummy12

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlimGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
