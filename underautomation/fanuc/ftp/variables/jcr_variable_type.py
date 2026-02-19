import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import JcrVariableType as jcr_variable_type

class JcrVariableType(GenericVariableType):
	'''Describes the Fanuc type JCR_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jcr_variable_type()
		else:
			self._instance = _internal

	@property
	def jog_gp(self) -> int:
		'''Value of variable $JOG_GP'''
		return self._instance.JogGp

	@property
	def jog_subgp(self) -> bool:
		'''Value of variable $JOG_SUBGP'''
		return self._instance.JogSubgp

	@property
	def jog_dct_nam(self) -> typing.List[int]:
		'''Value of variable $JOG_DCT_NAM'''
		return self._instance.JogDctNam

	@property
	def jog_dct_ele(self) -> typing.List[int]:
		'''Value of variable $JOG_DCT_ELE'''
		return self._instance.JogDctEle

	@property
	def mp_jog(self) -> int:
		'''Value of variable $MP_JOG'''
		return self._instance.MpJog

	@property
	def spjog_msk(self) -> int:
		'''Value of variable $SPJOG_MSK'''
		return self._instance.SpjogMsk

	@property
	def ijog_key(self) -> int:
		'''Value of variable $IJOG_KEY'''
		return self._instance.IjogKey

	@property
	def ijog_stat(self) -> int:
		'''Value of variable $IJOG_STAT'''
		return self._instance.IjogStat

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JcrVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
