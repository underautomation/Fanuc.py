import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlResGVariableType as pl_res_g_variable_type

class PlResGVariableType(GenericVariableType):
	'''Describes the Fanuc type PL_RES_G_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pl_res_g_variable_type()
		else:
			self._instance = _internal

	@property
	def payload(self) -> float:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def savmoment4(self) -> float:
		'''Value of variable $SAVMOMENT4'''
		return self._instance.Savmoment4

	@property
	def savmoment5(self) -> float:
		'''Value of variable $SAVMOMENT5'''
		return self._instance.Savmoment5

	@property
	def savmoment6(self) -> float:
		'''Value of variable $SAVMOMENT6'''
		return self._instance.Savmoment6

	@property
	def savinertia4(self) -> float:
		'''Value of variable $SAVINERTIA4'''
		return self._instance.Savinertia4

	@property
	def savinertia5(self) -> float:
		'''Value of variable $SAVINERTIA5'''
		return self._instance.Savinertia5

	@property
	def savinertia6(self) -> float:
		'''Value of variable $SAVINERTIA6'''
		return self._instance.Savinertia6

	@property
	def est_result(self) -> int:
		'''Value of variable $EST_RESULT'''
		return self._instance.EstResult

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlResGVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
