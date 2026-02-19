import typing
from underautomation.fanuc.ftp.variables.resume_ofst_variable_type import ResumeOfstVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CpcfgVariableType as cpcfg_variable_type

class CpcfgVariableType(GenericVariableType):
	'''Describes the Fanuc type CPCFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpcfg_variable_type()
		else:
			self._instance = _internal

	@property
	def group_mask(self) -> int:
		'''Value of variable $GROUP_MASK'''
		return self._instance.GroupMask

	@property
	def cp_debug(self) -> int:
		'''Value of variable $CP_DEBUG'''
		return self._instance.CpDebug

	@property
	def cp_enable(self) -> bool:
		'''Value of variable $CP_ENABLE'''
		return self._instance.CpEnable

	@property
	def comp_switch(self) -> int:
		'''Value of variable $COMP_SWITCH'''
		return self._instance.CompSwitch

	@property
	def extra_int(self) -> typing.List[int]:
		'''Value of variable $EXTRA_INT'''
		return self._instance.ExtraInt

	@property
	def extra_flt(self) -> typing.List[float]:
		'''Value of variable $EXTRA_FLT'''
		return self._instance.ExtraFlt

	@property
	def tf_mode(self) -> int:
		'''Value of variable $TF_MODE'''
		return self._instance.TfMode

	@property
	def md3itptol(self) -> int:
		'''Value of variable $MD3ITPTOL'''
		return self._instance.Md3itptol

	@property
	def resume_ofst(self) -> ResumeOfstVariableType:
		'''Value of variable $RESUME_OFST'''
		return ResumeOfstVariableType(self._instance.ResumeOfst)

	@property
	def cp_hstart(self) -> float:
		'''Value of variable $CP_HSTART'''
		return self._instance.CpHstart

	@property
	def t1_hstart(self) -> float:
		'''Value of variable $T1_HSTART'''
		return self._instance.T1Hstart

	@property
	def test(self) -> typing.List[int]:
		'''Value of variable $TEST'''
		return self._instance.Test

	@property
	def comp_sw2(self) -> int:
		'''Value of variable $COMP_SW2'''
		return self._instance.CompSw2

	@property
	def comp_sw3(self) -> int:
		'''Value of variable $COMP_SW3'''
		return self._instance.CompSw3

	@property
	def comp_sw4(self) -> int:
		'''Value of variable $COMP_SW4'''
		return self._instance.CompSw4

	@property
	def cp_dynt1(self) -> int:
		'''Value of variable $CP_DYNT1'''
		return self._instance.CpDynt1

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CpcfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
