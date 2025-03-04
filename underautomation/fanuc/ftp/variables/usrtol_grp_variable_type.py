import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UsrtolGrpVariableType as usrtol_grp_variable_type

class UsrtolGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usrtol_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def dist_tol(self) -> float:
		return self._instance.DistTol
	@property
	def ornt_tol(self) -> float:
		return self._instance.OrntTol
	@property
	def raux_tol(self) -> float:
		return self._instance.RauxTol
	@property
	def taux_tol(self) -> float:
		return self._instance.TauxTol
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
