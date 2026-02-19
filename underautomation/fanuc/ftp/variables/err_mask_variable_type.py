import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ErrMaskVariableType as err_mask_variable_type

class ErrMaskVariableType(GenericVariableType):
	'''Describes the Fanuc type ERR_MASK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = err_mask_variable_type()
		else:
			self._instance = _internal

	@property
	def ssc_mask1(self) -> int:
		'''Value of variable $SSC_MASK1'''
		return self._instance.SscMask1

	@property
	def ssc_mask2(self) -> int:
		'''Value of variable $SSC_MASK2'''
		return self._instance.SscMask2

	@property
	def ssc_mask3(self) -> int:
		'''Value of variable $SSC_MASK3'''
		return self._instance.SscMask3

	@property
	def ssc_mask4(self) -> int:
		'''Value of variable $SSC_MASK4'''
		return self._instance.SscMask4

	@property
	def sev_mask(self) -> int:
		'''Value of variable $SEV_MASK'''
		return self._instance.SevMask

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErrMaskVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
