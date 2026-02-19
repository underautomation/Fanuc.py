import typing
from underautomation.fanuc.snpx.internal.alarm_id import AlarmId
from underautomation.fanuc.snpx.internal.alarm_severity import AlarmSeverity
from datetime import datetime, timedelta
from underautomation.fanuc.common.languages import Languages
from UnderAutomation.Fanuc.Snpx.Internal import RobotAlarm as robot_alarm
from UnderAutomation.Fanuc.Snpx.Internal import AlarmId as alarm_id
from UnderAutomation.Fanuc.Snpx.Internal import AlarmSeverity as alarm_severity
from UnderAutomation.Fanuc.Common import Languages as languages

class RobotAlarm:
	'''Represents a robot alarm with its category, severity, time, and message.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot_alarm()
		else:
			self._instance = _internal

	@staticmethod
	def from_bytes(bytes: typing.List[int], language: Languages, start: int=0) -> 'RobotAlarm':
		'''Creates a RobotAlarm from a byte array.

		:param bytes: The byte array containing alarm data.
		:param language: The controller language for string decoding.
		:param start: The starting offset in the byte array.
		:returns: A RobotAlarm parsed from the byte data, or null if bytes is null.
		'''
		return RobotAlarm(robot_alarm.FromBytes(bytes, languages(int(language)), start))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def id(self) -> AlarmId:
		'''Alarm Category'''
		return AlarmId(int(self._instance.Id))

	@id.setter
	def id(self, value: AlarmId):
		self._instance.Id = alarm_id(int(value))

	@property
	def number(self) -> int:
		'''Alarm Number'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def cause_id(self) -> AlarmId:
		'''Cause Category'''
		return AlarmId(int(self._instance.CauseId))

	@cause_id.setter
	def cause_id(self, value: AlarmId):
		self._instance.CauseId = alarm_id(int(value))

	@property
	def cause_number(self) -> int:
		'''Cause Number'''
		return self._instance.CauseNumber

	@cause_number.setter
	def cause_number(self, value: int):
		self._instance.CauseNumber = value

	@property
	def severity(self) -> AlarmSeverity:
		'''Alarm Severity'''
		return AlarmSeverity(int(self._instance.Severity))

	@severity.setter
	def severity(self, value: AlarmSeverity):
		self._instance.Severity = alarm_severity(int(value))

	@property
	def time(self) -> datetime:
		'''Occurrence Time'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Time.Ticks // 10)

	@time.setter
	def time(self, value: datetime):
		self._instance.Time = value

	@property
	def message(self) -> str:
		'''Error Message'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	@property
	def cause_message(self) -> str:
		'''Cause message'''
		return self._instance.CauseMessage

	@cause_message.setter
	def cause_message(self, value: str):
		self._instance.CauseMessage = value

	@property
	def severity_message(self) -> str:
		'''Severity message'''
		return self._instance.SeverityMessage

	@severity_message.setter
	def severity_message(self, value: str):
		self._instance.SeverityMessage = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotAlarm):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
