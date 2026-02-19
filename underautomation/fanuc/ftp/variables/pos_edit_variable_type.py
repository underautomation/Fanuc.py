import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import PosEditVariableType as pos_edit_variable_type

class PosEditVariableType(GenericVariableType):
	'''Describes the Fanuc type POS_EDIT_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pos_edit_variable_type()
		else:
			self._instance = _internal

	@property
	def lock_posnum(self) -> bool:
		'''Value of variable $LOCK_POSNUM'''
		return self._instance.LockPosnum

	@property
	def hide_menu(self) -> bool:
		'''Value of variable $HIDE_MENU'''
		return self._instance.HideMenu

	@property
	def hide_posnum(self) -> bool:
		'''Value of variable $HIDE_POSNUM'''
		return self._instance.HidePosnum

	@property
	def auto_renum(self) -> bool:
		'''Value of variable $AUTO_RENUM'''
		return self._instance.AutoRenum

	@property
	def copy_posdat(self) -> bool:
		'''Value of variable $COPY_POSDAT'''
		return self._instance.CopyPosdat

	@property
	def auto_renum2(self) -> bool:
		'''Value of variable $AUTO_RENUM2'''
		return self._instance.AutoRenum2

	@property
	def rmv_manrenm(self) -> bool:
		'''Value of variable $RMV_MANRENM'''
		return self._instance.RmvManrenm

	@property
	def copy_postyp(self) -> int:
		'''Value of variable $COPY_POSTYP'''
		return self._instance.CopyPostyp

	@property
	def cprut_enb(self) -> bool:
		'''Value of variable $CPRUT_ENB'''
		return self._instance.CprutEnb

	@property
	def conf_touch(self) -> bool:
		'''Value of variable $CONF_TOUCH'''
		return self._instance.ConfTouch

	@property
	def gun_touch(self) -> bool:
		'''Value of variable $GUN_TOUCH'''
		return self._instance.GunTouch

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PosEditVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
