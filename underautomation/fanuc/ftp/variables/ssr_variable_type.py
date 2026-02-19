import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import SsrVariableType as ssr_variable_type

class SsrVariableType(GenericVariableType):
	'''Describes the Fanuc type SSR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ssr_variable_type()
		else:
			self._instance = _internal

	@property
	def singlestep(self) -> int:
		'''Value of variable $SINGLESTEP'''
		return self._instance.Singlestep

	@property
	def dummy8(self) -> int:
		'''Value of variable $DUMMY8'''
		return self._instance.Dummy8

	@property
	def sglsteptask(self) -> typing.List[int]:
		'''Value of variable $SGLSTEPTASK'''
		return self._instance.Sglsteptask

	@property
	def steptasknum(self) -> int:
		'''Value of variable $STEPTASKNUM'''
		return self._instance.Steptasknum

	@property
	def stepstmttyp(self) -> int:
		'''Value of variable $STEPSTMTTYP'''
		return self._instance.Stepstmttyp

	@property
	def stpsegtype(self) -> int:
		'''Value of variable $STPSEGTYPE'''
		return self._instance.Stpsegtype

	@property
	def bwdstep(self) -> int:
		'''Value of variable $BWDSTEP'''
		return self._instance.Bwdstep

	@property
	def showstmttyp(self) -> int:
		'''Value of variable $SHOWSTMTTYP'''
		return self._instance.Showstmttyp

	@property
	def banstptpoff(self) -> int:
		'''Value of variable $BANSTPTPOFF'''
		return self._instance.Banstptpoff

	@property
	def dummy9(self) -> int:
		'''Value of variable $DUMMY9'''
		return self._instance.Dummy9

	@property
	def dummy10(self) -> int:
		'''Value of variable $DUMMY10'''
		return self._instance.Dummy10

	@property
	def dummy11(self) -> int:
		'''Value of variable $DUMMY11'''
		return self._instance.Dummy11

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SsrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
