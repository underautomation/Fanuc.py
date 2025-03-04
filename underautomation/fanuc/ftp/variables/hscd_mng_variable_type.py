import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import HscdMngVariableType as hscd_mng_variable_type

class HscdMngVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = hscd_mng_variable_type()
		else:
			self._instance = _internal
	@property
	def coll_mode(self) -> bool:
		return self._instance.CollMode
	@property
	def threshold(self) -> int:
		return self._instance.Threshold
	@property
	def do_err(self) -> int:
		return self._instance.DoErr
	@property
	def do_enable(self) -> int:
		return self._instance.DoEnable
	@property
	def macro_reg(self) -> int:
		return self._instance.MacroReg
	@property
	def stnd_cd(self) -> int:
		return self._instance.StndCd
	@property
	def auto_reset(self) -> int:
		return self._instance.AutoReset
	@property
	def upd_groups(self) -> int:
		return self._instance.UpdGroups
	@property
	def param_verid(self) -> str:
		return self._instance.ParamVerid
	@property
	def param119(self) -> typing.List[int]:
		return self._instance.Param119
	@property
	def param120(self) -> typing.List[int]:
		return self._instance.Param120
	@property
	def param121(self) -> typing.List[int]:
		return self._instance.Param121
	@property
	def param122(self) -> typing.List[int]:
		return self._instance.Param122
	@property
	def param123(self) -> typing.List[int]:
		return self._instance.Param123
	@property
	def param124(self) -> typing.List[int]:
		return self._instance.Param124
	@property
	def param125(self) -> typing.List[int]:
		return self._instance.Param125
	@property
	def act_ratio(self) -> int:
		return self._instance.ActRatio
	@property
	def saved119(self) -> typing.List[int]:
		return self._instance.Saved119
	@property
	def saved120(self) -> typing.List[int]:
		return self._instance.Saved120
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
