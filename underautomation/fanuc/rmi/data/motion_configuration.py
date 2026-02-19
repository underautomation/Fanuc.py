import typing
from UnderAutomation.Fanuc.Rmi.Data import MotionConfiguration as motion_configuration

class MotionConfiguration:
	'''Motion configuration including frame/tool numbers and turn/flip bits.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_configuration()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def u_tool_number(self) -> int:
		'''Active UTOOL number.'''
		return self._instance.UToolNumber

	@u_tool_number.setter
	def u_tool_number(self, value: int):
		self._instance.UToolNumber = value

	@property
	def u_frame_number(self) -> int:
		'''Active UFRAME number.'''
		return self._instance.UFrameNumber

	@u_frame_number.setter
	def u_frame_number(self, value: int):
		self._instance.UFrameNumber = value

	@property
	def front(self) -> int:
		'''FRONT bit (0/1).'''
		return self._instance.Front

	@front.setter
	def front(self, value: int):
		self._instance.Front = value

	@property
	def up(self) -> int:
		'''UP bit (0/1).'''
		return self._instance.Up

	@up.setter
	def up(self, value: int):
		self._instance.Up = value

	@property
	def left(self) -> int:
		'''LEFT bit (0/1).'''
		return self._instance.Left

	@left.setter
	def left(self, value: int):
		self._instance.Left = value

	@property
	def flip(self) -> int:
		'''FLIP bit (0/1).'''
		return self._instance.Flip

	@flip.setter
	def flip(self, value: int):
		self._instance.Flip = value

	@property
	def turn4(self) -> int:
		'''Turn 4.'''
		return self._instance.Turn4

	@turn4.setter
	def turn4(self, value: int):
		self._instance.Turn4 = value

	@property
	def turn5(self) -> int:
		'''Turn 5.'''
		return self._instance.Turn5

	@turn5.setter
	def turn5(self, value: int):
		self._instance.Turn5 = value

	@property
	def turn6(self) -> int:
		'''Turn 6.'''
		return self._instance.Turn6

	@turn6.setter
	def turn6(self, value: int):
		self._instance.Turn6 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
