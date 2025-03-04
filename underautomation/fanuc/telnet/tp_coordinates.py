import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Telnet import TpCoordinates as tp_coordinates

class TpCoordinates(int):
	Unknown = tp_coordinates.Unknown
	Tool = tp_coordinates.Tool
	User = tp_coordinates.User
	Joint = tp_coordinates.Joint
	JogFrame = tp_coordinates.JogFrame
	World = tp_coordinates.World
