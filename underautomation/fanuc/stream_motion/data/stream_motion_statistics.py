from __future__ import annotations
import typing
from UnderAutomation.Fanuc.StreamMotion.Data import StreamMotionStatistics as stream_motion_statistics

class StreamMotionStatistics:
	'''Communication statistics of a Stream Motion client, since the status output was started'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stream_motion_statistics()
		else:
			self._instance = _internal

	@property
	def status_count(self) -> int:
		'''Number of status received from the robot'''
		return self._instance.StatusCount

	@property
	def lost_status_count(self) -> int:
		'''Number of status sent by the robot but not received (detected with the sequence numbers)'''
		return self._instance.LostStatusCount

	@property
	def command_count(self) -> int:
		'''Number of positions sent to the robot'''
		return self._instance.CommandCount

	@property
	def catch_up_command_count(self) -> int:
		'''Number of extra positions sent to fill the robot buffer again after lost or late status'''
		return self._instance.CatchUpCommandCount

	@property
	def underrun_count(self) -> int:
		'''Number of times the queue became empty while the robot was moving'''
		return self._instance.UnderrunCount

	@property
	def estimated_buffer_level(self) -> int:
		'''Estimated number of positions waiting in the robot buffer'''
		return self._instance.EstimatedBufferLevel

	@property
	def mean_status_interval(self) -> float:
		'''Mean time between two received status, measured with the PC clock, in seconds'''
		return self._instance.MeanStatusInterval

	@property
	def max_status_interval(self) -> float:
		'''Maximum time between two received status, measured with the PC clock, in seconds'''
		return self._instance.MaxStatusInterval

	@property
	def max_processing_time(self) -> float:
		'''Maximum time spent to process a status and send the positions, in seconds'''
		return self._instance.MaxProcessingTime

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StreamMotionStatistics):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
