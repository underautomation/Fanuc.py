import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FileSetup2VariableType as file_setup2_variable_type

class FileSetup2VariableType(GenericVariableType):
	'''Describes the Fanuc type FILE_SETUP2_'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_setup2_variable_type()
		else:
			self._instance = _internal

	@property
	def file_tdc_sc(self) -> int:
		'''Value of variable $FILE_TDC_SC'''
		return self._instance.FileTdcSc

	@property
	def file_tv_sec(self) -> int:
		'''Value of variable $FILE_TV_SEC'''
		return self._instance.FileTvSec

	@property
	def file_tvc_sc(self) -> int:
		'''Value of variable $FILE_TVC_SC'''
		return self._instance.FileTvcSc

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileSetup2VariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
