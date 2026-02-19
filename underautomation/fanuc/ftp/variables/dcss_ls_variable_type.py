import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssLsVariableType as dcss_ls_variable_type

class DcssLsVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_LS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_ls_variable_type()
		else:
			self._instance = _internal

	@property
	def stoout_idx(self) -> int:
		'''Value of variable $STOOUT_IDX'''
		return self._instance.StooutIdx

	@property
	def stofb_idx(self) -> int:
		'''Value of variable $STOFB_IDX'''
		return self._instance.StofbIdx

	@property
	def stofb_ch(self) -> int:
		'''Value of variable $STOFB_CH'''
		return self._instance.StofbCh

	@property
	def fence_type(self) -> int:
		'''Value of variable $FENCE_TYPE'''
		return self._instance.FenceType

	@property
	def fence_idx(self) -> int:
		'''Value of variable $FENCE_IDX'''
		return self._instance.FenceIdx

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssLsVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
