from enum import IntEnum

class InstructionVerb(IntEnum):
	'''Instruction verbs that append to the TP program.'''
	FRC_WaitDin = 0 # WAIT DI[x] = ON/OFF.
	FRC_SetUFrame = 1 # UFRAME_NUM = n.
	FRC_SetUTool = 2 # UTOOL_NUM = n.
	FRC_Wait = 3 # WAIT t (sec).
	FRC_PayLoad = 4 # PAYLOAD[n].
	FRC_LinearMotion = 5 # Linear motion in Cartesian representation.
	FRC_LinearRelative = 6 # Linear incremental motion in Cartesian representation.
	FRC_JointMotion = 7 # Joint motion in Cartesian representation.
	FRC_JointRelative = 8 # Joint incremental motion in Cartesian representation.
	FRC_CircularMotion = 9 # Circular motion in Cartesian representation.
	FRC_CircularRelative = 10 # Circular incremental motion in Cartesian representation.
	FRC_JointMotionJRep = 11 # Joint motion specified by joint angles.
	FRC_JointRelativeJRep = 12 # Joint incremental motion specified by joint angles.
	FRC_LinearMotionJRep = 13 # Linear motion specified by joint angles.
	FRC_LinearRelativeJRep = 14 # Linear incremental motion specified by joint angles.
