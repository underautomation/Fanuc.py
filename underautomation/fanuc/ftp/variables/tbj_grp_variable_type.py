import typing
from underautomation.fanuc.ftp.variables.tbparam_variable_type import TbparamVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import TbjGrpVariableType as tbj_grp_variable_type

class TbjGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type TBJ_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbj_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def tbj_accel1(self) -> typing.List[int]:
		'''Value of variable $TBJ_ACCEL1'''
		return self._instance.TbjAccel1

	@property
	def tbj_accel2(self) -> typing.List[int]:
		'''Value of variable $TBJ_ACCEL2'''
		return self._instance.TbjAccel2

	@property
	def asym_param(self) -> typing.List[float]:
		'''Value of variable $ASYM_PARAM'''
		return self._instance.AsymParam

	@property
	def tb_param(self) -> typing.List[TbparamVariableType]:
		'''Value of variable $TB_PARAM'''
		return [TbparamVariableType(x) for x in self._instance.TbParam]

	@property
	def shortmo_scl(self) -> float:
		'''Value of variable $SHORTMO_SCL'''
		return self._instance.ShortmoScl

	@property
	def longmo_scl(self) -> float:
		'''Value of variable $LONGMO_SCL'''
		return self._instance.LongmoScl

	@property
	def min_acc_shm(self) -> int:
		'''Value of variable $MIN_ACC_SHM'''
		return self._instance.MinAccShm

	@property
	def min_acc_uma(self) -> int:
		'''Value of variable $MIN_ACC_UMA'''
		return self._instance.MinAccUma

	@property
	def shortmo_mgn(self) -> float:
		'''Value of variable $SHORTMO_MGN'''
		return self._instance.ShortmoMgn

	@property
	def longmo_mgn(self) -> float:
		'''Value of variable $LONGMO_MGN'''
		return self._instance.LongmoMgn

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
	def j2j_upr_ang(self) -> float:
		'''Value of variable $J2J_UPR_ANG'''
		return self._instance.J2jUprAng

	@property
	def j2j_lwr_ang(self) -> float:
		'''Value of variable $J2J_LWR_ANG'''
		return self._instance.J2jLwrAng

	@property
	def j2j_upr_mgn(self) -> float:
		'''Value of variable $J2J_UPR_MGN'''
		return self._instance.J2jUprMgn

	@property
	def j2j_lwr_mgn(self) -> float:
		'''Value of variable $J2J_LWR_MGN'''
		return self._instance.J2jLwrMgn

	@property
	def inertia_vib(self) -> typing.List[float]:
		'''Value of variable $INERTIA_VIB'''
		return self._instance.InertiaVib

	@property
	def inertia_vi2(self) -> typing.List[float]:
		'''Value of variable $INERTIA_VI2'''
		return self._instance.InertiaVi2

	@property
	def iv_unit(self) -> float:
		'''Value of variable $IV_UNIT'''
		return self._instance.IvUnit

	@property
	def iv_unit2(self) -> float:
		'''Value of variable $IV_UNIT2'''
		return self._instance.IvUnit2

	@property
	def r_f2jacc(self) -> float:
		'''Value of variable $R_F2JACC'''
		return self._instance.RF2jacc

	@property
	def r_f2jdec(self) -> float:
		'''Value of variable $R_F2JDEC'''
		return self._instance.RF2jdec

	@property
	def r_f2jlong(self) -> float:
		'''Value of variable $R_F2JLONG'''
		return self._instance.RF2jlong

	@property
	def min_f2jacc(self) -> int:
		'''Value of variable $MIN_F2JACC'''
		return self._instance.MinF2jacc

	@property
	def min_f2jdec(self) -> int:
		'''Value of variable $MIN_F2JDEC'''
		return self._instance.MinF2jdec

	@property
	def min_f2jlong(self) -> int:
		'''Value of variable $MIN_F2JLONG'''
		return self._instance.MinF2jlong

	@property
	def min_acrj_s(self) -> float:
		'''Value of variable $MIN_ACRJ_S'''
		return self._instance.MinAcrjS

	@property
	def min_acrj_l(self) -> float:
		'''Value of variable $MIN_ACRJ_L'''
		return self._instance.MinAcrjL

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
	def haxs(self) -> typing.List[int]:
		'''Value of variable $HAXS'''
		return self._instance.Haxs

	@property
	def flex(self) -> typing.List[float]:
		'''Value of variable $FLEX'''
		return self._instance.Flex

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TbjGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
