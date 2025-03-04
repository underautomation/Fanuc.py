import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcssLsVariableType as dcss_ls_variable_type

class DcssLsVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_ls_variable_type()
		else:
			self._instance = _internal
	@property
	def stoout_idx(self) -> int:
		return self._instance.StooutIdx
	@property
	def stofb_idx(self) -> int:
		return self._instance.StofbIdx
	@property
	def stofb_ch(self) -> int:
		return self._instance.StofbCh
	@property
	def fence_type(self) -> int:
		return self._instance.FenceType
	@property
	def fence_idx(self) -> int:
		return self._instance.FenceIdx
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
