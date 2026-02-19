import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssCnstcyVariableType as dcss_cnstcy_variable_type

class DcssCnstcyVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_CNSTCY_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_cnstcy_variable_type()
		else:
			self._instance = _internal

	@property
	def sig1_type(self) -> int:
		'''Value of variable $SIG1_TYPE'''
		return self._instance.Sig1Type

	@property
	def sig1_idx(self) -> int:
		'''Value of variable $SIG1_IDX'''
		return self._instance.Sig1Idx

	@property
	def sig2_type(self) -> int:
		'''Value of variable $SIG2_TYPE'''
		return self._instance.Sig2Type

	@property
	def sig2_idx(self) -> int:
		'''Value of variable $SIG2_IDX'''
		return self._instance.Sig2Idx

	@property
	def not_ope(self) -> int:
		'''Value of variable $NOT_OPE'''
		return self._instance.NotOpe

	@property
	def time(self) -> int:
		'''Value of variable $TIME'''
		return self._instance.Time

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssCnstcyVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
