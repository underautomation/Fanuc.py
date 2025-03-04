import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ValueKind as value_kind

class ValueKind(int):
	Value = value_kind.Value
	Array = value_kind.Array
	Structure = value_kind.Structure
	File = value_kind.File
