import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PrgadjSchVariableType as prgadj_sch_variable_type

class PrgadjSchVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgadj_sch_variable_type()
		else:
			self._instance = _internal
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def line_strt(self) -> int:
		return self._instance.LineStrt
	@property
	def line_end(self) -> int:
		return self._instance.LineEnd
	@property
	def begin_line(self) -> int:
		return self._instance.BeginLine
	@property
	def last_line(self) -> int:
		return self._instance.LastLine
	@property
	def last_posnum(self) -> int:
		return self._instance.LastPosnum
	@property
	def status(self) -> int:
		return self._instance.Status
	@property
	def units(self) -> int:
		return self._instance.Units
	@property
	def frame_name(self) -> int:
		return self._instance.FrameName
	@property
	def x_adj(self) -> float:
		return self._instance.XAdj
	@property
	def y_adj(self) -> float:
		return self._instance.YAdj
	@property
	def z_adj(self) -> float:
		return self._instance.ZAdj
	@property
	def w_adj(self) -> float:
		return self._instance.WAdj
	@property
	def p_adj(self) -> float:
		return self._instance.PAdj
	@property
	def r_adj(self) -> float:
		return self._instance.RAdj
	@property
	def y_opt_adj(self) -> int:
		return self._instance.YOptAdj
	@property
	def lin_spd_adj(self) -> int:
		return self._instance.LinSpdAdj
	@property
	def jt_spd_adj(self) -> int:
		return self._instance.JtSpdAdj
	@property
	def group_adj(self) -> int:
		return self._instance.GroupAdj
	@property
	def grp_parten(self) -> typing.List[bool]:
		return self._instance.GrpParten
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
