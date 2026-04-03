from __future__ import annotations
import typing
from underautomation.fanuc.common.position_register import PositionRegister
from UnderAutomation.Fanuc.Common import PositionRegisterWithComment as position_register_with_comment

class PositionRegisterWithComment(PositionRegister):
	'''Represents a position register with an associated comment.'''
	def __init__(self, _internal = 0):
		'''Default constructor.'''
		if(_internal == 0):
			self._instance = position_register_with_comment()
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'PositionRegisterWithComment':
		'''Parses a position register with comment from its string representation.'''
		return PositionRegisterWithComment(position_register_with_comment.Parse(value))

	@property
	def comment(self) -> str:
		'''Comment associated with this position register.'''
		return self._instance.Comment

	@comment.setter
	def comment(self, value: str):
		self._instance.Comment = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PositionRegisterWithComment):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
