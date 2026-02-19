import typing
from underautomation.fanuc.ftp.variables.vcal_vd_variable_type import VcalVdVariableType
from underautomation.fanuc.ftp.variables.vcal_vf_variable_type import VcalVfVariableType
from underautomation.fanuc.ftp.variables.vcal_mv_variable_type import VcalMvVariableType
from underautomation.fanuc.ftp.variables.vtcpset_variable_type import VtcpsetVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import VcmrinitFile as vcmrinit_file

class VcmrinitFile(GenericVariableFile):
	'''Describes the Fanuc variable file vcmrinit.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcmrinit_file()
		else:
			self._instance = _internal

	@property
	def vdetect_var(self) -> VcalVdVariableType:
		'''Value of variable VDETECT_VAR'''
		return VcalVdVariableType(self._instance.VdetectVar)

	@property
	def vfb_var(self) -> VcalVfVariableType:
		'''Value of variable VFB_VAR'''
		return VcalVfVariableType(self._instance.VfbVar)

	@property
	def move_var(self) -> VcalMvVariableType:
		'''Value of variable MOVE_VAR'''
		return VcalMvVariableType(self._instance.MoveVar)

	@property
	def vtcp_var(self) -> VtcpsetVariableType:
		'''Value of variable VTCP_VAR'''
		return VtcpsetVariableType(self._instance.VtcpVar)

	@property
	def select_grp(self) -> int:
		'''Value of variable SELECT_GRP'''
		return self._instance.SelectGrp

	@property
	def arg_str(self) -> str:
		'''Value of variable ARG_STR'''
		return self._instance.ArgStr

	@property
	def data_type(self) -> int:
		'''Value of variable DATA_TYPE'''
		return self._instance.DataType

	@property
	def dmy_int(self) -> int:
		'''Value of variable DMY_INT'''
		return self._instance.DmyInt

	@property
	def dmy_real(self) -> float:
		'''Value of variable DMY_REAL'''
		return self._instance.DmyReal

	@property
	def dmy_str(self) -> str:
		'''Value of variable DMY_STR'''
		return self._instance.DmyStr

	@property
	def dmy_stat(self) -> int:
		'''Value of variable DMY_STAT'''
		return self._instance.DmyStat

	@property
	def param_val(self) -> str:
		'''Value of variable PARAM_VAL'''
		return self._instance.ParamVal

	@property
	def prm_set_done(self) -> bool:
		'''Value of variable PRM_SET_DONE'''
		return self._instance.PrmSetDone

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VcmrinitFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
