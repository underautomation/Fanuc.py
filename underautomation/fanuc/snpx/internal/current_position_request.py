import typing
from UnderAutomation.Fanuc.Snpx.Internal import CurrentPositionRequest as current_position_request

class CurrentPositionRequest:
	'''Specifies the motion group and user frame for reading the current robot position.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = current_position_request()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def group(self) -> int:
		'''Gets or sets the motion group number.'''
		return self._instance.Group

	@group.setter
	def group(self, value: int):
		self._instance.Group = value

	@property
	def user_frame(self) -> int:
		'''Gets or sets the user frame number.'''
		return self._instance.UserFrame

	@user_frame.setter
	def user_frame(self, value: int):
		self._instance.UserFrame = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CurrentPositionRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
