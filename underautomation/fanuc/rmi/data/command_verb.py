import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import CommandVerb as command_verb

class CommandVerb(int):
	FRC_Initialize = int(command_verb.FRC_Initialize)
	FRC_Abort = int(command_verb.FRC_Abort)
	FRC_Pause = int(command_verb.FRC_Pause)
	FRC_Continue = int(command_verb.FRC_Continue)
	FRC_Reset = int(command_verb.FRC_Reset)
	FRC_ReadError = int(command_verb.FRC_ReadError)
	FRC_SetUFrameUTool = int(command_verb.FRC_SetUFrameUTool)
	FRC_GetStatus = int(command_verb.FRC_GetStatus)
	FRC_ReadUFrameData = int(command_verb.FRC_ReadUFrameData)
	FRC_WriteUFrameData = int(command_verb.FRC_WriteUFrameData)
	FRC_ReadUToolData = int(command_verb.FRC_ReadUToolData)
	FRC_WriteUToolData = int(command_verb.FRC_WriteUToolData)
	FRC_ReadDIN = int(command_verb.FRC_ReadDIN)
	FRC_WriteDOUT = int(command_verb.FRC_WriteDOUT)
	FRC_ReadCartesianPosition = int(command_verb.FRC_ReadCartesianPosition)
	FRC_ReadJointAngles = int(command_verb.FRC_ReadJointAngles)
	FRC_SetOverRide = int(command_verb.FRC_SetOverRide)
	FRC_GetUFrameUTool = int(command_verb.FRC_GetUFrameUTool)
	FRC_ReadPositionRegister = int(command_verb.FRC_ReadPositionRegister)
	FRC_WritePositionRegister = int(command_verb.FRC_WritePositionRegister)
	FRC_ReadTCPSpeed = int(command_verb.FRC_ReadTCPSpeed)

	def __repr__(self):
		for name, value in vars(CommandVerb).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
