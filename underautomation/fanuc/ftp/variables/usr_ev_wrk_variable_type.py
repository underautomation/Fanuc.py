import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import UsrEvWrkVariableType as usr_ev_wrk_variable_type

class UsrEvWrkVariableType(GenericVariableType):
	'''Describes the Fanuc type USR_EV_WRK_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usr_ev_wrk_variable_type()
		else:
			self._instance = _internal

	@property
	def work_name(self) -> str:
		'''Value of variable $WORK_NAME'''
		return self._instance.WorkName

	@property
	def start_copy(self) -> bool:
		'''Value of variable $START_COPY'''
		return self._instance.StartCopy

	@property
	def num_in_fil(self) -> int:
		'''Value of variable $NUM_IN_FIL'''
		return self._instance.NumInFil

	@property
	def num_out_fil(self) -> int:
		'''Value of variable $NUM_OUT_FIL'''
		return self._instance.NumOutFil

	@property
	def wait_ctr(self) -> int:
		'''Value of variable $WAIT_CTR'''
		return self._instance.WaitCtr

	@property
	def work1(self) -> int:
		'''Value of variable $WORK1'''
		return self._instance.Work1

	@property
	def work2(self) -> int:
		'''Value of variable $WORK2'''
		return self._instance.Work2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UsrEvWrkVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
