from enum import IntEnum

class SegmentOffset(IntEnum):
	'''Families of I/O signals that the SNPX client reads and writes. Used by the SDK to address the signals.'''
	SDIO = 0 # Digital I/O
	RDIO = 5000 # Robot I/O
	UOP = 6000 # UI and UO
	SOP = 7000 # SI and SO
	WIO = 8000 # Weld I/O
	WSI = 8400 # Wire Stick I/O
	PMC_K = 10000 # PMC Keep Relay
	PMC_R = 11000 # PMC Internal Relay
	GIO = 0 # Group I/O
	AIO = 1000 # Analog I/O
	PMC_D = 10000 # PMC Data table
