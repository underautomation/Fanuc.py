import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import InstructionVerb as instruction_verb

class InstructionVerb(int):
	FRC_WaitDin = instruction_verb.FRC_WaitDin
	FRC_SetUFrame = instruction_verb.FRC_SetUFrame
	FRC_SetUTool = instruction_verb.FRC_SetUTool
	FRC_Wait = instruction_verb.FRC_Wait
	FRC_PayLoad = instruction_verb.FRC_PayLoad
	FRC_LinearMotion = instruction_verb.FRC_LinearMotion
	FRC_LinearRelative = instruction_verb.FRC_LinearRelative
	FRC_JointMotion = instruction_verb.FRC_JointMotion
	FRC_JointRelative = instruction_verb.FRC_JointRelative
	FRC_CircularMotion = instruction_verb.FRC_CircularMotion
	FRC_CircularRelative = instruction_verb.FRC_CircularRelative
	FRC_JointMotionJRep = instruction_verb.FRC_JointMotionJRep
	FRC_JointRelativeJRep = instruction_verb.FRC_JointRelativeJRep
	FRC_LinearMotionJRep = instruction_verb.FRC_LinearMotionJRep
	FRC_LinearRelativeJRep = instruction_verb.FRC_LinearRelativeJRep
