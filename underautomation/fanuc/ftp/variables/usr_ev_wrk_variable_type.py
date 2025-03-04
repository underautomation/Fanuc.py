import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UsrEvWrkVariableType as usr_ev_wrk_variable_type

class UsrEvWrkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = usr_ev_wrk_variable_type()
		else:
			self._instance = _internal
	@property
	def work_name(self) -> str:
		return self._instance.WorkName
	@property
	def start_copy(self) -> bool:
		return self._instance.StartCopy
	@property
	def num_in_fil(self) -> int:
		return self._instance.NumInFil
	@property
	def num_out_fil(self) -> int:
		return self._instance.NumOutFil
	@property
	def wait_ctr(self) -> int:
		return self._instance.WaitCtr
	@property
	def work1(self) -> int:
		return self._instance.Work1
	@property
	def work2(self) -> int:
		return self._instance.Work2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
