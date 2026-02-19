import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PrgadjSchVariableType as prgadj_sch_variable_type

class PrgadjSchVariableType(GenericVariableType):
	'''Describes the Fanuc type PRGADJ_SCH_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgadj_sch_variable_type()
		else:
			self._instance = _internal

	@property
	def prog_name(self) -> str:
		'''Value of variable $PROG_NAME'''
		return self._instance.ProgName

	@property
	def line_strt(self) -> int:
		'''Value of variable $LINE_STRT'''
		return self._instance.LineStrt

	@property
	def line_end(self) -> int:
		'''Value of variable $LINE_END'''
		return self._instance.LineEnd

	@property
	def begin_line(self) -> int:
		'''Value of variable $BEGIN_LINE'''
		return self._instance.BeginLine

	@property
	def last_line(self) -> int:
		'''Value of variable $LAST_LINE'''
		return self._instance.LastLine

	@property
	def last_posnum(self) -> int:
		'''Value of variable $LAST_POSNUM'''
		return self._instance.LastPosnum

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def units(self) -> int:
		'''Value of variable $UNITS'''
		return self._instance.Units

	@property
	def frame_name(self) -> int:
		'''Value of variable $FRAME_NAME'''
		return self._instance.FrameName

	@property
	def x_adj(self) -> float:
		'''Value of variable $X_ADJ'''
		return self._instance.XAdj

	@property
	def y_adj(self) -> float:
		'''Value of variable $Y_ADJ'''
		return self._instance.YAdj

	@property
	def z_adj(self) -> float:
		'''Value of variable $Z_ADJ'''
		return self._instance.ZAdj

	@property
	def w_adj(self) -> float:
		'''Value of variable $W_ADJ'''
		return self._instance.WAdj

	@property
	def p_adj(self) -> float:
		'''Value of variable $P_ADJ'''
		return self._instance.PAdj

	@property
	def r_adj(self) -> float:
		'''Value of variable $R_ADJ'''
		return self._instance.RAdj

	@property
	def y_opt_adj(self) -> int:
		'''Value of variable $Y_OPT_ADJ'''
		return self._instance.YOptAdj

	@property
	def lin_spd_adj(self) -> int:
		'''Value of variable $LIN_SPD_ADJ'''
		return self._instance.LinSpdAdj

	@property
	def jt_spd_adj(self) -> int:
		'''Value of variable $JT_SPD_ADJ'''
		return self._instance.JtSpdAdj

	@property
	def group_adj(self) -> int:
		'''Value of variable $GROUP_ADJ'''
		return self._instance.GroupAdj

	@property
	def grp_parten(self) -> typing.List[bool]:
		'''Value of variable $GRP_PARTEN'''
		return self._instance.GrpParten

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PrgadjSchVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
