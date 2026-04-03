from __future__ import annotations
import typing
from underautomation.fanuc.common.numeric_register import NumericRegister
from UnderAutomation.Fanuc.Common import NumericRegisterWithComment as numeric_register_with_comment

class NumericRegisterWithComment(NumericRegister):
	'''Represents a numeric register with an associated comment.'''
	def __init__(self, value: int, comment: str, _internal = 0):
		'''Creates a numeric register with an integer value and comment.'''
		if(_internal == 0):
			self._instance = numeric_register_with_comment(value, comment)
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Comment associated with this register.'''
		return self._instance.Comment

	@comment.setter
	def comment(self, value: str):
		self._instance.Comment = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NumericRegisterWithComment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
