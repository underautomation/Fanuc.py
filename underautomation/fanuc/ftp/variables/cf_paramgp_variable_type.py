import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import CfParamgpVariableType as cf_paramgp_variable_type

class CfParamgpVariableType(GenericVariableType):
	'''Describes the Fanuc type CF_PARAMGP_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cf_paramgp_variable_type()
		else:
			self._instance = _internal

	@property
	def warnmessenb(self) -> bool:
		'''Value of variable $WARNMESSENB'''
		return self._instance.Warnmessenb

	@property
	def chkjntlim(self) -> bool:
		'''Value of variable $CHKJNTLIM'''
		return self._instance.Chkjntlim

	@property
	def cnstnt_corn(self) -> bool:
		'''Value of variable $CNSTNT_CORN'''
		return self._instance.CnstntCorn

	@property
	def timefltrenb(self) -> bool:
		'''Value of variable $TIMEFLTRENB'''
		return self._instance.Timefltrenb

	@property
	def tratio_tb(self) -> typing.List[float]:
		'''Value of variable $TRATIO_TB'''
		return self._instance.TratioTb

	@property
	def acctime_tb1(self) -> typing.List[float]:
		'''Value of variable $ACCTIME_TB1'''
		return self._instance.AcctimeTb1

	@property
	def acctime_tb2(self) -> typing.List[float]:
		'''Value of variable $ACCTIME_TB2'''
		return self._instance.AcctimeTb2

	@property
	def orient_type(self) -> int:
		'''Value of variable $ORIENT_TYPE'''
		return self._instance.OrientType

	@property
	def debug(self) -> int:
		'''Value of variable $DEBUG'''
		return self._instance.Debug

	@property
	def rtspd_sf(self) -> float:
		'''Value of variable $RTSPD_SF'''
		return self._instance.RtspdSf

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CfParamgpVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
