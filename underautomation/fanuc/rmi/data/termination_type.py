import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Rmi.Data import TerminationType as termination_type

class TerminationType(int):
	Fine = int(termination_type.Fine)
	Cnt = int(termination_type.Cnt)
	Cr = int(termination_type.Cr)

	def __repr__(self):
		for name, value in vars(TerminationType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
