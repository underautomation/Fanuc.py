import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import Tbc2GrpVariableType as tbc2_grp_variable_type

class Tbc2GrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tbc2_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def enb_flim(self) -> bool:
		return self._instance.EnbFlim
	@property
	def lim_ftm1(self) -> int:
		return self._instance.LimFtm1
	@property
	def lim_ftm2(self) -> int:
		return self._instance.LimFtm2
	@property
	def tdc_flag(self) -> bool:
		return self._instance.TdcFlag
	@property
	def tdc_minf(self) -> int:
		return self._instance.TdcMinf
	@property
	def tdc_minf2(self) -> int:
		return self._instance.TdcMinf2
	@property
	def tdc_thdist(self) -> float:
		return self._instance.TdcThdist
	@property
	def tdc_thspeed(self) -> float:
		return self._instance.TdcThspeed
	@property
	def tdc_throt(self) -> float:
		return self._instance.TdcThrot
	@property
	def reserve1(self) -> int:
		return self._instance.Reserve1
	@property
	def reserve2(self) -> int:
		return self._instance.Reserve2
	@property
	def reserve3(self) -> int:
		return self._instance.Reserve3
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
