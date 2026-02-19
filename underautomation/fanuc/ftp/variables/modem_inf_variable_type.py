import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ModemInfVariableType as modem_inf_variable_type

class ModemInfVariableType(GenericVariableType):
	'''Describes the Fanuc type MODEM_INF_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = modem_inf_variable_type()
		else:
			self._instance = _internal

	@property
	def mdm_init(self) -> str:
		'''Value of variable $MDM_INIT'''
		return self._instance.MdmInit

	@property
	def mdm_init1(self) -> str:
		'''Value of variable $MDM_INIT1'''
		return self._instance.MdmInit1

	@property
	def mdm_reset(self) -> str:
		'''Value of variable $MDM_RESET'''
		return self._instance.MdmReset

	@property
	def mdm_hangup(self) -> str:
		'''Value of variable $MDM_HANGUP'''
		return self._instance.MdmHangup

	@property
	def mdm_dial(self) -> str:
		'''Value of variable $MDM_DIAL'''
		return self._instance.MdmDial

	@property
	def mdm_answer(self) -> str:
		'''Value of variable $MDM_ANSWER'''
		return self._instance.MdmAnswer

	@property
	def mdm_status(self) -> str:
		'''Value of variable $MDM_STATUS'''
		return self._instance.MdmStatus

	@property
	def mdm_ident(self) -> str:
		'''Value of variable $MDM_IDENT'''
		return self._instance.MdmIdent

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ModemInfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
