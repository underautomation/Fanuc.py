from enum import IntEnum

class AlarmType(IntEnum):
	'''Defines whether an alarm is active or historical.'''
	Active = 10 # Currently active alarm.
	History = 9 # Historical alarm from the alarm log.
