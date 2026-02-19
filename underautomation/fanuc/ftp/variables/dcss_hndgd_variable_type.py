import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssHndgdVariableType as dcss_hndgd_variable_type

class DcssHndgdVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_HNDGD_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_hndgd_variable_type()
		else:
			self._instance = _internal

	@property
	def grp_num(self) -> int:
		'''Value of variable $GRP_NUM'''
		return self._instance.GrpNum

	@property
	def speed_lim(self) -> float:
		'''Value of variable $SPEED_LIM'''
		return self._instance.SpeedLim

	@property
	def dsblio_typ(self) -> int:
		'''Value of variable $DSBLIO_TYP'''
		return self._instance.DsblioTyp

	@property
	def dsblio_idx(self) -> int:
		'''Value of variable $DSBLIO_IDX'''
		return self._instance.DsblioIdx

	@property
	def stop_type(self) -> int:
		'''Value of variable $STOP_TYPE'''
		return self._instance.StopType

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssHndgdVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
