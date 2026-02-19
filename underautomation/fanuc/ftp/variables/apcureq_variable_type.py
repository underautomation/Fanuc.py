import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ApcureqVariableType as apcureq_variable_type

class ApcureqVariableType(GenericVariableType):
	'''Describes the Fanuc type APCUREQ_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = apcureq_variable_type()
		else:
			self._instance = _internal

	@property
	def softpart_id(self) -> int:
		'''Value of variable $SOFTPART_ID'''
		return self._instance.SoftpartId

	@property
	def total_eq(self) -> int:
		'''Value of variable $TOTAL_EQ'''
		return self._instance.TotalEq

	@property
	def cur_eqno(self) -> int:
		'''Value of variable $CUR_EQNO'''
		return self._instance.CurEqno

	@property
	def spi_index(self) -> int:
		'''Value of variable $SPI_INDEX'''
		return self._instance.SpiIndex

	@property
	def screen_name(self) -> str:
		'''Value of variable $SCREEN_NAME'''
		return self._instance.ScreenName

	@property
	def app_sign(self) -> str:
		'''Value of variable $APP_SIGN'''
		return self._instance.AppSign

	@property
	def app_proces0(self) -> int:
		'''Value of variable $APP_PROCES0'''
		return self._instance.AppProces0

	@property
	def app_proces1(self) -> int:
		'''Value of variable $APP_PROCES1'''
		return self._instance.AppProces1

	@property
	def topk_file(self) -> str:
		'''Value of variable $TOPK_FILE'''
		return self._instance.TopkFile

	@property
	def thky_file(self) -> str:
		'''Value of variable $THKY_FILE'''
		return self._instance.ThkyFile

	@property
	def pane_eqno(self) -> typing.List[int]:
		'''Value of variable $PANE_EQNO'''
		return self._instance.PaneEqno

	@property
	def dummy12(self) -> int:
		'''Value of variable $DUMMY12'''
		return self._instance.Dummy12

	@property
	def dummy13(self) -> int:
		'''Value of variable $DUMMY13'''
		return self._instance.Dummy13

	@property
	def dummy14(self) -> int:
		'''Value of variable $DUMMY14'''
		return self._instance.Dummy14

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ApcureqVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
