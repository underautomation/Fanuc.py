import typing
from underautomation.fanuc.rmi.data.joint_angles import JointAngles
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
from UnderAutomation.Fanuc.Rmi.Data import JointAnglesSample as joint_angles_sample

class JointAnglesSample(RmiTimedResponse):
	'''Result of reading joint angles.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_angles_sample()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def joint_angle(self) -> JointAngles:
		'''Joint angle set.'''
		return JointAngles(self._instance.JointAngle)

	@joint_angle.setter
	def joint_angle(self, value: JointAngles):
		self._instance.JointAngle = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointAnglesSample):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
