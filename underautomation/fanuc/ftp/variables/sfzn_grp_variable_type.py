import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SfznGrpVariableType as sfzn_grp_variable_type

class SfznGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sfzn_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def min_ovrd(self) -> float:
		return self._instance.MinOvrd
	@property
	def int_ang(self) -> float:
		return self._instance.IntAng
	@property
	def min_ang(self) -> float:
		return self._instance.MinAng
	@property
	def face_spd(self) -> float:
		return self._instance.FaceSpd
	@property
	def safe_spd(self) -> float:
		return self._instance.SafeSpd
	@property
	def mixed_spd(self) -> float:
		return self._instance.MixedSpd
	@property
	def mixed_ang(self) -> float:
		return self._instance.MixedAng
	@property
	def min_dist(self) -> float:
		return self._instance.MinDist
	@property
	def rob_name(self) -> str:
		return self._instance.RobName
	@property
	def need_app(self) -> int:
		return self._instance.NeedApp
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
