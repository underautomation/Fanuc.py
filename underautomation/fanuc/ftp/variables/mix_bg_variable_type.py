import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MixBgVariableType as mix_bg_variable_type

class MixBgVariableType(GenericVariableType):
	'''Describes the Fanuc type MIX_BG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mix_bg_variable_type()
		else:
			self._instance = _internal

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def modify_time(self) -> int:
		'''Value of variable $MODIFY_TIME'''
		return self._instance.ModifyTime

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MixBgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
