import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlclGrpVariableType as plcl_grp_variable_type

class PlclGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PLCL_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plcl_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def calib_stat(self) -> int:
		'''Value of variable $CALIB_STAT'''
		return self._instance.CalibStat

	@property
	def trq_mgn(self) -> typing.List[float]:
		'''Value of variable $TRQ_MGN'''
		return self._instance.TrqMgn

	@property
	def link_m(self) -> typing.List[float]:
		'''Value of variable $LINK_M'''
		return self._instance.LinkM

	@property
	def link_sx(self) -> typing.List[float]:
		'''Value of variable $LINK_SX'''
		return self._instance.LinkSx

	@property
	def link_sy(self) -> typing.List[float]:
		'''Value of variable $LINK_SY'''
		return self._instance.LinkSy

	@property
	def link_sz(self) -> typing.List[float]:
		'''Value of variable $LINK_SZ'''
		return self._instance.LinkSz

	@property
	def link_ix(self) -> typing.List[float]:
		'''Value of variable $LINK_IX'''
		return self._instance.LinkIx

	@property
	def link_iy(self) -> typing.List[float]:
		'''Value of variable $LINK_IY'''
		return self._instance.LinkIy

	@property
	def link_iz(self) -> typing.List[float]:
		'''Value of variable $LINK_IZ'''
		return self._instance.LinkIz

	@property
	def calib3a(self) -> int:
		'''Value of variable $CALIB_3A'''
		return self._instance.Calib3a

	@property
	def tq_mgn3a(self) -> typing.List[float]:
		'''Value of variable $TQ_MGN3A'''
		return self._instance.TqMgn3a

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlclGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
