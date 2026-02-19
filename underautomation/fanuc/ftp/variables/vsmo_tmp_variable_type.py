import typing
from underautomation.fanuc.ftp.variables.vsmo_pls_variable_type import VsmoPlsVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VsmoTmpVariableType as vsmo_tmp_variable_type

class VsmoTmpVariableType(GenericVariableType):
	'''Describes the Fanuc type VSMO_TMP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vsmo_tmp_variable_type()
		else:
			self._instance = _internal

	@property
	def snap_stat(self) -> int:
		'''Value of variable $SNAP_STAT'''
		return self._instance.SnapStat

	@property
	def snap_time_h(self) -> int:
		'''Value of variable $SNAP_TIME_H'''
		return self._instance.SnapTimeH

	@property
	def snap_time_l(self) -> int:
		'''Value of variable $SNAP_TIME_L'''
		return self._instance.SnapTimeL

	@property
	def prv1_time_h(self) -> int:
		'''Value of variable $PRV1_TIME_H'''
		return self._instance.Prv1TimeH

	@property
	def prv1_time_l(self) -> int:
		'''Value of variable $PRV1_TIME_L'''
		return self._instance.Prv1TimeL

	@property
	def prv2_time_h(self) -> int:
		'''Value of variable $PRV2_TIME_H'''
		return self._instance.Prv2TimeH

	@property
	def prv2_time_l(self) -> int:
		'''Value of variable $PRV2_TIME_L'''
		return self._instance.Prv2TimeL

	@property
	def prv1_pls(self) -> typing.List[VsmoPlsVariableType]:
		'''Value of variable $PRV1_PLS'''
		return [VsmoPlsVariableType(x) for x in self._instance.Prv1Pls]

	@property
	def prv2_pls(self) -> typing.List[VsmoPlsVariableType]:
		'''Value of variable $PRV2_PLS'''
		return [VsmoPlsVariableType(x) for x in self._instance.Prv2Pls]

	@property
	def robot_group(self) -> int:
		'''Value of variable $ROBOT_GROUP'''
		return self._instance.RobotGroup

	@property
	def snap_pls(self) -> VsmoPlsVariableType:
		'''Value of variable $SNAP_PLS'''
		return VsmoPlsVariableType(self._instance.SnapPls)

	@property
	def prv_snp_pls(self) -> VsmoPlsVariableType:
		'''Value of variable $PRV_SNP_PLS'''
		return VsmoPlsVariableType(self._instance.PrvSnpPls)

	@property
	def pst_snp_pls(self) -> VsmoPlsVariableType:
		'''Value of variable $PST_SNP_PLS'''
		return VsmoPlsVariableType(self._instance.PstSnpPls)

	@property
	def diff_time(self) -> float:
		'''Value of variable $DIFF_TIME'''
		return self._instance.DiffTime

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VsmoTmpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
