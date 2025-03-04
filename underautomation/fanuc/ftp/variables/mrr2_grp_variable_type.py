import typing
from underautomation.fanuc.ftp.variables.armload_variable_type import ArmloadVariableType
from underautomation.fanuc.ftp.variables.armload_p_variable_type import ArmloadPVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Mrr2GrpVariableType as mrr2_grp_variable_type

class Mrr2GrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mrr2_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def arm_param(self) -> typing.List[float]:
		return self._instance.ArmParam
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
	def rlibsw01(self) -> int:
		return self._instance.Rlibsw01
	@property
	def rlibsw02(self) -> int:
		return self._instance.Rlibsw02
	@property
	def abc_flag(self) -> int:
		return self._instance.AbcFlag
	@property
	def md_j2sect(self) -> typing.List[float]:
		return self._instance.MdJ2sect
	@property
	def md_j3sect(self) -> typing.List[float]:
		return self._instance.MdJ3sect
	@property
	def md_j1spcons(self) -> typing.List[float]:
		return self._instance.MdJ1spcons
	@property
	def md_j2spcons(self) -> typing.List[float]:
		return self._instance.MdJ2spcons
	@property
	def md_j3spcons(self) -> typing.List[float]:
		return self._instance.MdJ3spcons
	@property
	def md_cur_k(self) -> typing.List[float]:
		return self._instance.MdCurK
	@property
	def md_cur_j2(self) -> int:
		return self._instance.MdCurJ2
	@property
	def md_cur_j3(self) -> int:
		return self._instance.MdCurJ3
	@property
	def sv_off_tim2(self) -> typing.List[int]:
		return self._instance.SvOffTim2
	@property
	def cskplim_enb(self) -> bool:
		return self._instance.CskplimEnb
	@property
	def cskplim_lin(self) -> int:
		return self._instance.CskplimLin
	@property
	def cskplim_jnt(self) -> typing.List[int]:
		return self._instance.CskplimJnt
	@property
	def qskplim_enb(self) -> bool:
		return self._instance.QskplimEnb
	@property
	def qskplim_lin(self) -> int:
		return self._instance.QskplimLin
	@property
	def qskplim_jnt(self) -> typing.List[int]:
		return self._instance.QskplimJnt
	@property
	def ext_azim(self) -> typing.List[float]:
		return self._instance.ExtAzim
	@property
	def ext_elev(self) -> typing.List[float]:
		return self._instance.ExtElev
	@property
	def servocmptol(self) -> typing.List[int]:
		return self._instance.Servocmptol
	@property
	def axisinertil(self) -> typing.List[int]:
		return self._instance.Axisinertil
	@property
	def armload(self) -> typing.List[ArmloadVariableType]:
		return [ArmloadVariableType(x) for x in self._instance.Armload]
	@property
	def armload_x(self) -> typing.List[ArmloadPVariableType]:
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadX]
	@property
	def armload_y(self) -> typing.List[ArmloadPVariableType]:
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadY]
	@property
	def armload_z(self) -> typing.List[ArmloadPVariableType]:
		return [ArmloadPVariableType(x) for x in self._instance.ArmloadZ]
	@property
	def smgrsttim(self) -> typing.List[int]:
		return self._instance.Smgrsttim
	@property
	def jgfl_scl_ex(self) -> float:
		return self._instance.JgflSclEx
	@property
	def extsph_i(self) -> typing.List[int]:
		return self._instance.ExtsphI
	@property
	def extsph_r(self) -> typing.List[float]:
		return self._instance.ExtsphR
	@property
	def carterrlim(self) -> typing.List[float]:
		return self._instance.Carterrlim
	@property
	def scara_lead(self) -> float:
		return self._instance.ScaraLead
	@property
	def gratio_num(self) -> typing.List[int]:
		return self._instance.GratioNum
	@property
	def gratio_div(self) -> typing.List[int]:
		return self._instance.GratioDiv
	@property
	def j23uplim_df(self) -> float:
		return self._instance.J23uplimDf
	@property
	def j23lwlim_df(self) -> float:
		return self._instance.J23lwlimDf
	@property
	def vellim_inrt(self) -> bool:
		return self._instance.VellimInrt
	@property
	def inrt_bl1(self) -> typing.List[float]:
		return self._instance.InrtBl1
	@property
	def inrt_bl2(self) -> typing.List[float]:
		return self._instance.InrtBl2
	@property
	def jvellim_bl1(self) -> typing.List[float]:
		return self._instance.JvellimBl1
	@property
	def jvellim_bl2(self) -> typing.List[float]:
		return self._instance.JvellimBl2
	@property
	def mech_type2(self) -> int:
		return self._instance.MechType2
	@property
	def rtsa_rlib(self) -> bool:
		return self._instance.RtsaRlib
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
