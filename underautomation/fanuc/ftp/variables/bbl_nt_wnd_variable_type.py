import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import BblNtWndVariableType as bbl_nt_wnd_variable_type

class BblNtWndVariableType(GenericVariableType):
	'''Describes the Fanuc type BBL_NT_WND_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bbl_nt_wnd_variable_type()
		else:
			self._instance = _internal

	@property
	def wnd_top(self) -> int:
		'''Value of variable $WND_TOP'''
		return self._instance.WndTop

	@property
	def wnd_left(self) -> int:
		'''Value of variable $WND_LEFT'''
		return self._instance.WndLeft

	@property
	def wnd_bottom(self) -> int:
		'''Value of variable $WND_BOTTOM'''
		return self._instance.WndBottom

	@property
	def wnd_right(self) -> int:
		'''Value of variable $WND_RIGHT'''
		return self._instance.WndRight

	@property
	def brdr_clr(self) -> int:
		'''Value of variable $BRDR_CLR'''
		return self._instance.BrdrClr

	@property
	def bckgrnd_clr(self) -> int:
		'''Value of variable $BCKGRND_CLR'''
		return self._instance.BckgrndClr

	@property
	def text_clr(self) -> int:
		'''Value of variable $TEXT_CLR'''
		return self._instance.TextClr

	@property
	def brdr_width(self) -> int:
		'''Value of variable $BRDR_WIDTH'''
		return self._instance.BrdrWidth

	@property
	def disptime(self) -> int:
		'''Value of variable $DISPTIME'''
		return self._instance.Disptime

	@property
	def flags(self) -> int:
		'''Value of variable $FLAGS'''
		return self._instance.Flags

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BblNtWndVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
