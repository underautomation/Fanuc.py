import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UsrEvCfgVariableType as usr_ev_cfg_variable_type

class UsrEvCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type USR_EV_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usr_ev_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Value of variable $ENABLE'''
		return self._instance.Enable

	@property
	def owner_name(self) -> str:
		'''Value of variable $OWNER_NAME'''
		return self._instance.OwnerName

	@property
	def src_dir(self) -> str:
		'''Value of variable $SRC_DIR'''
		return self._instance.SrcDir

	@property
	def dst_dir(self) -> str:
		'''Value of variable $DST_DIR'''
		return self._instance.DstDir

	@property
	def max_tmpfile(self) -> int:
		'''Value of variable $MAX_TMPFILE'''
		return self._instance.MaxTmpfile

	@property
	def min_freespc(self) -> int:
		'''Value of variable $MIN_FREESPC'''
		return self._instance.MinFreespc

	@property
	def options(self) -> int:
		'''Value of variable $OPTIONS'''
		return self._instance.Options

	@property
	def reserved1(self) -> int:
		'''Value of variable $RESERVED1'''
		return self._instance.Reserved1

	@property
	def reserved2(self) -> int:
		'''Value of variable $RESERVED2'''
		return self._instance.Reserved2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UsrEvCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
