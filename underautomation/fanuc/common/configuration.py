import typing
from underautomation.fanuc.common.wrist_flip import WristFlip
from underautomation.fanuc.common.arm_up_down import ArmUpDown
from underautomation.fanuc.common.arm_left_right import ArmLeftRight
from underautomation.fanuc.common.arm_front_back import ArmFrontBack
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import Configuration as configuration

class Configuration:
	def __init__(self, wristFlip: WristFlip, armUpDown: ArmUpDown, armLeftRight: ArmLeftRight, armFrontBack: ArmFrontBack, turnAxis1: int, turnAxis2: int, turnAxis3: int, _internal = 0):
		if(_internal == 0):
			self._instance = configuration(wristFlip, armUpDown, armLeftRight, armFrontBack, turnAxis1, turnAxis2, turnAxis3)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	def from_string(self, value: str) -> None:
		self._instance.FromString(value)
	@property
	def is_unknown(self) -> bool:
		return self._instance.IsUnknown
	@property
	def wrist_flip(self) -> WristFlip:
		return WristFlip(self._instance.WristFlip)
	@wrist_flip.setter
	def wrist_flip(self, value: WristFlip):
		self._instance.WristFlip = value
	@property
	def arm_up_down(self) -> ArmUpDown:
		return ArmUpDown(self._instance.ArmUpDown)
	@arm_up_down.setter
	def arm_up_down(self, value: ArmUpDown):
		self._instance.ArmUpDown = value
	@property
	def arm_left_right(self) -> ArmLeftRight:
		return ArmLeftRight(self._instance.ArmLeftRight)
	@arm_left_right.setter
	def arm_left_right(self, value: ArmLeftRight):
		self._instance.ArmLeftRight = value
	@property
	def arm_front_back(self) -> ArmFrontBack:
		return ArmFrontBack(self._instance.ArmFrontBack)
	@arm_front_back.setter
	def arm_front_back(self, value: ArmFrontBack):
		self._instance.ArmFrontBack = value
	@property
	def turn_axis4(self) -> int:
		return self._instance.TurnAxis4
	@turn_axis4.setter
	def turn_axis4(self, value: int):
		self._instance.TurnAxis4 = value
	@property
	def turn_axis5(self) -> int:
		return self._instance.TurnAxis5
	@turn_axis5.setter
	def turn_axis5(self, value: int):
		self._instance.TurnAxis5 = value
	@property
	def turn_axis6(self) -> int:
		return self._instance.TurnAxis6
	@turn_axis6.setter
	def turn_axis6(self, value: int):
		self._instance.TurnAxis6 = value
