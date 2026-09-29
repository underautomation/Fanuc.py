from __future__ import annotations
import typing
from underautomation.robotics.motion.joint_limits import JointLimits
from underautomation.robotics.motion.cartesian_limits import CartesianLimits
from underautomation.robotics.geometry.cartesian_pose import CartesianPose
from underautomation.robotics.motion.joint_path_builder import JointPathBuilder
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.cartesian_path_builder import CartesianPathBuilder
from UnderAutomation.Robotics.Motion import MotionPlanner as motion_planner

class MotionPlanner:
	'''Creates trajectories from joint motions, linear and circular motions, splines and shapes, with velocity, acceleration and jerk limits.'''
	def __init__(self, jointLimits: JointLimits, cartesianLimits: CartesianLimits, _internal = 0):
		'''Creates a planner

		:param jointLimits: Limits for joint motions (can be null if only Cartesian motions are planned)
		:param cartesianLimits: Limits for Cartesian motions (can be null if only joint motions are planned)
		'''
		if(_internal == 0):
			self._instance = motion_planner(jointLimits._instance if jointLimits else None, cartesianLimits._instance if cartesianLimits else None)
		else:
			self._instance = _internal

	def create_joint_path(self, start: JointValues) -> JointPathBuilder:
		'''Starts a joint path

		:param start: Start position, for example the current position of the robot (up to MaxJointCount axes)
		'''
		return JointPathBuilder(self._instance.CreateJointPath(start._instance if start else None))

	def create_cartesian_path(self, start: CartesianPose) -> CartesianPathBuilder:
		'''Starts a Cartesian path

		:param start: Start pose of the flange in the world frame, for example the current pose of the robot. It is converted with tool_frame and user_frame.
		'''
		return CartesianPathBuilder(self._instance.CreateCartesianPath(start._instance if start else None))

	@property
	def joint_limits(self) -> JointLimits:
		'''Limits for joint motions. 100% speed uses the velocity limits of this object. The limits of axes 7 to 9 are also used for the external axes of Cartesian motions.'''
		return JointLimits(None, None, None, self._instance.JointLimits)

	@joint_limits.setter
	def joint_limits(self, value: JointLimits):
		self._instance.JointLimits = value._instance if value else None

	@property
	def cartesian_limits(self) -> CartesianLimits:
		'''Limits for Cartesian motions'''
		return CartesianLimits(None, None, None, None, None, None, self._instance.CartesianLimits)

	@cartesian_limits.setter
	def cartesian_limits(self, value: CartesianLimits):
		self._instance.CartesianLimits = value._instance if value else None

	@property
	def tool_frame(self) -> CartesianPose:
		'''Tool frame, relative to the flange. When it is set, the targets of Cartesian motions are poses of this tool, and the trajectory gives the flange poses. Null when the targets are flange poses.'''
		return CartesianPose(None, None, None, None, self._instance.ToolFrame)

	@tool_frame.setter
	def tool_frame(self, value: CartesianPose):
		self._instance.ToolFrame = value._instance if value else None

	@property
	def user_frame(self) -> CartesianPose:
		'''User frame, relative to the world frame. When it is set, the targets of Cartesian motions are expressed in this frame, and the trajectory gives poses in the world frame. Null when the targets are in the world frame.'''
		return CartesianPose(None, None, None, None, self._instance.UserFrame)

	@user_frame.setter
	def user_frame(self, value: CartesianPose):
		self._instance.UserFrame = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionPlanner):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
