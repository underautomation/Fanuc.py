import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.kinematics.dh_parameters import DhParameters
from UnderAutomation.Fanuc.Kinematics import KinematicsUtils as kinematics_utils

class KinematicsUtils:
	'''Kinematics utilities'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = kinematics_utils()
		else:
			self._instance = _internal

	@staticmethod
	def forward_kinematics(jointAnglesRad: typing.List[float], dhParameters: DhParameters) -> CartesianPosition:
		'''Compute FK for given joint angles (rad) and DH parameters'''
		return CartesianPosition(None, None, None, None, None, None, None, kinematics_utils.ForwardKinematics(jointAnglesRad, dhParameters._instance if dhParameters else None))

	@staticmethod
	def inverse_kinematics(position: CartesianPosition, parameters: DhParameters) -> typing.List[JointsPosition]:
		'''Compute all inverse kinematics solutions for a desired end effector pose.

		:param position: Target Cartesian position.
		:param parameters: DH parameters of the robot.
		:returns: An array of joint angle solutions.
		'''
		return [JointsPosition(None, None, None, None, None, None, None, None, None, x) for x in kinematics_utils.InverseKinematics(position._instance if position else None, parameters._instance if parameters else None)]

	@staticmethod
	def mul(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
		return kinematics_utils.Mul(A, B)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, KinematicsUtils):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
