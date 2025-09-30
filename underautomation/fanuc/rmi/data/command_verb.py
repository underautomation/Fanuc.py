import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import CommandVerb as command_verb

class CommandVerb(int):
	FRC_Initialize = command_verb.FRC_Initialize
	FRC_Abort = command_verb.FRC_Abort
	FRC_Pause = command_verb.FRC_Pause
	FRC_Continue = command_verb.FRC_Continue
	FRC_Reset = command_verb.FRC_Reset
	FRC_ReadError = command_verb.FRC_ReadError
	FRC_SetUFrameUTool = command_verb.FRC_SetUFrameUTool
	FRC_GetStatus = command_verb.FRC_GetStatus
	FRC_ReadUFrameData = command_verb.FRC_ReadUFrameData
	FRC_WriteUFrameData = command_verb.FRC_WriteUFrameData
	FRC_ReadUToolData = command_verb.FRC_ReadUToolData
	FRC_WriteUToolData = command_verb.FRC_WriteUToolData
	FRC_ReadDIN = command_verb.FRC_ReadDIN
	FRC_WriteDOUT = command_verb.FRC_WriteDOUT
	FRC_ReadCartesianPosition = command_verb.FRC_ReadCartesianPosition
	FRC_ReadJointAngles = command_verb.FRC_ReadJointAngles
	FRC_SetOverRide = command_verb.FRC_SetOverRide
	FRC_GetUFrameUTool = command_verb.FRC_GetUFrameUTool
	FRC_ReadPositionRegister = command_verb.FRC_ReadPositionRegister
	FRC_WritePositionRegister = command_verb.FRC_WritePositionRegister
	FRC_ReadTCPSpeed = command_verb.FRC_ReadTCPSpeed
