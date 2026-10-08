from __future__ import annotations
import typing
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.robotics.motion.termination import Termination
from underautomation.robotics.io.digital_signal import DigitalSignal
from underautomation.robotics.motion.trajectory import Trajectory
from UnderAutomation.Robotics.Motion import JointPathBuilder as joint_path_builder

class JointPathBuilder:
	'''Builds a joint trajectory from a sequence of joint motions. Create it with create_joint_path().'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_path_builder()
		else:
			self._instance = _internal

	def move_joint(self, target: JointValues, speedPercent: float, termination: Termination, accelerationPercent: float=100) -> 'JointPathBuilder':
		'''Adds a joint motion: all axes move on a straight line in joint space and arrive at the same time

		:param target: Target joint position
		:param speedPercent: Speed in percent of the velocity limits (greater than 0, up to 100)
		:param termination: Termination: stop or overlap
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		__r = self._instance.MoveJoint(target._instance if target else None, speedPercent, termination._instance if termination else None, accelerationPercent)
		return None if __r is None else JointPathBuilder(__r)

	def move_joint_time(self, target: JointValues, duration: float, termination: Termination) -> 'JointPathBuilder':
		'''Adds a joint motion that lasts a given time. The motion takes more time when the limits do not allow this duration.

		:param target: Target joint position
		:param duration: Duration in seconds
		:param termination: Termination: stop or overlap
		'''
		__r = self._instance.MoveJointTime(target._instance if target else None, duration, termination._instance if termination else None)
		return None if __r is None else JointPathBuilder(__r)

	def move_joint_spline(self, points: typing.List[JointValues], speedPercent: float, termination: Termination, accelerationPercent: float=100) -> 'JointPathBuilder':
		'''Adds a smooth joint motion that passes through a list of positions (cubic spline) and ends at the last one. The speed changes along the path so that the velocity, acceleration and jerk of each axis stay within the limits. The points must describe a smooth path: close or noisy points give high curvatures and a slow motion.

		:param points: Positions to pass through. A first position equal to the current position is ignored.
		:param speedPercent: Speed in percent of the velocity limits (greater than 0, up to 100)
		:param termination: Termination at the last position: stop or overlap
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		__r = self._instance.MoveJointSpline([x._instance if x else None for x in points], speedPercent, termination._instance if termination else None, accelerationPercent)
		return None if __r is None else JointPathBuilder(__r)

	def wait(self, duration: float) -> 'JointPathBuilder':
		'''Keeps the current position during a given time

		:param duration: Duration in seconds
		'''
		__r = self._instance.Wait(duration)
		return None if __r is None else JointPathBuilder(__r)

	def set_io(self, signal: DigitalSignal, value: bool) -> 'JointPathBuilder':
		'''Writes a digital signal when the previous motion ends

		:param signal: Signal to write
		:param value: Value to write
		'''
		__r = self._instance.SetIO(signal._instance if signal else None, value)
		return None if __r is None else JointPathBuilder(__r)

	def build(self) -> Trajectory:
		'''Creates the trajectory'''
		__r = self._instance.Build()
		return None if __r is None else Trajectory(__r)

	@property
	def end_position(self) -> JointValues:
		'''Position at the end of the motions added so far'''
		__r = self._instance.EndPosition
		return None if __r is None else JointValues(None, __r)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointPathBuilder):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
