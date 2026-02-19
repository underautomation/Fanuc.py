import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import BackEditVariableType as back_edit_variable_type

class BackEditVariableType(GenericVariableType):
	'''Describes the Fanuc type BACK_EDIT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = back_edit_variable_type()
		else:
			self._instance = _internal

	@property
	def program(self) -> str:
		'''Value of variable $PROGRAM'''
		return self._instance.Program

	@property
	def src_name(self) -> str:
		'''Value of variable $SRC_NAME'''
		return self._instance.SrcName

	@property
	def ept_idx(self) -> int:
		'''Value of variable $EPT_IDX'''
		return self._instance.EptIdx

	@property
	def open_id(self) -> int:
		'''Value of variable $OPEN_ID'''
		return self._instance.OpenId

	@property
	def delete_ok(self) -> bool:
		'''Value of variable $DELETE_OK'''
		return self._instance.DeleteOk

	@property
	def used_tp_crt(self) -> int:
		'''Value of variable $USED_TP_CRT'''
		return self._instance.UsedTpCrt

	@property
	def backup_name(self) -> str:
		'''Value of variable $BACKUP_NAME'''
		return self._instance.BackupName

	@property
	def replacing(self) -> bool:
		'''Value of variable $REPLACING'''
		return self._instance.Replacing

	@property
	def bck_comment(self) -> str:
		'''Value of variable $BCK_COMMENT'''
		return self._instance.BckComment

	@property
	def d_replacing(self) -> int:
		'''Value of variable $D_REPLACING'''
		return self._instance.DReplacing

	@property
	def sel_program(self) -> str:
		'''Value of variable $SEL_PROGRAM'''
		return self._instance.SelProgram

	@property
	def dummy12(self) -> int:
		'''Value of variable $DUMMY12'''
		return self._instance.Dummy12

	@property
	def dummy13(self) -> int:
		'''Value of variable $DUMMY13'''
		return self._instance.Dummy13

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BackEditVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
