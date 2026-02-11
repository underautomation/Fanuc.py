import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import InstructionVerb as instruction_verb

class InstructionVerb(int):
	FRC_WaitDin = int(instruction_verb.FRC_WaitDin)
	FRC_SetUFrame = int(instruction_verb.FRC_SetUFrame)
	FRC_SetUTool = int(instruction_verb.FRC_SetUTool)
	FRC_Wait = int(instruction_verb.FRC_Wait)
	FRC_PayLoad = int(instruction_verb.FRC_PayLoad)
	FRC_LinearMotion = int(instruction_verb.FRC_LinearMotion)
	FRC_LinearRelative = int(instruction_verb.FRC_LinearRelative)
	FRC_JointMotion = int(instruction_verb.FRC_JointMotion)
	FRC_JointRelative = int(instruction_verb.FRC_JointRelative)
	FRC_CircularMotion = int(instruction_verb.FRC_CircularMotion)
	FRC_CircularRelative = int(instruction_verb.FRC_CircularRelative)
	FRC_JointMotionJRep = int(instruction_verb.FRC_JointMotionJRep)
	FRC_JointRelativeJRep = int(instruction_verb.FRC_JointRelativeJRep)
	FRC_LinearMotionJRep = int(instruction_verb.FRC_LinearMotionJRep)
	FRC_LinearRelativeJRep = int(instruction_verb.FRC_LinearRelativeJRep)

	def __repr__(self):
		for name, value in vars(InstructionVerb).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
