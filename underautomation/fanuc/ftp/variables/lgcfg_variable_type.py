import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LgcfgVariableType as lgcfg_variable_type

class LgcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = lgcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def lg_size(self) -> int:
		return self._instance.LgSize
	@property
	def ev_size(self) -> int:
		return self._instance.EvSize
	@property
	def mr_size(self) -> int:
		return self._instance.MrSize
	@property
	def sg_size(self) -> int:
		return self._instance.SgSize
	@property
	def fd_size(self) -> int:
		return self._instance.FdSize
	@property
	def mi_size(self) -> int:
		return self._instance.MiSize
	@property
	def er_size(self) -> int:
		return self._instance.ErSize
	@property
	def mp_size(self) -> int:
		return self._instance.MpSize
	@property
	def mg_size(self) -> int:
		return self._instance.MgSize
	@property
	def pe_size(self) -> int:
		return self._instance.PeSize
	@property
	def sv_size(self) -> int:
		return self._instance.SvSize
	@property
	def lg_mode(self) -> int:
		return self._instance.LgMode
	@property
	def ev_mode(self) -> int:
		return self._instance.EvMode
	@property
	def mr_mode(self) -> int:
		return self._instance.MrMode
	@property
	def sg_mode(self) -> int:
		return self._instance.SgMode
	@property
	def fd_mode(self) -> int:
		return self._instance.FdMode
	@property
	def pe_mode(self) -> int:
		return self._instance.PeMode
	@property
	def comp_sw(self) -> int:
		return self._instance.CompSw
	@property
	def tol_rot_cmd(self) -> float:
		return self._instance.TolRotCmd
	@property
	def tol_lin_cmd(self) -> float:
		return self._instance.TolLinCmd
	@property
	def tol_rot_fb(self) -> float:
		return self._instance.TolRotFb
	@property
	def tol_lin_fb(self) -> float:
		return self._instance.TolLinFb
	@property
	def lg_path(self) -> str:
		return self._instance.LgPath
	@property
	def lg_file(self) -> str:
		return self._instance.LgFile
	@property
	def ev_file(self) -> str:
		return self._instance.EvFile
	@property
	def mr_file(self) -> str:
		return self._instance.MrFile
	@property
	def sg_file(self) -> str:
		return self._instance.SgFile
	@property
	def fd_file(self) -> str:
		return self._instance.FdFile
	@property
	def mi_file(self) -> str:
		return self._instance.MiFile
	@property
	def er_file(self) -> str:
		return self._instance.ErFile
	@property
	def mp_file(self) -> str:
		return self._instance.MpFile
	@property
	def pe_file(self) -> str:
		return self._instance.PeFile
	@property
	def sv_file(self) -> str:
		return self._instance.SvFile
	@property
	def lg_zipdump(self) -> int:
		return self._instance.LgZipdump
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
