import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FluiCfgVariableType as flui_cfg_variable_type

class FluiCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type FLUI_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def recurse(self) -> int:
		'''Value of variable $RECURSE'''
		return self._instance.Recurse

	@property
	def style(self) -> int:
		'''Value of variable $STYLE'''
		return self._instance.Style

	@property
	def edt_rcnt_si(self) -> int:
		'''Value of variable $EDT_RCNT_SI'''
		return self._instance.EdtRcntSi

	@property
	def tempint(self) -> typing.List[int]:
		'''Value of variable $TEMPINT'''
		return self._instance.Tempint

	@property
	def tempstr(self) -> typing.List[str]:
		'''Value of variable $TEMPSTR'''
		return self._instance.Tempstr

	@property
	def jog_coord(self) -> int:
		'''Value of variable $JOG_COORD'''
		return self._instance.JogCoord

	@property
	def ovrtext(self) -> str:
		'''Value of variable $OVRTEXT'''
		return self._instance.Ovrtext

	@property
	def shotemplate(self) -> bool:
		'''Value of variable $SHOTEMPLATE'''
		return self._instance.Shotemplate

	@property
	def assist_mode(self) -> int:
		'''Value of variable $ASSIST_MODE'''
		return self._instance.AssistMode

	@property
	def custom(self) -> int:
		'''Value of variable $CUSTOM'''
		return self._instance.Custom

	@property
	def dbg1(self) -> int:
		'''Value of variable $DBG_1'''
		return self._instance.Dbg1

	@property
	def dbg2(self) -> int:
		'''Value of variable $DBG_2'''
		return self._instance.Dbg2

	@property
	def dbg3(self) -> int:
		'''Value of variable $DBG_3'''
		return self._instance.Dbg3

	@property
	def dbg4(self) -> int:
		'''Value of variable $DBG_4'''
		return self._instance.Dbg4

	@property
	def dbg5(self) -> int:
		'''Value of variable $DBG_5'''
		return self._instance.Dbg5

	@property
	def force(self) -> bool:
		'''Value of variable $FORCE'''
		return self._instance.Force

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FluiCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
