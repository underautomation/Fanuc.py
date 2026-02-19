import typing
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PlidCllbVariableType as plid_cllb_variable_type

class PlidCllbVariableType(GenericVariableType):
	'''Describes the Fanuc type PLID_CLLB_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = plid_cllb_variable_type()
		else:
			self._instance = _internal

	@property
	def barecd_done(self) -> int:
		'''Value of variable $BARECD_DONE'''
		return self._instance.BarecdDone

	@property
	def bamove_dir(self) -> int:
		'''Value of variable $BAMOVE_DIR'''
		return self._instance.BamoveDir

	@property
	def bamove_dis(self) -> float:
		'''Value of variable $BAMOVE_DIS'''
		return self._instance.BamoveDis

	@property
	def baj5_deg(self) -> float:
		'''Value of variable $BAJ5_DEG'''
		return self._instance.Baj5Deg

	@property
	def baj6_deg(self) -> float:
		'''Value of variable $BAJ6_DEG'''
		return self._instance.Baj6Deg

	@property
	def mass_known(self) -> int:
		'''Value of variable $MASS_KNOWN'''
		return self._instance.MassKnown

	@property
	def mass_value(self) -> float:
		'''Value of variable $MASS_VALUE'''
		return self._instance.MassValue

	@property
	def adrecd_done(self) -> typing.List[int]:
		'''Value of variable $ADRECD_DONE'''
		return self._instance.AdrecdDone

	@property
	def aduse_done(self) -> typing.List[int]:
		'''Value of variable $ADUSE_DONE'''
		return self._instance.AduseDone

	@property
	def payload(self) -> float:
		'''Value of variable $PAYLOAD'''
		return self._instance.Payload

	@property
	def payload_x(self) -> float:
		'''Value of variable $PAYLOAD_X'''
		return self._instance.PayloadX

	@property
	def payload_y(self) -> float:
		'''Value of variable $PAYLOAD_Y'''
		return self._instance.PayloadY

	@property
	def payload_z(self) -> float:
		'''Value of variable $PAYLOAD_Z'''
		return self._instance.PayloadZ

	@property
	def plnum_ap(self) -> int:
		'''Value of variable $PLNUM_AP'''
		return self._instance.PlnumAp

	@property
	def plcl_pos(self) -> typing.List[CartesianPositionVariable]:
		'''Value of variable $PLCL_POS'''
		return [CartesianPositionVariable(x) for x in self._instance.PlclPos]

	@property
	def plcl_dis(self) -> typing.List[float]:
		'''Value of variable $PLCL_DIS'''
		return self._instance.PlclDis

	@property
	def plcl_ut(self) -> typing.List[int]:
		'''Value of variable $PLCL_UT'''
		return self._instance.PlclUt

	@property
	def plcl_uf(self) -> typing.List[int]:
		'''Value of variable $PLCL_UF'''
		return self._instance.PlclUf

	@property
	def plcl_crpo(self) -> int:
		'''Value of variable $PLCL_CRPO'''
		return self._instance.PlclCrpo

	@property
	def plcl_posid(self) -> int:
		'''Value of variable $PLCL_POSID'''
		return self._instance.PlclPosid

	@property
	def plcl_esti(self) -> int:
		'''Value of variable $PLCL_ESTI'''
		return self._instance.PlclEsti

	@property
	def plcl_prost(self) -> int:
		'''Value of variable $PLCL_PROST'''
		return self._instance.PlclProst

	@property
	def plcl_axism(self) -> typing.List[float]:
		'''Value of variable $PLCL_AXISM'''
		return self._instance.PlclAxism

	@property
	def basepos_j(self) -> bool:
		'''Value of variable $BASEPOS_J'''
		return self._instance.BaseposJ

	@property
	def base_jpos(self) -> typing.List[float]:
		'''Value of variable $BASE_JPOS'''
		return self._instance.BaseJpos

	@property
	def extand_axis(self) -> bool:
		'''Value of variable $EXTAND_AXIS'''
		return self._instance.ExtandAxis

	@property
	def extand_pos(self) -> typing.List[float]:
		'''Value of variable $EXTAND_POS'''
		return self._instance.ExtandPos

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PlidCllbVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
