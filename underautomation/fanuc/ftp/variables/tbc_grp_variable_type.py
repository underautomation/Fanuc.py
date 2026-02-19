import typing
from underautomation.fanuc.ftp.variables.tbcparam_variable_type import TbcparamVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbcGrpVariableType as tbc_grp_variable_type

class TbcGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TBC_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbc_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def tbc_accel1(self) -> int:
		'''Value of variable $TBC_ACCEL1'''
		return self._instance.TbcAccel1

	@property
	def tbc_accel2(self) -> int:
		'''Value of variable $TBC_ACCEL2'''
		return self._instance.TbcAccel2

	@property
	def tbc_path1(self) -> int:
		'''Value of variable $TBC_PATH1'''
		return self._instance.TbcPath1

	@property
	def tbc_path2(self) -> int:
		'''Value of variable $TBC_PATH2'''
		return self._instance.TbcPath2

	@property
	def path_ratio(self) -> float:
		'''Value of variable $PATH_RATIO'''
		return self._instance.PathRatio

	@property
	def tbc_param(self) -> typing.List[TbcparamVariableType]:
		'''Value of variable $TBC_PARAM'''
		return [TbcparamVariableType(x) for x in self._instance.TbcParam]

	@property
	def cnt_scale(self) -> float:
		'''Value of variable $CNT_SCALE'''
		return self._instance.CntScale

	@property
	def shortmo_scl(self) -> float:
		'''Value of variable $SHORTMO_SCL'''
		return self._instance.ShortmoScl

	@property
	def min_acc_uca(self) -> int:
		'''Value of variable $MIN_ACC_UCA'''
		return self._instance.MinAccUca

	@property
	def min_cat_uma(self) -> int:
		'''Value of variable $MIN_CAT_UMA'''
		return self._instance.MinCatUma

	@property
	def min_cyc_id(self) -> str:
		'''Value of variable $MIN_CYC_ID'''
		return self._instance.MinCycId

	@property
	def min_c_id_e1(self) -> str:
		'''Value of variable $MIN_C_ID_E1'''
		return self._instance.MinCIdE1

	@property
	def min_c_id_e2(self) -> str:
		'''Value of variable $MIN_C_ID_E2'''
		return self._instance.MinCIdE2

	@property
	def min_c_id_e3(self) -> str:
		'''Value of variable $MIN_C_ID_E3'''
		return self._instance.MinCIdE3

	@property
	def payload_mgn(self) -> float:
		'''Value of variable $PAYLOAD_MGN'''
		return self._instance.PayloadMgn

	@property
	def j2l_upr_ang(self) -> float:
		'''Value of variable $J2L_UPR_ANG'''
		return self._instance.J2lUprAng

	@property
	def j2l_lwr_ang(self) -> float:
		'''Value of variable $J2L_LWR_ANG'''
		return self._instance.J2lLwrAng

	@property
	def j2l_upr_mgn(self) -> float:
		'''Value of variable $J2L_UPR_MGN'''
		return self._instance.J2lUprMgn

	@property
	def j2l_lwr_mgn(self) -> float:
		'''Value of variable $J2L_LWR_MGN'''
		return self._instance.J2lLwrMgn

	@property
	def r_f2lshrt(self) -> float:
		'''Value of variable $R_F2LSHRT'''
		return self._instance.RF2lshrt

	@property
	def r_f2llong(self) -> float:
		'''Value of variable $R_F2LLONG'''
		return self._instance.RF2llong

	@property
	def min_f2lshrt(self) -> int:
		'''Value of variable $MIN_F2LSHRT'''
		return self._instance.MinF2lshrt

	@property
	def min_f2llong(self) -> int:
		'''Value of variable $MIN_F2LLONG'''
		return self._instance.MinF2llong

	@property
	def min_acrl_s(self) -> float:
		'''Value of variable $MIN_ACRL_S'''
		return self._instance.MinAcrlS

	@property
	def min_acrl_l(self) -> float:
		'''Value of variable $MIN_ACRL_L'''
		return self._instance.MinAcrlL

	@property
	def min_payload(self) -> float:
		'''Value of variable $MIN_PAYLOAD'''
		return self._instance.MinPayload

	@property
	def hval(self) -> typing.List[float]:
		'''Value of variable $HVAL'''
		return self._instance.Hval

	@property
	def hmgn(self) -> typing.List[float]:
		'''Value of variable $HMGN'''
		return self._instance.Hmgn

	@property
	def flexl(self) -> typing.List[float]:
		'''Value of variable $FLEXL'''
		return self._instance.Flexl

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbcGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
