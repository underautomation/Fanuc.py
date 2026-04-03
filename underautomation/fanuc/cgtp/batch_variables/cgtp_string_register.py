from __future__ import annotations
import typing
from underautomation.fanuc.cgtp.batch_variables.i_cgtp_batch_variable import ICgtpBatchVariable
from underautomation.fanuc.common.string_register_with_comment import StringRegisterWithComment
from UnderAutomation.Fanuc.Cgtp.BatchVariables import CgtpStringRegister as cgtp_string_register

class CgtpStringRegister(StringRegisterWithComment, ICgtpBatchVariable):
	'''Represents a string register (SR[]) for batch read/write operations. A string register always has a comment and a string value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cgtp_string_register()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''1-based index of the string register'''
		return self._instance.Index

	@property
	def name(self) -> str:
		return self._instance.Name

	@property
	def program(self) -> str:
		return self._instance.Program

	@property
	def string_value(self) -> str:
		return self._instance.StringValue

	@property
	def exists(self) -> bool:
		return self._instance.Exists

	@property
	def is_uninitialized(self) -> bool:
		return self._instance.IsUninitialized

	@property
	def is_read_only(self) -> bool:
		return self._instance.IsReadOnly

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CgtpStringRegister):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
