import typing
from underautomation.fanuc.ftp.variables.camera_variable_type import CameraVariableType
from underautomation.fanuc.ftp.variables.vcmr_trgt_variable_type import VcmrTrgtVariableType
from underautomation.fanuc.ftp.variables.create_prg_variable_type import CreatePrgVariableType
from underautomation.fanuc.ftp.variables.chk_result_variable_type import ChkResultVariableType
from underautomation.fanuc.ftp.variables.recovery_variable_type import RecoveryVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import VcmrGrpVariableType as vcmr_grp_variable_type

class VcmrGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type VCMR_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcmr_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def stat_flags(self) -> int:
		'''Value of variable $STAT_FLAGS'''
		return self._instance.StatFlags

	@property
	def menu_code(self) -> int:
		'''Value of variable $MENU_CODE'''
		return self._instance.MenuCode

	@property
	def group_num(self) -> int:
		'''Value of variable $GROUP_NUM'''
		return self._instance.GroupNum

	@property
	def utool_num(self) -> int:
		'''Value of variable $UTOOL_NUM'''
		return self._instance.UtoolNum

	@property
	def camera(self) -> CameraVariableType:
		'''Value of variable $CAMERA'''
		return CameraVariableType(self._instance.Camera)

	@property
	def target_id(self) -> typing.List[VcmrTrgtVariableType]:
		'''Value of variable $TARGET_ID'''
		return [VcmrTrgtVariableType(x) for x in self._instance.TargetId]

	@property
	def create_prg(self) -> CreatePrgVariableType:
		'''Value of variable $CREATE_PRG'''
		return CreatePrgVariableType(self._instance.CreatePrg)

	@property
	def data_id(self) -> int:
		'''Value of variable $DATA_ID'''
		return self._instance.DataId

	@property
	def chk_result(self) -> ChkResultVariableType:
		'''Value of variable $CHK_RESULT'''
		return ChkResultVariableType(self._instance.ChkResult)

	@property
	def recovery(self) -> RecoveryVariableType:
		'''Value of variable $RECOVERY'''
		return RecoveryVariableType(self._instance.Recovery)

	@property
	def ext_int1(self) -> int:
		'''Value of variable $EXT_INT1'''
		return self._instance.ExtInt1

	@property
	def ext_int2(self) -> int:
		'''Value of variable $EXT_INT2'''
		return self._instance.ExtInt2

	@property
	def ext_int3(self) -> int:
		'''Value of variable $EXT_INT3'''
		return self._instance.ExtInt3

	@property
	def ext_int4(self) -> int:
		'''Value of variable $EXT_INT4'''
		return self._instance.ExtInt4

	@property
	def ext_real1(self) -> float:
		'''Value of variable $EXT_REAL1'''
		return self._instance.ExtReal1

	@property
	def ext_real2(self) -> float:
		'''Value of variable $EXT_REAL2'''
		return self._instance.ExtReal2

	@property
	def ext_real3(self) -> float:
		'''Value of variable $EXT_REAL3'''
		return self._instance.ExtReal3

	@property
	def ext_real4(self) -> float:
		'''Value of variable $EXT_REAL4'''
		return self._instance.ExtReal4

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcmrGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
