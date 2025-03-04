import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlidCfgVariableType as plid_cfg_variable_type

class PlidCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def comp_switch(self) -> int:
		return self._instance.CompSwitch
	@property
	def est_wo_mass(self) -> bool:
		return self._instance.EstWoMass
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
