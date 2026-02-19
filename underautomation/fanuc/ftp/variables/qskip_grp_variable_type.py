import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import QskipGrpVariableType as qskip_grp_variable_type

class QskipGrpVariableType(GenericVariableType):
	'''Describes the Fanuc type QSKIP_GRP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = qskip_grp_variable_type()
		else:
			self._instance = _internal

	@property
	def error_cnt2(self) -> typing.List[int]:
		'''Value of variable $ERROR_CNT2'''
		return self._instance.ErrorCnt2

	@property
	def qskp_errcnt(self) -> typing.List[int]:
		'''Value of variable $QSKP_ERRCNT'''
		return self._instance.QskpErrcnt

	@property
	def qskp_curang(self) -> float:
		'''Value of variable $QSKP_CURANG'''
		return self._instance.QskpCurang

	@property
	def qskp_curan1(self) -> float:
		'''Value of variable $QSKP_CURAN1'''
		return self._instance.QskpCuran1

	@property
	def qskp_curan2(self) -> float:
		'''Value of variable $QSKP_CURAN2'''
		return self._instance.QskpCuran2

	@property
	def qskp_curan3(self) -> float:
		'''Value of variable $QSKP_CURAN3'''
		return self._instance.QskpCuran3

	@property
	def qskp_curan4(self) -> float:
		'''Value of variable $QSKP_CURAN4'''
		return self._instance.QskpCuran4

	@property
	def qskp_curan5(self) -> float:
		'''Value of variable $QSKP_CURAN5'''
		return self._instance.QskpCuran5

	@property
	def qskp_curan6(self) -> float:
		'''Value of variable $QSKP_CURAN6'''
		return self._instance.QskpCuran6

	@property
	def qskp_curan7(self) -> float:
		'''Value of variable $QSKP_CURAN7'''
		return self._instance.QskpCuran7

	@property
	def qskp_curan8(self) -> float:
		'''Value of variable $QSKP_CURAN8'''
		return self._instance.QskpCuran8

	@property
	def qskp_curan9(self) -> float:
		'''Value of variable $QSKP_CURAN9'''
		return self._instance.QskpCuran9

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, QskipGrpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
