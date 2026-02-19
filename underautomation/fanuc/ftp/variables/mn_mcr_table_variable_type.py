import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrTableVariableType as mn_mcr_table_variable_type

class MnMcrTableVariableType(GenericVariableType):
	'''Describes the Fanuc type MN_MCR_TABLE'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_table_variable_type()
		else:
			self._instance = _internal

	@property
	def macro_name(self) -> str:
		'''Value of variable $MACRO_NAME'''
		return self._instance.MacroName

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def ept_index(self) -> int:
		'''Value of variable $EPT_INDEX'''
		return self._instance.EptIndex

	@property
	def open_id(self) -> int:
		'''Value of variable $OPEN_ID'''
		return self._instance.OpenId

	@property
	def assign_type(self) -> int:
		'''Value of variable $ASSIGN_TYPE'''
		return self._instance.AssignType

	@property
	def assign_id(self) -> int:
		'''Value of variable $ASSIGN_ID'''
		return self._instance.AssignId

	@property
	def mon_no(self) -> int:
		'''Value of variable $MON_NO'''
		return self._instance.MonNo

	@property
	def prev_subtyp(self) -> int:
		'''Value of variable $PREV_SUBTYP'''
		return self._instance.PrevSubtyp

	@property
	def user_work(self) -> int:
		'''Value of variable $USER_WORK'''
		return self._instance.UserWork

	@property
	def sys_lev_msk(self) -> int:
		'''Value of variable $SYS_LEV_MSK'''
		return self._instance.SysLevMsk

	@property
	def mcr_rtn(self) -> int:
		'''Value of variable $MCR_RTN'''
		return self._instance.McrRtn

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MnMcrTableVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
