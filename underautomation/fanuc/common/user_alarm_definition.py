from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Common import UserAlarmDefinition as user_alarm_definition

class UserAlarmDefinition:
	'''Represents a user alarm definition with a comment and severity level.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = user_alarm_definition()
		else:
			self._instance = _internal

	@property
	def comment(self) -> str:
		'''Comment associated with this alarm.'''
		return self._instance.Comment

	@comment.setter
	def comment(self, value: str):
		self._instance.Comment = value

	@property
	def severity(self) -> int:
		'''Severity level of the alarm.'''
		return self._instance.Severity

	@severity.setter
	def severity(self, value: int):
		self._instance.Severity = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UserAlarmDefinition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
