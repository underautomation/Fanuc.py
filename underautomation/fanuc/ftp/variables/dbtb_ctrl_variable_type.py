import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import DbtbCtrlVariableType as dbtb_ctrl_variable_type

class DbtbCtrlVariableType(GenericVariableType):
	'''Describes the Fanuc type DBTB_CTRL_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbtb_ctrl_variable_type()
		else:
			self._instance = _internal

	@property
	def acrt_mode(self) -> bool:
		'''Value of variable $ACRT_MODE'''
		return self._instance.AcrtMode

	@property
	def mindt_adj(self) -> bool:
		'''Value of variable $MINDT_ADJ'''
		return self._instance.MindtAdj

	@property
	def delay_call(self) -> int:
		'''Value of variable $DELAY_CALL'''
		return self._instance.DelayCall

	@property
	def delay_do(self) -> int:
		'''Value of variable $DELAY_DO'''
		return self._instance.DelayDo

	@property
	def delay_pls(self) -> int:
		'''Value of variable $DELAY_PLS'''
		return self._instance.DelayPls

	@property
	def rsm_wait(self) -> int:
		'''Value of variable $RSM_WAIT'''
		return self._instance.RsmWait

	@property
	def reserved2(self) -> int:
		'''Value of variable $RESERVED2'''
		return self._instance.Reserved2

	@property
	def reserved3(self) -> int:
		'''Value of variable $RESERVED3'''
		return self._instance.Reserved3

	@property
	def num_io(self) -> int:
		'''Value of variable $NUM_IO'''
		return self._instance.NumIo

	@property
	def dummy9(self) -> int:
		'''Value of variable $DUMMY9'''
		return self._instance.Dummy9

	@property
	def dummy10(self) -> int:
		'''Value of variable $DUMMY10'''
		return self._instance.Dummy10

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DbtbCtrlVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
