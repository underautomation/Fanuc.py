from __future__ import annotations
import typing
from underautomation.robotics.geometry.euler_convention import EulerConvention
from underautomation.robotics.geometry.cartesian_pose import CartesianPose
from underautomation.fanuc.common.xyzwpr_position import XYZWPRPosition
from underautomation.fanuc.common.extended_cartesian_position import ExtendedCartesianPosition
from underautomation.robotics.geometry.joint_values import JointValues
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.robotics.motion.termination import Termination
from underautomation.robotics.io.digital_signal import DigitalSignal
from underautomation.fanuc.stream_motion.data.io_type import IOType
from underautomation.robotics.motion.trajectory import Trajectory
from UnderAutomation.Fanuc.Motion import FanucMotion as fanuc_motion
from UnderAutomation.Robotics.Geometry import EulerConvention as euler_convention
from UnderAutomation.Fanuc.StreamMotion.Data import IOType as io_type

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class FanucMotion:
	'''Conversions between the FANUC types (positions, FINE/CNT/CR terminations, I/O types) and the types of the motion planner of namespace UnderAutomation.Robotics.Motion.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = fanuc_motion()
		else:
			self._instance = _internal

	@staticmethod
	def to_cartesian_pose(position: XYZWPRPosition) -> CartesianPose:
		'''Converts a FANUC position to a pose. The extended axes E1, E2 and E3 are copied when the position is an ExtendedCartesianPosition.

		:param position: Position X, Y, Z, W, P, R
		'''
		__r = fanuc_motion.ToCartesianPose(position._instance if position else None)
		return None if __r is None else CartesianPose(None, None, None, None, __r)

	@staticmethod
	def to_extended_cartesian_position(pose: CartesianPose, reference: XYZWPRPosition) -> ExtendedCartesianPosition:
		'''Converts a pose to a FANUC position with extended axes (0 when the pose has no external axes).

		:param pose: Pose to convert
		:param reference: Position used to choose the W, P, R angles: the angles closest to the ones of this position are returned, so that a sequence of positions stays continuous. When it is null, W and R are between -180 and 180 degrees, and P between -90 and 90 degrees.
		'''
		__r = fanuc_motion.ToExtendedCartesianPosition(pose._instance if pose else None, reference._instance if reference else None)
		return None if __r is None else ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, __r)

	@staticmethod
	def to_joint_values(position: JointsPosition) -> JointValues:
		'''Converts a FANUC joint position (J1 to J9) to joint values

		:param position: Joint position
		'''
		__r = fanuc_motion.ToJointValues(position._instance if position else None)
		return None if __r is None else JointValues(None, __r)

	@staticmethod
	def to_joints_position(values: JointValues) -> JointsPosition:
		'''Converts joint values to a FANUC joint position. Missing axes are 0.

		:param values: Joint values (up to 9 axes)
		'''
		__r = fanuc_motion.ToJointsPosition(values._instance if values else None)
		return None if __r is None else JointsPosition(None, None, None, None, None, None, None, None, None, __r)

	@staticmethod
	def fine() -> Termination:
		'''FINE termination: the robot stops at the target position'''
		__r = fanuc_motion.Fine()
		return None if __r is None else Termination(__r)

	@staticmethod
	def cnt(value: int) -> Termination:
		'''CNT termination: the next motion starts during the deceleration of this one

		:param value: From 0 to 100: part of the deceleration during which both motions are combined. 100 gives the smoothest motion.
		'''
		__r = fanuc_motion.Cnt(value)
		return None if __r is None else Termination(__r)

	@staticmethod
	def cr(distance: float) -> Termination:
		'''CR termination (corner region): the corner is replaced by a smooth curve at constant speed. Only between Cartesian motions.

		:param distance: Distance from the target position where the curve starts and ends, in mm. It is limited to half of the length of each motion.
		'''
		__r = fanuc_motion.Cr(distance)
		return None if __r is None else Termination(__r)

	@staticmethod
	def signal(type: IOType, index: int) -> DigitalSignal:
		'''Returns the digital signal of an I/O, to write it during a trajectory (for example DO[5])

		:param type: I/O type
		:param index: I/O index (starts at 1)
		'''
		__r = fanuc_motion.Signal(io_type(int(type)), index)
		return None if __r is None else DigitalSignal(None, None, __r)

	@staticmethod
	def from_cartesian_samples(samples: typing.List[XYZWPRPosition], cycleTime: float) -> Trajectory:
		'''Creates a Cartesian trajectory from FANUC positions taken at a fixed period. The W, P, R angles are kept without any change, and the extended axes are used when the positions are ExtendedCartesianPosition.

		:param samples: Positions (flange center in the world frame for Stream Motion), one per period
		:param cycleTime: Period between two positions, in seconds
		'''
		__r = fanuc_motion.FromCartesianSamples([x._instance if x else None for x in samples], cycleTime)
		return None if __r is None else Trajectory(__r)

	@staticmethod
	def sample_cartesian(trajectory: Trajectory, cycleTime: float) -> typing.List[ExtendedCartesianPosition]:
		'''Samples a Cartesian trajectory at a fixed period and returns FANUC positions. The W, P, R angles stay continuous from one position to the next.

		:param trajectory: Trajectory in Cartesian format
		:param cycleTime: Period between two samples, in seconds
		:returns: Positions from time 0 to the end of the trajectory
		'''
		__r = fanuc_motion.SampleCartesian(trajectory._instance if trajectory else None, cycleTime)
		return None if __r is None else [None if x is None else ExtendedCartesianPosition(None, None, None, None, None, None, None, None, None, x) for x in __r]

	@staticmethod
	def _get_wpr_convention() -> EulerConvention:
		'''Convention of the W, P, R angles of FANUC positions: rotation W around the fixed X axis, then P around the fixed Y axis, then R around the fixed Z axis'''
		return EulerConvention(int(fanuc_motion.WprConvention))

	wpr_convention = _StaticProperty(_get_wpr_convention)
	del _get_wpr_convention

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FanucMotion):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
