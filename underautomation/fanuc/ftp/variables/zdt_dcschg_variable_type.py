import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ZdtDcschgVariableType as zdt_dcschg_variable_type

class ZdtDcschgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = zdt_dcschg_variable_type()
		else:
			self._instance = _internal
	@property
	def dcschg_enb(self) -> bool:
		return self._instance.DcschgEnb
	@property
	def login_idx(self) -> int:
		return self._instance.LoginIdx
	@property
	def last_signat(self) -> int:
		return self._instance.LastSignat
	@property
	def lst_time(self) -> int:
		return self._instance.LstTime
	@property
	def dcs_funct(self) -> int:
		return self._instance.DcsFunct
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
