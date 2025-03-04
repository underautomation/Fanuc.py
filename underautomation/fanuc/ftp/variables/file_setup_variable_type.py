import typing
from underautomation.fanuc.ftp.variables.filecomp_variable_type import FilecompVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import FileSetupVariableType as file_setup_variable_type

class FileSetupVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_setup_variable_type()
		else:
			self._instance = _internal
	@property
	def file_basept(self) -> int:
		return self._instance.FileBasept
	@property
	def filecomp(self) -> FilecompVariableType:
		return FilecompVariableType(self._instance.Filecomp)
	@property
	def file_mask(self) -> bool:
		return self._instance.FileMask
	@property
	def file_td_sec(self) -> int:
		return self._instance.FileTdSec
	@property
	def fat_typ_msk(self) -> int:
		return self._instance.FatTypMsk
	@property
	def fal_saf_msk(self) -> int:
		return self._instance.FalSafMsk
	@property
	def open_files(self) -> int:
		return self._instance.OpenFiles
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def menu_cntrl(self) -> int:
		return self._instance.MenuCntrl
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
