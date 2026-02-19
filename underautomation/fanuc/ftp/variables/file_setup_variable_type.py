import typing
from underautomation.fanuc.ftp.variables.filecomp_variable_type import FilecompVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import FileSetupVariableType as file_setup_variable_type

class FileSetupVariableType(GenericVariableType):
	'''Describes the Fanuc type FILE_SETUP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_setup_variable_type()
		else:
			self._instance = _internal

	@property
	def file_basept(self) -> int:
		'''Value of variable $FILE_BASEPT'''
		return self._instance.FileBasept

	@property
	def filecomp(self) -> FilecompVariableType:
		'''Value of variable $FILECOMP'''
		return FilecompVariableType(self._instance.Filecomp)

	@property
	def file_mask(self) -> bool:
		'''Value of variable $FILE_MASK'''
		return self._instance.FileMask

	@property
	def file_td_sec(self) -> int:
		'''Value of variable $FILE_TD_SEC'''
		return self._instance.FileTdSec

	@property
	def fat_typ_msk(self) -> int:
		'''Value of variable $FAT_TYP_MSK'''
		return self._instance.FatTypMsk

	@property
	def fal_saf_msk(self) -> int:
		'''Value of variable $FAL_SAF_MSK'''
		return self._instance.FalSafMsk

	@property
	def open_files(self) -> int:
		'''Value of variable $OPEN_FILES'''
		return self._instance.OpenFiles

	@property
	def dbglvl(self) -> int:
		'''Value of variable $DBGLVL'''
		return self._instance.Dbglvl

	@property
	def menu_cntrl(self) -> int:
		'''Value of variable $MENU_CNTRL'''
		return self._instance.MenuCntrl

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileSetupVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
