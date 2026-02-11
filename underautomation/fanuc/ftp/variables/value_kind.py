import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ValueKind as value_kind

class ValueKind(int):
	Value = int(value_kind.Value)
	Array = int(value_kind.Array)
	Structure = int(value_kind.Structure)
	File = int(value_kind.File)

	def __repr__(self):
		for name, value in vars(ValueKind).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
