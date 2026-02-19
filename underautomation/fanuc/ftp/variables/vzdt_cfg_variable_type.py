import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VzdtCfgVariableType as vzdt_cfg_variable_type

class VzdtCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type VZDT_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vzdt_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool:
		'''Value of variable $ENABLED'''
		return self._instance.Enabled

	@property
	def allow_image(self) -> bool:
		'''Value of variable $ALLOW_IMAGE'''
		return self._instance.AllowImage

	@property
	def period(self) -> int:
		'''Value of variable $PERIOD'''
		return self._instance.Period

	@property
	def msg_qsiz(self) -> int:
		'''Value of variable $MSG_QSIZ'''
		return self._instance.MsgQsiz

	@property
	def size_lim(self) -> int:
		'''Value of variable $SIZE_LIM'''
		return self._instance.SizeLim

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VzdtCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
