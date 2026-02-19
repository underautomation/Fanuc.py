import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TpvwvarVariableType as tpvwvar_variable_type

class TpvwvarVariableType(GenericVariableType):
	'''Describes the Fanuc type TPVWVAR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpvwvar_variable_type()
		else:
			self._instance = _internal

	@property
	def tpview_enb(self) -> bool:
		'''Value of variable $TPVIEW_ENB'''
		return self._instance.TpviewEnb

	@property
	def prev_rtn(self) -> bool:
		'''Value of variable $PREV_RTN'''
		return self._instance.PrevRtn

	@property
	def edit_rtn(self) -> bool:
		'''Value of variable $EDIT_RTN'''
		return self._instance.EditRtn

	@property
	def vshwrk(self) -> int:
		'''Value of variable $VSHWRK'''
		return self._instance.Vshwrk

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def display(self) -> int:
		'''Value of variable $DISPLAY'''
		return self._instance.Display

	@property
	def indent1(self) -> int:
		'''Value of variable $INDENT1'''
		return self._instance.Indent1

	@property
	def indent2(self) -> int:
		'''Value of variable $INDENT2'''
		return self._instance.Indent2

	@property
	def head1(self) -> str:
		'''Value of variable $HEAD1'''
		return self._instance.Head1

	@property
	def head2(self) -> str:
		'''Value of variable $HEAD2'''
		return self._instance.Head2

	@property
	def edit_key(self) -> int:
		'''Value of variable $EDIT_KEY'''
		return self._instance.EditKey

	@property
	def tcpspd_key(self) -> int:
		'''Value of variable $TCPSPD_KEY'''
		return self._instance.TcpspdKey

	@property
	def jmpcall_enb(self) -> bool:
		'''Value of variable $JMPCALL_ENB'''
		return self._instance.JmpcallEnb

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TpvwvarVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
