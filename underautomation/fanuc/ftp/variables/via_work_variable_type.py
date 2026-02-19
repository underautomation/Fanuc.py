import typing
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ViaWorkVariableType as via_work_variable_type

class ViaWorkVariableType(GenericVariableType):
	'''Describes the Fanuc type VIA_WORK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = via_work_variable_type()
		else:
			self._instance = _internal

	@property
	def hdr(self) -> typing.List[int]:
		'''Value of variable $HDR'''
		return self._instance.Hdr

	@property
	def joint_pos(self) -> JointPositionVariable:
		'''Value of variable $JOINT_POS'''
		return JointPositionVariable(self._instance.JointPos)

	@property
	def z_uplim(self) -> float:
		'''Value of variable $Z_UPLIM'''
		return self._instance.ZUplim

	@property
	def z_lowlim(self) -> float:
		'''Value of variable $Z_LOWLIM'''
		return self._instance.ZLowlim

	@property
	def via_created(self) -> bool:
		'''Value of variable $VIA_CREATED'''
		return self._instance.ViaCreated

	@property
	def cur_lin(self) -> int:
		'''Value of variable $CUR_LIN'''
		return self._instance.CurLin

	@property
	def ept_idx(self) -> int:
		'''Value of variable $EPT_IDX'''
		return self._instance.EptIdx

	@property
	def task_id(self) -> int:
		'''Value of variable $TASK_ID'''
		return self._instance.TaskId

	@property
	def int_via_mod(self) -> int:
		'''Value of variable $INT_VIA_MOD'''
		return self._instance.IntViaMod

	@property
	def reserved(self) -> int:
		'''Value of variable $RESERVED'''
		return self._instance.Reserved

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ViaWorkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
