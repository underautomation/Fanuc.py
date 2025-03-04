import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZdtActvsptVariableType as zdt_actvspt_variable_type

class ZdtActvsptVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zdt_actvspt_variable_type()
		else:
			self._instance = _internal
	@property
	def actvspt_enb(self) -> bool:
		return self._instance.ActvsptEnb
	@property
	def activate(self) -> int:
		return self._instance.Activate
	@property
	def iotype(self) -> int:
		return self._instance.Iotype
	@property
	def ioport(self) -> int:
		return self._instance.Ioport
	@property
	def timeitvl(self) -> int:
		return self._instance.Timeitvl
	@property
	def trgtdvc(self) -> str:
		return self._instance.Trgtdvc
	@property
	def trgcfg(self) -> str:
		return self._instance.Trgcfg
	@property
	def tmpdir(self) -> str:
		return self._instance.Tmpdir
	@property
	def ps_numfile(self) -> int:
		return self._instance.PsNumfile
	@property
	def numfile(self) -> int:
		return self._instance.Numfile
	@property
	def numcfg(self) -> int:
		return self._instance.Numcfg
	@property
	def lsttime(self) -> int:
		return self._instance.Lsttime
	@property
	def extra(self) -> int:
		return self._instance.Extra
	@property
	def extra_str(self) -> str:
		return self._instance.ExtraStr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
