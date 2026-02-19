from enum import IntEnum

class CommandVerb(IntEnum):
	'''RMI command verbs that do not add TP instructions.'''
	FRC_Initialize = 0 # Initialize and start the RMI_MOVE program.
	FRC_Abort = 1 # Abort the running RMI_MOVE program.
	FRC_Pause = 2 # Pause the running RMI_MOVE program.
	FRC_Continue = 3 # Resume a paused RMI_MOVE program.
	FRC_Reset = 4 # Reset controller errors and recover from HOLD / faults.
	FRC_ReadError = 5 # Read most recent controller error text.
	FRC_SetUFrameUTool = 6 # Set current UFRAME and UTOOL numbers.
	FRC_GetStatus = 7 # Get controller status and RMI state.
	FRC_ReadUFrameData = 8 # Read a user frame definition.
	FRC_WriteUFrameData = 9 # Write a user frame definition.
	FRC_ReadUToolData = 10 # Read a user tool definition.
	FRC_WriteUToolData = 11 # Write a user tool definition.
	FRC_ReadDIN = 12 # Read a digital input port.
	FRC_WriteDOUT = 13 # Write a digital output port.
	FRC_ReadCartesianPosition = 14 # Read current Cartesian position.
	FRC_ReadJointAngles = 15 # Read current joint angles.
	FRC_SetOverRide = 16 # Set program override (1-100%).
	FRC_GetUFrameUTool = 17 # Get current UFRAME/UTOOL numbers.
	FRC_ReadPositionRegister = 18 # Read a position register.
	FRC_WritePositionRegister = 19 # Write a position register.
	FRC_ReadTCPSpeed = 20 # Read current TCP speed.
