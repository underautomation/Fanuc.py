import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import GravcGrpVariableType as gravc_grp_variable_type

class GravcGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type GRAVC_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gravc_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def mode_sw(self) -> int:
		'''Value of variable $MODE_SW'''
		return self._instance.ModeSw

	@property
	def spcons(self) -> typing.List[float]:
		'''Value of variable $SPCONS'''
		return self._instance.Spcons

	@property
	def debug1(self) -> int:
		'''Value of variable $DEBUG1'''
		return self._instance.Debug1

	@property
	def debug2(self) -> typing.List[float]:
		'''Value of variable $DEBUG2'''
		return self._instance.Debug2

	@property
	def grv_status(self) -> int:
		'''Value of variable $GRV_STATUS'''
		return self._instance.GrvStatus

	@property
	def bkup_no116(self) -> typing.List[int]:
		'''Value of variable $BKUP_NO116'''
		return self._instance.BkupNo116

	@property
	def poff_no116(self) -> typing.List[int]:
		'''Value of variable $POFF_NO116'''
		return self._instance.PoffNo116

	@property
	def grvcmp_sw(self) -> int:
		'''Value of variable $GRVCMP_SW'''
		return self._instance.GrvcmpSw

	@property
	def grvmst_loop(self) -> int:
		'''Value of variable $GRVMST_LOOP'''
		return self._instance.GrvmstLoop

	@property
	def mst_smt_len(self) -> int:
		'''Value of variable $MST_SMT_LEN'''
		return self._instance.MstSmtLen

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GravcGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
