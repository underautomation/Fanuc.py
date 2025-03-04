import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SsrVariableType as ssr_variable_type

class SsrVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssr_variable_type()
		else:
			self._instance = _internal
	@property
	def singlestep(self) -> int:
		return self._instance.Singlestep
	@property
	def dummy8(self) -> int:
		return self._instance.Dummy8
	@property
	def sglsteptask(self) -> typing.List[int]:
		return self._instance.Sglsteptask
	@property
	def steptasknum(self) -> int:
		return self._instance.Steptasknum
	@property
	def stepstmttyp(self) -> int:
		return self._instance.Stepstmttyp
	@property
	def stpsegtype(self) -> int:
		return self._instance.Stpsegtype
	@property
	def bwdstep(self) -> int:
		return self._instance.Bwdstep
	@property
	def showstmttyp(self) -> int:
		return self._instance.Showstmttyp
	@property
	def banstptpoff(self) -> int:
		return self._instance.Banstptpoff
	@property
	def dummy9(self) -> int:
		return self._instance.Dummy9
	@property
	def dummy10(self) -> int:
		return self._instance.Dummy10
	@property
	def dummy11(self) -> int:
		return self._instance.Dummy11
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
