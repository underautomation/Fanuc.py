import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ItemAccVariableType as item_acc_variable_type

class ItemAccVariableType(GenericVariableType):
	'''Describes the Fanuc type ITEM_ACC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = item_acc_variable_type()
		else:
			self._instance = _internal

	@property
	def time_stamp(self) -> int:
		'''Value of variable $TIME_STAMP'''
		return self._instance.TimeStamp

	@property
	def last_tick(self) -> int:
		'''Value of variable $LAST_TICK'''
		return self._instance.LastTick

	@property
	def on_acc(self) -> int:
		'''Value of variable $ON_ACC'''
		return self._instance.OnAcc

	@property
	def off_acc(self) -> int:
		'''Value of variable $OFF_ACC'''
		return self._instance.OffAcc

	@property
	def elaps_acc(self) -> int:
		'''Value of variable $ELAPS_ACC'''
		return self._instance.ElapsAcc

	@property
	def buff_idx(self) -> int:
		'''Value of variable $BUFF_IDX'''
		return self._instance.BuffIdx

	@property
	def hist_idx(self) -> int:
		'''Value of variable $HIST_IDX'''
		return self._instance.HistIdx

	@property
	def rep_idx(self) -> int:
		'''Value of variable $REP_IDX'''
		return self._instance.RepIdx

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ItemAccVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
