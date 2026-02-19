import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SyslogVariableType as syslog_variable_type

class SyslogVariableType(GenericVariableType):
	'''Describes the Fanuc type SYSLOG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = syslog_variable_type()
		else:
			self._instance = _internal

	@property
	def size(self) -> int:
		'''Value of variable $SIZE'''
		return self._instance.Size

	@property
	def mode(self) -> int:
		'''Value of variable $MODE'''
		return self._instance.Mode

	@property
	def status(self) -> int:
		'''Value of variable $STATUS'''
		return self._instance.Status

	@property
	def address(self) -> int:
		'''Value of variable $ADDRESS'''
		return self._instance.Address

	@property
	def data_size(self) -> int:
		'''Value of variable $DATA_SIZE'''
		return self._instance.DataSize

	@property
	def comp_value(self) -> int:
		'''Value of variable $COMP_VALUE'''
		return self._instance.CompValue

	@property
	def stop_mode(self) -> int:
		'''Value of variable $STOP_MODE'''
		return self._instance.StopMode

	@property
	def curr_value(self) -> int:
		'''Value of variable $CURR_VALUE'''
		return self._instance.CurrValue

	@property
	def flog_id_lo(self) -> int:
		'''Value of variable $FLOG_ID_LO'''
		return self._instance.FlogIdLo

	@property
	def flog_id_hi(self) -> int:
		'''Value of variable $FLOG_ID_HI'''
		return self._instance.FlogIdHi

	@property
	def flog_id_in(self) -> bool:
		'''Value of variable $FLOG_ID_IN'''
		return self._instance.FlogIdIn

	@property
	def file_out(self) -> bool:
		'''Value of variable $FILE_OUT'''
		return self._instance.FileOut

	@property
	def file_name(self) -> str:
		'''Value of variable $FILE_NAME'''
		return self._instance.FileName

	@property
	def id(self) -> int:
		'''Value of variable $ID'''
		return self._instance.Id

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SyslogVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
