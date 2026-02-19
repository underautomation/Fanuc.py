from enum import IntEnum

class SegmentSelector(IntEnum):
	'''Defines segment selector codes for SNPX memory access operations.'''
	BIT_I = 70 # Bit-level input segment.
	BIT_Q = 72 # Bit-level output segment.
	BIT_T = 74 # Bit-level T segment.
	BIT_M = 76 # Bit-level M segment.
	BIT_SA = 78 # Bit-level SA segment.
	BIT_SB = 80 # Bit-level SB segment.
	BIT_SC = 82 # Bit-level SC segment.
	BIT_S = 84 # Bit-level S segment.
	BIT_G = 86 # Bit-level G segment.
	BYTE_I = 16 # Byte-level input segment.
	BYTE_Q = 18 # Byte-level output segment.
	BYTE_T = 20 # Byte-level T segment.
	BYTE_M = 22 # Byte-level M segment.
	BYTE_SA = 26 # Byte-level SA segment.
	BYTE_SB = 28 # Byte-level SB segment.
	BYTE_SC = 30 # Byte-level SC segment.
	BYTE_G = 56 # Byte-level G segment.
	WORD_R = 8 # Word-level R segment for register access.
	WORD_AI = 10 # Word-level AI segment for analog input.
	WORD_AQ = 12 # Word-level AQ segment for analog output.
	INIT = 1 # Selector used during connection initialization.
