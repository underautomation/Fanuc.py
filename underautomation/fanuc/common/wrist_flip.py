import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import WristFlip as wrist_flip

class WristFlip(int):
	Unknown = int(wrist_flip.Unknown)
	Flip = int(wrist_flip.Flip)
	NoFlip = int(wrist_flip.NoFlip)

	def __repr__(self):
		for name, value in vars(WristFlip).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
