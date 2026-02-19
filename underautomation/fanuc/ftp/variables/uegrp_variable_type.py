import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UegrpVariableType as uegrp_variable_type

class UegrpVariableType(GenericVariableType):
	'''Describes the Fanuc type UEGRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = uegrp_variable_type()
		else:
			self._instance = _internal

	@property
	def err_count(self) -> int:
		'''Value of variable $ERR_COUNT'''
		return self._instance.ErrCount

	@property
	def progmtn_flg(self) -> bool:
		'''Value of variable $PROGMTN_FLG'''
		return self._instance.ProgmtnFlg

	@property
	def curr_pos(self) -> typing.List[float]:
		'''Value of variable $CURR_POS'''
		return self._instance.CurrPos

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UegrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
