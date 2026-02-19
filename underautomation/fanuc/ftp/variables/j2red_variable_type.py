import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import J2redVariableType as j2red_variable_type

class J2redVariableType(GenericVariableType):
	'''Describes the Fanuc type J2RED_T'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = j2red_variable_type()
		else:
			self._instance = _internal

	@property
	def exd_rtq(self) -> float:
		'''Value of variable $EXD_RTQ'''
		return self._instance.ExdRtq

	@property
	def exd_itp(self) -> int:
		'''Value of variable $EXD_ITP'''
		return self._instance.ExdItp

	@property
	def exd_prg(self) -> int:
		'''Value of variable $EXD_PRG'''
		return self._instance.ExdPrg

	@property
	def exd_line(self) -> int:
		'''Value of variable $EXD_LINE'''
		return self._instance.ExdLine

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, J2redVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
