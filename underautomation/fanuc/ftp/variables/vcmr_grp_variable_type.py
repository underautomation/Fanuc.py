import typing
from underautomation.fanuc.ftp.variables.camera_variable_type import CameraVariableType
from underautomation.fanuc.ftp.variables.vcmr_trgt_variable_type import VcmrTrgtVariableType
from underautomation.fanuc.ftp.variables.create_prg_variable_type import CreatePrgVariableType
from underautomation.fanuc.ftp.variables.chk_result_variable_type import ChkResultVariableType
from underautomation.fanuc.ftp.variables.recovery_variable_type import RecoveryVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcmrGrpVariableType as vcmr_grp_variable_type

class VcmrGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcmr_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def stat_flags(self) -> int:
		return self._instance.StatFlags
	@property
	def menu_code(self) -> int:
		return self._instance.MenuCode
	@property
	def group_num(self) -> int:
		return self._instance.GroupNum
	@property
	def utool_num(self) -> int:
		return self._instance.UtoolNum
	@property
	def camera(self) -> CameraVariableType:
		return CameraVariableType(self._instance.Camera)
	@property
	def target_id(self) -> typing.List[VcmrTrgtVariableType]:
		return [VcmrTrgtVariableType(x) for x in self._instance.TargetId]
	@property
	def create_prg(self) -> CreatePrgVariableType:
		return CreatePrgVariableType(self._instance.CreatePrg)
	@property
	def data_id(self) -> int:
		return self._instance.DataId
	@property
	def chk_result(self) -> ChkResultVariableType:
		return ChkResultVariableType(self._instance.ChkResult)
	@property
	def recovery(self) -> RecoveryVariableType:
		return RecoveryVariableType(self._instance.Recovery)
	@property
	def ext_int1(self) -> int:
		return self._instance.ExtInt1
	@property
	def ext_int2(self) -> int:
		return self._instance.ExtInt2
	@property
	def ext_int3(self) -> int:
		return self._instance.ExtInt3
	@property
	def ext_int4(self) -> int:
		return self._instance.ExtInt4
	@property
	def ext_real1(self) -> float:
		return self._instance.ExtReal1
	@property
	def ext_real2(self) -> float:
		return self._instance.ExtReal2
	@property
	def ext_real3(self) -> float:
		return self._instance.ExtReal3
	@property
	def ext_real4(self) -> float:
		return self._instance.ExtReal4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
