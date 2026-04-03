from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.batch_variables.i_cgtp_batch_variable import ICgtpBatchVariable
from underautomation.fanuc.cgtp.batch_variables.cgtp_numeric_register import CgtpNumericRegister
from underautomation.fanuc.cgtp.batch_variables.cgtp_string_register import CgtpStringRegister
from underautomation.fanuc.cgtp.batch_variables.cgtp_position_register import CgtpPositionRegister
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.cgtp.batch_variables.cgtp_variable import CgtpVariable
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpBatchVariables as cgtp_batch_variables

class CgtpBatchVariables:
	'''Collection of batch variables to read from or write to the controller in a single operation. Provides convenience methods to add typed variables.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_batch_variables()
		else:
			self._instance = _internal

	def add(self, item: ICgtpBatchVariable) -> None:
		self._instance.Add(item._instance if item else None)

	def clear(self) -> None:
		self._instance.Clear()

	def contains(self, item: ICgtpBatchVariable) -> bool:
		return self._instance.Contains(item._instance if item else None)

	def copy_to(self, array: typing.List[ICgtpBatchVariable], arrayIndex: int) -> None:
		self._instance.CopyTo([x._instance if x else None for x in array], arrayIndex)

	def get_enumerator(self) -> typing.Any:
		return self._instance.GetEnumerator()

	def index_of(self, item: ICgtpBatchVariable) -> int:
		return self._instance.IndexOf(item._instance if item else None)

	def insert(self, index: int, item: ICgtpBatchVariable) -> None:
		self._instance.Insert(index, item._instance if item else None)

	def remove(self, item: ICgtpBatchVariable) -> bool:
		return self._instance.Remove(item._instance if item else None)

	def remove_at(self, index: int) -> None:
		self._instance.RemoveAt(index)

	def add_range(self, items: typing.Any) -> None:
		self._instance.AddRange(items)

	def add_numeric_register(self, index: int) -> CgtpNumericRegister:
		'''Add a numeric register for reading. The value and comment will be populated after a batch read.

		:param index: 1-based register index (R[index])
		:returns: The variable added to the collection
		'''
		return CgtpNumericRegister(self._instance.AddNumericRegister(index))

	def add_numeric_register_as_integer(self, index: int, comment: str, value: int) -> CgtpNumericRegister:
		'''Add a numeric register with an integer value and comment for writing.

		:param index: 1-based register index (R[index])
		:param comment: Register comment (mandatory)
		:param value: Integer value to write
		:returns: The variable added to the collection
		'''
		return CgtpNumericRegister(self._instance.AddNumericRegisterAsInteger(index, comment, value))

	def add_numeric_register_as_real(self, index: int, comment: str, value: float) -> CgtpNumericRegister:
		'''Add a numeric register with a real (double) value and comment for writing.

		:param index: 1-based register index (R[index])
		:param comment: Register comment (mandatory)
		:param value: Real value to write
		:returns: The variable added to the collection
		'''
		return CgtpNumericRegister(self._instance.AddNumericRegisterAsReal(index, comment, value))

	def add_string_register(self, index: int) -> CgtpStringRegister:
		'''Add a string register for reading. The value and comment will be populated after a batch read.

		:param index: 1-based register index (SR[index])
		:returns: The variable added to the collection
		'''
		return CgtpStringRegister(self._instance.AddStringRegister(index))

	def add_string_register_with_value(self, index: int, comment: str, value: str) -> CgtpStringRegister:
		'''Add a string register with a value and comment for writing.

		:param index: 1-based register index (SR[index])
		:param comment: Register comment (mandatory)
		:param value: String value to write
		:returns: The variable added to the collection
		'''
		return CgtpStringRegister(self._instance.AddStringRegisterWithValue(index, comment, value))

	def add_position_register(self, index: int, group: int=1) -> CgtpPositionRegister:
		'''Add a position register for reading. The position data will be populated after a batch read.

		:param index: 1-based register index (PR[index])
		:param group: Motion group number (default 1)
		:returns: The variable added to the collection
		'''
		return CgtpPositionRegister(self._instance.AddPositionRegister(index, group))

	def add_position_register_as_cartesian(self, index: int, position: CartesianPosition, group: int=1, comment: str=None) -> CgtpPositionRegister:
		'''Add a position register with a Cartesian position for writing.

		:param index: 1-based register index (PR[index])
		:param position: Cartesian position to write
		:param group: Motion group number (default 1)
		:param comment: Optional comment. Null means no comment is written.
		:returns: The variable added to the collection
		'''
		return CgtpPositionRegister(self._instance.AddPositionRegisterAsCartesian(index, position._instance if position else None, group, comment))

	def add_position_register_as_joint(self, index: int, position: JointsPosition, group: int=1, comment: str=None) -> CgtpPositionRegister:
		'''Add a position register with a joint position for writing.

		:param index: 1-based register index (PR[index])
		:param position: Joint position to write
		:param group: Motion group number (default 1)
		:param comment: Optional comment. Null means no comment is written.
		:returns: The variable added to the collection
		'''
		return CgtpPositionRegister(self._instance.AddPositionRegisterAsJoint(index, position._instance if position else None, group, comment))

	def add_variable(self, name: str, programName: str=None) -> CgtpVariable:
		'''Add a generic variable for reading or writing. For system variables, leave programName null. Set the desired value on the returned object before performing a batch write.

		:param name: Full variable name (e.g. "$RMT_MASTER", "$MNUTOOL[1,1]")
		:param programName: Program name that owns the variable. Null for system variables.
		:returns: The variable added to the collection
		'''
		return CgtpVariable(self._instance.AddVariable(name, programName))

	@property
	def item(self) -> ICgtpBatchVariable:
		return ICgtpBatchVariable(self._instance.Item)

	@item.setter
	def item(self, value: ICgtpBatchVariable):
		self._instance.Item = value._instance if value else None

	@property
	def count(self) -> int:
		return self._instance.Count

	@property
	def is_read_only(self) -> bool:
		return self._instance.IsReadOnly

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpBatchVariables):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

	def __iter__(self):
		enumerator = self._instance.GetEnumerator()
		while enumerator.MoveNext():
			yield ICgtpBatchVariable(enumerator.Current)

	def __len__(self) -> int:
		return self._instance.Count

	def __getitem__(self, index: int) -> ICgtpBatchVariable:
		return ICgtpBatchVariable(self._instance[index])
