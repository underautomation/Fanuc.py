import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TorqctrlVariableType as torqctrl_variable_type

class TorqctrlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = torqctrl_variable_type()
		else:
			self._instance = _internal
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def grp_stt(self) -> typing.List[bool]:
		return self._instance.GrpStt
	@property
	def sbr_pam21_v(self) -> typing.List[int]:
		return self._instance.SbrPam21V
	@property
	def sv_err_mod(self) -> typing.List[bool]:
		return self._instance.SvErrMod
	@property
	def sv_err_clr(self) -> typing.List[bool]:
		return self._instance.SvErrClr
	@property
	def action(self) -> int:
		return self._instance.Action
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
