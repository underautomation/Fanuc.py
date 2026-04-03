from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.batch_variables.i_cgtp_batch_variable import ICgtpBatchVariable
from underautomation.fanuc.cgtp.batch_variables.cgtp_structure_field import CgtpStructureField
from underautomation.fanuc.common.cartesian_position_variable import CartesianPositionVariable
from underautomation.fanuc.common.joint_position_variable import JointPositionVariable
from underautomation.fanuc.common.vector_variable import VectorVariable
from underautomation.fanuc.common.configuration import Configuration
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpVariable as cgtp_variable

class CgtpVariable(ICgtpBatchVariable):
	'''Represents a generic controller variable for batch read/write operations. Supports scalar values (integer, real, boolean, string, position, vector, configuration) and structured values (FIELD/ARRAY hierarchies).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_variable()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		return self._instance.Name

	@property
	def program(self) -> str:
		return self._instance.Program

	@property
	def string_value(self) -> str:
		return self._instance.StringValue

	@string_value.setter
	def string_value(self, value: str):
		self._instance.StringValue = value

	@property
	def exists(self) -> bool:
		return self._instance.Exists

	@property
	def is_uninitialized(self) -> bool:
		return self._instance.IsUninitialized

	@property
	def is_read_only(self) -> bool:
		return self._instance.IsReadOnly

	@property
	def structure_value(self) -> CgtpStructureField:
		'''Structured value returned for complex variables (with FIELD/ARRAY children). Null for scalar variables. When writing, if this is not null each leaf field is written independently.'''
		return CgtpStructureField(self._instance.StructureValue)

	@structure_value.setter
	def structure_value(self, value: CgtpStructureField):
		self._instance.StructureValue = value._instance if value else None

	@property
	def cartesian_position_value(self) -> CartesianPositionVariable:
		'''Gets or sets the value as a Cartesian position. Setting this property updates StringValue.'''
		return CartesianPositionVariable(None, None, self._instance.CartesianPositionValue)

	@cartesian_position_value.setter
	def cartesian_position_value(self, value: CartesianPositionVariable):
		self._instance.CartesianPositionValue = value._instance if value else None

	@property
	def joint_position_value(self) -> JointPositionVariable:
		'''Gets or sets the value as a joint position. Setting this property updates StringValue.'''
		return JointPositionVariable(None, None, self._instance.JointPositionValue)

	@joint_position_value.setter
	def joint_position_value(self, value: JointPositionVariable):
		self._instance.JointPositionValue = value._instance if value else None

	@property
	def integer_value(self) -> int:
		'''Gets or sets the value as an integer. Setting this property updates StringValue.'''
		return self._instance.IntegerValue

	@integer_value.setter
	def integer_value(self, value: int):
		self._instance.IntegerValue = value

	@property
	def real_value(self) -> float:
		'''Gets or sets the value as a double. Setting this property updates StringValue.'''
		return self._instance.RealValue

	@real_value.setter
	def real_value(self, value: float):
		self._instance.RealValue = value

	@property
	def boolean_value(self) -> bool:
		'''Gets or sets the value as a boolean. Setting this property updates StringValue.'''
		return self._instance.BooleanValue

	@boolean_value.setter
	def boolean_value(self, value: bool):
		self._instance.BooleanValue = value

	@property
	def vector_value(self) -> VectorVariable:
		'''Gets or sets the value as a 3D vector. Setting this property updates StringValue.'''
		return VectorVariable(self._instance.VectorValue)

	@vector_value.setter
	def vector_value(self, value: VectorVariable):
		self._instance.VectorValue = value._instance if value else None

	@property
	def configuration_value(self) -> Configuration:
		'''Gets or sets the value as a robot configuration. Setting this property updates StringValue.'''
		return Configuration(None, None, None, None, None, None, None, self._instance.ConfigurationValue)

	@configuration_value.setter
	def configuration_value(self, value: Configuration):
		self._instance.ConfigurationValue = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
