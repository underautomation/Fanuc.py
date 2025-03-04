import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MnMcrTableVariableType as mn_mcr_table_variable_type

class MnMcrTableVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mn_mcr_table_variable_type()
		else:
			self._instance = _internal
	@property
	def macro_name(self) -> str:
		return self._instance.MacroName
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def ept_index(self) -> int:
		return self._instance.EptIndex
	@property
	def open_id(self) -> int:
		return self._instance.OpenId
	@property
	def assign_type(self) -> int:
		return self._instance.AssignType
	@property
	def assign_id(self) -> int:
		return self._instance.AssignId
	@property
	def mon_no(self) -> int:
		return self._instance.MonNo
	@property
	def prev_subtyp(self) -> int:
		return self._instance.PrevSubtyp
	@property
	def user_work(self) -> int:
		return self._instance.UserWork
	@property
	def sys_lev_msk(self) -> int:
		return self._instance.SysLevMsk
	@property
	def mcr_rtn(self) -> int:
		return self._instance.McrRtn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
