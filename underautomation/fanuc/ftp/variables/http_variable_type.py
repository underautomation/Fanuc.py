import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import HttpVariableType as http_variable_type

class HttpVariableType(GenericVariableType):
	'''Describes the Fanuc type HTTP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = http_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> int:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def enab_diagtp(self) -> int:
		'''Value of variable $ENAB_DIAGTP'''
		return self._instance.EnabDiagtp

	@property
	def enab_spart(self) -> int:
		'''Value of variable $ENAB_SPART'''
		return self._instance.EnabSpart

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def krl_timout(self) -> int:
		'''Value of variable $KRL_TIMOUT'''
		return self._instance.KrlTimout

	@property
	def hitcount(self) -> int:
		'''Value of variable $HITCOUNT'''
		return self._instance.Hitcount

	@property
	def bg_color(self) -> str:
		'''Value of variable $BG_COLOR'''
		return self._instance.BgColor

	@property
	def enab_templ(self) -> int:
		'''Value of variable $ENAB_TEMPL'''
		return self._instance.EnabTempl

	@property
	def template(self) -> str:
		'''Value of variable $TEMPLATE'''
		return self._instance.Template

	@property
	def comment(self) -> str:
		'''Value of variable $COMMENT'''
		return self._instance.Comment

	@property
	def rss_inum(self) -> int:
		'''Value of variable $RSS_INUM'''
		return self._instance.RssInum

	@property
	def jquery_flag(self) -> int:
		'''Value of variable $JQUERY_FLAG'''
		return self._instance.JqueryFlag

	@property
	def enb_websock(self) -> int:
		'''Value of variable $ENB_WEBSOCK'''
		return self._instance.EnbWebsock

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, HttpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
