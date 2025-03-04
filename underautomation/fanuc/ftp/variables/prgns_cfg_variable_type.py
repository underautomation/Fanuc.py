import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PrgnsCfgVariableType as prgns_cfg_variable_type

class PrgnsCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = prgns_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def algo_ver(self) -> float:
		return self._instance.AlgoVer
	@property
	def nyq_freq(self) -> float:
		return self._instance.NyqFreq
	@property
	def win_type(self) -> int:
		return self._instance.WinType
	@property
	def win_size(self) -> int:
		return self._instance.WinSize
	@property
	def overlap(self) -> int:
		return self._instance.Overlap
	@property
	def freq_lim(self) -> float:
		return self._instance.FreqLim
	@property
	def min_num(self) -> int:
		return self._instance.MinNum
	@property
	def created(self) -> int:
		return self._instance.Created
	@property
	def verify(self) -> int:
		return self._instance.Verify
	@property
	def progname(self) -> str:
		return self._instance.Progname
	@property
	def create_gp(self) -> int:
		return self._instance.CreateGp
	@property
	def status_gp(self) -> int:
		return self._instance.StatusGp
	@property
	def debug(self) -> int:
		return self._instance.Debug
	@property
	def mailtime(self) -> int:
		return self._instance.Mailtime
	@property
	def mailevent(self) -> int:
		return self._instance.Mailevent
	@property
	def lastmail(self) -> int:
		return self._instance.Lastmail
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
