import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import DataStyle as data_style

class DataStyle(int):
	Cartesian = int(data_style.Cartesian)
	Joint = int(data_style.Joint)

	def __repr__(self):
		for name, value in vars(DataStyle).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
