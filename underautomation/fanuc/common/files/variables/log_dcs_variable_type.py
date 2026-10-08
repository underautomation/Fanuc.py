from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.stop_variable_type import StopVariableType
from underautomation.fanuc.common.files.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Common.Files.Variables import LogDcsVariableType as log_dcs_variable_type

class LogDcsVariableType(GenericVariableType):
	'''Describes the Fanuc type LOG_DCS_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_dcs_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> int:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def spd_tol(self) -> float:
		'''Value of variable $SPD_TOL'''
		return self._instance.SpdTol

	@property
	def output_typ(self) -> int:
		'''Value of variable $OUTPUT_TYP'''
		return self._instance.OutputTyp

	@property
	def output_idx(self) -> int:
		'''Value of variable $OUTPUT_IDX'''
		return self._instance.OutputIdx

	@property
	def grp_num(self) -> int:
		'''Value of variable $GRP_NUM'''
		return self._instance.GrpNum

	@property
	def pos_typ(self) -> int:
		'''Value of variable $POS_TYP'''
		return self._instance.PosTyp

	@property
	def axis_num(self) -> int:
		'''Value of variable $AXIS_NUM'''
		return self._instance.AxisNum

	@property
	def stop_ready(self) -> bool:
		'''Value of variable $STOP_READY'''
		return self._instance.StopReady

	@property
	def stop(self) -> StopVariableType:
		'''Value of variable $STOP'''
		__r = self._instance.Stop
		return None if __r is None else StopVariableType(__r)

	@property
	def estop(self) -> StopVariableType:
		'''Value of variable $ESTOP'''
		__r = self._instance.Estop
		return None if __r is None else StopVariableType(__r)

	@property
	def cstop(self) -> StopVariableType:
		'''Value of variable $CSTOP'''
		__r = self._instance.Cstop
		return None if __r is None else StopVariableType(__r)

	@property
	def estop_diff(self) -> StopVariableType:
		'''Value of variable $ESTOP_DIFF'''
		__r = self._instance.EstopDiff
		return None if __r is None else StopVariableType(__r)

	@property
	def cstop_diff(self) -> StopVariableType:
		'''Value of variable $CSTOP_DIFF'''
		__r = self._instance.CstopDiff
		return None if __r is None else StopVariableType(__r)

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogDcsVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
