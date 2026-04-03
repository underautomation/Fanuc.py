from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Cgtp.BatchVariables import ICgtpBatchVariable as i_cgtp_batch_variable

class ICgtpBatchVariable:
	'''Common interface for all batch variable types used with batch read/write operations.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_cgtp_batch_variable()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Full variable name (e.g. "$NUMREG[1]", "$POSREG[1,2]", "$RMT_MASTER")'''
		return self._instance.Name

	@property
	def program(self) -> str:
		'''Program name that owns this variable'''
		return self._instance.Program

	@property
	def string_value(self) -> str:
		'''Raw string value as read from or to be written to the controller'''
		return self._instance.StringValue

	@property
	def exists(self) -> bool:
		'''Indicates whether a value was returned by the controller during a batch read. False if the variable was not found.'''
		return self._instance.Exists

	@property
	def is_uninitialized(self) -> bool:
		'''Indicates whether the variable is uninitialized on the controller'''
		return self._instance.IsUninitialized

	@property
	def is_read_only(self) -> bool:
		'''Indicates whether the variable is read-only on the controller and cannot be written with CGTP'''
		return self._instance.IsReadOnly

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ICgtpBatchVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
