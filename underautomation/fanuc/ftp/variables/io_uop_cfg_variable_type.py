import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import IoUopCfgVariableType as io_uop_cfg_variable_type

class IoUopCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type IO_UOP_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_uop_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def uop_type(self) -> int:
		'''Value of variable $UOP_TYPE'''
		return self._instance.UopType

	@property
	def in_rack(self) -> int:
		'''Value of variable $IN_RACK'''
		return self._instance.InRack

	@property
	def in_slot(self) -> int:
		'''Value of variable $IN_SLOT'''
		return self._instance.InSlot

	@property
	def in_strtpt(self) -> int:
		'''Value of variable $IN_STRTPT'''
		return self._instance.InStrtpt

	@property
	def out_rack(self) -> int:
		'''Value of variable $OUT_RACK'''
		return self._instance.OutRack

	@property
	def out_slot(self) -> int:
		'''Value of variable $OUT_SLOT'''
		return self._instance.OutSlot

	@property
	def out_strtpt(self) -> int:
		'''Value of variable $OUT_STRTPT'''
		return self._instance.OutStrtpt

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoUopCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
