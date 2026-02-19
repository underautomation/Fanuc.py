import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MndspMstVariableType as mndsp_mst_variable_type

class MndspMstVariableType(GenericVariableType):
	'''Describes the Fanuc type MNDSP_MST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mndsp_mst_variable_type()
		else:
			self._instance = _internal

	@property
	def disp_enable(self) -> bool:
		'''Value of variable $DISP_ENABLE'''
		return self._instance.DispEnable

	@property
	def disp_edcmd(self) -> bool:
		'''Value of variable $DISP_EDCMD'''
		return self._instance.DispEdcmd

	@property
	def disp_inauto(self) -> bool:
		'''Value of variable $DISP_INAUTO'''
		return self._instance.DispInauto

	@property
	def disp_rsmdis(self) -> bool:
		'''Value of variable $DISP_RSMDIS'''
		return self._instance.DispRsmdis

	@property
	def disp_is_on(self) -> bool:
		'''Value of variable $DISP_IS_ON'''
		return self._instance.DispIsOn

	@property
	def mode_grp(self) -> typing.List[int]:
		'''Value of variable $MODE_GRP'''
		return self._instance.ModeGrp

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MndspMstVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
