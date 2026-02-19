import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from UnderAutomation.Fanuc.Ftp.Variables import JointPositionVariable as joint_position_variable

class JointPositionVariable(JointsPosition):
	'''Represents a joint position variable parsed from a Fanuc variable file'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_position_variable()
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'JointPositionVariable':
		'''Parses a joint position from its string representation'''
		return JointPositionVariable(joint_position_variable.Parse(value))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def group(self) -> int:
		'''Motion group number'''
		return self._instance.Group

	@group.setter
	def group(self, value: int):
		self._instance.Group = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointPositionVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
