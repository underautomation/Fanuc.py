import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CreatePrgVariableType as create_prg_variable_type

class CreatePrgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = create_prg_variable_type()
		else:
			self._instance = _internal
	@property
	def axis_flag(self) -> typing.List[bool]:
		return self._instance.AxisFlag
	@property
	def num_axs_rep(self) -> int:
		return self._instance.NumAxsRep
	@property
	def swing_ang(self) -> typing.List[float]:
		return self._instance.SwingAng
	@property
	def num_ms_pose(self) -> int:
		return self._instance.NumMsPose
	@property
	def base_pose(self) -> typing.List[float]:
		return self._instance.BasePose
	@property
	def evalue_idx(self) -> typing.List[float]:
		return self._instance.EvalueIdx
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
