import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PssaveGrpVariableType as pssave_grp_variable_type

class PssaveGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type PSSAVE_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pssave_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def flange(self) -> int:
		'''Value of variable $FLANGE'''
		return self._instance.Flange

	@property
	def sync_flange(self) -> int:
		'''Value of variable $SYNC_FLANGE'''
		return self._instance.SyncFlange

	@property
	def sync_mst_cn(self) -> int:
		'''Value of variable $SYNC_MST_CN'''
		return self._instance.SyncMstCn

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PssaveGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
