import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.StreamMotion.Data import DataStyle as data_style

class DataStyle(int):
	Cartesian = data_style.Cartesian
	Joint = data_style.Joint
