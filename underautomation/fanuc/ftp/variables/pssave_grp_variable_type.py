import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PssaveGrpVariableType as pssave_grp_variable_type

class PssaveGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pssave_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def flange(self) -> int:
		return self._instance.Flange
	@property
	def sync_flange(self) -> int:
		return self._instance.SyncFlange
	@property
	def sync_mst_cn(self) -> int:
		return self._instance.SyncMstCn
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
