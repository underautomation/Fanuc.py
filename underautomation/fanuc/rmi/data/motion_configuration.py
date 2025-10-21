import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import MotionConfiguration as motion_configuration

class MotionConfiguration:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_configuration()
		else:
			self._instance = _internal
	@property
	def u_tool_number(self) -> int:
		return self._instance.UToolNumber
	@u_tool_number.setter
	def u_tool_number(self, value: int):
		self._instance.UToolNumber = value
	@property
	def u_frame_number(self) -> int:
		return self._instance.UFrameNumber
	@u_frame_number.setter
	def u_frame_number(self, value: int):
		self._instance.UFrameNumber = value
	@property
	def front(self) -> int:
		return self._instance.Front
	@front.setter
	def front(self, value: int):
		self._instance.Front = value
	@property
	def up(self) -> int:
		return self._instance.Up
	@up.setter
	def up(self, value: int):
		self._instance.Up = value
	@property
	def left(self) -> int:
		return self._instance.Left
	@left.setter
	def left(self, value: int):
		self._instance.Left = value
	@property
	def flip(self) -> int:
		return self._instance.Flip
	@flip.setter
	def flip(self, value: int):
		self._instance.Flip = value
	@property
	def turn4(self) -> int:
		return self._instance.Turn4
	@turn4.setter
	def turn4(self, value: int):
		self._instance.Turn4 = value
	@property
	def turn5(self) -> int:
		return self._instance.Turn5
	@turn5.setter
	def turn5(self, value: int):
		self._instance.Turn5 = value
	@property
	def turn6(self) -> int:
		return self._instance.Turn6
	@turn6.setter
	def turn6(self, value: int):
		self._instance.Turn6 = value
