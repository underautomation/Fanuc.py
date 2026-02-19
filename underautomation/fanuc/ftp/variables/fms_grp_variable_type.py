import typing
from underautomation.fanuc.ftp.variables.clhist_variable_type import ClhistVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FmsGrpVariableType as fms_grp_variable_type

class FmsGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type FMS_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fms_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def rem_life(self) -> typing.List[float]:
		'''Value of variable $REM_LIFE'''
		return self._instance.RemLife

	@property
	def nt_life(self) -> typing.List[float]:
		'''Value of variable $NT_LIFE'''
		return self._instance.NtLife

	@property
	def t_life(self) -> typing.List[float]:
		'''Value of variable $T_LIFE'''
		return self._instance.TLife

	@property
	def cldet_ang(self) -> typing.List[float]:
		'''Value of variable $CLDET_ANG'''
		return self._instance.CldetAng

	@property
	def nt_life0(self) -> typing.List[float]:
		'''Value of variable $NT_LIFE_0'''
		return self._instance.NtLife0

	@property
	def t_life_temp(self) -> typing.List[float]:
		'''Value of variable $T_LIFE_TEMP'''
		return self._instance.TLifeTemp

	@property
	def rem_life0(self) -> typing.List[float]:
		'''Value of variable $REM_LIFE_0'''
		return self._instance.RemLife0

	@property
	def grp_cl_time(self) -> int:
		'''Value of variable $GRP_CL_TIME'''
		return self._instance.GrpClTime

	@property
	def pccomer_cnt(self) -> typing.List[int]:
		'''Value of variable $PCCOMER_CNT'''
		return self._instance.PccomerCnt

	@property
	def fb_comp_cnt(self) -> typing.List[int]:
		'''Value of variable $FB_COMP_CNT'''
		return self._instance.FbCompCnt

	@property
	def cmal_detect(self) -> typing.List[bool]:
		'''Value of variable $CMAL_DETECT'''
		return self._instance.CmalDetect

	@property
	def cldet_pt(self) -> int:
		'''Value of variable $CLDET_PT'''
		return self._instance.CldetPt

	@property
	def ps_dty_str(self) -> int:
		'''Value of variable $PS_DTY_STR_'''
		return self._instance.PsDtyStr

	@property
	def dty_str_t(self) -> int:
		'''Value of variable $DTY_STR_T'''
		return self._instance.DtyStrT

	@property
	def dty_end_t(self) -> int:
		'''Value of variable $DTY_END_T'''
		return self._instance.DtyEndT

	@property
	def cldet_cnt(self) -> typing.List[int]:
		'''Value of variable $CLDET_CNT'''
		return self._instance.CldetCnt

	@property
	def clhist(self) -> typing.List[ClhistVariableType]:
		'''Value of variable $CLHIST'''
		return [ClhistVariableType(x) for x in self._instance.Clhist]

	@property
	def t_life_ms(self) -> typing.List[int]:
		'''Value of variable $T_LIFE_MS'''
		return self._instance.TLifeMs

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FmsGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
