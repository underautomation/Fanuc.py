import typing
from underautomation.fanuc.ftp.variables.clhist_variable_type import ClhistVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FmsGrpVariableType as fms_grp_variable_type

class FmsGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fms_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def rem_life(self) -> typing.List[float]:
		return self._instance.RemLife
	@property
	def nt_life(self) -> typing.List[float]:
		return self._instance.NtLife
	@property
	def t_life(self) -> typing.List[float]:
		return self._instance.TLife
	@property
	def cldet_ang(self) -> typing.List[float]:
		return self._instance.CldetAng
	@property
	def nt_life0(self) -> typing.List[float]:
		return self._instance.NtLife0
	@property
	def t_life_temp(self) -> typing.List[float]:
		return self._instance.TLifeTemp
	@property
	def rem_life0(self) -> typing.List[float]:
		return self._instance.RemLife0
	@property
	def grp_cl_time(self) -> int:
		return self._instance.GrpClTime
	@property
	def pccomer_cnt(self) -> typing.List[int]:
		return self._instance.PccomerCnt
	@property
	def fb_comp_cnt(self) -> typing.List[int]:
		return self._instance.FbCompCnt
	@property
	def cmal_detect(self) -> typing.List[bool]:
		return self._instance.CmalDetect
	@property
	def cldet_pt(self) -> int:
		return self._instance.CldetPt
	@property
	def ps_dty_str(self) -> int:
		return self._instance.PsDtyStr
	@property
	def dty_str_t(self) -> int:
		return self._instance.DtyStrT
	@property
	def dty_end_t(self) -> int:
		return self._instance.DtyEndT
	@property
	def cldet_cnt(self) -> typing.List[int]:
		return self._instance.CldetCnt
	@property
	def clhist(self) -> typing.List[ClhistVariableType]:
		return [ClhistVariableType(x) for x in self._instance.Clhist]
	@property
	def t_life_ms(self) -> typing.List[int]:
		return self._instance.TLifeMs
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
