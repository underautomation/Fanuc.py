from enum import IntEnum

class EulerConvention(IntEnum):
	'''Convention of three Euler angles (a, b, c) that describe an orientation. Angles are in degrees.'''
	FixedXYZ = 0 # Rotation a around the fixed X axis, then b around the fixed Y axis, then c around the fixed Z axis: R = Rz(c) * Ry(b) * Rx(a).
	MobileXYZ = 1 # Rotation a around X, then b around the new Y axis, then c around the new Z axis: R = Rx(a) * Ry(b) * Rz(c).
	MobileZYX = 2 # Rotation a around Z, then b around the new Y axis, then c around the new X axis: R = Rz(a) * Ry(b) * Rx(c). It is the same orientation as FixedXYZ with the angles in reverse order.
	MobileZYZ = 3 # Rotation a around Z, then b around the new Y axis, then c around the new Z axis: R = Rz(a) * Ry(b) * Rz(c).
