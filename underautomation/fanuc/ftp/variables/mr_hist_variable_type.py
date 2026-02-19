import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MrHistVariableType as mr_hist_variable_type

class MrHistVariableType(GenericVariableType):
	'''Describes the Fanuc type MR_HIST_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mr_hist_variable_type()
		else:
			self._instance = _internal

	@property
	def group(self) -> int:
		'''Value of variable $GROUP'''
		return self._instance.Group

	@property
	def id(self) -> int:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def type(self) -> int:
		'''Value of variable $TYPE'''
		return self._instance.Type

	@property
	def due_type(self) -> int:
		'''Value of variable $DUE_TYPE'''
		return self._instance.DueType

	@property
	def name(self) -> str:
		'''Value of variable $NAME'''
		return self._instance.Name

	@property
	def due_act(self) -> int:
		'''Value of variable $DUE_ACT'''
		return self._instance.DueAct

	@property
	def due_date(self) -> float:
		'''Value of variable $DUE_DATE'''
		return self._instance.DueDate

	@property
	def warn_date(self) -> int:
		'''Value of variable $WARN_DATE'''
		return self._instance.WarnDate

	@property
	def done(self) -> bool:
		'''Value of variable $DONE'''
		return self._instance.Done

	@property
	def done_date(self) -> int:
		'''Value of variable $DONE_DATE'''
		return self._instance.DoneDate

	@property
	def done_past(self) -> str:
		'''Value of variable $DONE_PAST'''
		return self._instance.DonePast

	@property
	def recorded(self) -> bool:
		'''Value of variable $RECORDED'''
		return self._instance.Recorded

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MrHistVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
