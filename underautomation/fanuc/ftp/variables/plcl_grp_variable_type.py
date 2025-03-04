import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlclGrpVariableType as plcl_grp_variable_type

class PlclGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plcl_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def calib_stat(self) -> int:
		return self._instance.CalibStat
	@property
	def trq_mgn(self) -> typing.List[float]:
		return self._instance.TrqMgn
	@property
	def link_m(self) -> typing.List[float]:
		return self._instance.LinkM
	@property
	def link_sx(self) -> typing.List[float]:
		return self._instance.LinkSx
	@property
	def link_sy(self) -> typing.List[float]:
		return self._instance.LinkSy
	@property
	def link_sz(self) -> typing.List[float]:
		return self._instance.LinkSz
	@property
	def link_ix(self) -> typing.List[float]:
		return self._instance.LinkIx
	@property
	def link_iy(self) -> typing.List[float]:
		return self._instance.LinkIy
	@property
	def link_iz(self) -> typing.List[float]:
		return self._instance.LinkIz
	@property
	def calib3a(self) -> int:
		return self._instance.Calib3a
	@property
	def tq_mgn3a(self) -> typing.List[float]:
		return self._instance.TqMgn3a
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
