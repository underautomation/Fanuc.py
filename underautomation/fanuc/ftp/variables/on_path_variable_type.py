import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import OnPathVariableType as on_path_variable_type

class OnPathVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = on_path_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def status(self) -> bool:
		return self._instance.Status
	@property
	def dist_diff(self) -> float:
		return self._instance.DistDiff
	@property
	def ornt_diff(self) -> float:
		return self._instance.OrntDiff
	@property
	def dist_rec(self) -> float:
		return self._instance.DistRec
	@property
	def ornt_rec(self) -> float:
		return self._instance.OrntRec
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
