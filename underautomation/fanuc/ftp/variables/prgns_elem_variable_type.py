import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsElemVariableType as prgns_elem_variable_type

class PrgnsElemVariableType(GenericVariableType):
	'''Describes the Fanuc type PRGNS_ELEM_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_elem_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> int:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def feasible(self) -> int:
		'''Value of variable $FEASIBLE'''
		return self._instance.Feasible

	@property
	def axis(self) -> int:
		'''Value of variable $AXIS'''
		return self._instance.Axis

	@property
	def elem_num(self) -> int:
		'''Value of variable $ELEM_NUM'''
		return self._instance.ElemNum

	@property
	def rot_ratio(self) -> float:
		'''Value of variable $ROT_RATIO'''
		return self._instance.RotRatio

	@property
	def max_freq(self) -> float:
		'''Value of variable $MAX_FREQ'''
		return self._instance.MaxFreq

	@property
	def thre_rel(self) -> float:
		'''Value of variable $THRE_REL'''
		return self._instance.ThreRel

	@property
	def thre_abs(self) -> float:
		'''Value of variable $THRE_ABS'''
		return self._instance.ThreAbs

	@property
	def degrad_lvl(self) -> float:
		'''Value of variable $DEGRAD_LVL'''
		return self._instance.DegradLvl

	@property
	def degrad_base(self) -> float:
		'''Value of variable $DEGRAD_BASE'''
		return self._instance.DegradBase

	@property
	def degrad_rate(self) -> float:
		'''Value of variable $DEGRAD_RATE'''
		return self._instance.DegradRate

	@property
	def upd_date(self) -> str:
		'''Value of variable $UPD_DATE'''
		return self._instance.UpdDate

	@property
	def base_date(self) -> str:
		'''Value of variable $BASE_DATE'''
		return self._instance.BaseDate

	@property
	def rms_trq(self) -> float:
		'''Value of variable $RMS_TRQ'''
		return self._instance.RmsTrq

	@property
	def max_distrq(self) -> int:
		'''Value of variable $MAX_DISTRQ'''
		return self._instance.MaxDistrq

	@property
	def max_spd(self) -> int:
		'''Value of variable $MAX_SPD'''
		return self._instance.MaxSpd

	@property
	def last_date(self) -> int:
		'''Value of variable $LAST_DATE'''
		return self._instance.LastDate

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrgnsElemVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
