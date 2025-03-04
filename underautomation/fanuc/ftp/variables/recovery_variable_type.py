import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RecoveryVariableType as recovery_variable_type

class RecoveryVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = recovery_variable_type()
		else:
			self._instance = _internal
	@property
	def org_mst_ct(self) -> typing.List[int]:
		return self._instance.OrgMstCt
	@property
	def org_uframe(self) -> typing.List[float]:
		return self._instance.OrgUframe
	@property
	def org_ref_pos(self) -> typing.List[float]:
		return self._instance.OrgRefPos
	@property
	def org_ref_ct(self) -> typing.List[int]:
		return self._instance.OrgRefCt
	@property
	def rcv_ang_pam(self) -> typing.List[float]:
		return self._instance.RcvAngPam
	@property
	def new_mst_ct(self) -> typing.List[int]:
		return self._instance.NewMstCt
	@property
	def new_uframe(self) -> typing.List[float]:
		return self._instance.NewUframe
	@property
	def new_ref_pos(self) -> typing.List[float]:
		return self._instance.NewRefPos
	@property
	def new_ref_ct(self) -> typing.List[int]:
		return self._instance.NewRefCt
	@property
	def evalue_idx(self) -> float:
		return self._instance.EvalueIdx
	@property
	def max_rc_err(self) -> float:
		return self._instance.MaxRcErr
	@property
	def mean_rc_err(self) -> float:
		return self._instance.MeanRcErr
	@property
	def worst_pose(self) -> int:
		return self._instance.WorstPose
	@property
	def master_time(self) -> int:
		return self._instance.MasterTime
	@property
	def debug_mode(self) -> int:
		return self._instance.DebugMode
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
