import typing
from underautomation.fanuc.ftp.variables.tbc_acc_variable_type import TbcAccVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TbccfgVariableType as tbccfg_variable_type

class TbccfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbccfg_variable_type()
		else:
			self._instance = _internal
	@property
	def group_mask(self) -> int:
		return self._instance.GroupMask
	@property
	def mb_conflict(self) -> int:
		return self._instance.MbConflict
	@property
	def mb_required(self) -> int:
		return self._instance.MbRequired
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def tbc_stat(self) -> typing.List[int]:
		return self._instance.TbcStat
	@property
	def tc(self) -> typing.List[TbcAccVariableType]:
		return [TbcAccVariableType(x) for x in self._instance.Tc]
	@property
	def tbc_debug(self) -> int:
		return self._instance.TbcDebug
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
