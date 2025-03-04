import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DcssHndgdVariableType as dcss_hndgd_variable_type

class DcssHndgdVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dcss_hndgd_variable_type()
		else:
			self._instance = _internal
	@property
	def grp_num(self) -> int:
		return self._instance.GrpNum
	@property
	def speed_lim(self) -> float:
		return self._instance.SpeedLim
	@property
	def dsblio_typ(self) -> int:
		return self._instance.DsblioTyp
	@property
	def dsblio_idx(self) -> int:
		return self._instance.DsblioIdx
	@property
	def stop_type(self) -> int:
		return self._instance.StopType
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
