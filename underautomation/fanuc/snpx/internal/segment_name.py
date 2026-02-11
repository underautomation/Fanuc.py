import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentName as segment_name

class SegmentName(int):
	SDI = int(segment_name.SDI)
	SDO = int(segment_name.SDO)
	RDI = int(segment_name.RDI)
	RDO = int(segment_name.RDO)
	UI = int(segment_name.UI)
	UO = int(segment_name.UO)
	SI = int(segment_name.SI)
	SO = int(segment_name.SO)
	WI = int(segment_name.WI)
	WO = int(segment_name.WO)
	WSI = int(segment_name.WSI)
	PMC_K = int(segment_name.PMC_K)
	PMC_R = int(segment_name.PMC_R)
	AI = int(segment_name.AI)
	AO = int(segment_name.AO)
	GI = int(segment_name.GI)
	GO = int(segment_name.GO)
	PMC_D = int(segment_name.PMC_D)

	def __repr__(self):
		for name, value in vars(SegmentName).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
