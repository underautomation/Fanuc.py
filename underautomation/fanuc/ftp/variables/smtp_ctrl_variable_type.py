import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SmtpCtrlVariableType as smtp_ctrl_variable_type

class SmtpCtrlVariableType(GenericVariableType):
	'''Describes the Fanuc type SMTP_CTRL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smtp_ctrl_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def server(self) -> str:
		'''Value of variable $SERVER'''
		return self._instance.Server

	@property
	def port(self) -> int:
		'''Value of variable $PORT'''
		return self._instance.Port

	@property
	def timeout(self) -> int:
		'''Value of variable $TIMEOUT'''
		return self._instance.Timeout

	@property
	def cc_addr(self) -> str:
		'''Value of variable $CC_ADDR'''
		return self._instance.CcAddr

	@property
	def from_addr(self) -> str:
		'''Value of variable $FROM_ADDR'''
		return self._instance.FromAddr

	@property
	def rt_addr(self) -> str:
		'''Value of variable $RT_ADDR'''
		return self._instance.RtAddr

	@property
	def post_dlvr(self) -> bool:
		'''Value of variable $POST_DLVR'''
		return self._instance.PostDlvr

	@property
	def spare(self) -> int:
		'''Value of variable $SPARE'''
		return self._instance.Spare

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SmtpCtrlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
