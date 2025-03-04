import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TracectlVariableType as tracectl_variable_type

class TracectlVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tracectl_variable_type()
		else:
			self._instance = _internal
	@property
	def task_status(self) -> int:
		return self._instance.TaskStatus
	@property
	def trc_top_idx(self) -> int:
		return self._instance.TrcTopIdx
	@property
	def trc_btm_idx(self) -> int:
		return self._instance.TrcBtmIdx
	@property
	def task_id(self) -> int:
		return self._instance.TaskId
	@property
	def dummy4(self) -> int:
		return self._instance.Dummy4
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
