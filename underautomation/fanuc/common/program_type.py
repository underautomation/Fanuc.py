import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import ProgramType as program_type

class ProgramType(int):
	Unknown = int(program_type.Unknown)
	Karel = int(program_type.Karel)
	TP = int(program_type.TP)

	def __repr__(self):
		for name, value in vars(ProgramType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
