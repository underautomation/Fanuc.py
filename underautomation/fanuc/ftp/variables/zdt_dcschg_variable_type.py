import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ZdtDcschgVariableType as zdt_dcschg_variable_type

class ZdtDcschgVariableType(GenericVariableType):
	'''Describes the Fanuc type ZDT_DCSCHG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zdt_dcschg_variable_type()
		else:
			self._instance = _internal

	@property
	def dcschg_enb(self) -> bool:
		'''Value of variable $DCSCHG_ENB'''
		return self._instance.DcschgEnb

	@property
	def login_idx(self) -> int:
		'''Value of variable $LOGIN_IDX'''
		return self._instance.LoginIdx

	@property
	def last_signat(self) -> int:
		'''Value of variable $LAST_SIGNAT'''
		return self._instance.LastSignat

	@property
	def lst_time(self) -> int:
		'''Value of variable $LST_TIME'''
		return self._instance.LstTime

	@property
	def dcs_funct(self) -> int:
		'''Value of variable $DCS_FUNCT'''
		return self._instance.DcsFunct

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ZdtDcschgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
