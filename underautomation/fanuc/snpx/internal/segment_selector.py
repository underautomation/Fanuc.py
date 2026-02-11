import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentSelector as segment_selector

class SegmentSelector(int):
	BIT_I = int(segment_selector.BIT_I)
	BIT_Q = int(segment_selector.BIT_Q)
	BIT_T = int(segment_selector.BIT_T)
	BIT_M = int(segment_selector.BIT_M)
	BIT_SA = int(segment_selector.BIT_SA)
	BIT_SB = int(segment_selector.BIT_SB)
	BIT_SC = int(segment_selector.BIT_SC)
	BIT_S = int(segment_selector.BIT_S)
	BIT_G = int(segment_selector.BIT_G)
	BYTE_I = int(segment_selector.BYTE_I)
	BYTE_Q = int(segment_selector.BYTE_Q)
	BYTE_T = int(segment_selector.BYTE_T)
	BYTE_M = int(segment_selector.BYTE_M)
	BYTE_SA = int(segment_selector.BYTE_SA)
	BYTE_SB = int(segment_selector.BYTE_SB)
	BYTE_SC = int(segment_selector.BYTE_SC)
	BYTE_G = int(segment_selector.BYTE_G)
	WORD_R = int(segment_selector.WORD_R)
	WORD_AI = int(segment_selector.WORD_AI)
	WORD_AQ = int(segment_selector.WORD_AQ)
	INIT = int(segment_selector.INIT)

	def __repr__(self):
		for name, value in vars(SegmentSelector).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
