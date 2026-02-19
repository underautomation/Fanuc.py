import typing
from underautomation.fanuc.common.wrist_flip import WristFlip
from underautomation.fanuc.common.arm_up_down import ArmUpDown
from underautomation.fanuc.common.arm_left_right import ArmLeftRight
from underautomation.fanuc.common.arm_front_back import ArmFrontBack
from UnderAutomation.Fanuc.Common import Configuration as configuration
from UnderAutomation.Fanuc.Common import WristFlip as wrist_flip
from UnderAutomation.Fanuc.Common import ArmUpDown as arm_up_down
from UnderAutomation.Fanuc.Common import ArmLeftRight as arm_left_right
from UnderAutomation.Fanuc.Common import ArmFrontBack as arm_front_back

class Configuration:
	'''Fanuc arm configuration'''
	def __init__(self, wristFlip: WristFlip, armUpDown: ArmUpDown, armLeftRight: ArmLeftRight, armFrontBack: ArmFrontBack, turnAxis1: int, turnAxis2: int, turnAxis3: int, _internal = 0):
		'''Constructor with all configuration parameters'''
		if(_internal == 0):
			self._instance = configuration(wristFlip, armUpDown, armLeftRight, armFrontBack, turnAxis1, turnAxis2, turnAxis3)
		else:
			self._instance = _internal

	def from_string(self, value: str) -> None:
		'''Parse a Fanuc configuration string representation, like : "N U T, 0, 0, 0" or "R, 0, 0, 0"'''
		self._instance.FromString(value)

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def is_unknown(self) -> bool:
		'''Indicates if the configuration is unknown'''
		return self._instance.IsUnknown

	@property
	def wrist_flip(self) -> WristFlip:
		'''Wrist configuration'''
		return WristFlip(int(self._instance.WristFlip))

	@wrist_flip.setter
	def wrist_flip(self, value: WristFlip):
		self._instance.WristFlip = wrist_flip(int(value))

	@property
	def arm_up_down(self) -> ArmUpDown:
		'''Arm up/down configuration'''
		return ArmUpDown(int(self._instance.ArmUpDown))

	@arm_up_down.setter
	def arm_up_down(self, value: ArmUpDown):
		self._instance.ArmUpDown = arm_up_down(int(value))

	@property
	def arm_left_right(self) -> ArmLeftRight:
		'''Arm left/right configuration'''
		return ArmLeftRight(int(self._instance.ArmLeftRight))

	@arm_left_right.setter
	def arm_left_right(self, value: ArmLeftRight):
		self._instance.ArmLeftRight = arm_left_right(int(value))

	@property
	def arm_front_back(self) -> ArmFrontBack:
		'''Arm back/front configuration'''
		return ArmFrontBack(int(self._instance.ArmFrontBack))

	@arm_front_back.setter
	def arm_front_back(self, value: ArmFrontBack):
		self._instance.ArmFrontBack = arm_front_back(int(value))

	@property
	def turn_axis4(self) -> int:
		'''Turn number of axis J4 (1:180° to 539°, 0:-179° to 179°, -1:-539° to -180°)'''
		return self._instance.TurnAxis4

	@turn_axis4.setter
	def turn_axis4(self, value: int):
		self._instance.TurnAxis4 = value

	@property
	def turn_axis5(self) -> int:
		'''Turn number of axis J5 (1:180° to 539°, 0:-179° to 179°, -1:-539° to -180°)'''
		return self._instance.TurnAxis5

	@turn_axis5.setter
	def turn_axis5(self, value: int):
		self._instance.TurnAxis5 = value

	@property
	def turn_axis6(self) -> int:
		'''Turn number of axis J6 (1:180° to 539°, 0:-179° to 179°, -1:-539° to -180°)'''
		return self._instance.TurnAxis6

	@turn_axis6.setter
	def turn_axis6(self, value: int):
		self._instance.TurnAxis6 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Configuration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
