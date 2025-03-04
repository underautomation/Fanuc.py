import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentSelector as segment_selector

class SegmentSelector(int):
	BIT_I = segment_selector.BIT_I
	BIT_Q = segment_selector.BIT_Q
	BIT_T = segment_selector.BIT_T
	BIT_M = segment_selector.BIT_M
	BIT_SA = segment_selector.BIT_SA
	BIT_SB = segment_selector.BIT_SB
	BIT_SC = segment_selector.BIT_SC
	BIT_S = segment_selector.BIT_S
	BIT_G = segment_selector.BIT_G
	BYTE_I = segment_selector.BYTE_I
	BYTE_Q = segment_selector.BYTE_Q
	BYTE_T = segment_selector.BYTE_T
	BYTE_M = segment_selector.BYTE_M
	BYTE_SA = segment_selector.BYTE_SA
	BYTE_SB = segment_selector.BYTE_SB
	BYTE_SC = segment_selector.BYTE_SC
	BYTE_G = segment_selector.BYTE_G
	WORD_R = segment_selector.WORD_R
	WORD_AI = segment_selector.WORD_AI
	WORD_AQ = segment_selector.WORD_AQ
	INIT = segment_selector.INIT
