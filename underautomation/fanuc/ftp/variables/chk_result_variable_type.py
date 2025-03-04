import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ChkResultVariableType as chk_result_variable_type

class ChkResultVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = chk_result_variable_type()
		else:
			self._instance = _internal
	@property
	def evalue_idx(self) -> float:
		return self._instance.EvalueIdx
	@property
	def max_ms_err(self) -> float:
		return self._instance.MaxMsErr
	@property
	def mean_ms_err(self) -> float:
		return self._instance.MeanMsErr
	@property
	def worst_pose(self) -> int:
		return self._instance.WorstPose
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
