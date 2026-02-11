import typing
from underautomation.fanuc.stream_motion.data.packet_type_from_robot import PacketTypeFromRobot
from underautomation.fanuc.stream_motion.data.threshold_type import ThresholdType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import AckPacket as ack_packet
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeFromRobot as packet_type_from_robot
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class AckPacket:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ack_packet()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def packet_type(self) -> PacketTypeFromRobot:
		return PacketTypeFromRobot(self._instance.PacketType)
	@property
	def version_number(self) -> int:
		return self._instance.VersionNumber
	@property
	def axis_number(self) -> int:
		return self._instance.AxisNumber
	@property
	def threshold_type(self) -> ThresholdType:
		return ThresholdType(self._instance.ThresholdType)
	@property
	def max_cartesian_speed(self) -> int:
		return self._instance.MaxCartesianSpeed
	@property
	def unknown0(self) -> int:
		return self._instance.Unknown0
	@property
	def thresholds_no_load(self) -> typing.List[float]:
		return self._instance.ThresholdsNoLoad
	@property
	def thresholds_max_load(self) -> typing.List[float]:
		return self._instance.ThresholdsMaxLoad
