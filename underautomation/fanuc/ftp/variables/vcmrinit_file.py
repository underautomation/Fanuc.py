import typing
from underautomation.fanuc.ftp.variables.vcal_vd_variable_type import VcalVdVariableType
from underautomation.fanuc.ftp.variables.vcal_vf_variable_type import VcalVfVariableType
from underautomation.fanuc.ftp.variables.vcal_mv_variable_type import VcalMvVariableType
from underautomation.fanuc.ftp.variables.vtcpset_variable_type import VtcpsetVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import VcmrinitFile as vcmrinit_file

class VcmrinitFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vcmrinit_file()
		else:
			self._instance = _internal
	@property
	def vdetect_var(self) -> VcalVdVariableType:
		return VcalVdVariableType(self._instance.VdetectVar)
	@property
	def vfb_var(self) -> VcalVfVariableType:
		return VcalVfVariableType(self._instance.VfbVar)
	@property
	def move_var(self) -> VcalMvVariableType:
		return VcalMvVariableType(self._instance.MoveVar)
	@property
	def vtcp_var(self) -> VtcpsetVariableType:
		return VtcpsetVariableType(self._instance.VtcpVar)
	@property
	def select_grp(self) -> int:
		return self._instance.SelectGrp
	@property
	def arg_str(self) -> str:
		return self._instance.ArgStr
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def dmy_int(self) -> int:
		return self._instance.DmyInt
	@property
	def dmy_real(self) -> float:
		return self._instance.DmyReal
	@property
	def dmy_str(self) -> str:
		return self._instance.DmyStr
	@property
	def dmy_stat(self) -> int:
		return self._instance.DmyStat
	@property
	def param_val(self) -> str:
		return self._instance.ParamVal
	@property
	def prm_set_done(self) -> bool:
		return self._instance.PrmSetDone
