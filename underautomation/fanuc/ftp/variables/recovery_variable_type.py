import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import RecoveryVariableType as recovery_variable_type

class RecoveryVariableType(GenericVariableType):
	'''Describes the Fanuc type $RECOVERY'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = recovery_variable_type()
		else:
			self._instance = _internal

	@property
	def org_mst_ct(self) -> typing.List[int]:
		'''Value of variable $ORG_MST_CT'''
		return self._instance.OrgMstCt

	@property
	def org_uframe(self) -> typing.List[float]:
		'''Value of variable $ORG_UFRAME'''
		return self._instance.OrgUframe

	@property
	def org_ref_pos(self) -> typing.List[float]:
		'''Value of variable $ORG_REF_POS'''
		return self._instance.OrgRefPos

	@property
	def org_ref_ct(self) -> typing.List[int]:
		'''Value of variable $ORG_REF_CT'''
		return self._instance.OrgRefCt

	@property
	def rcv_ang_pam(self) -> typing.List[float]:
		'''Value of variable $RCV_ANG_PAM'''
		return self._instance.RcvAngPam

	@property
	def new_mst_ct(self) -> typing.List[int]:
		'''Value of variable $NEW_MST_CT'''
		return self._instance.NewMstCt

	@property
	def new_uframe(self) -> typing.List[float]:
		'''Value of variable $NEW_UFRAME'''
		return self._instance.NewUframe

	@property
	def new_ref_pos(self) -> typing.List[float]:
		'''Value of variable $NEW_REF_POS'''
		return self._instance.NewRefPos

	@property
	def new_ref_ct(self) -> typing.List[int]:
		'''Value of variable $NEW_REF_CT'''
		return self._instance.NewRefCt

	@property
	def evalue_idx(self) -> float:
		'''Value of variable $EVALUE_IDX'''
		return self._instance.EvalueIdx

	@property
	def max_rc_err(self) -> float:
		'''Value of variable $MAX_RC_ERR'''
		return self._instance.MaxRcErr

	@property
	def mean_rc_err(self) -> float:
		'''Value of variable $MEAN_RC_ERR'''
		return self._instance.MeanRcErr

	@property
	def worst_pose(self) -> int:
		'''Value of variable $WORST_POSE'''
		return self._instance.WorstPose

	@property
	def master_time(self) -> int:
		'''Value of variable $MASTER_TIME'''
		return self._instance.MasterTime

	@property
	def debug_mode(self) -> int:
		'''Value of variable $DEBUG_MODE'''
		return self._instance.DebugMode

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RecoveryVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
