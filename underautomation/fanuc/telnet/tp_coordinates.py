import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import TpCoordinates as tp_coordinates

class TpCoordinates(int):
	Unknown = int(tp_coordinates.Unknown)
	Tool = int(tp_coordinates.Tool)
	User = int(tp_coordinates.User)
	Joint = int(tp_coordinates.Joint)
	JogFrame = int(tp_coordinates.JogFrame)
	World = int(tp_coordinates.World)

	def __repr__(self):
		for name, value in vars(TpCoordinates).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
