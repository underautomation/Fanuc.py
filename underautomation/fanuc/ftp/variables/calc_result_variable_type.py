import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CalcResultVariableType as calc_result_variable_type

class CalcResultVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = calc_result_variable_type()
		else:
			self._instance = _internal
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def payload1(self) -> float:
		return self._instance.Payload1
	@property
	def payload2(self) -> float:
		return self._instance.Payload2
	@property
	def pld_j3arm(self) -> float:
		return self._instance.PldJ3arm
	@property
	def pld_j3arm1(self) -> float:
		return self._instance.PldJ3arm1
	@property
	def pld_j3arm2(self) -> float:
		return self._instance.PldJ3arm2
	@property
	def inertia4(self) -> float:
		return self._instance.Inertia4
	@property
	def inertia5(self) -> float:
		return self._instance.Inertia5
	@property
	def inertia6(self) -> float:
		return self._instance.Inertia6
	@property
	def moment4(self) -> float:
		return self._instance.Moment4
	@property
	def moment5(self) -> float:
		return self._instance.Moment5
	@property
	def moment6(self) -> float:
		return self._instance.Moment6
	@property
	def comb_load4(self) -> float:
		return self._instance.CombLoad4
	@property
	def comb_load5(self) -> float:
		return self._instance.CombLoad5
	@property
	def comb_load6(self) -> float:
		return self._instance.CombLoad6
	@property
	def pub_inrt4(self) -> float:
		return self._instance.PubInrt4
	@property
	def pub_inrt5(self) -> float:
		return self._instance.PubInrt5
	@property
	def pub_inrt6(self) -> float:
		return self._instance.PubInrt6
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
