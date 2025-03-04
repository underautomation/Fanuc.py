import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlimGrpVariableType as plim_grp_variable_type

class PlimGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plim_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def max_pyld(self) -> float:
		return self._instance.MaxPyld
	@property
	def axisinertia(self) -> typing.List[int]:
		return self._instance.Axisinertia
	@property
	def axisinertil(self) -> typing.List[int]:
		return self._instance.Axisinertil
	@property
	def axismoment(self) -> typing.List[int]:
		return self._instance.Axismoment
	@property
	def axis_im_scl(self) -> int:
		return self._instance.AxisImScl
	@property
	def lim_wt_scl(self) -> float:
		return self._instance.LimWtScl
	@property
	def lim_inr_scl(self) -> typing.List[float]:
		return self._instance.LimInrScl
	@property
	def lim_mnt_scl(self) -> typing.List[float]:
		return self._instance.LimMntScl
	@property
	def lim_cl_scl(self) -> typing.List[float]:
		return self._instance.LimClScl
	@property
	def pld_mode(self) -> int:
		return self._instance.PldMode
	@property
	def dummy11(self) -> int:
		return self._instance.Dummy11
	@property
	def dummy12(self) -> int:
		return self._instance.Dummy12
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
