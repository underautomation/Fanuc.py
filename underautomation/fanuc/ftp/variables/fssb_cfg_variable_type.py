import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FssbCfgVariableType as fssb_cfg_variable_type

class FssbCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type FSSB_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fssb_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def fssb_line(self) -> typing.List[int]:
		'''Value of variable $FSSB_LINE'''
		return self._instance.FssbLine

	@property
	def ex_fssbline(self) -> typing.List[int]:
		'''Value of variable $EX_FSSBLINE'''
		return self._instance.ExFssbline

	@property
	def fssb1_axes(self) -> int:
		'''Value of variable $FSSB1_AXES'''
		return self._instance.Fssb1Axes

	@property
	def fssb3_axes(self) -> int:
		'''Value of variable $FSSB3_AXES'''
		return self._instance.Fssb3Axes

	@property
	def fssb5_axes(self) -> int:
		'''Value of variable $FSSB5_AXES'''
		return self._instance.Fssb5Axes

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FssbCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
