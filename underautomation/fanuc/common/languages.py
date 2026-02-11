import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import Languages as languages

class Languages(int):
	English = int(languages.English)
	Japanese = int(languages.Japanese)
	Chinese = int(languages.Chinese)

	def __repr__(self):
		for name, value in vars(Languages).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
