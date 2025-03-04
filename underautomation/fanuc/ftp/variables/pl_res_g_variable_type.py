import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlResGVariableType as pl_res_g_variable_type

class PlResGVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pl_res_g_variable_type()
		else:
			self._instance = _internal
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def savmoment4(self) -> float:
		return self._instance.Savmoment4
	@property
	def savmoment5(self) -> float:
		return self._instance.Savmoment5
	@property
	def savmoment6(self) -> float:
		return self._instance.Savmoment6
	@property
	def savinertia4(self) -> float:
		return self._instance.Savinertia4
	@property
	def savinertia5(self) -> float:
		return self._instance.Savinertia5
	@property
	def savinertia6(self) -> float:
		return self._instance.Savinertia6
	@property
	def est_result(self) -> int:
		return self._instance.EstResult
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
