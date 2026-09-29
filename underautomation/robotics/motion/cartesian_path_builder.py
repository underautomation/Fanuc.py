from __future__ import annotations
import typing
from underautomation.robotics.geometry.cartesian_pose import CartesianPose
from underautomation.robotics.motion.termination import Termination
from underautomation.robotics.io.digital_signal import DigitalSignal
from underautomation.robotics.motion.trajectory import Trajectory
from UnderAutomation.Robotics.Motion import CartesianPathBuilder as cartesian_path_builder

class CartesianPathBuilder:
	'''Builds a Cartesian trajectory from a sequence of linear and circular motions, splines and shapes. Create it with create_cartesian_path(). Targets are poses of the tool of the planner, in its user frame.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_path_builder()
		else:
			self._instance = _internal

	def move_linear(self, target: CartesianPose, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a linear motion: the tool moves on a straight line and its orientation turns on the shortest way.

		:param target: Target pose. When it has no external axes, the external axes keep their current values.
		:param speed: Speed in mm/s
		:param termination: Termination: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.MoveLinear(target._instance if target else None, speed, termination._instance if termination else None, accelerationPercent))

	def move_linear_time(self, target: CartesianPose, duration: float, termination: Termination) -> 'CartesianPathBuilder':
		'''Adds a linear motion that lasts a given time. The motion takes more time when the limits do not allow this duration.

		:param target: Target pose. When it has no external axes, the external axes keep their current values.
		:param duration: Duration in seconds
		:param termination: Termination: stop or overlap
		'''
		return CartesianPathBuilder(self._instance.MoveLinearTime(target._instance if target else None, duration, termination._instance if termination else None))

	def move_circular(self, via: CartesianPose, target: CartesianPose, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a circular motion: the tool moves on the circle arc that passes through the via point and ends at the target. The orientation turns from the current orientation to the orientation of the target (the orientation of the via point is not used).

		:param via: Point on the arc
		:param target: Target pose. When it has no external axes, the external axes keep their current values.
		:param speed: Speed in mm/s
		:param termination: Termination: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.MoveCircular(via._instance if via else None, target._instance if target else None, speed, termination._instance if termination else None, accelerationPercent))

	def move_spline(self, points: typing.List[CartesianPose], speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a smooth motion that passes through a list of positions (cubic spline) and ends at the last one. The orientation passes through the orientation of each position. The speed is constant along the path, except where the curvature, the change of orientation or the external axes need a lower speed. The points must describe a smooth path: close or noisy points give high curvatures and a slow motion.

		:param points: Positions to pass through. A first position equal to the current position is ignored. Two consecutive positions cannot have the same X, Y, Z with different orientations.
		:param speed: Speed in mm/s
		:param termination: Termination at the last position: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.MoveSpline([x._instance if x else None for x in points], speed, termination._instance if termination else None, accelerationPercent))

	def add_circle(self, plane: CartesianPose, radius: float, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a full circle in the XY plane of a frame, counterclockwise around its Z axis. The circle starts and ends at the point (radius, 0, 0) of the frame. A linear motion to this point is added first when the tool is not there. The orientation of the tool does not change.

		:param plane: Frame of the circle, in the user frame of the planner: its origin is the center and its XY plane is the plane of the circle
		:param radius: Radius in mm
		:param speed: Speed in mm/s. It is reduced if the curvature needs it.
		:param termination: Termination at the end of the circle: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.AddCircle(plane._instance if plane else None, radius, speed, termination._instance if termination else None, accelerationPercent))

	def add_helix(self, plane: CartesianPose, radius: float, pitch: float, turns: float, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a helix around the Z axis of a frame, counterclockwise. It starts at the point (radius, 0, 0) of the frame and rises by the pitch along Z at each turn. A linear motion to the start point is added first when the tool is not there. The orientation of the tool does not change.

		:param plane: Frame of the helix, in the user frame of the planner: its origin is the center of the first turn
		:param radius: Radius in mm
		:param pitch: Distance along Z of the frame for each turn, in mm (negative to go down)
		:param turns: Number of turns (greater than 0, can be fractional)
		:param speed: Speed in mm/s. It is reduced if the curvature needs it.
		:param termination: Termination at the end of the helix: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.AddHelix(plane._instance if plane else None, radius, pitch, turns, speed, termination._instance if termination else None, accelerationPercent))

	def add_spiral(self, plane: CartesianPose, startRadius: float, endRadius: float, turns: float, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a spiral in the XY plane of a frame, counterclockwise around its Z axis. The distance to the center changes regularly from the start radius to the end radius (Archimedean spiral). It starts at the point (startRadius, 0, 0) of the frame. A linear motion to the start point is added first when the tool is not there. The orientation of the tool does not change.

		:param plane: Frame of the spiral, in the user frame of the planner: its origin is the center and its XY plane is the plane of the spiral
		:param startRadius: Distance to the center at the start, in mm (0 or more)
		:param endRadius: Distance to the center at the end, in mm (0 or more)
		:param turns: Number of turns (greater than 0, can be fractional)
		:param speed: Speed in mm/s. It is reduced if the curvature needs it.
		:param termination: Termination at the end of the spiral: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.AddSpiral(plane._instance if plane else None, startRadius, endRadius, turns, speed, termination._instance if termination else None, accelerationPercent))

	def add_rectangle(self, plane: CartesianPose, width: float, height: float, cornerRadius: float, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a rectangle centered on the origin of a frame, in its XY plane: the width is along X and the height along Y. It starts and ends at the middle of the side at +X, the point (width / 2, 0, 0) of the frame, and turns counterclockwise around Z. With a corner radius, the corners are circle arcs of this radius, and the curvature changes progressively at their ends. Without corner radius, the robot stops at each corner. A linear motion to the start point is added first when the tool is not there. The orientation of the tool does not change.

		:param plane: Frame of the rectangle, in the user frame of the planner
		:param width: Size along X of the frame in mm
		:param height: Size along Y of the frame in mm
		:param cornerRadius: Radius of the corners in mm, from 0 to half of the smallest side
		:param speed: Speed in mm/s. It is reduced if the curvature needs it.
		:param termination: Termination at the end of the rectangle: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.AddRectangle(plane._instance if plane else None, width, height, cornerRadius, speed, termination._instance if termination else None, accelerationPercent))

	def add_polygon(self, plane: CartesianPose, sideCount: int, radius: float, cornerRadius: float, speed: float, termination: Termination, accelerationPercent: float=100) -> 'CartesianPathBuilder':
		'''Adds a regular polygon centered on the origin of a frame, in its XY plane. One side is perpendicular to X: the polygon starts and ends at the middle of this side, and turns counterclockwise around Z. With a corner radius, the corners are circle arcs of this radius, and the curvature changes progressively at their ends. Without corner radius, the robot stops at each corner. A linear motion to the start point is added first when the tool is not there. The orientation of the tool does not change.

		:param plane: Frame of the polygon, in the user frame of the planner
		:param sideCount: Number of sides (3 or more)
		:param radius: Distance from the center to the corners (circumscribed circle), in mm
		:param cornerRadius: Radius of the corners in mm (0 for sharp corners)
		:param speed: Speed in mm/s. It is reduced if the curvature needs it.
		:param termination: Termination at the end of the polygon: stop, overlap or corner
		:param accelerationPercent: Acceleration and jerk in percent of the limits (greater than 0, up to 100)
		'''
		return CartesianPathBuilder(self._instance.AddPolygon(plane._instance if plane else None, sideCount, radius, cornerRadius, speed, termination._instance if termination else None, accelerationPercent))

	def wait(self, duration: float) -> 'CartesianPathBuilder':
		'''Keeps the current position during a given time

		:param duration: Duration in seconds
		'''
		return CartesianPathBuilder(self._instance.Wait(duration))

	def set_io(self, signal: DigitalSignal, value: bool) -> 'CartesianPathBuilder':
		'''Writes a digital signal when the previous motion ends

		:param signal: Signal to write
		:param value: Value to write
		'''
		return CartesianPathBuilder(self._instance.SetIO(signal._instance if signal else None, value))

	def build(self) -> Trajectory:
		'''Creates the trajectory. Its poses are flange poses in the world frame when the tool and user frames of the planner are set.'''
		return Trajectory(self._instance.Build())

	@property
	def end_position(self) -> CartesianPose:
		'''Pose at the end of the motions added so far, as a pose of the tool in the user frame of the planner'''
		return CartesianPose(None, None, None, None, self._instance.EndPosition)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPathBuilder):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
