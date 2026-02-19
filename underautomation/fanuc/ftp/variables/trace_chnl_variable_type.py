import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TraceChnlVariableType as trace_chnl_variable_type

class TraceChnlVariableType(GenericVariableType):
	'''Describes the Fanuc type TRACE_CHNL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = trace_chnl_variable_type()
		else:
			self._instance = _internal

	@property
	def item_num(self) -> int:
		'''Value of variable $ITEM_NUM'''
		return self._instance.ItemNum

	@property
	def tcp_gp_num(self) -> int:
		'''Value of variable $TCP_GP_NUM'''
		return self._instance.TcpGpNum

	@property
	def visible(self) -> bool:
		'''Value of variable $VISIBLE'''
		return self._instance.Visible

	@property
	def style(self) -> int:
		'''Value of variable $STYLE'''
		return self._instance.Style

	@property
	def color(self) -> int:
		'''Value of variable $COLOR'''
		return self._instance.Color

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TraceChnlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
