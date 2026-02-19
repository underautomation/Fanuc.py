import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VtcpsetVariableType as vtcpset_variable_type

class VtcpsetVariableType(GenericVariableType):
	'''Describes the Fanuc type VTCPSET_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vtcpset_variable_type()
		else:
			self._instance = _internal

	@property
	def move_dist_xy(self) -> float:
		'''Value of variable MOVE_DIST_XY'''
		return self._instance.MoveDistXy

	@property
	def move_dist_z(self) -> float:
		'''Value of variable MOVE_DIST_Z'''
		return self._instance.MoveDistZ

	@property
	def move_dist_r(self) -> float:
		'''Value of variable MOVE_DIST_R'''
		return self._instance.MoveDistR

	@property
	def move_dist_w(self) -> float:
		'''Value of variable MOVE_DIST_W'''
		return self._instance.MoveDistW

	@property
	def move_dist_p(self) -> float:
		'''Value of variable MOVE_DIST_P'''
		return self._instance.MoveDistP

	@property
	def move_dist_fw(self) -> float:
		'''Value of variable MOVE_DIST_FW'''
		return self._instance.MoveDistFw

	@property
	def move_dist_fp(self) -> float:
		'''Value of variable MOVE_DIST_FP'''
		return self._instance.MoveDistFp

	@property
	def div_num_z(self) -> int:
		'''Value of variable DIV_NUM_Z'''
		return self._instance.DivNumZ

	@property
	def div_num_r(self) -> int:
		'''Value of variable DIV_NUM_R'''
		return self._instance.DivNumR

	@property
	def div_num_wp(self) -> int:
		'''Value of variable DIV_NUM_WP'''
		return self._instance.DivNumWp

	@property
	def div_num_fwp(self) -> int:
		'''Value of variable DIV_NUM_FWP'''
		return self._instance.DivNumFwp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VtcpsetVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
