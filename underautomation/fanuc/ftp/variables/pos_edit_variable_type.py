import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PosEditVariableType as pos_edit_variable_type

class PosEditVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pos_edit_variable_type()
		else:
			self._instance = _internal
	@property
	def lock_posnum(self) -> bool:
		return self._instance.LockPosnum
	@property
	def hide_menu(self) -> bool:
		return self._instance.HideMenu
	@property
	def hide_posnum(self) -> bool:
		return self._instance.HidePosnum
	@property
	def auto_renum(self) -> bool:
		return self._instance.AutoRenum
	@property
	def copy_posdat(self) -> bool:
		return self._instance.CopyPosdat
	@property
	def auto_renum2(self) -> bool:
		return self._instance.AutoRenum2
	@property
	def rmv_manrenm(self) -> bool:
		return self._instance.RmvManrenm
	@property
	def copy_postyp(self) -> int:
		return self._instance.CopyPostyp
	@property
	def cprut_enb(self) -> bool:
		return self._instance.CprutEnb
	@property
	def conf_touch(self) -> bool:
		return self._instance.ConfTouch
	@property
	def gun_touch(self) -> bool:
		return self._instance.GunTouch
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
