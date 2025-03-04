import typing
from underautomation.fanuc.ftp.variables.tbparam_variable_type import TbparamVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbjGrpVariableType as tbj_grp_variable_type

class TbjGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbj_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def tbj_accel1(self) -> typing.List[int]:
		return self._instance.TbjAccel1
	@property
	def tbj_accel2(self) -> typing.List[int]:
		return self._instance.TbjAccel2
	@property
	def asym_param(self) -> typing.List[float]:
		return self._instance.AsymParam
	@property
	def tb_param(self) -> typing.List[TbparamVariableType]:
		return [TbparamVariableType(x) for x in self._instance.TbParam]
	@property
	def shortmo_scl(self) -> float:
		return self._instance.ShortmoScl
	@property
	def longmo_scl(self) -> float:
		return self._instance.LongmoScl
	@property
	def min_acc_shm(self) -> int:
		return self._instance.MinAccShm
	@property
	def min_acc_uma(self) -> int:
		return self._instance.MinAccUma
	@property
	def shortmo_mgn(self) -> float:
		return self._instance.ShortmoMgn
	@property
	def longmo_mgn(self) -> float:
		return self._instance.LongmoMgn
	@property
	def min_cyc_id(self) -> str:
		return self._instance.MinCycId
	@property
	def min_c_id_e1(self) -> str:
		return self._instance.MinCIdE1
	@property
	def min_c_id_e2(self) -> str:
		return self._instance.MinCIdE2
	@property
	def min_c_id_e3(self) -> str:
		return self._instance.MinCIdE3
	@property
	def payload_mgn(self) -> float:
		return self._instance.PayloadMgn
	@property
	def j2j_upr_ang(self) -> float:
		return self._instance.J2jUprAng
	@property
	def j2j_lwr_ang(self) -> float:
		return self._instance.J2jLwrAng
	@property
	def j2j_upr_mgn(self) -> float:
		return self._instance.J2jUprMgn
	@property
	def j2j_lwr_mgn(self) -> float:
		return self._instance.J2jLwrMgn
	@property
	def inertia_vib(self) -> typing.List[float]:
		return self._instance.InertiaVib
	@property
	def inertia_vi2(self) -> typing.List[float]:
		return self._instance.InertiaVi2
	@property
	def iv_unit(self) -> float:
		return self._instance.IvUnit
	@property
	def iv_unit2(self) -> float:
		return self._instance.IvUnit2
	@property
	def r_f2jacc(self) -> float:
		return self._instance.RF2jacc
	@property
	def r_f2jdec(self) -> float:
		return self._instance.RF2jdec
	@property
	def r_f2jlong(self) -> float:
		return self._instance.RF2jlong
	@property
	def min_f2jacc(self) -> int:
		return self._instance.MinF2jacc
	@property
	def min_f2jdec(self) -> int:
		return self._instance.MinF2jdec
	@property
	def min_f2jlong(self) -> int:
		return self._instance.MinF2jlong
	@property
	def min_acrj_s(self) -> float:
		return self._instance.MinAcrjS
	@property
	def min_acrj_l(self) -> float:
		return self._instance.MinAcrjL
	@property
	def min_payload(self) -> float:
		return self._instance.MinPayload
	@property
	def hval(self) -> typing.List[float]:
		return self._instance.Hval
	@property
	def hmgn(self) -> typing.List[float]:
		return self._instance.Hmgn
	@property
	def haxs(self) -> typing.List[int]:
		return self._instance.Haxs
	@property
	def flex(self) -> typing.List[float]:
		return self._instance.Flex
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
