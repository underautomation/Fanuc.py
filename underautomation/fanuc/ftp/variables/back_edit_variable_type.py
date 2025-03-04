import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import BackEditVariableType as back_edit_variable_type

class BackEditVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = back_edit_variable_type()
		else:
			self._instance = _internal
	@property
	def program(self) -> str:
		return self._instance.Program
	@property
	def src_name(self) -> str:
		return self._instance.SrcName
	@property
	def ept_idx(self) -> int:
		return self._instance.EptIdx
	@property
	def open_id(self) -> int:
		return self._instance.OpenId
	@property
	def delete_ok(self) -> bool:
		return self._instance.DeleteOk
	@property
	def used_tp_crt(self) -> int:
		return self._instance.UsedTpCrt
	@property
	def backup_name(self) -> str:
		return self._instance.BackupName
	@property
	def replacing(self) -> bool:
		return self._instance.Replacing
	@property
	def bck_comment(self) -> str:
		return self._instance.BckComment
	@property
	def d_replacing(self) -> int:
		return self._instance.DReplacing
	@property
	def sel_program(self) -> str:
		return self._instance.SelProgram
	@property
	def dummy12(self) -> int:
		return self._instance.Dummy12
	@property
	def dummy13(self) -> int:
		return self._instance.Dummy13
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
