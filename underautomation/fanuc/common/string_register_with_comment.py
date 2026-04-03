from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common import StringRegisterWithComment as string_register_with_comment

class StringRegisterWithComment:
	'''Represents a string register with an associated comment.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = string_register_with_comment()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Comment associated with this register.'''
		return self._instance.Comment

	@comment.setter
	def comment(self, value: str):
		self._instance.Comment = value

	@property
	def value(self) -> str:
		'''String value of the register.'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StringRegisterWithComment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
