import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import KarelCfgVariableType as karel_cfg_variable_type

class KarelCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type KAREL_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = karel_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def conv_enable(self) -> bool:
		'''Value of variable $CONV_ENABLE'''
		return self._instance.ConvEnable

	@property
	def conv_ctrl(self) -> bool:
		'''Value of variable $CONV_CTRL'''
		return self._instance.ConvCtrl

	@property
	def conv_flags(self) -> int:
		'''Value of variable $CONV_FLAGS'''
		return self._instance.ConvFlags

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KarelCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
