import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import T2modeLimVariableType as t2mode_lim_variable_type

class T2modeLimVariableType(GenericVariableType):
	'''Describes the Fanuc type T2MODE_LIM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = t2mode_lim_variable_type()
		else:
			self._instance = _internal

	@property
	def jog_ope(self) -> bool:
		'''Value of variable $JOG_OPE'''
		return self._instance.JogOpe

	@property
	def tpp_edit(self) -> bool:
		'''Value of variable $TPP_EDIT'''
		return self._instance.TppEdit

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, T2modeLimVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
