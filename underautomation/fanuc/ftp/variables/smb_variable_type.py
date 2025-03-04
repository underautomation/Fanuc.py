import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SmbVariableType as smb_variable_type

class SmbVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = smb_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def bcast(self) -> bool:
		return self._instance.Bcast
	@property
	def wins_ip(self) -> str:
		return self._instance.WinsIp
	@property
	def domain(self) -> str:
		return self._instance.Domain
	@property
	def expsrv(self) -> bool:
		return self._instance.Expsrv
	@property
	def spare(self) -> int:
		return self._instance.Spare
	@property
	def smb_rand(self) -> typing.List[int]:
		return self._instance.SmbRand
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
