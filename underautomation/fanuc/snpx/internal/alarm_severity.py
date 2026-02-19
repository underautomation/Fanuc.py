from enum import IntEnum

class AlarmSeverity(IntEnum):
	'''Represents the severity level of a robot alarm.'''
	NONE = 128 # No severity.
	WARN = 0 # Warning level alarm.
	PAUSE_L = 2 # Local pause level alarm.
	PAUSE_G = 34 # Global pause level alarm.
	STOP_L = 6 # Local stop level alarm.
	STOP_G = 38 # Global stop level alarm.
	SERVO = 54 # Servo error alarm.
	ABORT_L = 11 # Local abort level alarm.
	ABORT_G = 45 # Global abort level alarm.
	SERVO2 = 58 # Servo error level 2 alarm.
	SYSTEM = 122 # System level alarm.
