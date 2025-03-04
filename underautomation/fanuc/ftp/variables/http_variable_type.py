import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HttpVariableType as http_variable_type

class HttpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def enab_diagtp(self) -> int:
		return self._instance.EnabDiagtp
	@property
	def enab_spart(self) -> int:
		return self._instance.EnabSpart
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def krl_timout(self) -> int:
		return self._instance.KrlTimout
	@property
	def hitcount(self) -> int:
		return self._instance.Hitcount
	@property
	def bg_color(self) -> str:
		return self._instance.BgColor
	@property
	def enab_templ(self) -> int:
		return self._instance.EnabTempl
	@property
	def template(self) -> str:
		return self._instance.Template
	@property
	def comment(self) -> str:
		return self._instance.Comment
	@property
	def rss_inum(self) -> int:
		return self._instance.RssInum
	@property
	def jquery_flag(self) -> int:
		return self._instance.JqueryFlag
	@property
	def enb_websock(self) -> int:
		return self._instance.EnbWebsock
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
