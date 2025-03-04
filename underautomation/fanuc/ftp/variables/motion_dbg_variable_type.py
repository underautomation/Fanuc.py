import typing
from underautomation.fanuc.ftp.variables.mgdebug_variable_type import MgdebugVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MotionDbgVariableType as motion_dbg_variable_type

class MotionDbgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_dbg_variable_type()
		else:
			self._instance = _internal
	@property
	def output(self) -> bool:
		return self._instance.Output
	@property
	def mgdebug(self) -> MgdebugVariableType:
		return MgdebugVariableType(self._instance.Mgdebug)
	@property
	def midebug(self) -> MgdebugVariableType:
		return MgdebugVariableType(self._instance.Midebug)
	@property
	def mpdebug(self) -> MgdebugVariableType:
		return MgdebugVariableType(self._instance.Mpdebug)
	@property
	def midebug_itp(self) -> MgdebugVariableType:
		return MgdebugVariableType(self._instance.MidebugItp)
	@property
	def pgdebug(self) -> MgdebugVariableType:
		return MgdebugVariableType(self._instance.Pgdebug)
	@property
	def keep(self) -> bool:
		return self._instance.Keep
	@property
	def path(self) -> str:
		return self._instance.Path
	@property
	def bin_output(self) -> int:
		return self._instance.BinOutput
	@property
	def snd2server(self) -> bool:
		return self._instance.Snd2server
	@property
	def bin2_txt(self) -> int:
		return self._instance.Bin2Txt
	@property
	def extra1(self) -> int:
		return self._instance.Extra1
	@property
	def extra2(self) -> int:
		return self._instance.Extra2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
