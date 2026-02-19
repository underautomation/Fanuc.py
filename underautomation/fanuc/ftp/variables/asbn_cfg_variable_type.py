import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import AsbnCfgVariableType as asbn_cfg_variable_type

class AsbnCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type ASBN_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = asbn_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def cnv_jnt_pos(self) -> bool:
		'''Value of variable $CNV_JNT_POS'''
		return self._instance.CnvJntPos

	@property
	def data_cmnts(self) -> int:
		'''Value of variable $DATA_CMNTS'''
		return self._instance.DataCmnts

	@property
	def flags(self) -> int:
		'''Value of variable $FLAGS'''
		return self._instance.Flags

	@property
	def pos_check(self) -> bool:
		'''Value of variable $POS_CHECK'''
		return self._instance.PosCheck

	@property
	def check_optn(self) -> int:
		'''Value of variable $CHECK_OPTN'''
		return self._instance.CheckOptn

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AsbnCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
