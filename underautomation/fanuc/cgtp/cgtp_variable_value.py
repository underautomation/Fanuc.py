from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.cgtp_variable_type import CgtpVariableType
from underautomation.fanuc.common.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.common.joint_position_variable import JointPositionVariable
from underautomation.fanuc.common.vector_variable import VectorVariable
from underautomation.fanuc.common.configuration import Configuration
from UnderAutomation.Fanuc.Cgtp import CgtpVariableValue as cgtp_variable_value
from UnderAutomation.Fanuc.Cgtp import CgtpVariableType as cgtp_variable_type

class CgtpVariableValue:
	'''Represents the value of a controller variable with its data type.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_variable_value()
		else:
			self._instance = _internal

	@property
	def type(self) -> CgtpVariableType:
		'''Data type of the variable'''
		return CgtpVariableType(int(self._instance.Type))

	@property
	def string_value(self) -> str:
		'''Raw string value of the variable'''
		return self._instance.StringValue

	@property
	def string_length(self) -> int:
		'''Maximum string length if the variable type is String'''
		return self._instance.StringLength

	@property
	def cartesian_position_value(self) -> CartesianPositionVariable:
		'''Value interpreted as a Cartesian position.'''
		__r = self._instance.CartesianPositionValue
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@property
	def joint_position_value(self) -> JointPositionVariable:
		'''Value interpreted as a joint position.'''
		__r = self._instance.JointPositionValue
		return None if __r is None else JointPositionVariable(None, None, __r)

	@property
	def integer_value(self) -> int:
		'''Value interpreted as an integer.'''
		return self._instance.IntegerValue

	@property
	def real_value(self) -> float:
		'''Value interpreted as a double-precision floating-point number.'''
		return self._instance.RealValue

	@property
	def boolean_value(self) -> bool:
		'''Value interpreted as a boolean (TRUE/FALSE).'''
		return self._instance.BooleanValue

	@property
	def vector_value(self) -> VectorVariable:
		'''Value interpreted as a 3D vector.'''
		__r = self._instance.VectorValue
		return None if __r is None else VectorVariable(__r)

	@property
	def configuration_value(self) -> Configuration:
		'''Value interpreted as a robot configuration.'''
		__r = self._instance.ConfigurationValue
		return None if __r is None else Configuration(None, None, None, None, None, None, None, __r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpVariableValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
