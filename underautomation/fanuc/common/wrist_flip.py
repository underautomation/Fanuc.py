import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import WristFlip as wrist_flip

class WristFlip(int):
	Unknown = wrist_flip.Unknown
	Flip = wrist_flip.Flip
	NoFlip = wrist_flip.NoFlip
