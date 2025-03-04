import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PlidCllbVariableType as plid_cllb_variable_type

class PlidCllbVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_cllb_variable_type()
		else:
			self._instance = _internal
	@property
	def barecd_done(self) -> int:
		return self._instance.BarecdDone
	@property
	def bamove_dir(self) -> int:
		return self._instance.BamoveDir
	@property
	def bamove_dis(self) -> float:
		return self._instance.BamoveDis
	@property
	def baj5_deg(self) -> float:
		return self._instance.Baj5Deg
	@property
	def baj6_deg(self) -> float:
		return self._instance.Baj6Deg
	@property
	def mass_known(self) -> int:
		return self._instance.MassKnown
	@property
	def mass_value(self) -> float:
		return self._instance.MassValue
	@property
	def adrecd_done(self) -> typing.List[int]:
		return self._instance.AdrecdDone
	@property
	def aduse_done(self) -> typing.List[int]:
		return self._instance.AduseDone
	@property
	def payload(self) -> float:
		return self._instance.Payload
	@property
	def payload_x(self) -> float:
		return self._instance.PayloadX
	@property
	def payload_y(self) -> float:
		return self._instance.PayloadY
	@property
	def payload_z(self) -> float:
		return self._instance.PayloadZ
	@property
	def plnum_ap(self) -> int:
		return self._instance.PlnumAp
	@property
	def plcl_pos(self) -> typing.List[CartesianPositionVariable]:
		return [CartesianPositionVariable(x) for x in self._instance.PlclPos]
	@property
	def plcl_dis(self) -> typing.List[float]:
		return self._instance.PlclDis
	@property
	def plcl_ut(self) -> typing.List[int]:
		return self._instance.PlclUt
	@property
	def plcl_uf(self) -> typing.List[int]:
		return self._instance.PlclUf
	@property
	def plcl_crpo(self) -> int:
		return self._instance.PlclCrpo
	@property
	def plcl_posid(self) -> int:
		return self._instance.PlclPosid
	@property
	def plcl_esti(self) -> int:
		return self._instance.PlclEsti
	@property
	def plcl_prost(self) -> int:
		return self._instance.PlclProst
	@property
	def plcl_axism(self) -> typing.List[float]:
		return self._instance.PlclAxism
	@property
	def basepos_j(self) -> bool:
		return self._instance.BaseposJ
	@property
	def base_jpos(self) -> typing.List[float]:
		return self._instance.BaseJpos
	@property
	def extand_axis(self) -> bool:
		return self._instance.ExtandAxis
	@property
	def extand_pos(self) -> typing.List[float]:
		return self._instance.ExtandPos
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
