import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DbtbCtrlVariableType as dbtb_ctrl_variable_type

class DbtbCtrlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dbtb_ctrl_variable_type()
		else:
			self._instance = _internal
	@property
	def acrt_mode(self) -> bool:
		return self._instance.AcrtMode
	@property
	def mindt_adj(self) -> bool:
		return self._instance.MindtAdj
	@property
	def delay_call(self) -> int:
		return self._instance.DelayCall
	@property
	def delay_do(self) -> int:
		return self._instance.DelayDo
	@property
	def delay_pls(self) -> int:
		return self._instance.DelayPls
	@property
	def rsm_wait(self) -> int:
		return self._instance.RsmWait
	@property
	def reserved2(self) -> int:
		return self._instance.Reserved2
	@property
	def reserved3(self) -> int:
		return self._instance.Reserved3
	@property
	def num_io(self) -> int:
		return self._instance.NumIo
	@property
	def dummy9(self) -> int:
		return self._instance.Dummy9
	@property
	def dummy10(self) -> int:
		return self._instance.Dummy10
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
