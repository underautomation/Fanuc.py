import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RschVariableType as rsch_variable_type

class RschVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rsch_variable_type()
		else:
			self._instance = _internal
	@property
	def old_spec_sw(self) -> bool:
		return self._instance.OldSpecSw
	@property
	def freefromsiz(self) -> int:
		return self._instance.Freefromsiz
	@property
	def target_dir(self) -> str:
		return self._instance.TargetDir
	@property
	def updt_map(self) -> int:
		return self._instance.UpdtMap
	@property
	def reptsk_enb(self) -> bool:
		return self._instance.ReptskEnb
	@property
	def exp_enb(self) -> bool:
		return self._instance.ExpEnb
	@property
	def exp_dir(self) -> str:
		return self._instance.ExpDir
	@property
	def default_dev(self) -> bool:
		return self._instance.DefaultDev
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
