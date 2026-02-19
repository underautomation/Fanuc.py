import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DcssParamVariableType as dcss_param_variable_type

class DcssParamVariableType(GenericVariableType):
	'''Describes the Fanuc type DCSS_PARAM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_param_variable_type()
		else:
			self._instance = _internal

	@property
	def dochk_enb(self) -> int:
		'''Value of variable $DOCHK_ENB'''
		return self._instance.DochkEnb

	@property
	def pmcs_enb(self) -> int:
		'''Value of variable $PMCS_ENB'''
		return self._instance.PmcsEnb

	@property
	def ls_stop(self) -> int:
		'''Value of variable $LS_STOP'''
		return self._instance.LsStop

	@property
	def ls_fence(self) -> int:
		'''Value of variable $LS_FENCE'''
		return self._instance.LsFence

	@property
	def hotswp_time(self) -> int:
		'''Value of variable $HOTSWP_TIME'''
		return self._instance.HotswpTime

	@property
	def mode_select(self) -> int:
		'''Value of variable $MODE_SELECT'''
		return self._instance.ModeSelect

	@property
	def mode_type(self) -> int:
		'''Value of variable $MODE_TYPE'''
		return self._instance.ModeType

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DcssParamVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
