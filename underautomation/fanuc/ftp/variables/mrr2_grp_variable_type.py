import typing
from underautomation.fanuc.ftp.variables.armload_variable_type import ArmloadVariableType
from underautomation.fanuc.ftp.variables.armload_p_variable_type import ArmloadPVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import Mrr2GrpVariableType as mrr2_grp_variable_type

class Mrr2GrpVariableType(GenericVariableType):
	'''Describes the Fanuc type MRR2_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mrr2_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def arm_param(self) -> typing.List[float]:
		'''Value of variable $ARM_PARAM'''
		return self._instance.ArmParam

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
	def rlibsw01(self) -> int:
		'''Value of variable $RLIBSW01'''
		return self._instance.Rlibsw01

	@property
	def rlibsw02(self) -> int:
		'''Value of variable $RLIBSW02'''
		return self._instance.Rlibsw02

	@property
	def abc_flag(self) -> int:
		'''Value of variable $ABC_FLAG'''
		return self._instance.AbcFlag

	@property
	def md_j2sect(self) -> typing.List[float]:
		'''Value of variable $MD_J2SECT'''
		return self._instance.MdJ2sect

	@property
	def md_j3sect(self) -> typing.List[float]:
		'''Value of variable $MD_J3SECT'''
		return self._instance.MdJ3sect

	@property
	def md_j1spcons(self) -> typing.List[float]:
		'''Value of variable $MD_J1SPCONS'''
		return self._instance.MdJ1spcons

	@property
	def md_j2spcons(self) -> typing.List[float]:
		'''Value of variable $MD_J2SPCONS'''
		return self._instance.MdJ2spcons

	@property
	def md_j3spcons(self) -> typing.List[float]:
		'''Value of variable $MD_J3SPCONS'''
		return self._instance.MdJ3spcons

	@property
	def md_cur_k(self) -> typing.List[float]:
		'''Value of variable $MD_CUR_K'''
		return self._instance.MdCurK

	@property
	def md_cur_j2(self) -> int:
		'''Value of variable $MD_CUR_J2'''
		return self._instance.MdCurJ2

	@property
	def md_cur_j3(self) -> int:
		'''Value of variable $MD_CUR_J3'''
		return self._instance.MdCurJ3

	@property
	def sv_off_tim2(self) -> typing.List[int]:
		'''Value of variable $SV_OFF_TIM2'''
		return self._instance.SvOffTim2

	@property
	def cskplim_enb(self) -> bool:
		'''Value of variable $CSKPLIM_ENB'''
		return self._instance.CskplimEnb

	@property
	def cskplim_lin(self) -> int:
		'''Value of variable $CSKPLIM_LIN'''
		return self._instance.CskplimLin

	@property
	def cskplim_jnt(self) -> typing.List[int]:
		'''Value of variable $CSKPLIM_JNT'''
		return self._instance.CskplimJnt

	@property
	def qskplim_enb(self) -> bool:
		'''Value of variable $QSKPLIM_ENB'''
		return self._instance.QskplimEnb

	@property
	def qskplim_lin(self) -> int:
		'''Value of variable $QSKPLIM_LIN'''
		return self._instance.QskplimLin

	@property
	def qskplim_jnt(self) -> typing.List[int]:
		'''Value of variable $QSKPLIM_JNT'''
		return self._instance.QskplimJnt

	@property
	def ext_azim(self) -> typing.List[float]:
		'''Value of variable $EXT_AZIM'''
		return self._instance.ExtAzim

	@property
	def ext_elev(self) -> typing.List[float]:
		'''Value of variable $EXT_ELEV'''
		return self._instance.ExtElev

	@property
	def servocmptol(self) -> typing.List[int]:
		'''Value of variable $SERVOCMPTOL'''
		return self._instance.Servocmptol

	@property
	def axisinertil(self) -> typing.List[int]:
		'''Value of variable $AXISINERTIL'''
		return self._instance.Axisinertil

	@property
	def armload(self) -> typing.List[ArmloadVariableType]:
		'''Value of variable $ARMLOAD'''
		return [ArmloadVariableType(x) for x in self._instance.Armload]

	@property
	def armload_x(self) -> typing.List[ArmloadPVariableType]:
		'''Value of variable $ARMLOAD_X'''
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadX]

	@property
	def armload_y(self) -> typing.List[ArmloadPVariableType]:
		'''Value of variable $ARMLOAD_Y'''
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadY]

	@property
	def armload_z(self) -> typing.List[ArmloadPVariableType]:
		'''Value of variable $ARMLOAD_Z'''
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadZ]

	@property
	def smgrsttim(self) -> typing.List[int]:
		'''Value of variable $SMGRSTTIM'''
		return self._instance.Smgrsttim

	@property
	def jgfl_scl_ex(self) -> float:
		'''Value of variable $JGFL_SCL_EX'''
		return self._instance.JgflSclEx

	@property
	def extsph_i(self) -> typing.List[int]:
		'''Value of variable $EXTSPH_I'''
		return self._instance.ExtsphI

	@property
	def extsph_r(self) -> typing.List[float]:
		'''Value of variable $EXTSPH_R'''
		return self._instance.ExtsphR

	@property
	def carterrlim(self) -> typing.List[float]:
		'''Value of variable $CARTERRLIM'''
		return self._instance.Carterrlim

	@property
	def scara_lead(self) -> float:
		'''Value of variable $SCARA_LEAD'''
		return self._instance.ScaraLead

	@property
	def gratio_num(self) -> typing.List[int]:
		'''Value of variable $GRATIO_NUM'''
		return self._instance.GratioNum

	@property
	def gratio_div(self) -> typing.List[int]:
		'''Value of variable $GRATIO_DIV'''
		return self._instance.GratioDiv

	@property
	def j23uplim_df(self) -> float:
		'''Value of variable $J23UPLIM_DF'''
		return self._instance.J23uplimDf

	@property
	def j23lwlim_df(self) -> float:
		'''Value of variable $J23LWLIM_DF'''
		return self._instance.J23lwlimDf

	@property
	def vellim_inrt(self) -> bool:
		'''Value of variable $VELLIM_INRT'''
		return self._instance.VellimInrt

	@property
	def inrt_bl1(self) -> typing.List[float]:
		'''Value of variable $INRT_BL1'''
		return self._instance.InrtBl1

	@property
	def inrt_bl2(self) -> typing.List[float]:
		'''Value of variable $INRT_BL2'''
		return self._instance.InrtBl2

	@property
	def jvellim_bl1(self) -> typing.List[float]:
		'''Value of variable $JVELLIM_BL1'''
		return self._instance.JvellimBl1

	@property
	def jvellim_bl2(self) -> typing.List[float]:
		'''Value of variable $JVELLIM_BL2'''
		return self._instance.JvellimBl2

	@property
	def mech_type2(self) -> int:
		'''Value of variable $MECH_TYPE2'''
		return self._instance.MechType2

	@property
	def rtsa_rlib(self) -> bool:
		'''Value of variable $RTSA_RLIB'''
		return self._instance.RtsaRlib

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Mrr2GrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
