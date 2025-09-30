import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import TerminationType as termination_type

class TerminationType(int):
	Fine = termination_type.Fine
	Cnt = termination_type.Cnt
	Cr = termination_type.Cr
