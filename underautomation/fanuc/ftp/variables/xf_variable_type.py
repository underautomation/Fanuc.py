import typing
from underautomation.fanuc.common.xyz_position import XYZPosition
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
from UnderAutomation.Fanuc.Ftp.Variables import XfVariableType as xf_variable_type

class XfVariableType(GenericVariableType):
	'''Describes the Fanuc type $XF'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = xf_variable_type()
		else:
			self._instance = _internal

	@property
	def n(self) -> XYZPosition:
		'''Value of variable $N'''
		return XYZPosition(None, None, None, self._instance.N)

	@property
	def o(self) -> XYZPosition:
		'''Value of variable $O'''
		return XYZPosition(None, None, None, self._instance.O)

	@property
	def a(self) -> XYZPosition:
		'''Value of variable $A'''
		return XYZPosition(None, None, None, self._instance.A)

	@property
	def l(self) -> XYZPosition:
		'''Value of variable $L'''
		return XYZPosition(None, None, None, self._instance.L)

	@property
	def fanuc_internal_type_name(self) -> str:
		'''Type Name on the robot'''
		return self._instance.FanucInternalTypeName

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, XfVariableType):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
