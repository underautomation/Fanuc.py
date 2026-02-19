import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TorqctrlVariableType as torqctrl_variable_type

class TorqctrlVariableType(GenericVariableType):
	'''Describes the Fanuc type TORQCTRL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = torqctrl_variable_type()
		else:
			self._instance = _internal

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def grp_stt(self) -> typing.List[bool]:
		'''Value of variable $GRP_STT'''
		return self._instance.GrpStt

	@property
	def sbr_pam21_v(self) -> typing.List[int]:
		'''Value of variable $SBR_PAM21_V'''
		return self._instance.SbrPam21V

	@property
	def sv_err_mod(self) -> typing.List[bool]:
		'''Value of variable $SV_ERR_MOD'''
		return self._instance.SvErrMod

	@property
	def sv_err_clr(self) -> typing.List[bool]:
		'''Value of variable $SV_ERR_CLR'''
		return self._instance.SvErrClr

	@property
	def action(self) -> int:
		'''Value of variable $ACTION'''
		return self._instance.Action

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TorqctrlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
