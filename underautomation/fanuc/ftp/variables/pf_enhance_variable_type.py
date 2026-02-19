import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PfEnhanceVariableType as pf_enhance_variable_type

class PfEnhanceVariableType(GenericVariableType):
	'''Describes the Fanuc type PF_ENHANCE_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pf_enhance_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def state(self) -> int:
		'''Value of variable $STATE'''
		return self._instance.State

	@property
	def hrs_intv(self) -> float:
		'''Value of variable $HRS_INTV'''
		return self._instance.HrsIntv

	@property
	def rm_cfg(self) -> int:
		'''Value of variable $RM_CFG'''
		return self._instance.RmCfg

	@property
	def grp_mask(self) -> int:
		'''Value of variable $GRP_MASK'''
		return self._instance.GrpMask

	@property
	def spd_ovrd(self) -> int:
		'''Value of variable $SPD_OVRD'''
		return self._instance.SpdOvrd

	@property
	def pg_prefix(self) -> str:
		'''Value of variable $PG_PREFIX'''
		return self._instance.PgPrefix

	@property
	def max_lines(self) -> int:
		'''Value of variable $MAX_LINES'''
		return self._instance.MaxLines

	@property
	def ovc_lim(self) -> int:
		'''Value of variable $OVC_LIM'''
		return self._instance.OvcLim

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
		if not isinstance(other, PfEnhanceVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
