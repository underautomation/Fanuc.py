from __future__ import annotations
import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.rmi.data.rmi_timed_response import RmiTimedResponse
from UnderAutomation.Fanuc.Rmi.Data import RmiJointAnglesSampleResponse as rmi_joint_angles_sample_response

class RmiJointAnglesSampleResponse(RmiTimedResponse):
	'''Result of reading the current joint angles.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_joint_angles_sample_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def joint_angle(self) -> JointsPosition:
		'''Joint angle set in degrees.'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.JointAngle)

	@joint_angle.setter
	def joint_angle(self, value: JointsPosition):
		self._instance.JointAngle = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiJointAnglesSampleResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
