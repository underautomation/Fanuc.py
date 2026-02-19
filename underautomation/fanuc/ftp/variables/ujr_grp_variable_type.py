import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UjrGrpVariableType as ujr_grp_variable_type

class UjrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type UJR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ujr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def fine_ovrd(self) -> int:
		'''Value of variable $FINE_OVRD'''
		return self._instance.FineOvrd

	@property
	def jogframe(self) -> CartesianPositionVariable:
		'''Value of variable $JOGFRAME'''
		return CartesianPositionVariable(self._instance.Jogframe)

	@property
	def fine_dist(self) -> float:
		'''Value of variable $FINE_DIST'''
		return self._instance.FineDist

	@property
	def j7_group(self) -> int:
		'''Value of variable $J7_GROUP'''
		return self._instance.J7Group

	@property
	def j8_group(self) -> int:
		'''Value of variable $J8_GROUP'''
		return self._instance.J8Group

	@property
	def j7_axis(self) -> int:
		'''Value of variable $J7_AXIS'''
		return self._instance.J7Axis

	@property
	def j8_axis(self) -> int:
		'''Value of variable $J8_AXIS'''
		return self._instance.J8Axis

	@property
	def j7_label(self) -> str:
		'''Value of variable $J7_LABEL'''
		return self._instance.J7Label

	@property
	def j8_label(self) -> str:
		'''Value of variable $J8_LABEL'''
		return self._instance.J8Label

	@property
	def j7_graphic(self) -> str:
		'''Value of variable $J7_GRAPHIC'''
		return self._instance.J7Graphic

	@property
	def j8_graphic(self) -> str:
		'''Value of variable $J8_GRAPHIC'''
		return self._instance.J8Graphic

	@property
	def dsb_j7j8(self) -> bool:
		'''Value of variable $DSB_J7J8'''
		return self._instance.DsbJ7j8

	@property
	def dsbl_key(self) -> typing.List[bool]:
		'''Value of variable $DSBL_KEY'''
		return self._instance.DsblKey

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UjrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
