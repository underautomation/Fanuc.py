import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VlexeCfgVariableType as vlexe_cfg_variable_type

class VlexeCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type VLEXE_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vlexe_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def date(self) -> int:
		'''Value of variable $DATE'''
		return self._instance.Date

	@property
	def fldr_index(self) -> int:
		'''Value of variable $FLDR_INDEX'''
		return self._instance.FldrIndex

	@property
	def file_index(self) -> int:
		'''Value of variable $FILE_INDEX'''
		return self._instance.FileIndex

	@property
	def rec_index(self) -> int:
		'''Value of variable $REC_INDEX'''
		return self._instance.RecIndex

	@property
	def output_idx(self) -> bool:
		'''Value of variable $OUTPUT_IDX'''
		return self._instance.OutputIdx

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VlexeCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
