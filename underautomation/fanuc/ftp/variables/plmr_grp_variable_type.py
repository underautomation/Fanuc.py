import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlmrGrpVariableType as plmr_grp_variable_type

class PlmrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plmr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def pyld_enb(self) -> bool:
		return self._instance.PyldEnb
	@property
	def wmr_enb(self) -> bool:
		return self._instance.WmrEnb
	@property
	def angle(self) -> float:
		return self._instance.Angle
	@property
	def plmr_aa(self) -> float:
		return self._instance.PlmrAa
	@property
	def plmr_bb(self) -> float:
		return self._instance.PlmrBb
	@property
	def plmr_cc(self) -> float:
		return self._instance.PlmrCc
	@property
	def plmr_dd(self) -> float:
		return self._instance.PlmrDd
	@property
	def plst_ang(self) -> typing.List[float]:
		return self._instance.PlstAng
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def max_xy_loc(self) -> float:
		return self._instance.MaxXyLoc
	@property
	def max_z_loc(self) -> float:
		return self._instance.MaxZLoc
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
