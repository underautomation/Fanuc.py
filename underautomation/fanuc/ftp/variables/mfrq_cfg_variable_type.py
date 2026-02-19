import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MfrqCfgVariableType as mfrq_cfg_variable_type

class MfrqCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type MFRQ_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mfrq_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def hrs_run(self) -> float:
		'''Value of variable $HRS_RUN'''
		return self._instance.HrsRun

	@property
	def state(self) -> int:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def act_grp(self) -> int:
		'''Value of variable $ACT_GRP'''
		return self._instance.ActGrp

	@property
	def freq_lim(self) -> float:
		'''Value of variable $FREQ_LIM'''
		return self._instance.FreqLim

	@property
	def win_size(self) -> int:
		'''Value of variable $WIN_SIZE'''
		return self._instance.WinSize

	@property
	def overlap(self) -> int:
		'''Value of variable $OVERLAP'''
		return self._instance.Overlap

	@property
	def flag(self) -> int:
		'''Value of variable $FLAG'''
		return self._instance.Flag

	@property
	def spd_ovrd(self) -> int:
		'''Value of variable $SPD_OVRD'''
		return self._instance.SpdOvrd

	@property
	def pg_prefix(self) -> str:
		'''Value of variable $PG_PREFIX'''
		return self._instance.PgPrefix

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MfrqCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
