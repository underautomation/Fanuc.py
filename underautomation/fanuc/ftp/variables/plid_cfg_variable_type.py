import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlidCfgVariableType as plid_cfg_variable_type

class PlidCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type PLID_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def comp_switch(self) -> int:
		'''Value of variable $COMP_SWITCH'''
		return self._instance.CompSwitch

	@property
	def est_wo_mass(self) -> bool:
		'''Value of variable $EST_WO_MASS'''
		return self._instance.EstWoMass

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlidCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
