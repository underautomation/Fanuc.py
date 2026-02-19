import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import JincVariableType as jinc_variable_type

class JincVariableType(GenericVariableType):
	'''Describes the Fanuc type JINC_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = jinc_variable_type()
		else:
			self._instance = _internal

	@property
	def jinc_enb(self) -> bool:
		'''Value of variable $JINC_ENB'''
		return self._instance.JincEnb

	@property
	def jog_incre(self) -> int:
		'''Value of variable $JOG_INCRE'''
		return self._instance.JogIncre

	@property
	def incre_trans(self) -> typing.List[float]:
		'''Value of variable $INCRE_TRANS'''
		return self._instance.IncreTrans

	@property
	def incre_jnt(self) -> typing.List[float]:
		'''Value of variable $INCRE_JNT'''
		return self._instance.IncreJnt

	@property
	def flex_i(self) -> typing.List[int]:
		'''Value of variable $FLEX_I'''
		return self._instance.FlexI

	@property
	def flex_r(self) -> typing.List[float]:
		'''Value of variable $FLEX_R'''
		return self._instance.FlexR

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JincVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
