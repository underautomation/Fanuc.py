import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentOffset as segment_offset

class SegmentOffset(int):
	SDIO = int(segment_offset.SDIO)
	RDIO = int(segment_offset.RDIO)
	UOP = int(segment_offset.UOP)
	SOP = int(segment_offset.SOP)
	WIO = int(segment_offset.WIO)
	WSI = int(segment_offset.WSI)
	PMC_K = int(segment_offset.PMC_K)
	PMC_R = int(segment_offset.PMC_R)
	GIO = int(segment_offset.GIO)
	AIO = int(segment_offset.AIO)
	PMC_D = int(segment_offset.PMC_D)

	def __repr__(self):
		for name, value in vars(SegmentOffset).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
