import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import ThrCfgVariableType as thr_cfg_variable_type

class ThrCfgVariableType(GenericVariableType):
	'''Describes the Fanuc type THR_CFG_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = thr_cfg_variable_type()
		else:
			self._instance = _internal

	@property
	def max_io_scan(self) -> int:
		'''Value of variable $MAX_IO_SCAN'''
		return self._instance.MaxIoScan

	@property
	def min_scan_ti(self) -> int:
		'''Value of variable $MIN_SCAN_TI'''
		return self._instance.MinScanTi

	@property
	def scan_time(self) -> int:
		'''Value of variable $SCAN_TIME'''
		return self._instance.ScanTime

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ThrCfgVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
