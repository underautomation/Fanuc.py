import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DmswCfgVariableType as dmsw_cfg_variable_type

class DmswCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type DMSW_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dmsw_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def keyimage(self) -> int:
		'''Value of variable $KEYIMAGE'''
		return self._instance.Keyimage

	@property
	def tms_dsb(self) -> bool:
		'''Value of variable $TMS_DSB'''
		return self._instance.TmsDsb

	@property
	def tms_stat(self) -> int:
		'''Value of variable $TMS_STAT'''
		return self._instance.TmsStat

	@property
	def tms_input(self) -> int:
		'''Value of variable $TMS_INPUT'''
		return self._instance.TmsInput

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DmswCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
