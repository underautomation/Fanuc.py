import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ProgramType as program_type

class ProgramType(int):
	Unknown = program_type.Unknown
	Karel = program_type.Karel
	TP = program_type.TP
