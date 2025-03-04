import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import AsbnCfgVariableType as asbn_cfg_variable_type

class AsbnCfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = asbn_cfg_variable_type()
		else:
			self._instance = _internal
	@property
	def cnv_jnt_pos(self) -> bool:
		return self._instance.CnvJntPos
	@property
	def data_cmnts(self) -> int:
		return self._instance.DataCmnts
	@property
	def flags(self) -> int:
		return self._instance.Flags
	@property
	def pos_check(self) -> bool:
		return self._instance.PosCheck
	@property
	def check_optn(self) -> int:
		return self._instance.CheckOptn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
