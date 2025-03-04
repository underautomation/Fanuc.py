import typing
from underautomation.fanuc.ftp.variables.user_tool_variable_type import UserToolVariableType
from underautomation.fanuc.ftp.variables.user_ufram_variable_type import UserUframVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UserOffstVariableType as user_offst_variable_type

class UserOffstVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_offst_variable_type()
		else:
			self._instance = _internal
	@property
	def tool_ofst(self) -> typing.List[UserToolVariableType]:
		return [UserToolVariableType(x) for x in self._instance.ToolOfst]
	@property
	def uframe_ofst(self) -> typing.List[UserUframVariableType]:
		return [UserUframVariableType(x) for x in self._instance.UframeOfst]
	@property
	def gun_tip_ofs(self) -> typing.List[float]:
		return self._instance.GunTipOfs
	@property
	def gun_cyc_ofs(self) -> typing.List[float]:
		return self._instance.GunCycOfs
	@property
	def enb_subnum(self) -> typing.List[bool]:
		return self._instance.EnbSubnum
	@property
	def pre_exe_adv(self) -> bool:
		return self._instance.PreExeAdv
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
