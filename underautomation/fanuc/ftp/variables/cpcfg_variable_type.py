import typing
from underautomation.fanuc.ftp.variables.resume_ofst_variable_type import ResumeOfstVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpcfgVariableType as cpcfg_variable_type

class CpcfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpcfg_variable_type()
		else:
			self._instance = _internal
	@property
	def group_mask(self) -> int:
		return self._instance.GroupMask
	@property
	def cp_debug(self) -> int:
		return self._instance.CpDebug
	@property
	def cp_enable(self) -> bool:
		return self._instance.CpEnable
	@property
	def comp_switch(self) -> int:
		return self._instance.CompSwitch
	@property
	def extra_int(self) -> typing.List[int]:
		return self._instance.ExtraInt
	@property
	def extra_flt(self) -> typing.List[float]:
		return self._instance.ExtraFlt
	@property
	def tf_mode(self) -> int:
		return self._instance.TfMode
	@property
	def md3itptol(self) -> int:
		return self._instance.Md3itptol
	@property
	def resume_ofst(self) -> ResumeOfstVariableType:
		return ResumeOfstVariableType(self._instance.ResumeOfst)
	@property
	def cp_hstart(self) -> float:
		return self._instance.CpHstart
	@property
	def t1_hstart(self) -> float:
		return self._instance.T1Hstart
	@property
	def test(self) -> typing.List[int]:
		return self._instance.Test
	@property
	def comp_sw2(self) -> int:
		return self._instance.CompSw2
	@property
	def comp_sw3(self) -> int:
		return self._instance.CompSw3
	@property
	def comp_sw4(self) -> int:
		return self._instance.CompSw4
	@property
	def cp_dynt1(self) -> int:
		return self._instance.CpDynt1
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
