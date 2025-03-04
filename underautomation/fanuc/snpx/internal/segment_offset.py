import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentOffset as segment_offset

class SegmentOffset(int):
	SDIO = segment_offset.SDIO
	RDIO = segment_offset.RDIO
	UOP = segment_offset.UOP
	SOP = segment_offset.SOP
	WIO = segment_offset.WIO
	WSI = segment_offset.WSI
	PMC_K = segment_offset.PMC_K
	PMC_R = segment_offset.PMC_R
	GIO = segment_offset.GIO
	AIO = segment_offset.AIO
	PMC_D = segment_offset.PMC_D
