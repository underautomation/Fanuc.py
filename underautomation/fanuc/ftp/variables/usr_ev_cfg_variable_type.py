import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UsrEvCfgVariableType as usr_ev_cfg_variable_type

class UsrEvCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usr_ev_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def owner_name(self) -> str:
		return self._instance.OwnerName
	@property
	def src_dir(self) -> str:
		return self._instance.SrcDir
	@property
	def dst_dir(self) -> str:
		return self._instance.DstDir
	@property
	def max_tmpfile(self) -> int:
		return self._instance.MaxTmpfile
	@property
	def min_freespc(self) -> int:
		return self._instance.MinFreespc
	@property
	def options(self) -> int:
		return self._instance.Options
	@property
	def reserved1(self) -> int:
		return self._instance.Reserved1
	@property
	def reserved2(self) -> int:
		return self._instance.Reserved2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
