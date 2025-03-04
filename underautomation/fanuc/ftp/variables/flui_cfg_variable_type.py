import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FluiCfgVariableType as flui_cfg_variable_type

class FluiCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = flui_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def recurse(self) -> int:
		return self._instance.Recurse
	@property
	def style(self) -> int:
		return self._instance.Style
	@property
	def edt_rcnt_si(self) -> int:
		return self._instance.EdtRcntSi
	@property
	def tempint(self) -> typing.List[int]:
		return self._instance.Tempint
	@property
	def tempstr(self) -> typing.List[str]:
		return self._instance.Tempstr
	@property
	def jog_coord(self) -> int:
		return self._instance.JogCoord
	@property
	def ovrtext(self) -> str:
		return self._instance.Ovrtext
	@property
	def shotemplate(self) -> bool:
		return self._instance.Shotemplate
	@property
	def assist_mode(self) -> int:
		return self._instance.AssistMode
	@property
	def custom(self) -> int:
		return self._instance.Custom
	@property
	def dbg1(self) -> int:
		return self._instance.Dbg1
	@property
	def dbg2(self) -> int:
		return self._instance.Dbg2
	@property
	def dbg3(self) -> int:
		return self._instance.Dbg3
	@property
	def dbg4(self) -> int:
		return self._instance.Dbg4
	@property
	def dbg5(self) -> int:
		return self._instance.Dbg5
	@property
	def force(self) -> bool:
		return self._instance.Force
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
