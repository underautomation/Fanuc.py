import typing
from underautomation.fanuc.stream_motion.data.packet_type_from_robot import PacketTypeFromRobot
from underautomation.fanuc.stream_motion.data.threshold_type import ThresholdType
from UnderAutomation.Fanuc.StreamMotion.Data import AckPacket as ack_packet
from UnderAutomation.Fanuc.StreamMotion.Data import PacketTypeFromRobot as packet_type_from_robot
from UnderAutomation.Fanuc.StreamMotion.Data import ThresholdType as threshold_type

class AckPacket:
	'''Acknowledgment packet received from the robot in response to a Request packet Contains threshold data for motion limits'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ack_packet()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def packet_type(self) -> PacketTypeFromRobot:
		'''Packet type (always Ack=3)'''
		return PacketTypeFromRobot(int(self._instance.PacketType))

	@property
	def version_number(self) -> int:
		'''Protocol version number'''
		return self._instance.VersionNumber

	@property
	def axis_number(self) -> int:
		'''Axis number (1-9)'''
		return self._instance.AxisNumber

	@property
	def threshold_type(self) -> ThresholdType:
		'''Type of threshold data'''
		return ThresholdType(int(self._instance.ThresholdType))

	@property
	def max_cartesian_speed(self) -> int:
		'''Maximum Cartesian program speed of the robot (mm/s)'''
		return self._instance.MaxCartesianSpeed

	@property
	def unknown0(self) -> int:
		'''Unknown field (reserved for future use)'''
		return self._instance.Unknown0

	@property
	def thresholds_no_load(self) -> typing.List[float]:
		'''Threshold values at various velocity percentages (no load) Index 0 = 5% of Vmax, Index 1 = 10%, ..., Index 19 = 100%'''
		return self._instance.ThresholdsNoLoad

	@property
	def thresholds_max_load(self) -> typing.List[float]:
		'''Threshold values at various velocity percentages (maximum load) Index 0 = 5% of Vmax, Index 1 = 10%, ..., Index 19 = 100%'''
		return self._instance.ThresholdsMaxLoad

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AckPacket):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
