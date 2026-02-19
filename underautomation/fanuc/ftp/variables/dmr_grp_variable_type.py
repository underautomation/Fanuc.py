import typing
from underautomation.fanuc.ftp.variables.dmr_shferr_variable_type import DmrShferrVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DmrGrpVariableType as dmr_grp_variable_type

class DmrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type DMR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dmr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def master_done(self) -> bool:
		'''Value of variable $MASTER_DONE'''
		return self._instance.MasterDone

	@property
	def ot_minus(self) -> typing.List[bool]:
		'''Value of variable $OT_MINUS'''
		return self._instance.OtMinus

	@property
	def ot_plus(self) -> typing.List[bool]:
		'''Value of variable $OT_PLUS'''
		return self._instance.OtPlus

	@property
	def master_coun(self) -> typing.List[int]:
		'''Value of variable $MASTER_COUN'''
		return self._instance.MasterCoun

	@property
	def ref_done(self) -> bool:
		'''Value of variable $REF_DONE'''
		return self._instance.RefDone

	@property
	def ref_pos(self) -> typing.List[float]:
		'''Value of variable $REF_POS'''
		return self._instance.RefPos

	@property
	def ref_count(self) -> typing.List[int]:
		'''Value of variable $REF_COUNT'''
		return self._instance.RefCount

	@property
	def bcklsh_sign(self) -> typing.List[bool]:
		'''Value of variable $BCKLSH_SIGN'''
		return self._instance.BcklshSign

	@property
	def eachmst_don(self) -> typing.List[int]:
		'''Value of variable $EACHMST_DON'''
		return self._instance.EachmstDon

	@property
	def spc_count(self) -> typing.List[int]:
		'''Value of variable $SPC_COUNT'''
		return self._instance.SpcCount

	@property
	def spc_move(self) -> typing.List[bool]:
		'''Value of variable $SPC_MOVE'''
		return self._instance.SpcMove

	@property
	def adapt_iner(self) -> typing.List[int]:
		'''Value of variable $ADAPT_INER'''
		return self._instance.AdaptIner

	@property
	def adapt_fric(self) -> typing.List[int]:
		'''Value of variable $ADAPT_FRIC'''
		return self._instance.AdaptFric

	@property
	def adapt_col_p(self) -> typing.List[int]:
		'''Value of variable $ADAPT_COL_P'''
		return self._instance.AdaptColP

	@property
	def adapt_col_m(self) -> typing.List[int]:
		'''Value of variable $ADAPT_COL_M'''
		return self._instance.AdaptColM

	@property
	def adapt_grav(self) -> typing.List[int]:
		'''Value of variable $ADAPT_GRAV'''
		return self._instance.AdaptGrav

	@property
	def spc_st_hist(self) -> typing.List[int]:
		'''Value of variable $SPC_ST_HIST'''
		return self._instance.SpcStHist

	@property
	def dsp_st_hist(self) -> typing.List[int]:
		'''Value of variable $DSP_ST_HIST'''
		return self._instance.DspStHist

	@property
	def shift_error(self) -> int:
		'''Value of variable $SHIFT_ERROR'''
		return self._instance.ShiftError

	@property
	def spc_cnt_his(self) -> typing.List[int]:
		'''Value of variable $SPC_CNT_HIS'''
		return self._instance.SpcCntHis

	@property
	def mch_pls_his(self) -> typing.List[int]:
		'''Value of variable $MCH_PLS_HIS'''
		return self._instance.MchPlsHis

	@property
	def arm_param(self) -> typing.List[float]:
		'''Value of variable $ARM_PARAM'''
		return self._instance.ArmParam

	@property
	def master_ang(self) -> float:
		'''Value of variable $MASTER_ANG'''
		return self._instance.MasterAng

	@property
	def dsp_st_his2(self) -> typing.List[int]:
		'''Value of variable $DSP_ST_HIS2'''
		return self._instance.DspStHis2

	@property
	def cldet_cnt(self) -> typing.List[int]:
		'''Value of variable $CLDET_CNT'''
		return self._instance.CldetCnt

	@property
	def calib_mode(self) -> int:
		'''Value of variable $CALIB_MODE'''
		return self._instance.CalibMode

	@property
	def gear_param(self) -> typing.List[float]:
		'''Value of variable $GEAR_PARAM'''
		return self._instance.GearParam

	@property
	def gear_param2(self) -> typing.List[float]:
		'''Value of variable $GEAR_PARAM2'''
		return self._instance.GearParam2

	@property
	def spring_pam(self) -> typing.List[float]:
		'''Value of variable $SPRING_PAM'''
		return self._instance.SpringPam

	@property
	def grav_mast(self) -> int:
		'''Value of variable $GRAV_MAST'''
		return self._instance.GravMast

	@property
	def rel_shf_err(self) -> typing.List[DmrShferrVariableType]:
		'''Value of variable $REL_SHF_ERR'''
		return [DmrShferrVariableType(x) for x in self._instance.RelShfErr]

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DmrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
