import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ResumeOfstVariableType as resume_ofst_variable_type

class ResumeOfstVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = resume_ofst_variable_type()
		else:
			self._instance = _internal
	@property
	def ro_enable(self) -> bool:
		return self._instance.RoEnable
	@property
	def ro_max_itp(self) -> int:
		return self._instance.RoMaxItp
	@property
	def ro_nom_dist(self) -> float:
		return self._instance.RoNomDist
	@property
	def ro_nom_spd(self) -> float:
		return self._instance.RoNomSpd
	@property
	def ro_mode_sw(self) -> int:
		return self._instance.RoModeSw
	@property
	def ro_tune_pam(self) -> float:
		return self._instance.RoTunePam
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
