import typing
from underautomation.fanuc.ftp.variables.tbcparam_variable_type import TbcparamVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbcGrpVariableType as tbc_grp_variable_type

class TbcGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbc_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def tbc_accel1(self) -> int:
		return self._instance.TbcAccel1
	@property
	def tbc_accel2(self) -> int:
		return self._instance.TbcAccel2
	@property
	def tbc_path1(self) -> int:
		return self._instance.TbcPath1
	@property
	def tbc_path2(self) -> int:
		return self._instance.TbcPath2
	@property
	def path_ratio(self) -> float:
		return self._instance.PathRatio
	@property
	def tbc_param(self) -> typing.List[TbcparamVariableType]:
		return [TbcparamVariableType(x) for x in self._instance.TbcParam]
	@property
	def cnt_scale(self) -> float:
		return self._instance.CntScale
	@property
	def shortmo_scl(self) -> float:
		return self._instance.ShortmoScl
	@property
	def min_acc_uca(self) -> int:
		return self._instance.MinAccUca
	@property
	def min_cat_uma(self) -> int:
		return self._instance.MinCatUma
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
	def j2l_upr_ang(self) -> float:
		return self._instance.J2lUprAng
	@property
	def j2l_lwr_ang(self) -> float:
		return self._instance.J2lLwrAng
	@property
	def j2l_upr_mgn(self) -> float:
		return self._instance.J2lUprMgn
	@property
	def j2l_lwr_mgn(self) -> float:
		return self._instance.J2lLwrMgn
	@property
	def r_f2lshrt(self) -> float:
		return self._instance.RF2lshrt
	@property
	def r_f2llong(self) -> float:
		return self._instance.RF2llong
	@property
	def min_f2lshrt(self) -> int:
		return self._instance.MinF2lshrt
	@property
	def min_f2llong(self) -> int:
		return self._instance.MinF2llong
	@property
	def min_acrl_s(self) -> float:
		return self._instance.MinAcrlS
	@property
	def min_acrl_l(self) -> float:
		return self._instance.MinAcrlL
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
	def flexl(self) -> typing.List[float]:
		return self._instance.Flexl
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
