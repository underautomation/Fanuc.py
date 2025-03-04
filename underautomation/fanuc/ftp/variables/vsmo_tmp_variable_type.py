import typing
from underautomation.fanuc.ftp.variables.vsmo_pls_variable_type import VsmoPlsVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VsmoTmpVariableType as vsmo_tmp_variable_type

class VsmoTmpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vsmo_tmp_variable_type()
		else:
			self._instance = _internal
	@property
	def snap_stat(self) -> int:
		return self._instance.SnapStat
	@property
	def snap_time_h(self) -> int:
		return self._instance.SnapTimeH
	@property
	def snap_time_l(self) -> int:
		return self._instance.SnapTimeL
	@property
	def prv1_time_h(self) -> int:
		return self._instance.Prv1TimeH
	@property
	def prv1_time_l(self) -> int:
		return self._instance.Prv1TimeL
	@property
	def prv2_time_h(self) -> int:
		return self._instance.Prv2TimeH
	@property
	def prv2_time_l(self) -> int:
		return self._instance.Prv2TimeL
	@property
	def prv1_pls(self) -> typing.List[VsmoPlsVariableType]:
		return [VsmoPlsVariableType(x) for x in self._instance.Prv1Pls]
	@property
	def prv2_pls(self) -> typing.List[VsmoPlsVariableType]:
		return [VsmoPlsVariableType(x) for x in self._instance.Prv2Pls]
	@property
	def robot_group(self) -> int:
		return self._instance.RobotGroup
	@property
	def snap_pls(self) -> VsmoPlsVariableType:
		return VsmoPlsVariableType(self._instance.SnapPls)
	@property
	def prv_snp_pls(self) -> VsmoPlsVariableType:
		return VsmoPlsVariableType(self._instance.PrvSnpPls)
	@property
	def pst_snp_pls(self) -> VsmoPlsVariableType:
		return VsmoPlsVariableType(self._instance.PstSnpPls)
	@property
	def diff_time(self) -> float:
		return self._instance.DiffTime
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
