import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcssParamVariableType as dcss_param_variable_type

class DcssParamVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_param_variable_type()
		else:
			self._instance = _internal
	@property
	def dochk_enb(self) -> int:
		return self._instance.DochkEnb
	@property
	def pmcs_enb(self) -> int:
		return self._instance.PmcsEnb
	@property
	def ls_stop(self) -> int:
		return self._instance.LsStop
	@property
	def ls_fence(self) -> int:
		return self._instance.LsFence
	@property
	def hotswp_time(self) -> int:
		return self._instance.HotswpTime
	@property
	def mode_select(self) -> int:
		return self._instance.ModeSelect
	@property
	def mode_type(self) -> int:
		return self._instance.ModeType
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
