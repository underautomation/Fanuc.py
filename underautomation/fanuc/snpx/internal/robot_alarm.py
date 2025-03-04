import typing
from underautomation.fanuc.snpx.internal.alarm_category import AlarmCategory
from underautomation.fanuc.snpx.internal.alarm_severity import AlarmSeverity
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import RobotAlarm as robot_alarm

class RobotAlarm:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_alarm()
		else:
			self._instance = _internal
	@staticmethod
	def from_bytes(bytes: typing.List[int], start: int=0) -> 'RobotAlarm':
		return RobotAlarm(robot_alarm.FromBytes(bytes, start))
	def equals(self, other: 'RobotAlarm') -> bool:
		return self._instance.Equals(other._instance)
	def __repr__(self):
		return self._instance.ToString()
	@property
	def category(self) -> AlarmCategory:
		return AlarmCategory(self._instance.Category)
	@category.setter
	def category(self, value: AlarmCategory):
		self._instance.Category = value
	@property
	def number(self) -> int:
		return self._instance.Number
	@number.setter
	def number(self, value: int):
		self._instance.Number = value
	@property
	def cause_category(self) -> AlarmCategory:
		return AlarmCategory(self._instance.CauseCategory)
	@cause_category.setter
	def cause_category(self, value: AlarmCategory):
		self._instance.CauseCategory = value
	@property
	def cause_number(self) -> int:
		return self._instance.CauseNumber
	@cause_number.setter
	def cause_number(self, value: int):
		self._instance.CauseNumber = value
	@property
	def severity(self) -> AlarmSeverity:
		return AlarmSeverity(self._instance.Severity)
	@severity.setter
	def severity(self, value: AlarmSeverity):
		self._instance.Severity = value
	@property
	def time(self) -> typing.Any:
		return self._instance.Time
	@time.setter
	def time(self, value: typing.Any):
		self._instance.Time = value
