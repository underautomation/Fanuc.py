import typing
from underautomation.fanuc.snpx.internal.alarm_id import AlarmId
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
		return self._instance.Equals(other._instance if other else None)
	def __repr__(self):
		return self._instance.ToString()
	@property
	def id(self) -> AlarmId:
		return AlarmId(self._instance.Id)
	@id.setter
	def id(self, value: AlarmId):
		self._instance.Id = value
	@property
	def number(self) -> int:
		return self._instance.Number
	@number.setter
	def number(self, value: int):
		self._instance.Number = value
	@property
	def cause_id(self) -> AlarmId:
		return AlarmId(self._instance.CauseId)
	@cause_id.setter
	def cause_id(self, value: AlarmId):
		self._instance.CauseId = value
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
	@property
	def message(self) -> str:
		return self._instance.Message
	@message.setter
	def message(self, value: str):
		self._instance.Message = value
	@property
	def cause_message(self) -> str:
		return self._instance.CauseMessage
	@cause_message.setter
	def cause_message(self, value: str):
		self._instance.CauseMessage = value
	@property
	def severity_message(self) -> str:
		return self._instance.SeverityMessage
	@severity_message.setter
	def severity_message(self, value: str):
		self._instance.SeverityMessage = value
