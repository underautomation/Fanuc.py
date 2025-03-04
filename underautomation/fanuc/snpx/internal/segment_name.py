import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Snpx.Internal import SegmentName as segment_name

class SegmentName(int):
	SDI = segment_name.SDI
	SDO = segment_name.SDO
	RDI = segment_name.RDI
	RDO = segment_name.RDO
	UI = segment_name.UI
	UO = segment_name.UO
	SI = segment_name.SI
	SO = segment_name.SO
	WI = segment_name.WI
	WO = segment_name.WO
	WSI = segment_name.WSI
	PMC_K = segment_name.PMC_K
	PMC_R = segment_name.PMC_R
	AI = segment_name.AI
	AO = segment_name.AO
	GI = segment_name.GI
	GO = segment_name.GO
	PMC_D = segment_name.PMC_D
