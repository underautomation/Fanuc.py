import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ModaqCfgVariableType as modaq_cfg_variable_type

class ModaqCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type MODAQ_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = modaq_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def on_line(self) -> bool:
		'''Value of variable $ON_LINE'''
		return self._instance.OnLine

	@property
	def mf_flag(self) -> int:
		'''Value of variable $MF_FLAG'''
		return self._instance.MfFlag

	@property
	def mi_flag(self) -> int:
		'''Value of variable $MI_FLAG'''
		return self._instance.MiFlag

	@property
	def grp_num(self) -> int:
		'''Value of variable $GRP_NUM'''
		return self._instance.GrpNum

	@property
	def startlog(self) -> int:
		'''Value of variable $STARTLOG'''
		return self._instance.Startlog

	@property
	def endlog(self) -> int:
		'''Value of variable $ENDLOG'''
		return self._instance.Endlog

	@property
	def ln_mask(self) -> int:
		'''Value of variable $LN_MASK'''
		return self._instance.LnMask

	@property
	def support(self) -> int:
		'''Value of variable $SUPPORT'''
		return self._instance.Support

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ModaqCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
