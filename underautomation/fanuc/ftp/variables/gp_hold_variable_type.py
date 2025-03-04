import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GpHoldVariableType as gp_hold_variable_type

class GpHoldVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gp_hold_variable_type()
		else:
			self._instance = _internal
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def gp_msk(self) -> int:
		return self._instance.GpMsk
	@property
	def space_num(self) -> int:
		return self._instance.SpaceNum
	@property
	def cspace_num(self) -> int:
		return self._instance.CspaceNum
	@property
	def req_grp(self) -> int:
		return self._instance.ReqGrp
	@property
	def ps_rate(self) -> int:
		return self._instance.PsRate
	@property
	def rate(self) -> typing.List[float]:
		return self._instance.Rate
	@property
	def int_pos(self) -> typing.List[float]:
		return self._instance.IntPos
	@property
	def act_pos(self) -> typing.List[float]:
		return self._instance.ActPos
	@property
	def prd_pos(self) -> typing.List[float]:
		return self._instance.PrdPos
	@property
	def s1(self) -> int:
		return self._instance.S1
	@property
	def s2(self) -> int:
		return self._instance.S2
	@property
	def s3(self) -> int:
		return self._instance.S3
	@property
	def s4(self) -> int:
		return self._instance.S4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
