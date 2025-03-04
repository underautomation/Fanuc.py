import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsElemVariableType as prgns_elem_variable_type

class PrgnsElemVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_elem_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def feasible(self) -> int:
		return self._instance.Feasible
	@property
	def axis(self) -> int:
		return self._instance.Axis
	@property
	def elem_num(self) -> int:
		return self._instance.ElemNum
	@property
	def rot_ratio(self) -> float:
		return self._instance.RotRatio
	@property
	def max_freq(self) -> float:
		return self._instance.MaxFreq
	@property
	def thre_rel(self) -> float:
		return self._instance.ThreRel
	@property
	def thre_abs(self) -> float:
		return self._instance.ThreAbs
	@property
	def degrad_lvl(self) -> float:
		return self._instance.DegradLvl
	@property
	def degrad_base(self) -> float:
		return self._instance.DegradBase
	@property
	def degrad_rate(self) -> float:
		return self._instance.DegradRate
	@property
	def upd_date(self) -> str:
		return self._instance.UpdDate
	@property
	def base_date(self) -> str:
		return self._instance.BaseDate
	@property
	def rms_trq(self) -> float:
		return self._instance.RmsTrq
	@property
	def max_distrq(self) -> int:
		return self._instance.MaxDistrq
	@property
	def max_spd(self) -> int:
		return self._instance.MaxSpd
	@property
	def last_date(self) -> int:
		return self._instance.LastDate
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
