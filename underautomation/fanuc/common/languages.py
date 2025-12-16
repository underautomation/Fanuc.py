import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Common import Languages as languages

class Languages(int):
	English = languages.English
	Japanese = languages.Japanese
	Chinese = languages.Chinese
