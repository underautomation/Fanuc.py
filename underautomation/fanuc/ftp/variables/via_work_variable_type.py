import typing
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ViaWorkVariableType as via_work_variable_type

class ViaWorkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = via_work_variable_type()
		else:
			self._instance = _internal
	@property
	def hdr(self) -> typing.List[int]:
		return self._instance.Hdr
	@property
	def joint_pos(self) -> JointPositionVariable:
		return JointPositionVariable(self._instance.JointPos)
	@property
	def z_uplim(self) -> float:
		return self._instance.ZUplim
	@property
	def z_lowlim(self) -> float:
		return self._instance.ZLowlim
	@property
	def via_created(self) -> bool:
		return self._instance.ViaCreated
	@property
	def cur_lin(self) -> int:
		return self._instance.CurLin
	@property
	def ept_idx(self) -> int:
		return self._instance.EptIdx
	@property
	def task_id(self) -> int:
		return self._instance.TaskId
	@property
	def int_via_mod(self) -> int:
		return self._instance.IntViaMod
	@property
	def reserved(self) -> int:
		return self._instance.Reserved
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
