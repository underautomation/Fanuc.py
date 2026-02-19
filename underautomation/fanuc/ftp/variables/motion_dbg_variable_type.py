import typing
from underautomation.fanuc.ftp.variables.mgdebug_variable_type import MgdebugVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import MotionDbgVariableType as motion_dbg_variable_type

class MotionDbgVariableType(GenericVariableType):
	'''Describes the Fanuc type MOTION_DBG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_dbg_variable_type()
		else:
			self._instance = _internal

	@property
	def output(self) -> bool:
		'''Value of variable $OUTPUT'''
		return self._instance.Output

	@property
	def mgdebug(self) -> MgdebugVariableType:
		'''Value of variable $MGDEBUG'''
		return MgdebugVariableType(self._instance.Mgdebug)

	@property
	def midebug(self) -> MgdebugVariableType:
		'''Value of variable $MIDEBUG'''
		return MgdebugVariableType(self._instance.Midebug)

	@property
	def mpdebug(self) -> MgdebugVariableType:
		'''Value of variable $MPDEBUG'''
		return MgdebugVariableType(self._instance.Mpdebug)

	@property
	def midebug_itp(self) -> MgdebugVariableType:
		'''Value of variable $MIDEBUG_ITP'''
		return MgdebugVariableType(self._instance.MidebugItp)

	@property
	def pgdebug(self) -> MgdebugVariableType:
		'''Value of variable $PGDEBUG'''
		return MgdebugVariableType(self._instance.Pgdebug)

	@property
	def keep(self) -> bool:
		'''Value of variable $KEEP'''
		return self._instance.Keep

	@property
	def path(self) -> str:
		'''Value of variable $PATH'''
		return self._instance.Path

	@property
	def bin_output(self) -> int:
		'''Value of variable $BIN_OUTPUT'''
		return self._instance.BinOutput

	@property
	def snd2server(self) -> bool:
		'''Value of variable $SND2SERVER'''
		return self._instance.Snd2server

	@property
	def bin2_txt(self) -> int:
		'''Value of variable $BIN_2_TXT'''
		return self._instance.Bin2Txt

	@property
	def extra1(self) -> int:
		'''Value of variable $EXTRA1'''
		return self._instance.Extra1

	@property
	def extra2(self) -> int:
		'''Value of variable $EXTRA2'''
		return self._instance.Extra2

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionDbgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
