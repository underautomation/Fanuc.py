import typing
from underautomation.fanuc.ftp.variables.stop_variable_type import StopVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LogDcsVariableType as log_dcs_variable_type

class LogDcsVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = log_dcs_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def spd_tol(self) -> float:
		return self._instance.SpdTol
	@property
	def output_typ(self) -> int:
		return self._instance.OutputTyp
	@property
	def output_idx(self) -> int:
		return self._instance.OutputIdx
	@property
	def grp_num(self) -> int:
		return self._instance.GrpNum
	@property
	def pos_typ(self) -> int:
		return self._instance.PosTyp
	@property
	def axis_num(self) -> int:
		return self._instance.AxisNum
	@property
	def stop_ready(self) -> bool:
		return self._instance.StopReady
	@property
	def stop(self) -> StopVariableType:
		return StopVariableType(self._instance.Stop)
	@property
	def estop(self) -> StopVariableType:
		return StopVariableType(self._instance.Estop)
	@property
	def cstop(self) -> StopVariableType:
		return StopVariableType(self._instance.Cstop)
	@property
	def estop_diff(self) -> StopVariableType:
		return StopVariableType(self._instance.EstopDiff)
	@property
	def cstop_diff(self) -> StopVariableType:
		return StopVariableType(self._instance.CstopDiff)
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
