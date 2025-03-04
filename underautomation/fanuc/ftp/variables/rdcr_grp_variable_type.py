import typing
from underautomation.fanuc.ftp.variables.j2red_variable_type import J2redVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RdcrGrpVariableType as rdcr_grp_variable_type

class RdcrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rdcr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def rmax_torque(self) -> typing.List[float]:
		return self._instance.RmaxTorque
	@property
	def rmin_torque(self) -> typing.List[float]:
		return self._instance.RminTorque
	@property
	def thres_torq(self) -> typing.List[float]:
		return self._instance.ThresTorq
	@property
	def rgear_ratio(self) -> typing.List[float]:
		return self._instance.RgearRatio
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def reserve(self) -> typing.List[float]:
		return self._instance.Reserve
	@property
	def spc_itp(self) -> int:
		return self._instance.SpcItp
	@property
	def num_exd(self) -> int:
		return self._instance.NumExd
	@property
	def j2th2nd(self) -> float:
		return self._instance.J2th2nd
	@property
	def j2red(self) -> typing.List[J2redVariableType]:
		return [J2redVariableType(x) for x in self._instance.J2red]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
