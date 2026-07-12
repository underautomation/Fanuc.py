from enum import IntEnum

class RmiPltzMode(IntEnum):
	'''Palletizing motion mode passed to RmiPltzMode}). Requires MajorVersion >= 7.'''
	ZeroDown = 0 # Zero-approach descent.
	ZeroUp = 1 # Zero-approach ascent.
	PspiDown = 2 # Palletizing-spine descent.
	PspiUp = 3 # Palletizing-spine ascent.
	MspiDown = 4 # Multi-spine descent.
	MspiUp = 5 # Multi-spine ascent.
