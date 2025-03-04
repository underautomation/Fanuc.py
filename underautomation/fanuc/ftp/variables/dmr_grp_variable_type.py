import typing
from underautomation.fanuc.ftp.variables.dmr_shferr_variable_type import DmrShferrVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DmrGrpVariableType as dmr_grp_variable_type

class DmrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dmr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def master_done(self) -> bool:
		return self._instance.MasterDone
	@property
	def ot_minus(self) -> typing.List[bool]:
		return self._instance.OtMinus
	@property
	def ot_plus(self) -> typing.List[bool]:
		return self._instance.OtPlus
	@property
	def master_coun(self) -> typing.List[int]:
		return self._instance.MasterCoun
	@property
	def ref_done(self) -> bool:
		return self._instance.RefDone
	@property
	def ref_pos(self) -> typing.List[float]:
		return self._instance.RefPos
	@property
	def ref_count(self) -> typing.List[int]:
		return self._instance.RefCount
	@property
	def bcklsh_sign(self) -> typing.List[bool]:
		return self._instance.BcklshSign
	@property
	def eachmst_don(self) -> typing.List[int]:
		return self._instance.EachmstDon
	@property
	def spc_count(self) -> typing.List[int]:
		return self._instance.SpcCount
	@property
	def spc_move(self) -> typing.List[bool]:
		return self._instance.SpcMove
	@property
	def adapt_iner(self) -> typing.List[int]:
		return self._instance.AdaptIner
	@property
	def adapt_fric(self) -> typing.List[int]:
		return self._instance.AdaptFric
	@property
	def adapt_col_p(self) -> typing.List[int]:
		return self._instance.AdaptColP
	@property
	def adapt_col_m(self) -> typing.List[int]:
		return self._instance.AdaptColM
	@property
	def adapt_grav(self) -> typing.List[int]:
		return self._instance.AdaptGrav
	@property
	def spc_st_hist(self) -> typing.List[int]:
		return self._instance.SpcStHist
	@property
	def dsp_st_hist(self) -> typing.List[int]:
		return self._instance.DspStHist
	@property
	def shift_error(self) -> int:
		return self._instance.ShiftError
	@property
	def spc_cnt_his(self) -> typing.List[int]:
		return self._instance.SpcCntHis
	@property
	def mch_pls_his(self) -> typing.List[int]:
		return self._instance.MchPlsHis
	@property
	def arm_param(self) -> typing.List[float]:
		return self._instance.ArmParam
	@property
	def master_ang(self) -> float:
		return self._instance.MasterAng
	@property
	def dsp_st_his2(self) -> typing.List[int]:
		return self._instance.DspStHis2
	@property
	def cldet_cnt(self) -> typing.List[int]:
		return self._instance.CldetCnt
	@property
	def calib_mode(self) -> int:
		return self._instance.CalibMode
	@property
	def gear_param(self) -> typing.List[float]:
		return self._instance.GearParam
	@property
	def gear_param2(self) -> typing.List[float]:
		return self._instance.GearParam2
	@property
	def spring_pam(self) -> typing.List[float]:
		return self._instance.SpringPam
	@property
	def grav_mast(self) -> int:
		return self._instance.GravMast
	@property
	def rel_shf_err(self) -> typing.List[DmrShferrVariableType]:
		return [DmrShferrVariableType(x) for x in self._instance.RelShfErr]
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
