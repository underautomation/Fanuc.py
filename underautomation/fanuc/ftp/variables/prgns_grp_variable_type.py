import typing
from underautomation.fanuc.ftp.variables.prgns_elem_variable_type import PrgnsElemVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsGrpVariableType as prgns_grp_variable_type

class PrgnsGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def elem(self) -> typing.List[PrgnsElemVariableType]:
		return [PrgnsElemVariableType(x) for x in self._instance.Elem]
	@property
	def min_ang(self) -> typing.List[float]:
		return self._instance.MinAng
	@property
	def max_ang(self) -> typing.List[float]:
		return self._instance.MaxAng
	@property
	def base_ang(self) -> typing.List[float]:
		return self._instance.BaseAng
	@property
	def last_mod(self) -> typing.List[int]:
		return self._instance.LastMod
	@property
	def base_mod(self) -> typing.List[int]:
		return self._instance.BaseMod
	@property
	def payload(self) -> int:
		return self._instance.Payload
	@property
	def warn_dout(self) -> int:
		return self._instance.WarnDout
	@property
	def warn_din(self) -> int:
		return self._instance.WarnDin
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
