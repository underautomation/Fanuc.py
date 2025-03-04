import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ThrCfgVariableType as thr_cfg_variable_type

class ThrCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = thr_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def max_io_scan(self) -> int:
		return self._instance.MaxIoScan
	@property
	def min_scan_ti(self) -> int:
		return self._instance.MinScanTi
	@property
	def scan_time(self) -> int:
		return self._instance.ScanTime
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
