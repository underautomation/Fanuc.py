import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ReqDataVariableType as req_data_variable_type

class ReqDataVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = req_data_variable_type()
		else:
			self._instance = _internal
	@property
	def err_type(self) -> int:
		return self._instance.ErrType
	@property
	def err_grp(self) -> int:
		return self._instance.ErrGrp
	@property
	def err_axis(self) -> int:
		return self._instance.ErrAxis
	@property
	def axis_type(self) -> bool:
		return self._instance.AxisType
	@property
	def error_dist(self) -> float:
		return self._instance.ErrorDist
	@property
	def err_time(self) -> int:
		return self._instance.ErrTime
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
