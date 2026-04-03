from enum import IntEnum

class CgtpVariableType(IntEnum):
	'''Data types that can be returned when reading a controller variable.'''
	CartesianPosition = 2 # Cartesian position (X, Y, Z, W, P, R with configuration).
	JointPosition = 9 # Joint position (J1..J9).
	Integer = 16 # 32-bit integer value.
	Real = 17 # Double-precision floating-point value.
	Boolean = 18 # Boolean value (TRUE or FALSE).
	Vector = 19 # 3D vector (X, Y, Z).
	Short = 23 # 16-bit short integer value.
	Byte = 24 # 8-bit byte value.
	Config = 28 # Robot configuration string.
	Numeric = 38 # Numeric value that can be either integer or real.
	XYZWPR = 256 # XYZWPR position type.
	POSITION = 257 # Full position type.
	XYZWPRExt = 262 # Extended XYZWPR position with additional axes.
	String = 7936 # String value. The actual type code encodes the maximum string length.
	JointPose9 = 8601 # Joint position with up to 9 axes.
